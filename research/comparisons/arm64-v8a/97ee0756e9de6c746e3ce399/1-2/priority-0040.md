# v15.7.3 → v15.7.4 · 最優先の変更候補 (40)

[一覧の目次](README.md)

<a id="compare-d88888332a38250ad279a2361c204b5a"></a>

### [`0083db14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db14.md) → [`0083db14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083db14.md) FUN_0083db14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0083db24",
      "incomplete_value": false,
      "site": "0083db2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083db24",
      "incomplete_value": false,
      "site": "0083db2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "0083db2c",
      "DATA",
      [
        "storage",
        "00c01668",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0083db2c",
      "DATA",
      [
        "storage",
        "00c016b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083db24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db14.md#insn-0083db24)
- 新版 `0083db24`（命令位置の公開資料なし）

~~~diff
- 0083db24 ["COPY", "tmp:0:8", ["const:668:8"]]
- 0083db24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083db24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083db24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083db24 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 0083db24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083db24 bytes 08a11991
+ 0083db24 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea1e4ee7c81d5d5844444ef520d5ac9"></a>

### [`0083db58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db58.md) → [`0083db58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083db58.md) FUN_0083db58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083db78",
      "incomplete_value": false,
      "site": "0083db7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083db78",
      "incomplete_value": false,
      "site": "0083db7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
      "0083db7c",
      "DATA",
      [
        "storage",
        "00c016b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083db7c",
      "DATA",
      [
        "storage",
        "00c01708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083db78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db58.md#insn-0083db78)
- 新版 `0083db78`（命令位置の公開資料なし）

~~~diff
- 0083db78 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 0083db78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083db78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083db78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083db78 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 0083db78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083db78 bytes 08e11a91
+ 0083db78 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55f1866f1b8d87b60fe07959d6739e61"></a>

### [`0083db90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db90.md) → [`0083db90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083db90.md) FUN_0083db90

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
      "definition_site": "0083db94",
      "incomplete_value": false,
      "site": "0083db98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083db94",
      "incomplete_value": false,
      "site": "0083db98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
      "0083db98",
      "DATA",
      [
        "storage",
        "00c016b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083db98",
      "DATA",
      [
        "storage",
        "00c01708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083db94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db90.md#insn-0083db94)
- 新版 `0083db94`（命令位置の公開資料なし）

~~~diff
- 0083db94 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 0083db94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083db94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083db94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083db94 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 0083db94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083db94 bytes 08e11a91
+ 0083db94 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a5b753898c0cd4d2fd08b2c814a8e5e"></a>

### [`0083dbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dbdc.md) → [`0083dbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dbdc.md) FUN_0083dbdc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0083dbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dbb0.md) [`0083df14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083df14.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md) [`0052dae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dae4.md) [`00574ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff0.md) [`00a28744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28744.md)
- 新版 呼出元 2件 [`0083dbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dbb0.md) [`0083df14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083df14.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md) [`0052dae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dae4.md) [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) [`00a28788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28788.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083dbf4",
      "incomplete_value": false,
      "site": "0083dc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c34000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083dbf4",
      "incomplete_value": false,
      "site": "0083dc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c34000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "0083dbf4",
      "PARAM",
      [
        "storage",
        "00c34400",
        null,
        null
      ]
    ],
    [
      "0083dc18",
      "READ",
      [
        "storage",
        "002a6cbc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083dbf4",
      "PARAM",
      [
        "storage",
        "00c34440",
        null,
        null
      ]
    ],
    [
      "0083dc18",
      "READ",
      [
        "storage",
        "002a6d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083dbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dbdc.md#insn-0083dbf4) · [`0083dc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dbdc.md#insn-0083dc10)
- 新版 `0083dbf4`（命令位置の公開資料なし） · `0083dc10`（命令位置の公開資料なし）

~~~diff
- 0083dbf4 ["COPY", "tmp:0:8", ["const:400:8"]]
- 0083dbf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0083dbf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0083dbf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0083dbf4 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0083dbf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0083dbf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0083dbf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0083dbf4 bytes 00001091
+ 0083dbf4 bytes 00001191
- 0083dc10 ["COPY", "tmp:0:8", ["const:cbc:8"]]
- 0083dc10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083dc10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083dc10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083dc10 ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 0083dc10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dc10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dc10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083dc10 bytes 29f13291
+ 0083dc10 bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767dabca2ff16dd3c169a5c6597f4005"></a>

### [`0083debc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083debc.md) → [`0083debc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083debc.md) FUN_0083debc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083dedc",
      "incomplete_value": false,
      "site": "0083dee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083dedc",
      "incomplete_value": false,
      "site": "0083dee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
      "0083dee0",
      "DATA",
      [
        "storage",
        "00c01738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083dee0",
      "DATA",
      [
        "storage",
        "00c01788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083dedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083debc.md#insn-0083dedc)
- 新版 `0083dedc`（命令位置の公開資料なし）

~~~diff
- 0083dedc ["COPY", "tmp:0:8", ["const:738:8"]]
- 0083dedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083dedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083dedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083dedc ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0083dedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083dedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083dedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083dedc bytes 08e11c91
+ 0083dedc bytes 08211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48bbcc6132a8e816fb95013ec3093efa"></a>

### [`0083df44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083df44.md) → [`0083df44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083df44.md) FUN_0083df44

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083df64",
      "incomplete_value": false,
      "site": "0083df68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083df64",
      "incomplete_value": false,
      "site": "0083df68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "0083df68",
      "DATA",
      [
        "storage",
        "00c017b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083df68",
      "DATA",
      [
        "storage",
        "00c01808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083df64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083df44.md#insn-0083df64)
- 新版 `0083df64`（命令位置の公開資料なし）

~~~diff
- 0083df64 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 0083df64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083df64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083df64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083df64 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 0083df64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083df64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083df64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083df64 bytes 08e11e91
+ 0083df64 bytes 08212091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c220bac9d38d13d67c4fee2ceb7253f0"></a>

### [`0083df7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083df7c.md) → [`0083df7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083df7c.md) FUN_0083df7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083df80",
      "incomplete_value": true,
      "site": "0083df84",
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
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083df80",
      "incomplete_value": true,
      "site": "0083df84",
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
            "const:7b8:8"
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
      "0083df84",
      "DATA",
      [
        "storage",
        "00c017b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083df84",
      "DATA",
      [
        "storage",
        "00c01808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083df80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083df7c.md#insn-0083df80)
- 新版 `0083df80`（命令位置の公開資料なし）

~~~diff
- 0083df80 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 0083df80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083df80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083df80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083df80 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 0083df80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083df80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083df80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083df80 bytes 08e11e91
+ 0083df80 bytes 08212091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0ab3446f9c3d33424a175f7b86d5930"></a>

### [`0083dfc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dfc8.md) → [`0083dfc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dfc8.md) FUN_0083dfc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0083df9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083df9c.md) [`0083e950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e950.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md)
- 新版 呼出元 2件 [`0083df9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083df9c.md) [`0083e950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e950.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083e168",
      "incomplete_value": true,
      "site": "0083e168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083e168",
      "incomplete_value": true,
      "site": "0083e168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:99b:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0083e23c",
      "incomplete_value": true,
      "site": "0083e23c",
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
      "definition_site": "0083e23c",
      "incomplete_value": true,
      "site": "0083e23c",
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
      "0083dff8",
      "READ",
      [
        "storage",
        "0029ea7f",
        null,
        "string"
      ]
    ],
    [
      "0083dffc",
      "READ",
      [
        "storage",
        "0029ea86",
        null,
        "string"
      ]
    ],
    [
      "0083e11c",
      "READ",
      [
        "storage",
        "002a1acf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083dff8",
      "READ",
      [
        "storage",
        "0029eb0a",
        null,
        "string"
      ]
    ],
    [
      "0083dffc",
      "READ",
      [
        "storage",
        "0029eb11",
        null,
        "string"
      ]
    ],
    [
      "0083e11c",
      "READ",
      [
        "storage",
        "002a1b5a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083dff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dfc8.md#insn-0083dff0) · [`0083e114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dfc8.md#insn-0083e114) · [`0083e150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dfc8.md#insn-0083e150)
- 新版 `0083dff0`（命令位置の公開資料なし） · `0083e114`（命令位置の公開資料なし） · `0083e150`（命令位置の公開資料なし）

~~~diff
- 0083dff0 ["COPY", "tmp:0:8", ["const:a7f:8"]]
- 0083dff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083dff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083dff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083dff0 ["COPY", "tmp:0:8", ["const:b0a:8"]]
+ 0083dff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083dff0 bytes 29fd2991
+ 0083dff0 bytes 29292c91
- 0083e114 ["COPY", "tmp:0:8", ["const:acf:8"]]
- 0083e114 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083e114 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083e114 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083e114 ["COPY", "tmp:0:8", ["const:b5a:8"]]
+ 0083e114 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083e114 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083e114 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083e114 bytes 293d2b91
+ 0083e114 bytes 29692d91
- 0083e150 ["COPY", "tmp:0:8", ["const:99b:8"]]
- 0083e150 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083e150 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083e150 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083e150 ["COPY", "tmp:0:8", ["const:a35:8"]]
+ 0083e150 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083e150 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083e150 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083e150 bytes 296d2691
+ 0083e150 bytes 29d52891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e65841b267e59e6391f6a46c67535de9"></a>

### [`0083e8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e8f8.md) → [`0083e8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e8f8.md) FUN_0083e8f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083e918",
      "incomplete_value": false,
      "site": "0083e91c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083e918",
      "incomplete_value": false,
      "site": "0083e91c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:838:8"
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
      "0083e91c",
      "DATA",
      [
        "storage",
        "00c01838",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083e91c",
      "DATA",
      [
        "storage",
        "00c01888",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083e918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e8f8.md#insn-0083e918)
- 新版 `0083e918`（命令位置の公開資料なし）

~~~diff
- 0083e918 ["COPY", "tmp:0:8", ["const:838:8"]]
- 0083e918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083e918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083e918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083e918 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 0083e918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083e918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083e918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083e918 bytes 08e12091
+ 0083e918 bytes 08212291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-999b7099974b08d48119354c7b952ce5"></a>

### [`0083e930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e930.md) → [`0083e930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e930.md) FUN_0083e930

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
      "definition_site": "0083e934",
      "incomplete_value": false,
      "site": "0083e938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083e934",
      "incomplete_value": false,
      "site": "0083e938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:838:8"
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
      "0083e938",
      "DATA",
      [
        "storage",
        "00c01838",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083e938",
      "DATA",
      [
        "storage",
        "00c01888",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083e934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e930.md#insn-0083e934)
- 新版 `0083e934`（命令位置の公開資料なし）

~~~diff
- 0083e934 ["COPY", "tmp:0:8", ["const:838:8"]]
- 0083e934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083e934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083e934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083e934 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 0083e934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083e934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083e934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083e934 bytes 08e12091
+ 0083e934 bytes 08212291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee8ffc7a2b2d4bf165043d3cd1500d18"></a>

### [`0083e97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e97c.md) → [`0083e97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e97c.md) FUN_0083e97c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0082b53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082b/0082b53c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0082b53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082b/0082b53c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0083e988",
      "incomplete_value": false,
      "site": "0083e98c",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083e988",
      "incomplete_value": false,
      "site": "0083e98c",
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
      "0083e988",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083e988",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083e988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e97c.md#insn-0083e988)
- 新版 `0083e988`（命令位置の公開資料なし）

~~~diff
- 0083e988 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0083e988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0083e988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0083e988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0083e988 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0083e988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0083e988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0083e988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0083e988 bytes 000c0c91
+ 0083e988 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be7606e83c3c94b9d07a84a54018d790"></a>

### [`0083f60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f60c.md) → [`0083f60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083f60c.md) FUN_0083f60c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083f630",
      "incomplete_value": false,
      "site": "0083f630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f630",
      "incomplete_value": false,
      "site": "0083f630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
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
      "0083f630",
      "DATA",
      [
        "storage",
        "00c018b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083f630",
      "DATA",
      [
        "storage",
        "00c01908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f60c.md#insn-0083f62c)
- 新版 `0083f62c`（命令位置の公開資料なし）

~~~diff
- 0083f62c ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 0083f62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083f62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083f62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083f62c ["COPY", "tmp:0:8", ["const:908:8"]]
+ 0083f62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083f62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083f62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083f62c bytes 08e12291
+ 0083f62c bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f2f99f0653be959804ecafc86f017fd"></a>

### [`0083f65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f65c.md) → [`0083f65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083f65c.md) FUN_0083f65c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0082b53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082b/0082b53c.md) · 呼出先 10件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`007cd120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd120.md) [`007cea80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ce/007cea80.md) [`007ceacc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ce/007ceacc.md) [`007d22d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d2/007d22d4.md)
- 新版 呼出元 1件 [`0082b53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082b/0082b53c.md) · 呼出先 10件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`007cd120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd120.md) [`007cea80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cea80.md) [`007ceacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007ceacc.md) [`007d22d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d22d4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.97% / 新版 98.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083f7d8",
      "incomplete_value": false,
      "site": "0083f7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:65a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f7d8",
      "incomplete_value": false,
      "site": "0083f7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:5cf:8"
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
      "0083f7d8",
      "PARAM",
      [
        "storage",
        "002a35cf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083f7d8",
      "PARAM",
      [
        "storage",
        "002a365a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f65c.md#insn-0083f7d8)
- 新版 `0083f7d8`（命令位置の公開資料なし）

~~~diff
- 0083f7d8 ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 0083f7d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0083f7d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0083f7d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0083f7d8 ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 0083f7d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0083f7d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0083f7d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0083f7d8 bytes 003c1791
+ 0083f7d8 bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdab3009c83f6ac00c0c60fff1fd5a58"></a>

### [`0083f810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f810.md) → [`0083f810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083f810.md) FUN_0083f810

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083f834",
      "incomplete_value": false,
      "site": "0083f834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f834",
      "incomplete_value": false,
      "site": "0083f834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0083f834",
      "DATA",
      [
        "storage",
        "00c01948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083f834",
      "DATA",
      [
        "storage",
        "00c01998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f810.md#insn-0083f830)
- 新版 `0083f830`（命令位置の公開資料なし）

~~~diff
- 0083f830 ["COPY", "tmp:0:8", ["const:948:8"]]
- 0083f830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083f830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083f830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083f830 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 0083f830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083f830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083f830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083f830 bytes 08212591
+ 0083f830 bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c37cfacd2c0d98620e5111f5280b39c8"></a>

### [`0083f844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f844.md) → [`0083f844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083f844.md) FUN_0083f844

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
      "definition_site": "0083f850",
      "incomplete_value": true,
      "site": "0083f850",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f850",
      "incomplete_value": true,
      "site": "0083f850",
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
            "const:948:8"
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
      "0083f850",
      "DATA",
      [
        "storage",
        "00c01948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083f850",
      "DATA",
      [
        "storage",
        "00c01998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f844.md#insn-0083f84c)
- 新版 `0083f84c`（命令位置の公開資料なし）

~~~diff
- 0083f84c ["COPY", "tmp:0:8", ["const:948:8"]]
- 0083f84c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083f84c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083f84c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083f84c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 0083f84c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083f84c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083f84c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083f84c bytes 29212591
+ 0083f84c bytes 29612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20e3fef2978847c3014a9590145ebf71"></a>

### [`0083fb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fb9c.md) → [`0083fb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fb9c.md) FUN_0083fb9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0083fba4",
      "incomplete_value": false,
      "site": "0083fba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fba4",
      "incomplete_value": false,
      "site": "0083fba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "0083fba8",
      "DATA",
      [
        "storage",
        "00c019d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fba8",
      "DATA",
      [
        "storage",
        "00c01a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fb9c.md#insn-0083fba4)
- 新版 `0083fba4`（命令位置の公開資料なし）

~~~diff
- 0083fba4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0083fba4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083fba4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083fba4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083fba4 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0083fba4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fba4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fba4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083fba4 bytes 29612791
+ 0083fba4 bytes 29a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49ee7c3a6dadcc346e487194e1b1c933"></a>

### [`0083fbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fbbc.md) → [`0083fbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fbbc.md) FUN_0083fbbc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0083fbc4",
      "incomplete_value": false,
      "site": "0083fbc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fbc4",
      "incomplete_value": false,
      "site": "0083fbc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "0083fbc8",
      "DATA",
      [
        "storage",
        "00c019d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fbc8",
      "DATA",
      [
        "storage",
        "00c01a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fbc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fbbc.md#insn-0083fbc4)
- 新版 `0083fbc4`（命令位置の公開資料なし）

~~~diff
- 0083fbc4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0083fbc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083fbc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083fbc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083fbc4 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0083fbc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fbc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fbc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083fbc4 bytes 29612791
+ 0083fbc4 bytes 29a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d315d1aaf79f77892411db42df4ae1a2"></a>

### [`0083fbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fbfc.md) → [`0083fbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fbfc.md) FUN_0083fbfc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083fc28",
      "incomplete_value": false,
      "site": "0083fc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fc28",
      "incomplete_value": false,
      "site": "0083fc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "0083fc28",
      "DATA",
      [
        "storage",
        "00c019d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fc28",
      "DATA",
      [
        "storage",
        "00c01a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fbfc.md#insn-0083fc20)
- 新版 `0083fc20`（命令位置の公開資料なし）

~~~diff
- 0083fc20 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0083fc20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083fc20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083fc20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083fc20 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0083fc20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083fc20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083fc20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083fc20 bytes 4a612791
+ 0083fc20 bytes 4aa12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3a7cfe34d92ed43fd37f39fc1b60151"></a>

### [`0083fc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fc70.md) → [`0083fc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fc70.md) FUN_0083fc70

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

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
      "definition_site": "0083fc78",
      "incomplete_value": false,
      "site": "0083fc78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fc78",
      "incomplete_value": false,
      "site": "0083fc78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "0083fc78",
      "DATA",
      [
        "storage",
        "00c019d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fc78",
      "DATA",
      [
        "storage",
        "00c01a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fc70.md#insn-0083fc74)
- 新版 `0083fc74`（命令位置の公開資料なし）

~~~diff
- 0083fc74 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0083fc74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083fc74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083fc74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083fc74 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0083fc74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083fc74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083fc74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083fc74 bytes 08612791
+ 0083fc74 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f42b6f74a076586b504049e3c80fcb"></a>

### [`0083fdcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fdcc.md) → [`0083fdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fdcc.md) FUN_0083fdcc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0083fdd4",
      "incomplete_value": false,
      "site": "0083fdd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fdd4",
      "incomplete_value": false,
      "site": "0083fdd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083fdd8",
      "DATA",
      [
        "storage",
        "00c01a58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fdd8",
      "DATA",
      [
        "storage",
        "00c01aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fdd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fdcc.md#insn-0083fdd4)
- 新版 `0083fdd4`（命令位置の公開資料なし）

~~~diff
- 0083fdd4 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 0083fdd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083fdd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083fdd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083fdd4 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 0083fdd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fdd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fdd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083fdd4 bytes 29612991
+ 0083fdd4 bytes 29a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c6b53871c8bf733053b6aac80208507"></a>

### [`0083fdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fdec.md) → [`0083fdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fdec.md) FUN_0083fdec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0083fdf4",
      "incomplete_value": false,
      "site": "0083fdf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fdf4",
      "incomplete_value": false,
      "site": "0083fdf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083fdf8",
      "DATA",
      [
        "storage",
        "00c01a58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fdf8",
      "DATA",
      [
        "storage",
        "00c01aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fdec.md#insn-0083fdf4)
- 新版 `0083fdf4`（命令位置の公開資料なし）

~~~diff
- 0083fdf4 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 0083fdf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083fdf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083fdf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083fdf4 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 0083fdf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fdf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fdf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083fdf4 bytes 29612991
+ 0083fdf4 bytes 29a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebcd83b642eb723c9598cce3e244f72d"></a>

### [`0083fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fe2c.md) → [`0083fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fe2c.md) FUN_0083fe2c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083fe58",
      "incomplete_value": false,
      "site": "0083fe58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fe58",
      "incomplete_value": false,
      "site": "0083fe58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "0083fe58",
      "DATA",
      [
        "storage",
        "00c01a58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fe58",
      "DATA",
      [
        "storage",
        "00c01aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fe50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fe2c.md#insn-0083fe50)
- 新版 `0083fe50`（命令位置の公開資料なし）

~~~diff
- 0083fe50 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 0083fe50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083fe50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083fe50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083fe50 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 0083fe50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083fe50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083fe50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083fe50 bytes 4a612991
+ 0083fe50 bytes 4aa12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1efe08fc35cd90c540da6d77e861621c"></a>

### [`0083fea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fea0.md) → [`0083fea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fea0.md) FUN_0083fea0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

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
      "definition_site": "0083fea8",
      "incomplete_value": false,
      "site": "0083fea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fea8",
      "incomplete_value": false,
      "site": "0083fea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083fea8",
      "DATA",
      [
        "storage",
        "00c01a58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fea8",
      "DATA",
      [
        "storage",
        "00c01aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fea0.md#insn-0083fea4)
- 新版 `0083fea4`（命令位置の公開資料なし）

~~~diff
- 0083fea4 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 0083fea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083fea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083fea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083fea4 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 0083fea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083fea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083fea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083fea4 bytes 08612991
+ 0083fea4 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-670ebb99d321436c8e3ec5d7c3634d20"></a>

### [`0083fffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fffc.md) → [`0083fffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fffc.md) FUN_0083fffc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00840000",
      "incomplete_value": false,
      "site": "00840004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840000",
      "incomplete_value": false,
      "site": "00840004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00840004",
      "DATA",
      [
        "storage",
        "00c01af0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00840004",
      "DATA",
      [
        "storage",
        "00c01b40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fffc.md#insn-00840000)
- 新版 `00840000`（命令位置の公開資料なし）

~~~diff
- 00840000 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 00840000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840000 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00840000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840000 bytes 08c12b91
+ 00840000 bytes 08012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74f2b1d1bcf70ddf94dfdd6438a99dcc"></a>

### [`0084000c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084000c.md) → [`0084000c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/0084000c.md) FUN_0084000c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0084001c",
      "incomplete_value": false,
      "site": "00840024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084001c",
      "incomplete_value": false,
      "site": "00840024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00840024",
      "DATA",
      [
        "storage",
        "00c01af0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00840024",
      "DATA",
      [
        "storage",
        "00c01b40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084001c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084000c.md#insn-0084001c)
- 新版 `0084001c`（命令位置の公開資料なし）

~~~diff
- 0084001c ["COPY", "tmp:0:8", ["const:af0:8"]]
- 0084001c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084001c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084001c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084001c ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 0084001c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084001c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084001c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084001c bytes 08c12b91
+ 0084001c bytes 08012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eafd00b5d1fb5e498ce2468d9ada673d"></a>

### [`0084004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084004c.md) → [`0084004c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/0084004c.md) FUN_0084004c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) · 呼出先 6件 [`004215a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md) [`00421b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b40.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) · 呼出先 6件 [`004215a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md) [`00421b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0084008c",
      "incomplete_value": false,
      "site": "0084008c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084008c",
      "incomplete_value": false,
      "site": "0084008c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "0084008c",
      "DATA",
      [
        "storage",
        "00c01b40",
        null,
        "undefined *"
      ]
    ],
    [
      "00840104",
      "READ",
      [
        "storage",
        "00298184",
        null,
        "string"
      ]
    ],
    [
      "00840108",
      "READ",
      [
        "storage",
        "0029818b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084008c",
      "DATA",
      [
        "storage",
        "00c01b90",
        null,
        "undefined *"
      ]
    ],
    [
      "00840104",
      "READ",
      [
        "storage",
        "002980f7",
        null,
        "string"
      ]
    ],
    [
      "00840108",
      "READ",
      [
        "storage",
        "002980fe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084004c.md#insn-00840088) · [`008400d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084004c.md#insn-008400d4) · [`008400dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084004c.md#insn-008400dc)
- 新版 `00840088`（命令位置の公開資料なし） · `008400d4`（命令位置の公開資料なし） · `008400dc`（命令位置の公開資料なし）

~~~diff
- 00840088 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 00840088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840088 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00840088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840088 bytes 08012d91
+ 00840088 bytes 08412e91
- 008400d4 ["COPY", "tmp:0:8", ["const:184:8"]]
- 008400d4 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 008400d4 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 008400d4 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 008400d4 ["COPY", "tmp:0:8", ["const:f7:8"]]
+ 008400d4 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 008400d4 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 008400d4 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 008400d4 bytes 9c130691
+ 008400d4 bytes 9cdf0391
- 008400dc ["COPY", "tmp:0:8", ["const:62c:8"]]
- 008400dc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 008400dc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 008400dc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 008400dc ["COPY", "tmp:0:8", ["const:67c:8"]]
+ 008400dc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 008400dc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 008400dc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 008400dc bytes f7b21891
+ 008400dc bytes f7f21991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13871bd59730265162404428644f1cf1"></a>

### [`00840274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840274.md) → [`00840274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840274.md) FUN_00840274

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008406c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406c0.md) · 呼出先 5件 [`004618e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00461/004618e8.md) [`00470ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470ac0.md) [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`008406c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406c0.md) · 呼出先 5件 [`004618e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/004618e8.md) [`00470ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ac0.md) [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.82% / 新版 87.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008402d8",
      "incomplete_value": false,
      "site": "008402e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109c000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008402d8",
      "incomplete_value": false,
      "site": "008402e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109c000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "definition_site": "008402e8",
      "incomplete_value": false,
      "site": "008402f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109d000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008402e8",
      "incomplete_value": false,
      "site": "008402f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109d000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "definition_site": "00840310",
      "incomplete_value": false,
      "site": "00840318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109c000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840310",
      "incomplete_value": false,
      "site": "00840318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109c000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "008402b4",
      "DATA",
      [
        "storage",
        "00c01b40",
        null,
        "undefined *"
      ]
    ],
    [
      "008402bc",
      "READ",
      [
        "storage",
        "00f5c818",
        null,
        "undefined1"
      ]
    ],
    [
      "008402cc",
      "READ",
      [
        "storage",
        "00fec273",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008402b4",
      "DATA",
      [
        "storage",
        "00c01b90",
        null,
        "undefined *"
      ]
    ],
    [
      "008402bc",
      "READ",
      [
        "storage",
        "00f5c858",
        null,
        "undefined1"
      ]
    ],
    [
      "008402cc",
      "READ",
      [
        "storage",
        "00fec2b3",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840274.md#insn-00840298) · [`008402a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840274.md#insn-008402a4) · [`008402d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840274.md#insn-008402d8)
- 新版 `00840298`（命令位置の公開資料なし） · `008402a4`（命令位置の公開資料なし） · `008402d8`（命令位置の公開資料なし）

~~~diff
- 00840298 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 00840298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00840298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00840298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00840298 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00840298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00840298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00840298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00840298 bytes 29012d91
+ 00840298 bytes 29412e91
- 008402a4 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 008402a4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 008402a4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 008402a4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 008402a4 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 008402a4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 008402a4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 008402a4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 008402a4 bytes 94c20691
+ 008402a4 bytes 94c20791
- 008402d8 ["COPY", "tmp:0:8", ["const:668:8"]]
- 008402d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008402d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008402d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008402d8 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 008402d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008402d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008402d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008402d8 bytes 00a01991
+ 008402d8 bytes 00a01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a08a24f69a0e227bc5a0e23a131b488"></a>

### [`008406e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406e4.md) → [`008406e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md) FUN_008406e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 17件 [`004215a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md) [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004215a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md) [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.24% / 新版 91.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0084071c",
      "incomplete_value": false,
      "site": "00840720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084071c",
      "incomplete_value": false,
      "site": "00840720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "definition_site": "00840838",
      "incomplete_value": false,
      "site": "00840850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840838",
      "incomplete_value": false,
      "site": "00840850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00840934",
      "incomplete_value": true,
      "site": "00840938",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840934",
      "incomplete_value": true,
      "site": "00840938",
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
            "const:38:8"
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
      "0084071c",
      "PARAM",
      [
        "storage",
        "00c281b0",
        null,
        null
      ]
    ],
    [
      "00840790",
      "READ",
      [
        "storage",
        "00298194",
        null,
        "string"
      ]
    ],
    [
      "00840794",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0084071c",
      "PARAM",
      [
        "storage",
        "00c281f0",
        null,
        null
      ]
    ],
    [
      "00840790",
      "READ",
      [
        "storage",
        "00298107",
        null,
        "string"
      ]
    ],
    [
      "00840794",
      "READ",
      [
        "storage",
        "00c1aea0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084071c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406e4.md#insn-0084071c) · [`00840760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406e4.md#insn-00840760) · [`0084078c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406e4.md#insn-0084078c)
- 新版 `0084071c`（命令位置の公開資料なし） · `00840760`（命令位置の公開資料なし） · `0084078c`（命令位置の公開資料なし）

~~~diff
- 0084071c ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 0084071c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0084071c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0084071c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0084071c ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 0084071c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0084071c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0084071c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0084071c bytes 00c00691
+ 0084071c bytes 00c00791
- 00840760 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 00840760 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00840760 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00840760 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00840760 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00840760 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00840760 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00840760 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00840760 bytes 39c30691
+ 00840760 bytes 39c30791
- 0084078c ["COPY", "tmp:0:8", ["const:194:8"]]
- 0084078c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084078c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084078c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084078c ["COPY", "tmp:0:8", ["const:107:8"]]
+ 0084078c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084078c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084078c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084078c bytes 08510691
+ 0084078c bytes 081d0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8625fc0a2a1dab7b472562a5ec7c2d8e"></a>

### [`00840d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d1c.md) → [`00840d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d1c.md) FUN_00840d1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00840d20",
      "incomplete_value": false,
      "site": "00840d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840d20",
      "incomplete_value": false,
      "site": "00840d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "00840d24",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00840d24",
      "DATA",
      [
        "storage",
        "00c01bd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d1c.md#insn-00840d20)
- 新版 `00840d20`（命令位置の公開資料なし）

~~~diff
- 00840d20 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00840d20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840d20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840d20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840d20 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00840d20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840d20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840d20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840d20 bytes 08212e91
+ 00840d20 bytes 08612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eb3fa39c85859fdcfa0635ddeaa4664"></a>

### [`00840d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d2c.md) → [`00840d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d2c.md) FUN_00840d2c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00840d3c",
      "incomplete_value": false,
      "site": "00840d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840d3c",
      "incomplete_value": false,
      "site": "00840d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "00840d44",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00840d44",
      "DATA",
      [
        "storage",
        "00c01bd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d2c.md#insn-00840d3c)
- 新版 `00840d3c`（命令位置の公開資料なし）

~~~diff
- 00840d3c ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00840d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840d3c ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00840d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840d3c bytes 08212e91
+ 00840d3c bytes 08612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb6f89f63a0f92a5237f9f4029000cdf"></a>

### [`00840d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d6c.md) → [`00840d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d6c.md) FUN_00840d6c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008443c8.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 2件 [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.87% / 新版 90.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00840db0",
      "incomplete_value": false,
      "site": "00840db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840db0",
      "incomplete_value": false,
      "site": "00840db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
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
      "definition_site": "00840e18",
      "incomplete_value": true,
      "site": "00840e18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840e18",
      "incomplete_value": true,
      "site": "00840e18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:315:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00840e4c",
      "incomplete_value": true,
      "site": "00840e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840e4c",
      "incomplete_value": true,
      "site": "00840e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "00840db0",
      "DATA",
      [
        "storage",
        "00c01bd8",
        null,
        "undefined *"
      ]
    ],
    [
      "00840de4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00840e04",
      "READ",
      [
        "storage",
        "002a0315",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00840db0",
      "DATA",
      [
        "storage",
        "00c01c28",
        null,
        "undefined *"
      ]
    ],
    [
      "00840de4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00840e04",
      "READ",
      [
        "storage",
        "002a03a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d6c.md#insn-00840dac) · [`00840de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d6c.md#insn-00840de0) · [`00840e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d6c.md#insn-00840e00)
- 新版 `00840dac`（命令位置の公開資料なし） · `00840de0`（命令位置の公開資料なし） · `00840e00`（命令位置の公開資料なし）

~~~diff
- 00840dac ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00840dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840dac ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 00840dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840dac bytes 08612f91
+ 00840dac bytes 08a13091
- 00840de0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00840de0 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00840de0 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00840de0 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 00840de0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00840de0 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 00840de0 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 00840de0 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00840de0 bytes 5ae30091
+ 00840de0 bytes 5ae30191
- 00840e00 ["COPY", "tmp:0:8", ["const:315:8"]]
- 00840e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840e00 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00840e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840e00 bytes 08550c91
+ 00840e00 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1bca2b3e2e3b021d33199b021092286"></a>

### [`00841168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841168.md) → [`00841168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841168.md) FUN_00841168

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00841180",
      "incomplete_value": false,
      "site": "00841184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841180",
      "incomplete_value": false,
      "site": "00841184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
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
      "00841184",
      "DATA",
      [
        "storage",
        "00c01bd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00841184",
      "DATA",
      [
        "storage",
        "00c01c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841168.md#insn-00841180)
- 新版 `00841180`（命令位置の公開資料なし）

~~~diff
- 00841180 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00841180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00841180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00841180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00841180 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 00841180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00841180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00841180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00841180 bytes 29612f91
+ 00841180 bytes 29a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ba00b3e2c33b101a304c624be476411"></a>

### [`00841214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841214.md) → [`00841214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841214.md) FUN_00841214

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0084122c",
      "incomplete_value": false,
      "site": "00841230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084122c",
      "incomplete_value": false,
      "site": "00841230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
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
      "00841230",
      "DATA",
      [
        "storage",
        "00c01bd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00841230",
      "DATA",
      [
        "storage",
        "00c01c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084122c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841214.md#insn-0084122c)
- 新版 `0084122c`（命令位置の公開資料なし）

~~~diff
- 0084122c ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 0084122c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084122c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084122c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084122c ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 0084122c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084122c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084122c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084122c bytes 29612f91
+ 0084122c bytes 29a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6172683ed457704b806c5ae198489ca6"></a>

### [`008412b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md) → [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) FUN_008412b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0053dc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dc30.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0053dc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc30.md) [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.46% / 新版 96.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00841304",
      "incomplete_value": true,
      "site": "00841314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2fd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841304",
      "incomplete_value": true,
      "site": "00841314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:272:8"
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
      "definition_site": "008413d4",
      "incomplete_value": true,
      "site": "008413d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:9c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008413d4",
      "incomplete_value": true,
      "site": "008413d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:9c5:8"
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
      "definition_site": "008413d8",
      "incomplete_value": true,
      "site": "008413d8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008413d8",
      "incomplete_value": true,
      "site": "008413d8",
      "value": [
        "LOAD",
        "8",
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
      "00841304",
      "READ",
      [
        "storage",
        "002a4272",
        null,
        "string"
      ]
    ],
    [
      "008413c4",
      "READ",
      [
        "storage",
        "0029b9c5",
        null,
        "string"
      ]
    ],
    [
      "008413c8",
      "READ",
      [
        "storage",
        "0029b9cb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00841304",
      "READ",
      [
        "storage",
        "002a42fd",
        null,
        "string"
      ]
    ],
    [
      "008413c4",
      "READ",
      [
        "storage",
        "0029b9c3",
        null,
        "string"
      ]
    ],
    [
      "008413c8",
      "READ",
      [
        "storage",
        "0029b9c9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008412fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md#insn-008412fc) · [`008413bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md#insn-008413bc)
- 新版 `008412fc`（命令位置の公開資料なし） · `008413bc`（命令位置の公開資料なし）

~~~diff
- 008412fc ["COPY", "tmp:0:8", ["const:272:8"]]
- 008412fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008412fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008412fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008412fc ["COPY", "tmp:0:8", ["const:2fd:8"]]
+ 008412fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008412fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008412fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008412fc bytes 08c90991
+ 008412fc bytes 08f50b91
- 008413bc ["COPY", "tmp:0:8", ["const:9c5:8"]]
- 008413bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008413bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008413bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008413bc ["COPY", "tmp:0:8", ["const:9c3:8"]]
+ 008413bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008413bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008413bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008413bc bytes 29152791
+ 008413bc bytes 290d2791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac39bf5c41652b738026fb3a513a821f"></a>

### [`0084177c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/0084177c.md) → [`0084177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/0084177c.md) FUN_0084177c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008412b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md) [`008427a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008427a8.md) · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`0042ca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca70.md) [`0084224c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084224c.md) [`0084229c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084229c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 2件 [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) [`008427a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008427a8.md) · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`0042ca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca70.md) [`0084224c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084224c.md) [`0084229c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084229c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008417e4",
      "incomplete_value": false,
      "site": "008417e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008417e4",
      "incomplete_value": false,
      "site": "008417e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "definition_site": "00841804",
      "incomplete_value": false,
      "site": "00841804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841804",
      "incomplete_value": false,
      "site": "00841804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "008417e4",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ],
    [
      "00841804",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ],
    [
      "00841844",
      "READ",
      [
        "storage",
        "00c01c58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008417e4",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ],
    [
      "00841804",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ],
    [
      "00841844",
      "READ",
      [
        "storage",
        "00c01ca8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008417d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/0084177c.md#insn-008417d4) · [`008417fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/0084177c.md#insn-008417fc)
- 新版 `008417d4`（命令位置の公開資料なし） · `008417fc`（命令位置の公開資料なし）

~~~diff
- 008417d4 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 008417d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008417d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008417d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008417d4 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 008417d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008417d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008417d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008417d4 bytes 08e13091
+ 008417d4 bytes 08213291
- 008417fc ["COPY", "tmp:0:8", ["const:c38:8"]]
- 008417fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008417fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008417fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008417fc ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 008417fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008417fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008417fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008417fc bytes 08e13091
+ 008417fc bytes 08213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb643e5143fc8eda67061b78b1859efe"></a>

### [`00841924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841924.md) → [`00841924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md) FUN_00841924

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008412b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md) [`008423bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008423bc.md) · 呼出先 7件 [`0084297c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084297c.md) [`008429cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008429cc.md) [`0084d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d6d0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 2件 [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) [`008423bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md) · 呼出先 7件 [`0084297c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084297c.md) [`008429cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008429cc.md) [`0084d6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00841984",
      "incomplete_value": false,
      "site": "00841984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841984",
      "incomplete_value": false,
      "site": "00841984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "definition_site": "008419a4",
      "incomplete_value": false,
      "site": "008419a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008419a4",
      "incomplete_value": false,
      "site": "008419a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "00841984",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ],
    [
      "008419a4",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ],
    [
      "008419e8",
      "READ",
      [
        "storage",
        "00c01d58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00841984",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ],
    [
      "008419a4",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ],
    [
      "008419e8",
      "READ",
      [
        "storage",
        "00c01da8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841924.md#insn-00841974) · [`0084199c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841924.md#insn-0084199c)
- 新版 `00841974`（命令位置の公開資料なし） · `0084199c`（命令位置の公開資料なし）

~~~diff
- 00841974 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00841974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00841974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00841974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00841974 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00841974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00841974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00841974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00841974 bytes 08e13491
+ 00841974 bytes 08213691
- 0084199c ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0084199c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084199c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084199c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084199c ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0084199c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084199c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084199c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084199c bytes 08e13491
+ 0084199c bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d36c306f24310bd2a6cdfdeb72066fbc"></a>

### [`00841a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841a9c.md) → [`00841a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841a9c.md) FUN_00841a9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008412b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md) · 呼出先 7件 [`00842db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842db4.md) [`00842e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842e04.md) [`0084dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084dd1c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) · 呼出先 7件 [`00842db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842db4.md) [`00842e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e04.md) [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00841afc",
      "incomplete_value": false,
      "site": "00841afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841afc",
      "incomplete_value": false,
      "site": "00841afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "definition_site": "00841b1c",
      "incomplete_value": false,
      "site": "00841b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841b1c",
      "incomplete_value": false,
      "site": "00841b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "00841afc",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ],
    [
      "00841b1c",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ],
    [
      "00841b60",
      "READ",
      [
        "storage",
        "00c01dd8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00841afc",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ],
    [
      "00841b1c",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ],
    [
      "00841b60",
      "READ",
      [
        "storage",
        "00c01e28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841a9c.md#insn-00841aec) · [`00841b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841a9c.md#insn-00841b14)
- 新版 `00841aec`（命令位置の公開資料なし） · `00841b14`（命令位置の公開資料なし）

~~~diff
- 00841aec ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00841aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00841aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00841aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00841aec ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00841aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00841aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00841aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00841aec bytes 08e13691
+ 00841aec bytes 08213891
- 00841b14 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00841b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00841b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00841b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00841b14 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00841b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00841b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00841b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00841b14 bytes 08e13691
+ 00841b14 bytes 08213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd93dabb6cd3859dec86ebc56665a2db"></a>

### [`00841c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841c14.md) → [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) FUN_00841c14

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`008412b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md) [`00842a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842a50.md) [`00842e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842e88.md) [`00843d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843d2c.md) · 呼出先 16件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`00430dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430dd8.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md) [`008430b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/008430b0.md)
- 新版 呼出元 4件 [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) [`00842a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842a50.md) [`00842e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e88.md) [`00843d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843d2c.md) · 呼出先 16件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00430dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430dd8.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md) [`008430b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008430b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.90% / 新版 91.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00841c70",
      "incomplete_value": true,
      "site": "00841c70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:113:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841c70",
      "incomplete_value": true,
      "site": "00841c70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00841c78",
      "incomplete_value": true,
      "site": "00841c78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00841c78",
      "incomplete_value": true,
      "site": "00841c78",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00841cbc",
      "incomplete_value": true,
      "site": "00841ccc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d92:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841cbc",
      "incomplete_value": true,
      "site": "00841ccc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e1f:8"
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
      "00841c64",
      "READ",
      [
        "storage",
        "002981a0",
        null,
        "string"
      ]
    ],
    [
      "00841c68",
      "READ",
      [
        "storage",
        "002981a5",
        null,
        "string"
      ]
    ],
    [
      "00841cbc",
      "READ",
      [
        "storage",
        "00293e1f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00841c64",
      "READ",
      [
        "storage",
        "00298113",
        null,
        "string"
      ]
    ],
    [
      "00841c68",
      "READ",
      [
        "storage",
        "00298118",
        null,
        "string"
      ]
    ],
    [
      "00841cbc",
      "READ",
      [
        "storage",
        "00293d92",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841c14.md#insn-00841c5c) · [`00841cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841c14.md#insn-00841cb4) · [`00841d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841c14.md#insn-00841d04)
- 新版 `00841c5c`（命令位置の公開資料なし） · `00841cb4`（命令位置の公開資料なし） · `00841d04`（命令位置の公開資料なし）

~~~diff
- 00841c5c ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 00841c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00841c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00841c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00841c5c ["COPY", "tmp:0:8", ["const:113:8"]]
+ 00841c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00841c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00841c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00841c5c bytes 08810691
+ 00841c5c bytes 084d0491
- 00841cb4 ["COPY", "tmp:0:8", ["const:e1f:8"]]
- 00841cb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00841cb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00841cb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00841cb4 ["COPY", "tmp:0:8", ["const:d92:8"]]
+ 00841cb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00841cb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00841cb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00841cb4 bytes 297d3891
+ 00841cb4 bytes 29493691
- 00841d04 ["COPY", "tmp:0:8", ["const:f9f:8"]]
- 00841d04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00841d04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00841d04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00841d04 ["COPY", "tmp:0:8", ["const:f12:8"]]
+ 00841d04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00841d04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00841d04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00841d04 bytes 297d3e91
+ 00841d04 bytes 29493c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e05f9b44f4a322a8d0de084870d159db"></a>

### [`00842100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842100.md) → [`00842100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842100.md) FUN_00842100

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00842114",
      "incomplete_value": false,
      "site": "00842118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842114",
      "incomplete_value": false,
      "site": "00842118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00842118",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842118",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842100.md#insn-00842114)
- 新版 `00842114`（命令位置の公開資料なし）

~~~diff
- 00842114 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 00842114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842114 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00842114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842114 bytes 08e13091
+ 00842114 bytes 08213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d738b1285e8a05e243054c6d6fcffc54"></a>

### [`0084215c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084215c.md) → [`0084215c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084215c.md) FUN_0084215c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00842174",
      "incomplete_value": false,
      "site": "00842178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842174",
      "incomplete_value": false,
      "site": "00842178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "00842178",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842178",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084215c.md#insn-00842174)
- 新版 `00842174`（命令位置の公開資料なし）

~~~diff
- 00842174 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 00842174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842174 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00842174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842174 bytes 08e13091
+ 00842174 bytes 08213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c8dc7731f1662d6b07c855442077a29"></a>

### [`008421b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008421b8.md) → [`008421b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008421b8.md) FUN_008421b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "008421dc",
      "incomplete_value": false,
      "site": "008421e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008421dc",
      "incomplete_value": false,
      "site": "008421e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "008421e0",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008421e0",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008421dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008421b8.md#insn-008421dc)
- 新版 `008421dc`（命令位置の公開資料なし）

~~~diff
- 008421dc ["COPY", "tmp:0:8", ["const:c38:8"]]
- 008421dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008421dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008421dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008421dc ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 008421dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008421dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008421dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008421dc bytes 29e13091
+ 008421dc bytes 29213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4560b4f560ec33a72bfb79dcbbb5c19"></a>

### [`00842210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842210.md) → [`00842210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842210.md) FUN_00842210

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "00842218",
      "incomplete_value": false,
      "site": "0084221c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842218",
      "incomplete_value": false,
      "site": "0084221c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "0084221c",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084221c",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842210.md#insn-00842218)
- 新版 `00842218`（命令位置の公開資料なし）

~~~diff
- 00842218 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 00842218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00842218 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00842218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00842218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00842218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842218 bytes 29e13091
+ 00842218 bytes 29213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17639cb073e1a0065cdb41c208be6276"></a>

### [`008423bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008423bc.md) → [`008423bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md) FUN_008423bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008422ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008422ec.md) · 呼出先 7件 [`00841924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841924.md) [`00842708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842708.md) [`00842758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842758.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`008422ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008422ec.md) · 呼出先 7件 [`00841924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md) [`00842708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842708.md) [`00842758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842758.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00842458",
      "incomplete_value": false,
      "site": "00842458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842458",
      "incomplete_value": false,
      "site": "00842458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "definition_site": "00842474",
      "incomplete_value": false,
      "site": "00842474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842474",
      "incomplete_value": false,
      "site": "00842474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "00842458",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ],
    [
      "00842474",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ],
    [
      "008424bc",
      "READ",
      [
        "storage",
        "00c01cc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00842458",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ],
    [
      "00842474",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ],
    [
      "008424bc",
      "READ",
      [
        "storage",
        "00c01d18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008423bc.md#insn-00842448) · [`0084246c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008423bc.md#insn-0084246c)
- 新版 `00842448`（命令位置の公開資料なし） · `0084246c`（命令位置の公開資料なし）

~~~diff
- 00842448 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 00842448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842448 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00842448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842448 bytes 08a13291
+ 00842448 bytes 08e13391
- 0084246c ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 0084246c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084246c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084246c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084246c ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 0084246c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084246c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084246c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084246c bytes 08a13291
+ 0084246c bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd333c7c143117399fbe91e43d5085f3"></a>

### [`008425bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008425bc.md) → [`008425bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008425bc.md) FUN_008425bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "008425d0",
      "incomplete_value": false,
      "site": "008425d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008425d0",
      "incomplete_value": false,
      "site": "008425d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "008425d4",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008425d4",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008425d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008425bc.md#insn-008425d0)
- 新版 `008425d0`（命令位置の公開資料なし）

~~~diff
- 008425d0 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 008425d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008425d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008425d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008425d0 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 008425d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008425d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008425d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008425d0 bytes 08a13291
+ 008425d0 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d76d62d380c69b4712565734c3f2000d"></a>

### [`00842618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842618.md) → [`00842618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842618.md) FUN_00842618

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00842630",
      "incomplete_value": false,
      "site": "00842634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842630",
      "incomplete_value": false,
      "site": "00842634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "00842634",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842634",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842618.md#insn-00842630)
- 新版 `00842630`（命令位置の公開資料なし）

~~~diff
- 00842630 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 00842630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842630 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00842630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842630 bytes 08a13291
+ 00842630 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fa9c973a5c17e888f4d11a71e58793c"></a>

### [`00842674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842674.md) → [`00842674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842674.md) FUN_00842674

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00842698",
      "incomplete_value": false,
      "site": "0084269c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842698",
      "incomplete_value": false,
      "site": "0084269c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "0084269c",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084269c",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842674.md#insn-00842698)
- 新版 `00842698`（命令位置の公開資料なし）

~~~diff
- 00842698 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 00842698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00842698 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00842698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00842698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00842698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842698 bytes 29a13291
+ 00842698 bytes 29e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6898f30ecce32bc0c5be9e0de0f19ecc"></a>

### [`008426cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008426cc.md) → [`008426cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008426cc.md) FUN_008426cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "008426d4",
      "incomplete_value": false,
      "site": "008426d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008426d4",
      "incomplete_value": false,
      "site": "008426d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "008426d8",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008426d8",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008426d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008426cc.md#insn-008426d4)
- 新版 `008426d4`（命令位置の公開資料なし）

~~~diff
- 008426d4 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 008426d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008426d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008426d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008426d4 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 008426d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008426d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008426d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008426d4 bytes 29a13291
+ 008426d4 bytes 29e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a137122653d90bf033ae18deaaae399b"></a>

### [`00842830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842830.md) → [`00842830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842830.md) FUN_00842830

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00842844",
      "incomplete_value": false,
      "site": "00842848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842844",
      "incomplete_value": false,
      "site": "00842848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00842848",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842848",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842830.md#insn-00842844)
- 新版 `00842844`（命令位置の公開資料なし）

~~~diff
- 00842844 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00842844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842844 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00842844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842844 bytes 08e13491
+ 00842844 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2dd5097bfe1f8aad053b3160177ab2e"></a>

### [`0084288c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084288c.md) → [`0084288c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084288c.md) FUN_0084288c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "008428a4",
      "incomplete_value": false,
      "site": "008428a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008428a4",
      "incomplete_value": false,
      "site": "008428a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "008428a8",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008428a8",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008428a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084288c.md#insn-008428a4)
- 新版 `008428a4`（命令位置の公開資料なし）

~~~diff
- 008428a4 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 008428a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008428a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008428a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008428a4 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 008428a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008428a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008428a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008428a4 bytes 08e13491
+ 008428a4 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d423d4e07ed5d77e042c61d73098c9c8"></a>

### [`008428e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008428e8.md) → [`008428e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008428e8.md) FUN_008428e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0084290c",
      "incomplete_value": false,
      "site": "00842910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084290c",
      "incomplete_value": false,
      "site": "00842910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00842910",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842910",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084290c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008428e8.md#insn-0084290c)
- 新版 `0084290c`（命令位置の公開資料なし）

~~~diff
- 0084290c ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0084290c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084290c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084290c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084290c ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0084290c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084290c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084290c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084290c bytes 29e13491
+ 0084290c bytes 29213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1b8adb7f3d092259451e6c60a8cdfb9"></a>

### [`00842940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842940.md) → [`00842940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842940.md) FUN_00842940

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "00842948",
      "incomplete_value": false,
      "site": "0084294c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842948",
      "incomplete_value": false,
      "site": "0084294c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "0084294c",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084294c",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842940.md#insn-00842948)
- 新版 `00842948`（命令位置の公開資料なし）

~~~diff
- 00842948 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00842948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00842948 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00842948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00842948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00842948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842948 bytes 29e13491
+ 00842948 bytes 29213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d01c9b7633bf7a3002a8d4ae4e63ca3"></a>

### [`00842a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842a50.md) → [`00842a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842a50.md) FUN_00842a50

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00842a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842a1c.md) · 呼出先 6件 [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00841c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841c14.md) [`009bd60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd60c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00842a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842a1c.md) · 呼出先 6件 [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.16% / 新版 84.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00842aa0",
      "incomplete_value": true,
      "site": "00842ab0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842aa0",
      "incomplete_value": true,
      "site": "00842ab0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f50:8"
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
      "definition_site": "00842aa0",
      "incomplete_value": true,
      "site": "00842ab0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00842aa0",
      "incomplete_value": true,
      "site": "00842ab0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00842ab4",
      "incomplete_value": true,
      "site": "00842abc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00842ab4",
      "incomplete_value": true,
      "site": "00842abc",
      "value": [
        "LOAD",
        "16",
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
      "00842aa0",
      "READ",
      [
        "storage",
        "00294f50",
        null,
        "string"
      ]
    ],
    [
      "00842aa0",
      "READ",
      [
        "storage",
        "00294f60",
        null,
        "string"
      ]
    ],
    [
      "00842ab4",
      "READ",
      [
        "storage",
        "00294f70",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00842aa0",
      "READ",
      [
        "storage",
        "00294ec3",
        null,
        "string"
      ]
    ],
    [
      "00842aa0",
      "READ",
      [
        "storage",
        "00294ed3",
        null,
        "string"
      ]
    ],
    [
      "00842ab4",
      "READ",
      [
        "storage",
        "00294ee3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842a50.md#insn-00842a98) · [`00842a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842a50.md#insn-00842a9c)
- 新版 `00842a98`（命令位置の公開資料なし） · `00842a9c`（命令位置の公開資料なし）

~~~diff
- 00842a98 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00842a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842a98 ["COPY", "tmp:0:8", ["const:ec3:8"]]
+ 00842a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842a98 bytes 08413d91
+ 00842a98 bytes 080d3b91
- 00842a9c ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00842a9c bytes 69d3fff0
+ 00842a9c ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00842a9c bytes 69d3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d37f1c458c79bb40ae4cd6370c5b7442"></a>

### [`00842c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842c68.md) → [`00842c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842c68.md) FUN_00842c68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00842c7c",
      "incomplete_value": false,
      "site": "00842c80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842c7c",
      "incomplete_value": false,
      "site": "00842c80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00842c80",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842c80",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842c68.md#insn-00842c7c)
- 新版 `00842c7c`（命令位置の公開資料なし）

~~~diff
- 00842c7c ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00842c7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842c7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842c7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842c7c ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00842c7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842c7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842c7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842c7c bytes 08e13691
+ 00842c7c bytes 08213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37a0f0503b8918c8946ff79957c5ecea"></a>

### [`00842cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842cc4.md) → [`00842cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842cc4.md) FUN_00842cc4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00842cdc",
      "incomplete_value": false,
      "site": "00842ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842cdc",
      "incomplete_value": false,
      "site": "00842ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "00842ce0",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842ce0",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842cc4.md#insn-00842cdc)
- 新版 `00842cdc`（命令位置の公開資料なし）

~~~diff
- 00842cdc ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00842cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842cdc ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00842cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842cdc bytes 08e13691
+ 00842cdc bytes 08213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59a338f9841f735ea818d4edfcf014aa"></a>

### [`00842d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842d20.md) → [`00842d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842d20.md) FUN_00842d20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00842d44",
      "incomplete_value": false,
      "site": "00842d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842d44",
      "incomplete_value": false,
      "site": "00842d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00842d48",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842d48",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842d20.md#insn-00842d44)
- 新版 `00842d44`（命令位置の公開資料なし）

~~~diff
- 00842d44 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00842d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00842d44 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00842d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00842d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00842d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842d44 bytes 29e13691
+ 00842d44 bytes 29213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28072616310dfffc4efdafb6bebccbc6"></a>

### [`00842d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842d78.md) → [`00842d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842d78.md) FUN_00842d78

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "00842d80",
      "incomplete_value": false,
      "site": "00842d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842d80",
      "incomplete_value": false,
      "site": "00842d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "00842d84",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842d84",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842d78.md#insn-00842d80)
- 新版 `00842d80`（命令位置の公開資料なし）

~~~diff
- 00842d80 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00842d80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842d80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842d80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00842d80 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00842d80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00842d80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00842d80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842d80 bytes 29e13691
+ 00842d80 bytes 29213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24ee1b72b3df5c805623122fc5d0eb03"></a>

### [`00842e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842e88.md) → [`00842e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e88.md) FUN_00842e88

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00842e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842e54.md) · 呼出先 6件 [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00841c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841c14.md) [`009bd60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd60c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00842e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e54.md) · 呼出先 6件 [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00842ed8",
      "incomplete_value": true,
      "site": "00842ee8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d64:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842ed8",
      "incomplete_value": true,
      "site": "00842ee8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:df1:8"
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
      "definition_site": "00842ed8",
      "incomplete_value": true,
      "site": "00842ee8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00842ed8",
      "incomplete_value": true,
      "site": "00842ee8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00842eec",
      "incomplete_value": true,
      "site": "00842ef4",
      "value": [
        "LOAD",
        "16",
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
                "const:1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842eec",
      "incomplete_value": true,
      "site": "00842ef4",
      "value": [
        "LOAD",
        "16",
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
                "const:1d:8"
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
      "00842ed8",
      "READ",
      [
        "storage",
        "00293df1",
        null,
        "string"
      ]
    ],
    [
      "00842ed8",
      "READ",
      [
        "storage",
        "00293e01",
        null,
        "string"
      ]
    ],
    [
      "00842eec",
      "READ",
      [
        "storage",
        "00293e0e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00842ed8",
      "READ",
      [
        "storage",
        "00293d64",
        null,
        "string"
      ]
    ],
    [
      "00842ed8",
      "READ",
      [
        "storage",
        "00293d74",
        null,
        "string"
      ]
    ],
    [
      "00842eec",
      "READ",
      [
        "storage",
        "00293d81",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842e88.md#insn-00842ed0) · [`00842ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842e88.md#insn-00842ed4)
- 新版 `00842ed0`（命令位置の公開資料なし） · `00842ed4`（命令位置の公開資料なし）

~~~diff
- 00842ed0 ["COPY", "tmp:0:8", ["const:df1:8"]]
- 00842ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842ed0 ["COPY", "tmp:0:8", ["const:d64:8"]]
+ 00842ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842ed0 bytes 08c53791
+ 00842ed0 bytes 08913591
- 00842ed4 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00842ed4 bytes 69d3fff0
+ 00842ed4 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00842ed4 bytes 69d3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-765f1e5c48cad843eebedfda6cafdb37"></a>

### [`00843694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843694.md) → [`00843694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843694.md) FUN_00843694

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "008436b8",
      "incomplete_value": false,
      "site": "008436b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008436b8",
      "incomplete_value": false,
      "site": "008436b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "008436b8",
      "DATA",
      [
        "storage",
        "00c01e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008436b8",
      "DATA",
      [
        "storage",
        "00c01e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008436b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843694.md#insn-008436b4)
- 新版 `008436b4`（命令位置の公開資料なし）

~~~diff
- 008436b4 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 008436b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008436b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008436b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008436b4 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 008436b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008436b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008436b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008436b4 bytes 08e13891
+ 008436b4 bytes 08213a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59e2b94dd154fd6ae3a56f9309c16522"></a>

### [`008436c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/008436c8.md) → [`008436c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008436c8.md) FUN_008436c8

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
      "definition_site": "008436d4",
      "incomplete_value": true,
      "site": "008436d4",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008436d4",
      "incomplete_value": true,
      "site": "008436d4",
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
            "const:e38:8"
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
      "008436d4",
      "DATA",
      [
        "storage",
        "00c01e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008436d4",
      "DATA",
      [
        "storage",
        "00c01e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008436d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/008436c8.md#insn-008436d0)
- 新版 `008436d0`（命令位置の公開資料なし）

~~~diff
- 008436d0 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 008436d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008436d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008436d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008436d0 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 008436d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008436d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008436d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008436d0 bytes 29e13891
+ 008436d0 bytes 29213a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94e12313c4da2ecb3f8d98802c68d726"></a>

### [`0084372c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/0084372c.md) → [`0084372c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084372c.md) FUN_0084372c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00843740",
      "incomplete_value": false,
      "site": "00843744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843740",
      "incomplete_value": false,
      "site": "00843744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00843744",
      "DATA",
      [
        "storage",
        "00c01eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00843744",
      "DATA",
      [
        "storage",
        "00c01f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/0084372c.md#insn-00843740)
- 新版 `00843740`（命令位置の公開資料なし）

~~~diff
- 00843740 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00843740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00843740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00843740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00843740 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 00843740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00843740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00843740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00843740 bytes 08e13a91
+ 00843740 bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a24af3ce9defb4c1c303e46b4c809507"></a>

### [`00843788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843788.md) → [`00843788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843788.md) FUN_00843788

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "008437a0",
      "incomplete_value": false,
      "site": "008437a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008437a0",
      "incomplete_value": false,
      "site": "008437a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "008437a4",
      "DATA",
      [
        "storage",
        "00c01eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008437a4",
      "DATA",
      [
        "storage",
        "00c01f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008437a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843788.md#insn-008437a0)
- 新版 `008437a0`（命令位置の公開資料なし）

~~~diff
- 008437a0 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 008437a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008437a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008437a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008437a0 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 008437a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008437a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008437a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008437a0 bytes 08e13a91
+ 008437a0 bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4df6e6d60a392b58528a59ea9463641"></a>

### [`008437e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/008437e4.md) → [`008437e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008437e4.md) FUN_008437e4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00843808",
      "incomplete_value": false,
      "site": "0084380c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843808",
      "incomplete_value": false,
      "site": "0084380c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0084380c",
      "DATA",
      [
        "storage",
        "00c01eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084380c",
      "DATA",
      [
        "storage",
        "00c01f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/008437e4.md#insn-00843808)
- 新版 `00843808`（命令位置の公開資料なし）

~~~diff
- 00843808 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00843808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00843808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00843808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00843808 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 00843808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00843808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00843808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00843808 bytes 29e13a91
+ 00843808 bytes 29213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b10bf35ea2c6a1b3ad166a4bdc24bc28"></a>

### [`0084383c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/0084383c.md) → [`0084383c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084383c.md) FUN_0084383c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "00843844",
      "incomplete_value": false,
      "site": "00843848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843844",
      "incomplete_value": false,
      "site": "00843848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "00843848",
      "DATA",
      [
        "storage",
        "00c01eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00843848",
      "DATA",
      [
        "storage",
        "00c01f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/0084383c.md#insn-00843844)
- 新版 `00843844`（命令位置の公開資料なし）

~~~diff
- 00843844 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00843844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00843844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00843844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00843844 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 00843844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00843844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00843844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00843844 bytes 29e13a91
+ 00843844 bytes 29213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-093d596d2974c8b16f3375cdfcef5e5f"></a>

### [`0084394c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/0084394c.md) → [`0084394c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084394c.md) FUN_0084394c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00843918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843918.md) · 呼出先 6件 [`00843c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843c8c.md) [`00843cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843cdc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`00843918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843918.md) · 呼出先 6件 [`00843c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843c8c.md) [`00843cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843cdc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008439dc",
      "incomplete_value": false,
      "site": "008439dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008439dc",
      "incomplete_value": false,
      "site": "008439dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "008439f8",
      "incomplete_value": false,
      "site": "008439f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008439f8",
      "incomplete_value": false,
      "site": "008439f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "008439dc",
      "DATA",
      [
        "storage",
        "00c01f28",
        null,
        "undefined *"
      ]
    ],
    [
      "008439f8",
      "DATA",
      [
        "storage",
        "00c01f28",
        null,
        "undefined *"
      ]
    ],
    [
      "00843a40",
      "READ",
      [
        "storage",
        "00c01f48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008439dc",
      "DATA",
      [
        "storage",
        "00c01f78",
        null,
        "undefined *"
      ]
    ],
    [
      "008439f8",
      "DATA",
      [
        "storage",
        "00c01f78",
        null,
        "undefined *"
      ]
    ],
    [
      "00843a40",
      "READ",
      [
        "storage",
        "00c01f98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008439cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/0084394c.md#insn-008439cc) · [`008439f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/0084394c.md#insn-008439f0)
- 新版 `008439cc`（命令位置の公開資料なし） · `008439f0`（命令位置の公開資料なし）

~~~diff
- 008439cc ["COPY", "tmp:0:8", ["const:f28:8"]]
- 008439cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008439cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008439cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008439cc ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 008439cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008439cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008439cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008439cc bytes 08a13c91
+ 008439cc bytes 08e13d91
- 008439f0 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 008439f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008439f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008439f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008439f0 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 008439f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008439f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008439f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008439f0 bytes 08a13c91
+ 008439f0 bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8d24cbbd45f6df4f28c8c50afb495b3"></a>

### [`00843b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843b40.md) → [`00843b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843b40.md) FUN_00843b40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00843b54",
      "incomplete_value": false,
      "site": "00843b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843b54",
      "incomplete_value": false,
      "site": "00843b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "00843b58",
      "DATA",
      [
        "storage",
        "00c01f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00843b58",
      "DATA",
      [
        "storage",
        "00c01f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843b40.md#insn-00843b54)
- 新版 `00843b54`（命令位置の公開資料なし）

~~~diff
- 00843b54 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 00843b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00843b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00843b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00843b54 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 00843b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00843b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00843b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00843b54 bytes 08a13c91
+ 00843b54 bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d609372c9e2ea5cf52b837c160f60e2"></a>

### [`00843b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843b9c.md) → [`00843b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843b9c.md) FUN_00843b9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00843bb4",
      "incomplete_value": false,
      "site": "00843bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843bb4",
      "incomplete_value": false,
      "site": "00843bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "00843bb8",
      "DATA",
      [
        "storage",
        "00c01f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00843bb8",
      "DATA",
      [
        "storage",
        "00c01f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843b9c.md#insn-00843bb4)
- 新版 `00843bb4`（命令位置の公開資料なし）

~~~diff
- 00843bb4 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 00843bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00843bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00843bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00843bb4 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 00843bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00843bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00843bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00843bb4 bytes 08a13c91
+ 00843bb4 bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8b8bd4efe7c3f6713c8b7b0618e366d"></a>

### [`00843bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843bf8.md) → [`00843bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843bf8.md) FUN_00843bf8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00843c1c",
      "incomplete_value": false,
      "site": "00843c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843c1c",
      "incomplete_value": false,
      "site": "00843c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "00843c20",
      "DATA",
      [
        "storage",
        "00c01f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00843c20",
      "DATA",
      [
        "storage",
        "00c01f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843bf8.md#insn-00843c1c)
- 新版 `00843c1c`（命令位置の公開資料なし）

~~~diff
- 00843c1c ["COPY", "tmp:0:8", ["const:f28:8"]]
- 00843c1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00843c1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00843c1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00843c1c ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 00843c1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00843c1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00843c1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00843c1c bytes 29a13c91
+ 00843c1c bytes 29e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35593dee7ab0a3142208804d2c933a63"></a>

### [`00843c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843c50.md) → [`00843c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843c50.md) FUN_00843c50

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "00843c58",
      "incomplete_value": false,
      "site": "00843c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843c58",
      "incomplete_value": false,
      "site": "00843c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "00843c5c",
      "DATA",
      [
        "storage",
        "00c01f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00843c5c",
      "DATA",
      [
        "storage",
        "00c01f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843c50.md#insn-00843c58)
- 新版 `00843c58`（命令位置の公開資料なし）

~~~diff
- 00843c58 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 00843c58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00843c58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00843c58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00843c58 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 00843c58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00843c58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00843c58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00843c58 bytes 29a13c91
+ 00843c58 bytes 29e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b8db2301e5799a088180f6792b804a2"></a>

### [`00843db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843db4.md) → [`00843db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843db4.md) FUN_00843db4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00843db8",
      "incomplete_value": false,
      "site": "00843dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843db8",
      "incomplete_value": false,
      "site": "00843dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00843dbc",
      "DATA",
      [
        "storage",
        "00c01fb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00843dbc",
      "DATA",
      [
        "storage",
        "00c02008",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843db4.md#insn-00843db4) · [`00843db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843db4.md#insn-00843db8)
- 新版 `00843db4`（命令位置の公開資料なし） · `00843db8`（命令位置の公開資料なし）

~~~diff
- 00843db4 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00843db4 ["COPY", "register:4040:8", ["const:c02000:8"]]
- 00843db4 bytes e81d00d0
+ 00843db4 bytes e81d00f0
- 00843db8 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 00843db8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00843db8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00843db8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00843db8 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00843db8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00843db8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00843db8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00843db8 bytes 08e13e91
+ 00843db8 bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fbd2612d799be8968c8d693ef3f5d86"></a>

### [`00843e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843e04.md) → [`00843e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843e04.md) FUN_00843e04

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008443c8.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 2件 [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.47% / 新版 84.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00843e48",
      "incomplete_value": false,
      "site": "00843e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843e48",
      "incomplete_value": false,
      "site": "00843e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "definition_site": "00843eb0",
      "incomplete_value": true,
      "site": "00843eb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843eb0",
      "incomplete_value": true,
      "site": "00843eb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:315:8"
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
      "definition_site": "00843ec8",
      "incomplete_value": true,
      "site": "00843ec8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:47d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843ec8",
      "incomplete_value": true,
      "site": "00843ec8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e3:8"
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
      "00843e48",
      "DATA",
      [
        "storage",
        "00c02008",
        null,
        "undefined *"
      ]
    ],
    [
      "00843e7c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00843e9c",
      "READ",
      [
        "storage",
        "002a0315",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00843e48",
      "DATA",
      [
        "storage",
        "00c02058",
        null,
        "undefined *"
      ]
    ],
    [
      "00843e7c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00843e9c",
      "READ",
      [
        "storage",
        "002a03a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843e04.md#insn-00843e44) · [`00843e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843e04.md#insn-00843e78) · [`00843e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843e04.md#insn-00843e98)
- 新版 `00843e44`（命令位置の公開資料なし） · `00843e78`（命令位置の公開資料なし） · `00843e98`（命令位置の公開資料なし）

~~~diff
- 00843e44 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00843e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00843e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00843e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00843e44 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 00843e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00843e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00843e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00843e44 bytes 08210091
+ 00843e44 bytes 08610191
- 00843e78 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00843e78 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00843e78 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00843e78 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 00843e78 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00843e78 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 00843e78 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 00843e78 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00843e78 bytes 5ae30091
+ 00843e78 bytes 5ae30191
- 00843e98 ["COPY", "tmp:0:8", ["const:315:8"]]
- 00843e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00843e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00843e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00843e98 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00843e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00843e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00843e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00843e98 bytes 08550c91
+ 00843e98 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2191d9c044313f756d7323f68a3dfde5"></a>

### [`00844200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844200.md) → [`00844200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844200.md) FUN_00844200

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00844218",
      "incomplete_value": false,
      "site": "0084421c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00844218",
      "incomplete_value": false,
      "site": "0084421c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "0084421c",
      "DATA",
      [
        "storage",
        "00c02008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084421c",
      "DATA",
      [
        "storage",
        "00c02058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00844218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844200.md#insn-00844218)
- 新版 `00844218`（命令位置の公開資料なし）

~~~diff
- 00844218 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00844218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00844218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00844218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00844218 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 00844218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00844218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00844218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00844218 bytes 29210091
+ 00844218 bytes 29610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c27a3081f9087b4e1a5c5bbac01e4f86"></a>

### [`008442ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008442ac.md) → [`008442ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008442ac.md) FUN_008442ac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "008442c4",
      "incomplete_value": false,
      "site": "008442c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008442c4",
      "incomplete_value": false,
      "site": "008442c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "008442c8",
      "DATA",
      [
        "storage",
        "00c02008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008442c8",
      "DATA",
      [
        "storage",
        "00c02058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008442c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008442ac.md#insn-008442c4)
- 新版 `008442c4`（命令位置の公開資料なし）

~~~diff
- 008442c4 ["COPY", "tmp:0:8", ["const:8:8"]]
- 008442c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008442c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008442c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008442c4 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 008442c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008442c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008442c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008442c4 bytes 29210091
+ 008442c4 bytes 29610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-957b77253142e7c5698865ba23e4ef2e"></a>

### [`00844378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844378.md) → [`00844378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844378.md) FUN_00844378

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0084439c",
      "incomplete_value": false,
      "site": "0084439c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084439c",
      "incomplete_value": false,
      "site": "0084439c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:68:8"
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
      "0084439c",
      "DATA",
      [
        "storage",
        "00c02068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084439c",
      "DATA",
      [
        "storage",
        "00c020b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00844398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844378.md#insn-00844398)
- 新版 `00844398`（命令位置の公開資料なし）

~~~diff
- 00844398 ["COPY", "tmp:0:8", ["const:68:8"]]
- 00844398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00844398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00844398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00844398 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 00844398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00844398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00844398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00844398 bytes 08a10191
+ 00844398 bytes 08e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91042793f866a72f01852f0c8472346c"></a>

### [`008443ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008443ac.md) → [`008443ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443ac.md) FUN_008443ac

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
      "definition_site": "008443b8",
      "incomplete_value": false,
      "site": "008443b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008443b8",
      "incomplete_value": false,
      "site": "008443b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:68:8"
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
      "008443b8",
      "DATA",
      [
        "storage",
        "00c02068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008443b8",
      "DATA",
      [
        "storage",
        "00c020b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008443b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008443ac.md#insn-008443b4)
- 新版 `008443b4`（命令位置の公開資料なし）

~~~diff
- 008443b4 ["COPY", "tmp:0:8", ["const:68:8"]]
- 008443b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008443b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008443b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008443b4 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 008443b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008443b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008443b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008443b4 bytes 29a10191
+ 008443b4 bytes 29e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72bb41d069271101fd2a04b6e9349b87"></a>

### [`008443c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008443c8.md) → [`008443c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md) FUN_008443c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`004724fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00472/004724fc.md) [`00840d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d5c.md) [`00840d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d6c.md) [`00843df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843df4.md) [`00843e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843e04.md)
- 新版 呼出元 0件  · 呼出先 11件 [`004724fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004724fc.md) [`00840d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d5c.md) [`00840d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d6c.md) [`00843df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843df4.md) [`00843e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843e04.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.74% / 新版 97.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008444ec",
      "incomplete_value": false,
      "site": "008444f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008444ec",
      "incomplete_value": false,
      "site": "008444f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "00844480",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "pointer"
      ]
    ],
    [
      "008444cc",
      "READ",
      [
        "storage",
        "00c01b98",
        null,
        "undefined *"
      ]
    ],
    [
      "008444f8",
      "DATA",
      [
        "storage",
        "00c01fb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00844480",
      "DATA",
      [
        "storage",
        "00c01bd8",
        null,
        "pointer"
      ]
    ],
    [
      "008444cc",
      "READ",
      [
        "storage",
        "00c01be8",
        null,
        "undefined *"
      ]
    ],
    [
      "008444f8",
      "DATA",
      [
        "storage",
        "00c02008",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00844474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008443c8.md#insn-00844474) · [`008444e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008443c8.md#insn-008444e8) · [`008444ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008443c8.md#insn-008444ec)
- 新版 `00844474`（命令位置の公開資料なし） · `008444e8`（命令位置の公開資料なし） · `008444ec`（命令位置の公開資料なし）

~~~diff
- 00844474 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00844474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00844474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00844474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00844474 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00844474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00844474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00844474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00844474 bytes 08212e91
+ 00844474 bytes 08612f91
- 008444e8 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 008444e8 ["COPY", "register:4040:8", ["const:c02000:8"]]
- 008444e8 bytes e81d00b0
+ 008444e8 bytes e81d00d0
- 008444ec ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 008444ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008444ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008444ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008444ec ["COPY", "tmp:0:8", ["const:8:8"]]
+ 008444ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008444ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008444ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008444ec bytes 08e13e91
+ 008444ec bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-522f5604cf0464eb48dfaf8276c1c2ad"></a>

### [`00844694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844694.md) → [`00844694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844694.md) FUN_00844694

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "008446b8",
      "incomplete_value": false,
      "site": "008446b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008446b8",
      "incomplete_value": false,
      "site": "008446b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "008446b8",
      "DATA",
      [
        "storage",
        "00c020e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008446b8",
      "DATA",
      [
        "storage",
        "00c02138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008446b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844694.md#insn-008446b4)
- 新版 `008446b4`（命令位置の公開資料なし）

~~~diff
- 008446b4 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 008446b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008446b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008446b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008446b4 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 008446b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008446b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008446b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008446b4 bytes 08a10391
+ 008446b4 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ddfa3043a8ae2f5b8c5922e99c36388"></a>

### [`008446c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008446c8.md) → [`008446c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008446c8.md) FUN_008446c8

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
      "definition_site": "008446d4",
      "incomplete_value": false,
      "site": "008446d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008446d4",
      "incomplete_value": false,
      "site": "008446d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "008446d4",
      "DATA",
      [
        "storage",
        "00c020e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008446d4",
      "DATA",
      [
        "storage",
        "00c02138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008446d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008446c8.md#insn-008446d0)
- 新版 `008446d0`（命令位置の公開資料なし）

~~~diff
- 008446d0 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 008446d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008446d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008446d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008446d0 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 008446d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008446d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008446d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008446d0 bytes 29a10391
+ 008446d0 bytes 29e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28512aea6d071ef9a286d8f71f6ac1bb"></a>

### [`00844848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844848.md) → [`00844848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844848.md) _INIT_152

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00844884",
      "incomplete_value": true,
      "site": "008448a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00844884",
      "incomplete_value": true,
      "site": "008448a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008448a8",
      "incomplete_value": true,
      "site": "008448c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008448a8",
      "incomplete_value": true,
      "site": "008448c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008448c8",
      "incomplete_value": true,
      "site": "008448e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008448c8",
      "incomplete_value": true,
      "site": "008448e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00844884",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008448a8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008448c8",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00844884",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "008448a8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "008448c8",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00844874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844848.md#insn-00844874) · [`0084487c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844848.md#insn-0084487c)
- 新版 `00844874`（命令位置の公開資料なし） · `0084487c`（命令位置の公開資料なし）

~~~diff
- 00844874 ["COPY", "tmp:0:8", ["const:300:8"]]
- 00844874 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00844874 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00844874 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00844874 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00844874 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00844874 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00844874 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00844874 bytes 73020c91
+ 00844874 bytes 73020d91
- 0084487c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0084487c bytes 09d3fff0
+ 0084487c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0084487c bytes 09d3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc530e891374ccb2318ba6ab0d2cda32"></a>

### [`00844bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844bd8.md) → [`00844bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) FUN_00844bd8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008406e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406e4.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004215a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md) [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md)
- 新版 呼出元 1件 [`008406e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`004215a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md) [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00844c54",
      "incomplete_value": true,
      "site": "00844c64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d6a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00844c54",
      "incomplete_value": true,
      "site": "00844c64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cd0:8"
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
      "definition_site": "00844c58",
      "incomplete_value": true,
      "site": "00844c68",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00844c58",
      "incomplete_value": true,
      "site": "00844c68",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00844c9c",
      "incomplete_value": true,
      "site": "00844c9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:9c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00844c9c",
      "incomplete_value": true,
      "site": "00844c9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:9c5:8"
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
      "00844c54",
      "READ",
      [
        "storage",
        "002a6cd0",
        null,
        "string"
      ]
    ],
    [
      "00844c58",
      "READ",
      [
        "storage",
        "002a6cdf",
        null,
        "string"
      ]
    ],
    [
      "00844c8c",
      "READ",
      [
        "storage",
        "0029b9c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00844c54",
      "READ",
      [
        "storage",
        "002a6d6a",
        null,
        "string"
      ]
    ],
    [
      "00844c58",
      "READ",
      [
        "storage",
        "002a6d79",
        null,
        "string"
      ]
    ],
    [
      "00844c8c",
      "READ",
      [
        "storage",
        "0029b9c3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008450a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844bd8.md#insn-008450a0) · [`008452a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844bd8.md#insn-008452a4) · [`00844c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844bd8.md#insn-00844c4c)
- 新版 `008450a0`（命令位置の公開資料なし） · `008452a4`（命令位置の公開資料なし） · `00844c4c`（命令位置の公開資料なし）

~~~diff
- 008450a0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 008450a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:330:8"]]
- 008450a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 008450a0 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 008450a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:370:8"]]
+ 008450a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008450a0 bytes 09c10c39
+ 008450a0 bytes 09c10d39
- 008452a4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 008452a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008452a4 ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:330:8"]]
- 008452a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 008452a4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 008452a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 008452a4 ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:370:8"]]
+ 008452a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 008452a4 bytes 1fc10c39
+ 008452a4 bytes 1fc10d39
- 00844c4c ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00844c4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00844c4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00844c4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00844c4c ["COPY", "tmp:0:8", ["const:d6a:8"]]
+ 00844c4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00844c4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00844c4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00844c4c bytes 08413391
+ 00844c4c bytes 08a93591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aef9689f4dd97e82b3f4be2dd3aa909b"></a>

### [`00845744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845744.md) → [`00845744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845744.md) FUN_00845744

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`00574bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bb4.md) [`00574f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574f70.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) [`00845a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845a24.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00574bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bb4.md) [`00574f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f70.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`00845a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845a24.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008458a0",
      "incomplete_value": false,
      "site": "008458a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:544:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008458a0",
      "incomplete_value": false,
      "site": "008458a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:5d1:8"
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
      "008458a0",
      "PARAM",
      [
        "storage",
        "002945d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008458a0",
      "PARAM",
      [
        "storage",
        "00294544",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008458a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845744.md#insn-008458a0)
- 新版 `008458a0`（命令位置の公開資料なし）

~~~diff
- 008458a0 ["COPY", "tmp:0:8", ["const:5d1:8"]]
- 008458a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008458a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008458a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008458a0 ["COPY", "tmp:0:8", ["const:544:8"]]
+ 008458a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008458a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008458a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008458a0 bytes 21441791
+ 008458a0 bytes 21101591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfed48d4fb189bea6018faff0c3308bf"></a>

### [`00845b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845b6c.md) → [`00845b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845b6c.md) _INIT_153

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00845ba8",
      "incomplete_value": true,
      "site": "00845bc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00845ba8",
      "incomplete_value": true,
      "site": "00845bc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00845bcc",
      "incomplete_value": true,
      "site": "00845be8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00845bcc",
      "incomplete_value": true,
      "site": "00845be8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00845bec",
      "incomplete_value": true,
      "site": "00845c08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00845bec",
      "incomplete_value": true,
      "site": "00845c08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00845ba8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00845bcc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00845bec",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00845ba8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00845bcc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00845bec",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00845b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845b6c.md#insn-00845b98) · [`00845ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845b6c.md#insn-00845ba0)
- 新版 `00845b98`（命令位置の公開資料なし） · `00845ba0`（命令位置の公開資料なし）

~~~diff
- 00845b98 ["COPY", "tmp:0:8", ["const:318:8"]]
- 00845b98 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00845b98 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00845b98 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00845b98 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00845b98 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00845b98 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00845b98 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00845b98 bytes 73620c91
+ 00845b98 bytes 73620d91
- 00845ba0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00845ba0 bytes 09d3ffd0
+ 00845ba0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00845ba0 bytes 09d3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49031276d486a706cdb447e9492cf657"></a>

### [`008460c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/008460c4.md) → [`008460c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008460c4.md) FUN_008460c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 19件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`006c4ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c4/006c4ea8.md) [`006d584c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d584c.md) [`006e34b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e3/006e34b0.md) [`007317b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00731/007317b0.md) · 呼出先 6件 [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) [`0084642c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/0084642c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md)
- 新版 呼出元 19件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`006c4ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c4/006c4ea8.md) [`006d584c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d584c.md) [`006e34b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e3/006e34b0.md) [`007317b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/007317b0.md) · 呼出先 6件 [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`0084642c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/0084642c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00846184",
      "incomplete_value": false,
      "site": "00846184",
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
            "const:bc9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846184",
      "incomplete_value": false,
      "site": "00846184",
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
            "const:b3e:8"
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
      "definition_site": "008461f4",
      "incomplete_value": false,
      "site": "008461f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:37d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008461f4",
      "incomplete_value": false,
      "site": "008461f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:40a:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00846264",
      "incomplete_value": false,
      "site": "00846264",
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
            "const:b6f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846264",
      "incomplete_value": false,
      "site": "00846264",
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
            "const:ae4:8"
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
      "00846184",
      "DATA",
      [
        "storage",
        "0029fb3e",
        null,
        null
      ]
    ],
    [
      "008461cc",
      "DATA",
      [
        "storage",
        "0029fb3e",
        null,
        null
      ]
    ],
    [
      "008461f4",
      "DATA",
      [
        "storage",
        "0029940a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00846184",
      "DATA",
      [
        "storage",
        "0029fbc9",
        null,
        null
      ]
    ],
    [
      "008461cc",
      "DATA",
      [
        "storage",
        "0029fbc9",
        null,
        null
      ]
    ],
    [
      "008461f4",
      "DATA",
      [
        "storage",
        "0029937d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084617c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/008460c4.md#insn-0084617c) · [`008461f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/008460c4.md#insn-008461f0) · [`00846260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/008460c4.md#insn-00846260)
- 新版 `0084617c`（命令位置の公開資料なし） · `008461f0`（命令位置の公開資料なし） · `00846260`（命令位置の公開資料なし）

~~~diff
- 0084617c ["COPY", "tmp:0:8", ["const:b3e:8"]]
- 0084617c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084617c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084617c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084617c ["COPY", "tmp:0:8", ["const:bc9:8"]]
+ 0084617c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084617c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084617c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084617c bytes 08f92c91
+ 0084617c bytes 08252f91
- 008461f0 ["COPY", "tmp:0:8", ["const:40a:8"]]
- 008461f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008461f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008461f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008461f0 ["COPY", "tmp:0:8", ["const:37d:8"]]
+ 008461f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008461f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008461f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008461f0 bytes 08291091
+ 008461f0 bytes 08f50d91
- 00846260 ["COPY", "tmp:0:8", ["const:ae4:8"]]
- 00846260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00846260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00846260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00846260 ["COPY", "tmp:0:8", ["const:b6f:8"]]
+ 00846260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00846260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00846260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00846260 bytes 08912b91
+ 00846260 bytes 08bd2d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cec3772d3c5d799101b5a5af87b509cf"></a>

### [`0084642c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/0084642c.md) → [`0084642c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/0084642c.md) FUN_0084642c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`008460c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/008460c4.md) [`008468c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/008468c0.md) [`00846bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846bac.md) [`00846bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846bc4.md) [`00846f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846f70.md) · 呼出先 11件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00759ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759ddc.md) [`00adca98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adca98.md)
- 新版 呼出元 5件 [`008460c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008460c4.md) [`008468c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008468c0.md) [`00846bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846bac.md) [`00846bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846bc4.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) · 呼出先 11件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`00759ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759ddc.md) [`00adcadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 93.97% / 新版 93.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008464c4",
      "incomplete_value": false,
      "site": "008464c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:962:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008464c4",
      "incomplete_value": false,
      "site": "008464c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:8d7:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084658c"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00846590",
      "incomplete_value": false,
      "site": "00846590",
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
            "const:bce:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846590",
      "incomplete_value": false,
      "site": "00846590",
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
            "const:b43:8"
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
      "008464c4",
      "DATA",
      [
        "storage",
        "002a28d7",
        null,
        null
      ]
    ],
    [
      "008464e8",
      "DATA",
      [
        "storage",
        "002a28d7",
        null,
        null
      ]
    ],
    [
      "unmatched:0084658c",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008464c4",
      "DATA",
      [
        "storage",
        "002a2962",
        null,
        null
      ]
    ],
    [
      "008464e8",
      "DATA",
      [
        "storage",
        "002a2962",
        null,
        null
      ]
    ],
    [
      "0084658c",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084658c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/0084642c.md#insn-0084658c) · [`00846608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/0084642c.md#insn-00846608)
- 新版 `0084658c`（命令位置の公開資料なし）

~~~diff
- 0084658c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0084658c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0084658c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 0084658c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 0084658c bytes bf031cb8
+ 0084658c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0084658c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0084658c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
+ 0084658c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
+ 0084658c bytes bf031cb8
- 00846608 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00846608 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00846608 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 00846608 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00846608 bytes bf031cb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8712101279e9ef3bf4925fb83c158649"></a>

### [`008468c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/008468c0.md) → [`008468c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008468c0.md) FUN_008468c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`005ec96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ec96c.md) [`00670a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670a9c.md) [`006f5fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f5/006f5fe8.md) [`008d9aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d9aa4.md) [`009121c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00912/009121c4.md) · 呼出先 6件 [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) [`0084642c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/0084642c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md)
- 新版 呼出元 5件 [`005ec96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ec96c.md) [`00670a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md) [`006f5fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f5/006f5fe8.md) [`008d9aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d9/008d9aa4.md) [`009121c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00912/009121c4.md) · 呼出先 6件 [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`0084642c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/0084642c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00846970",
      "incomplete_value": false,
      "site": "00846970",
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
            "const:bc9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846970",
      "incomplete_value": false,
      "site": "00846970",
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
            "const:b3e:8"
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
      "definition_site": "008469e4",
      "incomplete_value": false,
      "site": "008469e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:37d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008469e4",
      "incomplete_value": false,
      "site": "008469e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:40a:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00846a54",
      "incomplete_value": false,
      "site": "00846a54",
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
            "const:b6f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846a54",
      "incomplete_value": false,
      "site": "00846a54",
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
            "const:ae4:8"
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
      "00846970",
      "DATA",
      [
        "storage",
        "0029fb3e",
        null,
        null
      ]
    ],
    [
      "008469b8",
      "DATA",
      [
        "storage",
        "0029fb3e",
        null,
        null
      ]
    ],
    [
      "008469e4",
      "DATA",
      [
        "storage",
        "0029940a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00846970",
      "DATA",
      [
        "storage",
        "0029fbc9",
        null,
        null
      ]
    ],
    [
      "008469b8",
      "DATA",
      [
        "storage",
        "0029fbc9",
        null,
        null
      ]
    ],
    [
      "008469e4",
      "DATA",
      [
        "storage",
        "0029937d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00846968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/008468c0.md#insn-00846968) · [`0084696c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/008468c0.md#insn-0084696c)
- 新版 `00846968`（命令位置の公開資料なし） · `0084696c`（命令位置の公開資料なし）

~~~diff
- 00846968 ["COPY", "tmp:0:8", ["const:b3e:8"]]
- 00846968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00846968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00846968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00846968 ["COPY", "tmp:0:8", ["const:bc9:8"]]
+ 00846968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00846968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00846968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00846968 bytes 08f92c91
+ 00846968 bytes 08252f91
- 0084696c ["INT_SUB", "register:40c8:8", ["register:40e8:8", "const:40:8"]]
- 0084696c bytes b90301d1
+ 0084696c ["INT_SUB", "register:40c8:8", ["register:40e8:8", "const:40:8"]]
+ 0084696c bytes b90301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4ba092baefdeb936694a440e7641b11"></a>

### [`00846bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846bdc.md) → [`00846bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846bdc.md) FUN_00846bdc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00733548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00733/00733548.md) · 呼出先 11件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00759ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759ddc.md) [`00adca98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adca98.md)
- 新版 呼出元 1件 [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) · 呼出先 11件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`00759ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759ddc.md) [`00adcadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md)

変更の種類 call_argument_candidate, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 94.35% / 新版 94.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00846c64",
      "incomplete_value": false,
      "site": "00846c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:962:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846c64",
      "incomplete_value": false,
      "site": "00846c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:8d7:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846d2c"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00846d30",
      "incomplete_value": false,
      "site": "00846d30",
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
            "const:bce:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846d30",
      "incomplete_value": false,
      "site": "00846d30",
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
            "const:b43:8"
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
      "00846c64",
      "DATA",
      [
        "storage",
        "002a28d7",
        null,
        null
      ]
    ],
    [
      "00846c88",
      "DATA",
      [
        "storage",
        "002a28d7",
        null,
        null
      ]
    ],
    [
      "unmatched:00846d2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00846c64",
      "DATA",
      [
        "storage",
        "002a2962",
        null,
        null
      ]
    ],
    [
      "00846c88",
      "DATA",
      [
        "storage",
        "002a2962",
        null,
        null
      ]
    ],
    [
      "00846d2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00846d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846bdc.md#insn-00846d2c) · [`00846da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846bdc.md#insn-00846da8)
- 新版 `00846d2c`（命令位置の公開資料なし）

~~~diff
- 00846d2c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00846d2c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00846d2c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 00846d2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00846d2c bytes bf031cb8
+ 00846d2c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00846d2c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00846d2c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
+ 00846d2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
+ 00846d2c bytes bf031cb8
- 00846da8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00846da8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00846da8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 00846da8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00846da8 bytes bf031cb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be7020476faba78432c08e57da3f659a"></a>

### [`00846f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846f88.md) → [`00846f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f88.md) _INIT_154

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00846fc4",
      "incomplete_value": true,
      "site": "00846fe0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846fc4",
      "incomplete_value": true,
      "site": "00846fe0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00846fe8",
      "incomplete_value": true,
      "site": "00847004",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846fe8",
      "incomplete_value": true,
      "site": "00847004",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00847008",
      "incomplete_value": true,
      "site": "00847024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00847008",
      "incomplete_value": true,
      "site": "00847024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00846fc4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00846fe8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00847008",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00846fc4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00846fe8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00847008",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00846fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846f88.md#insn-00846fb4) · [`00846fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846f88.md#insn-00846fbc)
- 新版 `00846fb4`（命令位置の公開資料なし） · `00846fbc`（命令位置の公開資料なし）

~~~diff
- 00846fb4 ["COPY", "tmp:0:8", ["const:338:8"]]
- 00846fb4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00846fb4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00846fb4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00846fb4 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00846fb4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00846fb4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00846fb4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00846fb4 bytes 73e20c91
+ 00846fb4 bytes 73e20d91
- 00846fbc ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00846fbc bytes 09d3ffb0
+ 00846fbc ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00846fbc bytes 09d3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97764c3ed3aa142a52f3763dc326ec24"></a>

### [`00847318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/00847318.md) → [`00847318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847318.md) FUN_00847318

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0084914c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/0084914c.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00470ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470ac0.md) [`0053f81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f81c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0084914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/0084914c.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00470ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ac0.md) [`0053f81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00847354",
      "incomplete_value": false,
      "site": "00847360",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00847354",
      "incomplete_value": false,
      "site": "00847360",
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
            "const:388:8"
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
      "definition_site": "008473a4",
      "incomplete_value": false,
      "site": "008473ac",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008473a4",
      "incomplete_value": false,
      "site": "008473ac",
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
            "const:370:8"
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
      "00847354",
      "PARAM",
      [
        "storage",
        "0109e388",
        null,
        "undefined2"
      ]
    ],
    [
      "008473a4",
      "PARAM",
      [
        "storage",
        "0109e370",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00847354",
      "PARAM",
      [
        "storage",
        "0109e3c8",
        null,
        "undefined2"
      ]
    ],
    [
      "008473a4",
      "PARAM",
      [
        "storage",
        "0109e3b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00847354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/00847318.md#insn-00847354) · [`008473a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/00847318.md#insn-008473a4)
- 新版 `00847354`（命令位置の公開資料なし） · `008473a4`（命令位置の公開資料なし）

~~~diff
- 00847354 ["COPY", "tmp:0:8", ["const:388:8"]]
- 00847354 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00847354 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00847354 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00847354 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 00847354 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00847354 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00847354 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00847354 bytes 21200e91
+ 00847354 bytes 21200f91
- 008473a4 ["COPY", "tmp:0:8", ["const:370:8"]]
- 008473a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008473a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008473a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008473a4 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 008473a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008473a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008473a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008473a4 bytes 21c00d91
+ 008473a4 bytes 21c00e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb510c572f81b65eb79a40fc72eb722c"></a>

### [`00847488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/00847488.md) → [`00847488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847488.md) _INIT_155

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.92% / 新版 85.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008474c4",
      "incomplete_value": true,
      "site": "008474e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008474c4",
      "incomplete_value": true,
      "site": "008474e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00847528",
      "incomplete_value": true,
      "site": "00847540",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00847528",
      "incomplete_value": true,
      "site": "00847540",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00847544",
      "incomplete_value": true,
      "site": "00847560",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:36c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00847544",
      "incomplete_value": true,
      "site": "00847560",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:36e:8"
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
      "008474c4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008474e8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00847508",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008474c4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "008474e8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00847508",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008474b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/00847488.md#insn-008474b4) · [`008474bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/00847488.md#insn-008474bc)
- 新版 `008474b4`（命令位置の公開資料なし） · `008474bc`（命令位置の公開資料なし）

~~~diff
- 008474b4 ["COPY", "tmp:0:8", ["const:350:8"]]
- 008474b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008474b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008474b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008474b4 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 008474b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008474b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008474b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008474b4 bytes 73420d91
+ 008474b4 bytes 73420e91
- 008474bc ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008474bc bytes 09d3ff90
+ 008474bc ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008474bc bytes 09d3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f598040e20fdbeff5ea66680496cf0c6"></a>

### [`00847a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/00847a5c.md) → [`00847a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847a5c.md) FUN_00847a5c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058d260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058d/0058d260.md) · 呼出先 11件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00848b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848b34.md) [`00848bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848bc0.md) [`00848e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848e34.md) [`008490cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008490cc.md)
- 新版 呼出元 1件 [`0058d260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058d260.md) · 呼出先 11件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00848b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848b34.md) [`00848bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848bc0.md) [`00848e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848e34.md) [`008490cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/008490cc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00847c9c",
      "incomplete_value": false,
      "site": "00847c9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00847c9c",
      "incomplete_value": false,
      "site": "00847c9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "00847ae0",
      "READ",
      [
        "storage",
        "00297093",
        null,
        null
      ]
    ],
    [
      "00847ae0",
      "READ",
      [
        "storage",
        "002970a3",
        null,
        null
      ]
    ],
    [
      "00847ae4",
      "READ",
      [
        "storage",
        "002970b3",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00847ae0",
      "READ",
      [
        "storage",
        "00297006",
        null,
        null
      ]
    ],
    [
      "00847ae0",
      "READ",
      [
        "storage",
        "00297016",
        null,
        null
      ]
    ],
    [
      "00847ae4",
      "READ",
      [
        "storage",
        "00297026",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00847ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/00847a5c.md#insn-00847ad8) · [`00847c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/00847a5c.md#insn-00847c94)
- 新版 `00847ad8`（命令位置の公開資料なし） · `00847c94`（命令位置の公開資料なし）

~~~diff
- 00847ad8 ["COPY", "tmp:0:8", ["const:93:8"]]
- 00847ad8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00847ad8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00847ad8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00847ad8 ["COPY", "tmp:0:8", ["const:6:8"]]
+ 00847ad8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00847ad8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00847ad8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00847ad8 bytes 294d0291
+ 00847ad8 bytes 29190091
- 00847c94 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 00847c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00847c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00847c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00847c94 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 00847c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00847c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00847c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00847c94 bytes 08810791
+ 00847c94 bytes 08c10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10b59c4123bee8fc160e4a7c51a9bdfd"></a>

### [`00848250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848250.md) → [`00848250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848250.md) FUN_00848250

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008480ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/008480ec.md) [`0084914c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/0084914c.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00848b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848b34.md) [`00848bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848bc0.md) [`00849548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849548.md) [`0084967c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/0084967c.md)
- 新版 呼出元 2件 [`008480ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/008480ec.md) [`0084914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/0084914c.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00848b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848b34.md) [`00848bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848bc0.md) [`00849548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849548.md) [`0084967c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/0084967c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0084836c",
      "incomplete_value": false,
      "site": "0084836c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084836c",
      "incomplete_value": false,
      "site": "0084836c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "0084836c",
      "DATA",
      [
        "storage",
        "00c02270",
        null,
        "pointer"
      ]
    ],
    [
      "008483b0",
      "READ",
      [
        "storage",
        "00c02280",
        null,
        "undefined *"
      ]
    ],
    [
      "00848424",
      "READ",
      [
        "storage",
        "00c02298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084836c",
      "DATA",
      [
        "storage",
        "00c022c0",
        null,
        "pointer"
      ]
    ],
    [
      "008483b0",
      "READ",
      [
        "storage",
        "00c022d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00848424",
      "READ",
      [
        "storage",
        "00c022e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00848364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848250.md#insn-00848364)
- 新版 `00848364`（命令位置の公開資料なし）

~~~diff
- 00848364 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00848364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00848364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00848364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00848364 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00848364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00848364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00848364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00848364 bytes 08c10991
+ 00848364 bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e51ec1173fea82dcd7b73128fe995f4"></a>

### [`0084859c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/0084859c.md) → [`0084859c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/0084859c.md) FUN_0084859c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058ecd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ecd8.md) · 呼出先 12件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00848b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848b34.md) [`00848bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848bc0.md) [`008499bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008499bc.md) [`00849c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849c54.md)
- 新版 呼出元 1件 [`0058ecd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ecd8.md) · 呼出先 12件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00848b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848b34.md) [`00848bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848bc0.md) [`008499bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/008499bc.md) [`00849c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849c54.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.14% / 新版 96.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084862c",
      "incomplete_value": true,
      "site": "00848638",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0084862c",
      "incomplete_value": true,
      "site": "00848638",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00848628",
      "incomplete_value": true,
      "site": "0084863c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
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
      "definition_site": "00848628",
      "incomplete_value": true,
      "site": "0084863c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:93:8"
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
      "definition_site": "00848628",
      "incomplete_value": true,
      "site": "0084863c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00848628",
      "incomplete_value": true,
      "site": "0084863c",
      "value": [
        "LOAD",
        "16",
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
      "00848628",
      "READ",
      [
        "storage",
        "00297093",
        null,
        null
      ]
    ],
    [
      "00848628",
      "READ",
      [
        "storage",
        "002970a3",
        null,
        null
      ]
    ],
    [
      "0084862c",
      "READ",
      [
        "storage",
        "002970b3",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00848628",
      "READ",
      [
        "storage",
        "00297006",
        null,
        null
      ]
    ],
    [
      "00848628",
      "READ",
      [
        "storage",
        "00297016",
        null,
        null
      ]
    ],
    [
      "0084862c",
      "READ",
      [
        "storage",
        "00297026",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00848620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/0084859c.md#insn-00848620) · [`00848624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/0084859c.md#insn-00848624)
- 新版 `00848620`（命令位置の公開資料なし） · `00848624`（命令位置の公開資料なし）

~~~diff
- 00848620 ["COPY", "tmp:0:8", ["const:93:8"]]
- 00848620 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00848620 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00848620 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00848620 ["COPY", "tmp:0:8", ["const:6:8"]]
+ 00848620 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00848620 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00848620 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00848620 bytes 294d0291
+ 00848620 bytes 29190091
- 00848624 ["COPY", "register:4050:8", ["const:2b1000:8"]]
- 00848624 bytes 4ad3ffb0
+ 00848624 ["COPY", "register:4050:8", ["const:2b1000:8"]]
+ 00848624 bytes 4ad3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc62010e67be24198c3a5d9868e245a3"></a>

### [`00848d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848d18.md) → [`00848d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848d18.md) FUN_00848d18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00848d30",
      "incomplete_value": false,
      "site": "00848d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00848d30",
      "incomplete_value": false,
      "site": "00848d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "00848d40",
      "DATA",
      [
        "storage",
        "00c021e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00848d40",
      "DATA",
      [
        "storage",
        "00c02230",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00848d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848d18.md#insn-00848d30)
- 新版 `00848d30`（命令位置の公開資料なし）

~~~diff
- 00848d30 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 00848d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00848d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00848d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00848d30 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 00848d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00848d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00848d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00848d30 bytes 08810791
+ 00848d30 bytes 08c10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89e036ad81f8f93bcec46ec6fd20abfb"></a>

### [`00848da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848da8.md) → [`00848da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848da8.md) FUN_00848da8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00848dc0",
      "incomplete_value": false,
      "site": "00848dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00848dc0",
      "incomplete_value": false,
      "site": "00848dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "00848dd0",
      "DATA",
      [
        "storage",
        "00c021e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00848dd0",
      "DATA",
      [
        "storage",
        "00c02230",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00848dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848da8.md#insn-00848dc0)
- 新版 `00848dc0`（命令位置の公開資料なし）

~~~diff
- 00848dc0 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 00848dc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00848dc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00848dc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00848dc0 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 00848dc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00848dc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00848dc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00848dc0 bytes 08810791
+ 00848dc0 bytes 08c10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5adb7e17df55e4989e9bf8e9e773e82c"></a>

### [`00848e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848e34.md) → [`00848e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848e34.md) FUN_00848e34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00847a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/00847a5c.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00847a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847a5c.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00848e64",
      "incomplete_value": false,
      "site": "00848e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00848e64",
      "incomplete_value": false,
      "site": "00848e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "00848e64",
      "DATA",
      [
        "storage",
        "00c021e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00848e64",
      "DATA",
      [
        "storage",
        "00c02230",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00848e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848e34.md#insn-00848e5c)
- 新版 `00848e5c`（命令位置の公開資料なし）

~~~diff
- 00848e5c ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 00848e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00848e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00848e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00848e5c ["COPY", "tmp:0:8", ["const:230:8"]]
+ 00848e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00848e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00848e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00848e5c bytes 08810791
+ 00848e5c bytes 08c10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4138c17b0048cd4faddad49de4e6a98"></a>

### [`008494a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008494a8.md) → [`008494a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/008494a8.md) FUN_008494a8

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
      "definition_site": "008494b4",
      "incomplete_value": false,
      "site": "008494c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008494b4",
      "incomplete_value": false,
      "site": "008494c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "008494c0",
      "DATA",
      [
        "storage",
        "00c02270",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008494c0",
      "DATA",
      [
        "storage",
        "00c022c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008494b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008494a8.md#insn-008494b4)
- 新版 `008494b4`（命令位置の公開資料なし）

~~~diff
- 008494b4 ["COPY", "tmp:0:8", ["const:270:8"]]
- 008494b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008494b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008494b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008494b4 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 008494b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008494b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008494b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008494b4 bytes 4ac10991
+ 008494b4 bytes 4a010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d93e7e7da1c3ab547e6ca987c07f04b9"></a>

### [`008494ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008494ec.md) → [`008494ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/008494ec.md) FUN_008494ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00849504",
      "incomplete_value": false,
      "site": "00849510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00849504",
      "incomplete_value": false,
      "site": "00849510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "00849510",
      "DATA",
      [
        "storage",
        "00c02270",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00849510",
      "DATA",
      [
        "storage",
        "00c022c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00849504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008494ec.md#insn-00849504)
- 新版 `00849504`（命令位置の公開資料なし）

~~~diff
- 00849504 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00849504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00849504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00849504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00849504 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00849504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00849504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00849504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00849504 bytes 08c10991
+ 00849504 bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da23ff5fe185fce052b72003a7ca13d6"></a>

### [`00849548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849548.md) → [`00849548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849548.md) FUN_00849548

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00848250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848250.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00848250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848250.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00849574",
      "incomplete_value": false,
      "site": "00849574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00849574",
      "incomplete_value": false,
      "site": "00849574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "00849574",
      "DATA",
      [
        "storage",
        "00c02270",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00849574",
      "DATA",
      [
        "storage",
        "00c022c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084956c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849548.md#insn-0084956c)
- 新版 `0084956c`（命令位置の公開資料なし）

~~~diff
- 0084956c ["COPY", "tmp:0:8", ["const:270:8"]]
- 0084956c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084956c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084956c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084956c ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 0084956c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084956c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084956c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084956c bytes 08c10991
+ 0084956c bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a43bcd9ae1212b5c41239cf3a5e55f1"></a>

### [`008495d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008495d0.md) → [`008495d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/008495d0.md) FUN_008495d0

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
      "definition_site": "008495ec",
      "incomplete_value": false,
      "site": "008495ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008495ec",
      "incomplete_value": false,
      "site": "008495ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "008495ec",
      "DATA",
      [
        "storage",
        "00c02270",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008495ec",
      "DATA",
      [
        "storage",
        "00c022c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008495e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008495d0.md#insn-008495e8)
- 新版 `008495e8`（命令位置の公開資料なし）

~~~diff
- 008495e8 ["COPY", "tmp:0:8", ["const:270:8"]]
- 008495e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008495e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008495e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008495e8 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 008495e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008495e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008495e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008495e8 bytes 29c10991
+ 008495e8 bytes 29010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-145eb02a93318b923d9507daeb2b2935"></a>

### [`008498a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008498a0.md) → [`008498a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/008498a0.md) FUN_008498a0

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
      "definition_site": "008498b8",
      "incomplete_value": false,
      "site": "008498c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008498b8",
      "incomplete_value": false,
      "site": "008498c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:300:8"
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
      "008498c8",
      "DATA",
      [
        "storage",
        "00c02300",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008498c8",
      "DATA",
      [
        "storage",
        "00c02350",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008498b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008498a0.md#insn-008498b8)
- 新版 `008498b8`（命令位置の公開資料なし）

~~~diff
- 008498b8 ["COPY", "tmp:0:8", ["const:300:8"]]
- 008498b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008498b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008498b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008498b8 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 008498b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008498b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008498b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008498b8 bytes 08010c91
+ 008498b8 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d9bcc9a7672170b3b03fcb0aaf27be3"></a>

### [`00849930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849930.md) → [`00849930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849930.md) FUN_00849930

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00849948",
      "incomplete_value": false,
      "site": "00849958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00849948",
      "incomplete_value": false,
      "site": "00849958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:300:8"
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
      "00849958",
      "DATA",
      [
        "storage",
        "00c02300",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00849958",
      "DATA",
      [
        "storage",
        "00c02350",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00849948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849930.md#insn-00849948)
- 新版 `00849948`（命令位置の公開資料なし）

~~~diff
- 00849948 ["COPY", "tmp:0:8", ["const:300:8"]]
- 00849948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00849948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00849948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00849948 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 00849948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00849948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00849948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00849948 bytes 08010c91
+ 00849948 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

