# v15.7.3 → v15.7.4 · 最優先の変更候補 (35)

[一覧の目次](README.md)

<a id="compare-5fd0be80a354d07c78347caa4c45d9bd"></a>

### [`00773668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773668.md) → [`00773668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773668.md) FUN_00773668

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
      "definition_site": "00773674",
      "incomplete_value": false,
      "site": "00773674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00773674",
      "incomplete_value": false,
      "site": "00773674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "00773674",
      "DATA",
      [
        "storage",
        "00bfca00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773674",
      "DATA",
      [
        "storage",
        "00bfca50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773668.md#insn-00773670)
- 新版 `00773670`（命令位置の公開資料なし）

~~~diff
- 00773670 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00773670 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00773670 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00773670 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00773670 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00773670 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00773670 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00773670 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00773670 bytes 29012891
+ 00773670 bytes 29412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e6a367bd0780e471e1f006e437c3522"></a>

### [`0077372c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/0077372c.md) → [`0077372c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/0077372c.md) FUN_0077372c

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
      "definition_site": "00773750",
      "incomplete_value": false,
      "site": "00773750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00773750",
      "incomplete_value": false,
      "site": "00773750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "00773750",
      "DATA",
      [
        "storage",
        "00bfca80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773750",
      "DATA",
      [
        "storage",
        "00bfcad0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077374c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/0077372c.md#insn-0077374c)
- 新版 `0077374c`（命令位置の公開資料なし）

~~~diff
- 0077374c ["COPY", "tmp:0:8", ["const:a80:8"]]
- 0077374c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077374c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077374c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077374c ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 0077374c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077374c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077374c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077374c bytes 08012a91
+ 0077374c bytes 08412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b62f29092b396e66ee7d2d181f74fe62"></a>

### [`00773760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773760.md) → [`00773760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773760.md) FUN_00773760

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
      "definition_site": "0077376c",
      "incomplete_value": false,
      "site": "0077376c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077376c",
      "incomplete_value": false,
      "site": "0077376c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "0077376c",
      "DATA",
      [
        "storage",
        "00bfca80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0077376c",
      "DATA",
      [
        "storage",
        "00bfcad0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773760.md#insn-00773768)
- 新版 `00773768`（命令位置の公開資料なし）

~~~diff
- 00773768 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00773768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00773768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00773768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00773768 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 00773768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00773768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00773768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00773768 bytes 29012a91
+ 00773768 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af2dd4b784f02e8fe152800a8032c963"></a>

### [`007737b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007737b0.md) → [`007737b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007737b0.md) FUN_007737b0

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
      "definition_site": "007737d4",
      "incomplete_value": false,
      "site": "007737d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007737d4",
      "incomplete_value": false,
      "site": "007737d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "007737d4",
      "DATA",
      [
        "storage",
        "00bfcb10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007737d4",
      "DATA",
      [
        "storage",
        "00bfcb60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007737d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007737b0.md#insn-007737d0)
- 新版 `007737d0`（命令位置の公開資料なし）

~~~diff
- 007737d0 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 007737d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007737d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007737d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007737d0 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 007737d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007737d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007737d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007737d0 bytes 08412c91
+ 007737d0 bytes 08812d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-539d6c33f58269a2e32c1addc26747da"></a>

### [`007737e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007737e4.md) → [`007737e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007737e4.md) FUN_007737e4

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
      "definition_site": "007737f0",
      "incomplete_value": false,
      "site": "007737f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007737f0",
      "incomplete_value": false,
      "site": "007737f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "007737f0",
      "DATA",
      [
        "storage",
        "00bfcb10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007737f0",
      "DATA",
      [
        "storage",
        "00bfcb60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007737ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007737e4.md#insn-007737ec)
- 新版 `007737ec`（命令位置の公開資料なし）

~~~diff
- 007737ec ["COPY", "tmp:0:8", ["const:b10:8"]]
- 007737ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007737ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007737ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007737ec ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 007737ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007737ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007737ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007737ec bytes 29412c91
+ 007737ec bytes 29812d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-521cf04e1136d4d8bee3b5b9f799bc26"></a>

### [`007738a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007738a0.md) → [`007738a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007738a0.md) FUN_007738a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007718f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007718f4.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`007718f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007718f4.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "007738d8",
      "incomplete_value": false,
      "site": "007738e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007738d8",
      "incomplete_value": false,
      "site": "007738e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "007738e0",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00773998",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007738e0",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00773998",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007738d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007738a0.md#insn-007738d8) · [`007738dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/007738a0.md#insn-007738dc)
- 新版 `007738d8`（命令位置の公開資料なし） · `007738dc`（命令位置の公開資料なし）

~~~diff
- 007738d8 ["COPY", "tmp:0:8", ["const:148:8"]]
- 007738d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007738d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007738d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007738d8 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 007738d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007738d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007738d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007738d8 bytes 08210591
+ 007738d8 bytes 08610691
- 007738dc ["COPY", "register:4098:8", ["register:4000:8"]]
- 007738dc bytes f30300aa
+ 007738dc ["COPY", "register:4098:8", ["register:4000:8"]]
+ 007738dc bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c4997f5942b72346f883a56c940dbab"></a>

### [`00773aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773aa8.md) → [`00773aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773aa8.md) FUN_00773aa8

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
      "definition_site": "00773ac0",
      "incomplete_value": false,
      "site": "00773ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00773ac0",
      "incomplete_value": false,
      "site": "00773ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "00773ad0",
      "DATA",
      [
        "storage",
        "00bfcb90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773ad0",
      "DATA",
      [
        "storage",
        "00bfcbe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773aa8.md#insn-00773ac0)
- 新版 `00773ac0`（命令位置の公開資料なし）

~~~diff
- 00773ac0 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00773ac0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00773ac0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00773ac0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00773ac0 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00773ac0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00773ac0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00773ac0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00773ac0 bytes 08412e91
+ 00773ac0 bytes 08812f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-328109649edcc4d638affb0268e8cba5"></a>

### [`00773b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773b34.md) → [`00773b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773b34.md) FUN_00773b34

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00773b64",
      "incomplete_value": false,
      "site": "00773b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00773b64",
      "incomplete_value": false,
      "site": "00773b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "00773b64",
      "DATA",
      [
        "storage",
        "00bfcb90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773b64",
      "DATA",
      [
        "storage",
        "00bfcbe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773b34.md#insn-00773b5c)
- 新版 `00773b5c`（命令位置の公開資料なし）

~~~diff
- 00773b5c ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00773b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00773b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00773b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00773b5c ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00773b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00773b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00773b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00773b5c bytes 08412e91
+ 00773b5c bytes 08812f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f80baf779b0085de6e07679668f154b"></a>

### [`00773c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773c3c.md) → [`00773c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773c3c.md) FUN_00773c3c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00773c64",
      "incomplete_value": false,
      "site": "00773c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00773c64",
      "incomplete_value": false,
      "site": "00773c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "00773c64",
      "DATA",
      [
        "storage",
        "00bfcb90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00773c64",
      "DATA",
      [
        "storage",
        "00bfcbe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00773c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773c3c.md#insn-00773c5c) · [`00773c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773c3c.md#insn-00773c60)
- 新版 `00773c5c`（命令位置の公開資料なし） · `00773c60`（命令位置の公開資料なし）

~~~diff
- 00773c5c ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00773c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00773c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00773c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00773c5c ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00773c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00773c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00773c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00773c5c bytes 08412e91
+ 00773c5c bytes 08812f91
- 00773c60 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 00773c60 bytes f40301aa
+ 00773c60 ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 00773c60 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29b9cf2f6e24f67fcb3f20569e67343d"></a>

### [`00774024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774024.md) → [`00774024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774024.md) FUN_00774024

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
      "definition_site": "0077403c",
      "incomplete_value": false,
      "site": "00774048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077403c",
      "incomplete_value": false,
      "site": "00774048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "00774048",
      "DATA",
      [
        "storage",
        "00bfcc10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774048",
      "DATA",
      [
        "storage",
        "00bfcc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077403c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774024.md#insn-0077403c)
- 新版 `0077403c`（命令位置の公開資料なし）

~~~diff
- 0077403c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0077403c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077403c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077403c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077403c ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 0077403c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077403c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077403c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077403c bytes 08413091
+ 0077403c bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd9b28687d722b6c4566d9f35c50e873"></a>

### [`00774080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774080.md) → [`00774080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774080.md) FUN_00774080

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007740ac",
      "incomplete_value": false,
      "site": "007740ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007740ac",
      "incomplete_value": false,
      "site": "007740ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "007740ac",
      "DATA",
      [
        "storage",
        "00bfcc10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007740ac",
      "DATA",
      [
        "storage",
        "00bfcc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007740a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774080.md#insn-007740a4)
- 新版 `007740a4`（命令位置の公開資料なし）

~~~diff
- 007740a4 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 007740a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007740a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007740a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007740a4 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 007740a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007740a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007740a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007740a4 bytes 08413091
+ 007740a4 bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33565b3313d24a3f51a547e4b07fe898"></a>

### [`00774108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774108.md) → [`00774108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774108.md) FUN_00774108

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
      "definition_site": "00774124",
      "incomplete_value": false,
      "site": "00774124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774124",
      "incomplete_value": false,
      "site": "00774124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "00774124",
      "DATA",
      [
        "storage",
        "00bfcc10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774124",
      "DATA",
      [
        "storage",
        "00bfcc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774108.md#insn-00774120)
- 新版 `00774120`（命令位置の公開資料なし）

~~~diff
- 00774120 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00774120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00774120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00774120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00774120 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 00774120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00774120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00774120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00774120 bytes 29413091
+ 00774120 bytes 29813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd7139eedbee5b656f9080032202bc1"></a>

### [`007743c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007743c4.md) → [`007743c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/007743c4.md) FUN_007743c4

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
      "definition_site": "007743dc",
      "incomplete_value": false,
      "site": "007743ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007743dc",
      "incomplete_value": false,
      "site": "007743ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "007743ec",
      "DATA",
      [
        "storage",
        "00bfcc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007743ec",
      "DATA",
      [
        "storage",
        "00bfcce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007743dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007743c4.md#insn-007743dc)
- 新版 `007743dc`（命令位置の公開資料なし）

~~~diff
- 007743dc ["COPY", "tmp:0:8", ["const:c90:8"]]
- 007743dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007743dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007743dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007743dc ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 007743dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007743dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007743dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007743dc bytes 08413291
+ 007743dc bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0e232d71f73df14cda720cf6782a353"></a>

### [`00774454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774454.md) → [`00774454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774454.md) FUN_00774454

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
      "definition_site": "0077446c",
      "incomplete_value": false,
      "site": "0077447c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077446c",
      "incomplete_value": false,
      "site": "0077447c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "0077447c",
      "DATA",
      [
        "storage",
        "00bfcc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0077447c",
      "DATA",
      [
        "storage",
        "00bfcce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077446c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774454.md#insn-0077446c)
- 新版 `0077446c`（命令位置の公開資料なし）

~~~diff
- 0077446c ["COPY", "tmp:0:8", ["const:c90:8"]]
- 0077446c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077446c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077446c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077446c ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 0077446c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077446c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077446c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077446c bytes 08413291
+ 0077446c bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3abb93a47418f152fd697e5a7e7afa3"></a>

### [`007744e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007744e0.md) → [`007744e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/007744e0.md) FUN_007744e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00774510",
      "incomplete_value": false,
      "site": "00774510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774510",
      "incomplete_value": false,
      "site": "00774510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "00774510",
      "DATA",
      [
        "storage",
        "00bfcc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774510",
      "DATA",
      [
        "storage",
        "00bfcce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007744e0.md#insn-00774508)
- 新版 `00774508`（命令位置の公開資料なし）

~~~diff
- 00774508 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 00774508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774508 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 00774508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774508 bytes 08413291
+ 00774508 bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a43ed129397318267f8a1565026704b"></a>

### [`007745e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007745e8.md) → [`007745e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/007745e8.md) FUN_007745e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00774610",
      "incomplete_value": false,
      "site": "00774610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774610",
      "incomplete_value": false,
      "site": "00774610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "00774610",
      "DATA",
      [
        "storage",
        "00bfcc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774610",
      "DATA",
      [
        "storage",
        "00bfcce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007745e8.md#insn-00774608) · [`0077460c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007745e8.md#insn-0077460c)
- 新版 `00774608`（命令位置の公開資料なし） · `0077460c`（命令位置の公開資料なし）

~~~diff
- 00774608 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 00774608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774608 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 00774608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774608 bytes 08413291
+ 00774608 bytes 08813391
- 0077460c ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0077460c bytes f40301aa
+ 0077460c ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 0077460c bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19452b2b82515f2ba9fe21c428a233e5"></a>

### [`007749b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007749b8.md) → [`007749b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/007749b8.md) FUN_007749b8

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
      "definition_site": "007749d0",
      "incomplete_value": false,
      "site": "007749dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007749d0",
      "incomplete_value": false,
      "site": "007749dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "007749dc",
      "DATA",
      [
        "storage",
        "00bfcd10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007749dc",
      "DATA",
      [
        "storage",
        "00bfcd60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007749d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007749b8.md#insn-007749d0)
- 新版 `007749d0`（命令位置の公開資料なし）

~~~diff
- 007749d0 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 007749d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007749d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007749d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007749d0 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 007749d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007749d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007749d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007749d0 bytes 08413491
+ 007749d0 bytes 08813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-590ce253351fdf6aa929f7625875d42f"></a>

### [`00774a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774a14.md) → [`00774a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774a14.md) FUN_00774a14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00774a40",
      "incomplete_value": false,
      "site": "00774a40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774a40",
      "incomplete_value": false,
      "site": "00774a40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "00774a40",
      "DATA",
      [
        "storage",
        "00bfcd10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774a40",
      "DATA",
      [
        "storage",
        "00bfcd60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774a14.md#insn-00774a38)
- 新版 `00774a38`（命令位置の公開資料なし）

~~~diff
- 00774a38 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00774a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774a38 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00774a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774a38 bytes 08413491
+ 00774a38 bytes 08813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f87836f23b41b1e344214d87f57869c0"></a>

### [`00774a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774a9c.md) → [`00774a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774a9c.md) FUN_00774a9c

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
      "definition_site": "00774ab8",
      "incomplete_value": false,
      "site": "00774ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774ab8",
      "incomplete_value": false,
      "site": "00774ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "00774ab8",
      "DATA",
      [
        "storage",
        "00bfcd10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774ab8",
      "DATA",
      [
        "storage",
        "00bfcd60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774a9c.md#insn-00774ab4)
- 新版 `00774ab4`（命令位置の公開資料なし）

~~~diff
- 00774ab4 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00774ab4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00774ab4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00774ab4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00774ab4 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00774ab4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00774ab4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00774ab4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00774ab4 bytes 29413491
+ 00774ab4 bytes 29813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f8d5edba2c7e07b3a6dabf56d5bd6ff"></a>

### [`00774be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774be0.md) → [`00774be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774be0.md) FUN_00774be0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00770eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770eb8.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`00770eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770eb8.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00774c18",
      "incomplete_value": true,
      "site": "00774c20",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774c18",
      "incomplete_value": true,
      "site": "00774c20",
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
            "const:148:8"
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
      "00774c20",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00774cd8",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774c20",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00774cd8",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774be0.md#insn-00774c18) · [`00774c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774be0.md#insn-00774c1c)
- 新版 `00774c18`（命令位置の公開資料なし） · `00774c1c`（命令位置の公開資料なし）

~~~diff
- 00774c18 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00774c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774c18 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00774c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774c18 bytes 08210591
+ 00774c18 bytes 08610691
- 00774c1c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00774c1c bytes f30300aa
+ 00774c1c ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00774c1c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4bdc23aca98c1370479b71be7ec10be"></a>

### [`00774d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774d58.md) → [`00774d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774d58.md) FUN_00774d58

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
      "definition_site": "00774d70",
      "incomplete_value": false,
      "site": "00774d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774d70",
      "incomplete_value": false,
      "site": "00774d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00774d80",
      "DATA",
      [
        "storage",
        "00bfcd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774d80",
      "DATA",
      [
        "storage",
        "00bfcde0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774d58.md#insn-00774d70)
- 新版 `00774d70`（命令位置の公開資料なし）

~~~diff
- 00774d70 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00774d70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774d70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774d70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774d70 ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 00774d70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774d70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774d70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774d70 bytes 08413691
+ 00774d70 bytes 08813791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e2558e1b2ebf7de1fabf33b7de559be"></a>

### [`00774de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774de8.md) → [`00774de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774de8.md) FUN_00774de8

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
      "definition_site": "00774e00",
      "incomplete_value": false,
      "site": "00774e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774e00",
      "incomplete_value": false,
      "site": "00774e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00774e10",
      "DATA",
      [
        "storage",
        "00bfcd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774e10",
      "DATA",
      [
        "storage",
        "00bfcde0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774de8.md#insn-00774e00)
- 新版 `00774e00`（命令位置の公開資料なし）

~~~diff
- 00774e00 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00774e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774e00 ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 00774e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774e00 bytes 08413691
+ 00774e00 bytes 08813791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-905103ddf10fbfe5df02602a9372a9a0"></a>

### [`00774e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774e74.md) → [`00774e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774e74.md) FUN_00774e74

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00774ea4",
      "incomplete_value": false,
      "site": "00774ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774ea4",
      "incomplete_value": false,
      "site": "00774ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00774ea4",
      "DATA",
      [
        "storage",
        "00bfcd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774ea4",
      "DATA",
      [
        "storage",
        "00bfcde0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774e74.md#insn-00774e9c)
- 新版 `00774e9c`（命令位置の公開資料なし）

~~~diff
- 00774e9c ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00774e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774e9c ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 00774e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774e9c bytes 08413691
+ 00774e9c bytes 08813791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ee5ea108281651aa6fab9c9a302e53d"></a>

### [`00774f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774f7c.md) → [`00774f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774f7c.md) FUN_00774f7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00774fa4",
      "incomplete_value": false,
      "site": "00774fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00774fa4",
      "incomplete_value": false,
      "site": "00774fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00774fa4",
      "DATA",
      [
        "storage",
        "00bfcd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00774fa4",
      "DATA",
      [
        "storage",
        "00bfcde0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00774f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774f7c.md#insn-00774f9c) · [`00774fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774f7c.md#insn-00774fa0)
- 新版 `00774f9c`（命令位置の公開資料なし） · `00774fa0`（命令位置の公開資料なし）

~~~diff
- 00774f9c ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00774f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00774f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00774f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00774f9c ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 00774f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00774f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00774f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00774f9c bytes 08413691
+ 00774f9c bytes 08813791
- 00774fa0 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 00774fa0 bytes f40301aa
+ 00774fa0 ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 00774fa0 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4484f85f4e6e138455b4f8c42a4adb5c"></a>

### [`00775320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775320.md) → [`00775320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775320.md) FUN_00775320

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
      "definition_site": "0077532c",
      "incomplete_value": false,
      "site": "00775338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077532c",
      "incomplete_value": false,
      "site": "00775338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
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
      "00775338",
      "DATA",
      [
        "storage",
        "00bfce10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00775338",
      "DATA",
      [
        "storage",
        "00bfce60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077532c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775320.md#insn-0077532c)
- 新版 `0077532c`（命令位置の公開資料なし）

~~~diff
- 0077532c ["COPY", "tmp:0:8", ["const:e10:8"]]
- 0077532c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0077532c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0077532c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0077532c ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0077532c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0077532c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0077532c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0077532c bytes 4a413891
+ 0077532c bytes 4a813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1be2808a7171da2526d6634acef2f71"></a>

### [`00775364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775364.md) → [`00775364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775364.md) FUN_00775364

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
      "definition_site": "0077537c",
      "incomplete_value": false,
      "site": "00775388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077537c",
      "incomplete_value": false,
      "site": "00775388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "00775388",
      "DATA",
      [
        "storage",
        "00bfce10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00775388",
      "DATA",
      [
        "storage",
        "00bfce60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077537c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775364.md#insn-0077537c)
- 新版 `0077537c`（命令位置の公開資料なし）

~~~diff
- 0077537c ["COPY", "tmp:0:8", ["const:e10:8"]]
- 0077537c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077537c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077537c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077537c ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0077537c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077537c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077537c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077537c bytes 08413891
+ 0077537c bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f81be0a60494861f9e4d62c708787acb"></a>

### [`007753c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/007753c0.md) → [`007753c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/007753c0.md) FUN_007753c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007753ec",
      "incomplete_value": false,
      "site": "007753ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007753ec",
      "incomplete_value": false,
      "site": "007753ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "007753ec",
      "DATA",
      [
        "storage",
        "00bfce10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007753ec",
      "DATA",
      [
        "storage",
        "00bfce60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007753e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/007753c0.md#insn-007753e4)
- 新版 `007753e4`（命令位置の公開資料なし）

~~~diff
- 007753e4 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 007753e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007753e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007753e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007753e4 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 007753e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007753e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007753e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007753e4 bytes 08413891
+ 007753e4 bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-321b32e001b00ecb01d2aaae800860b6"></a>

### [`00775448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775448.md) → [`00775448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775448.md) FUN_00775448

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
      "definition_site": "00775464",
      "incomplete_value": false,
      "site": "00775464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00775464",
      "incomplete_value": false,
      "site": "00775464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "00775464",
      "DATA",
      [
        "storage",
        "00bfce10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00775464",
      "DATA",
      [
        "storage",
        "00bfce60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00775460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775448.md#insn-00775460)
- 新版 `00775460`（命令位置の公開資料なし）

~~~diff
- 00775460 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 00775460 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00775460 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00775460 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00775460 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 00775460 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00775460 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00775460 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00775460 bytes 29413891
+ 00775460 bytes 29813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c057fcbfe8530e5fdc392db2b1158783"></a>

### [`0077558c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/0077558c.md) → [`0077558c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/0077558c.md) _INIT_139

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007755c8",
      "incomplete_value": true,
      "site": "007755e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007755c8",
      "incomplete_value": true,
      "site": "007755e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00775648",
      "incomplete_value": true,
      "site": "00775664",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:36c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00775648",
      "incomplete_value": true,
      "site": "00775664",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:36e:8"
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
      "definition_site": "007757b4",
      "incomplete_value": false,
      "site": "007757c0",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007757b4",
      "incomplete_value": false,
      "site": "007757c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "007755c8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "007755ec",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0077560c",
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
      "007755c8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "007755ec",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0077560c",
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

- 旧版 [`007755b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/0077558c.md#insn-007755b4) · [`007755b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/0077558c.md#insn-007755b8) · [`007755c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/0077558c.md#insn-007755c0)
- 新版 `007755b4`（命令位置の公開資料なし） · `007755b8`（命令位置の公開資料なし）

~~~diff
- 007755b4 ["COPY", "register:4098:8", ["const:c27000:8"]]
+ 007755b4 ["COPY", "register:4098:8", ["const:c28000:8"]]
- 007755b4 bytes 932500d0
+ 007755b4 bytes 932500f0
- 007755b8 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 007755b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 007755b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 007755b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007755b8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 007755b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007755b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007755b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 007755b8 bytes 73e23f91
+ 007755b8 bytes 73e20091
- 007755c0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 007755c0 bytes 89d9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c849a6e8ee4741b24d19de85765ac6d"></a>

### [`0077759c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00777/0077759c.md) → [`0077759c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/0077759c.md) FUN_0077759c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007773bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00777/007773bc.md) [`00777730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00777/00777730.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`007773bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/007773bc.md) [`00777730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00777/00777730.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007775a8",
      "incomplete_value": false,
      "site": "007775ac",
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
      "definition_site": "007775a8",
      "incomplete_value": false,
      "site": "007775ac",
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
      "007775a8",
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
      "007775a8",
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

- 旧版 [`007775a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00777/0077759c.md#insn-007775a8)
- 新版 `007775a8`（命令位置の公開資料なし）

~~~diff
- 007775a8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007775a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007775a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007775a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007775a8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007775a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007775a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007775a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007775a8 bytes 000c0c91
+ 007775a8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82f6564657ca38834b08751c3675155e"></a>

### [`0077fed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0077f/0077fed4.md) → [`0077fed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0077f/0077fed4.md) _INIT_140

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0077ff10",
      "incomplete_value": true,
      "site": "0077ff2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0077ff10",
      "incomplete_value": true,
      "site": "0077ff2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0077ff34",
      "incomplete_value": true,
      "site": "0077ff50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0077ff34",
      "incomplete_value": true,
      "site": "0077ff50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0077ff54",
      "incomplete_value": true,
      "site": "0077ff70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0077ff54",
      "incomplete_value": true,
      "site": "0077ff70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0077ff10",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0077ff34",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0077ff54",
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
      "0077ff10",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0077ff34",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0077ff54",
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

- 旧版 [`0077ff00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0077f/0077fed4.md#insn-0077ff00) · [`0077ff08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0077f/0077fed4.md#insn-0077ff08)
- 新版 `0077ff00`（命令位置の公開資料なし） · `0077ff08`（命令位置の公開資料なし）

~~~diff
- 0077ff00 ["COPY", "tmp:0:8", ["const:10:8"]]
- 0077ff00 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0077ff00 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0077ff00 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0077ff00 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 0077ff00 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0077ff00 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0077ff00 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0077ff00 bytes 73420091
+ 0077ff00 bytes 73420191
- 0077ff08 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0077ff08 bytes 49d9ff90
+ 0077ff08 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0077ff08 bytes 49d9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-022312e656fd0a557cc34dee6d82102d"></a>

### [`007802c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00780/007802c0.md) → [`007802c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00780/007802c0.md) FUN_007802c0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 51件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) · 呼出先 51件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044b660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b660.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.40% / 新版 88.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 334件, `store_destination` 119件, `store_value` 172件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00780300",
      "incomplete_value": false,
      "site": "00780308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00780300",
      "incomplete_value": false,
      "site": "00780308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "definition_site": "007804ec",
      "incomplete_value": true,
      "site": "007804ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007804ec",
      "incomplete_value": true,
      "site": "007804ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:895:8"
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
      "definition_site": "00780508",
      "incomplete_value": true,
      "site": "00780508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:88a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00780508",
      "incomplete_value": true,
      "site": "00780508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00780308",
      "DATA",
      [
        "storage",
        "00bfce90",
        null,
        "pointer"
      ]
    ],
    [
      "007804b4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "007804d8",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00780308",
      "DATA",
      [
        "storage",
        "00bfcee0",
        null,
        "pointer"
      ]
    ],
    [
      "007804b4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "007804d8",
      "READ",
      [
        "storage",
        "002a5920",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00780300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/00780/007802c0-007802c0-0078acd8.md#insn-00780300) · [`007804b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/00780/007802c0-007802c0-0078acd8.md#insn-007804b0) · [`007804d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/00780/007802c0-007802c0-0078acd8.md#insn-007804d4)
- 新版 `00780300`（命令位置の公開資料なし） · `007804b0`（命令位置の公開資料なし） · `007804d4`（命令位置の公開資料なし）

~~~diff
- 00780300 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00780300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00780300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00780300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00780300 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00780300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00780300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00780300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00780300 bytes 08413a91
+ 00780300 bytes 08813b91
- 007804b0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 007804b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007804b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007804b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007804b0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007804b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007804b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007804b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007804b0 bytes 08e10091
+ 007804b0 bytes 08e10191
- 007804d4 ["COPY", "tmp:0:8", ["const:895:8"]]
- 007804d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007804d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007804d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007804d4 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 007804d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007804d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007804d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007804d4 bytes 08552291
+ 007804d4 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72fa3ceb0f0d501bfa469f42d6f20b7c"></a>

### [`0078b0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078b/0078b0ec.md) → [`0078b0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078b/0078b0ec.md) FUN_0078b0ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007802c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00780/007802c0.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044b8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8ec.md) [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)
- 新版 呼出元 1件 [`007802c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00780/007802c0.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.81% / 新版 97.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078bfb4",
      "incomplete_value": true,
      "site": "0078bfc8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:1e4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078bfb4",
      "incomplete_value": true,
      "site": "0078bfc8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:271:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 321,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078bfcc",
      "incomplete_value": true,
      "site": "0078bfcc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0078bfcc",
      "incomplete_value": true,
      "site": "0078bfcc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 322,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078c264",
      "incomplete_value": true,
      "site": "0078c278",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a13:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078c264",
      "incomplete_value": true,
      "site": "0078c278",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a04:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 350,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0078bf44",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0078bfb4",
      "READ",
      [
        "storage",
        "00299271",
        null,
        "string"
      ]
    ],
    [
      "0078bfb8",
      "READ",
      [
        "storage",
        "0029927e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0078bf44",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0078bfb4",
      "READ",
      [
        "storage",
        "002991e4",
        null,
        "string"
      ]
    ],
    [
      "0078bfb8",
      "READ",
      [
        "storage",
        "002991f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078bf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078b/0078b0ec.md#insn-0078bf40) · [`0078bfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078b/0078b0ec.md#insn-0078bfb0) · [`0078c008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078b/0078b0ec.md#insn-0078c008)
- 新版 `0078bf40`（命令位置の公開資料なし） · `0078bfb0`（命令位置の公開資料なし） · `0078c008`（命令位置の公開資料なし）

~~~diff
- 0078bf40 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0078bf40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078bf40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078bf40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078bf40 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0078bf40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078bf40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078bf40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078bf40 bytes 08e10091
+ 0078bf40 bytes 08e10191
- 0078bfb0 ["COPY", "tmp:0:8", ["const:271:8"]]
- 0078bfb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0078bfb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0078bfb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0078bfb0 ["COPY", "tmp:0:8", ["const:1e4:8"]]
+ 0078bfb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0078bfb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0078bfb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0078bfb0 bytes 29c50991
+ 0078bfb0 bytes 29910791
- 0078c008 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0078c008 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0078c008 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0078c008 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0078c008 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0078c008 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0078c008 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0078c008 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0078c008 bytes 00000091
+ 0078c008 bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62d840e304a93d1d7aaae75ef9a4b93d"></a>

### [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) → [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) FUN_0078cd14

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 209件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 209件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 27件, `call_target` 5件, `store_destination` 19件, `store_value` 54件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078d948",
      "incomplete_value": true,
      "site": "0078d958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078d948",
      "incomplete_value": true,
      "site": "0078d958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 115,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0078e704",
      "incomplete_value": false,
      "site": "0078e704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e704",
      "incomplete_value": false,
      "site": "0078e704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 222,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078e6fc",
      "incomplete_value": true,
      "site": "0078e704",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e6fc",
      "incomplete_value": true,
      "site": "0078e704",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 222,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0078d948",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ],
    [
      "0078e3e8",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "0078e424",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0078d948",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "0078e3e8",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "0078e424",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0078c/0078cd14-0078cd14-007963a8.md#insn-0078e704) · [`0078e708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0078c/0078cd14-0078cd14-007963a8.md#insn-0078e708) · [`0078e720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0078c/0078cd14-0078cd14-007963a8.md#insn-0078e720)
- 新版 `0078e704`（命令位置の公開資料なし） · `0078e708`（命令位置の公開資料なし） · `0078e720`（命令位置の公開資料なし）

~~~diff
- 0078e704 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 0078e704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0078e704 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 0078e704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0078e704 bytes 093505f9
+ 0078e704 bytes 095505f9
- 0078e708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a78:8"]]
- 0078e708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0078e708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
+ 0078e708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0078e708 bytes 6a3e05f9
+ 0078e708 bytes 6a5e05f9
- 0078e720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a78:8"]]
- 0078e720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 0078e720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
+ 0078e720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0078e720 bytes 753e05f9
+ 0078e720 bytes 755e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-441cc645a5b6b94d21ec5e29a6b4ed5f"></a>

### [`00796acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796acc.md) → [`00796acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00796/00796acc.md) FUN_00796acc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`004652a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/004652a0.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`004652a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004652a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00796b04",
      "incomplete_value": false,
      "site": "00796b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00796b04",
      "incomplete_value": false,
      "site": "00796b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00796b18",
      "incomplete_value": true,
      "site": "00796b28",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:f11:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00796b18",
      "incomplete_value": true,
      "site": "00796b28",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:f9e:8"
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
      "definition_site": "00796c8c",
      "incomplete_value": true,
      "site": "00796c90",
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
      "definition_site": "00796c8c",
      "incomplete_value": true,
      "site": "00796c90",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00796b10",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00796b18",
      "READ",
      [
        "storage",
        "00296f9e",
        null,
        "string"
      ]
    ],
    [
      "00796c7c",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00796b10",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00796b18",
      "READ",
      [
        "storage",
        "00296f11",
        null,
        "string"
      ]
    ],
    [
      "00796c7c",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00796b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796acc.md#insn-00796b04) · [`00796b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796acc.md#insn-00796b08)
- 新版 `00796b04`（命令位置の公開資料なし） · `00796b08`（命令位置の公開資料なし）

~~~diff
- 00796b04 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00796b04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00796b04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00796b04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00796b04 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00796b04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00796b04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00796b04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00796b04 bytes 08a13491
+ 00796b04 bytes 08e13591
- 00796b08 ["COPY", "register:4048:8", ["const:296000:8"]]
- 00796b08 bytes 09d8ff90
+ 00796b08 ["COPY", "register:4048:8", ["const:296000:8"]]
+ 00796b08 bytes 09d8ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-564430ebce19f2b27476f0b9767119a9"></a>

### [`00796f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796f18.md) → [`00796f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00796/00796f18.md) FUN_00796f18

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 24件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`006f2f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f2f8c.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 24件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`006f2f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2f8c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.36% / 新版 93.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 25件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00797a08",
      "incomplete_value": false,
      "site": "00797a08",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "00797a08",
      "incomplete_value": false,
      "site": "00797a08",
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
                "const:c25000:8"
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
    "ordinal": 89,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00797a0c",
      "incomplete_value": false,
      "site": "00797a0c",
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
      "definition_site": "00797a0c",
      "incomplete_value": false,
      "site": "00797a0c",
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
    "ordinal": 90,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00797a08",
      "incomplete_value": false,
      "site": "00797a0c",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "00797a08",
      "incomplete_value": false,
      "site": "00797a0c",
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
                "const:c25000:8"
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
      "00796f60",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00796f74",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00796f7c",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00796f60",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00796f74",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00796f7c",
      "PARAM",
      [
        "storage",
        "00bf4568",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00796f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796f18.md#insn-00796f60) · [`00796f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796f18.md#insn-00796f74) · [`00796f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796f18.md#insn-00796f7c)
- 新版 `00796f60`（命令位置の公開資料なし） · `00796f74`（命令位置の公開資料なし） · `00796f7c`（命令位置の公開資料なし）

~~~diff
- 00796f60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00796f60 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00796f60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00796f60 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00796f60 bytes 003d45f9
+ 00796f60 bytes 005d45f9
- 00796f74 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00796f74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00796f74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00796f74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00796f74 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00796f74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00796f74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00796f74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00796f74 bytes 21203991
+ 00796f74 bytes 21603a91
- 00796f7c ["COPY", "tmp:0:8", ["const:518:8"]]
- 00796f7c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00796f7c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00796f7c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00796f7c ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00796f7c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00796f7c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00796f7c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00796f7c bytes 42601491
+ 00796f7c bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc52cb9dd37db14c433775bc6d8526df"></a>

### [`00797bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00797/00797bfc.md) → [`00797bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00797/00797bfc.md) FUN_00797bfc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 24件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c68.md) [`00467c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c70.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 24件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00467c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c68.md) [`00467c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.01% / 新版 86.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_destination` 14件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00797f40",
      "incomplete_value": false,
      "site": "00797f40",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "00797f40",
      "incomplete_value": false,
      "site": "00797f40",
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
                "const:c25000:8"
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
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00797f44",
      "incomplete_value": false,
      "site": "00797f44",
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
      "definition_site": "00797f44",
      "incomplete_value": false,
      "site": "00797f44",
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
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00797f40",
      "incomplete_value": false,
      "site": "00797f44",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "00797f40",
      "incomplete_value": false,
      "site": "00797f44",
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
                "const:c25000:8"
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
      "00797cc4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00797cf4",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "00797cf8",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00797cc4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00797cf4",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "00797cf8",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00797cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00797/00797bfc.md#insn-00797cbc) · [`00797cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00797/00797bfc.md#insn-00797cf4) · [`00797cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00797/00797bfc.md#insn-00797cf8)
- 新版 `00797cbc`（命令位置の公開資料なし） · `00797cf4`（命令位置の公開資料なし） · `00797cf8`（命令位置の公開資料なし）

~~~diff
- 00797cbc ["COPY", "tmp:0:8", ["const:38:8"]]
- 00797cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00797cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00797cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00797cbc ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00797cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00797cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00797cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00797cbc bytes 08e10091
+ 00797cbc bytes 08e10191
- 00797cf4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00797cf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00797cf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00797cf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00797cf4 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00797cf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00797cf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00797cf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00797cf4 bytes 00000091
+ 00797cf4 bytes 00000191
- 00797cf8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 00797cf8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00797cf8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 00797cf8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00797cf8 bytes 423047f9
+ 00797cf8 bytes 425847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4c2a7feb249bd68e82a6bda92f14865"></a>

### [`00798020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798020.md) → [`00798020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00798/00798020.md) FUN_00798020

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`007cbf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbf54.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`007cbf54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbf54.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.89% / 新版 97.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007983b4",
      "incomplete_value": false,
      "site": "007983b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007983b4",
      "incomplete_value": false,
      "site": "007983b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00798068",
      "incomplete_value": true,
      "site": "00798068",
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
      "definition_site": "00798068",
      "incomplete_value": true,
      "site": "00798068",
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
      "definition_site": "00798070",
      "incomplete_value": false,
      "site": "00798080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00798070",
      "incomplete_value": false,
      "site": "00798080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
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
      "0079805c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00798070",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00798078",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0079805c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00798070",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00798078",
      "PARAM",
      [
        "storage",
        "00bf4568",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007982c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798020.md#insn-007982c8) · [`0079805c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798020.md#insn-0079805c) · [`00798070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798020.md#insn-00798070)
- 新版 `007982c8`（命令位置の公開資料なし） · `0079805c`（命令位置の公開資料なし） · `00798070`（命令位置の公開資料なし）

~~~diff
- 007982c8 ["INT_ADD", "register:40f0:8", ["const:7982c8:8", "const:4:8"]]
- 007982c8 ["CALL", null, ["ram:a09924:8"]]
+ 007982c8 ["INT_ADD", "register:40f0:8", ["const:7982c8:8", "const:4:8"]]
+ 007982c8 ["CALL", null, ["ram:a09968:8"]]
- 007982c8 bytes 97c50994
+ 007982c8 bytes a8c50994
- 0079805c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0079805c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0079805c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0079805c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0079805c bytes 003d45f9
+ 0079805c bytes 005d45f9
- 00798070 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00798070 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00798070 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00798070 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00798070 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00798070 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00798070 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00798070 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00798070 bytes 21203991
+ 00798070 bytes 21603a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-986e72e55f8751c5e048da996c44b5e2"></a>

### [`00798650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798650.md) → [`00798650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00798/00798650.md) FUN_00798650

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 30件 [`0044ab84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab84.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bdafc.md) · 呼出先 30件 [`0044ab84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab84.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.02% / 新版 92.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 2件, `store_value` 8件

アドレスに依存する影響 `branch_value` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00798914",
      "incomplete_value": true,
      "site": "00798914",
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
      "definition_site": "00798914",
      "incomplete_value": true,
      "site": "00798914",
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
      "definition_site": "0079893c",
      "incomplete_value": true,
      "site": "00798940",
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
      "definition_site": "0079893c",
      "incomplete_value": true,
      "site": "00798940",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00798980",
      "incomplete_value": true,
      "site": "00798980",
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
      "definition_site": "00798980",
      "incomplete_value": true,
      "site": "00798980",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007986a0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007986ac",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007986b4",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007986a0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007986ac",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007986b4",
      "PARAM",
      [
        "storage",
        "00bf4568",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007986a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798650.md#insn-007986a0) · [`007986ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798650.md#insn-007986ac) · [`007986b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798650.md#insn-007986b4)
- 新版 `007986a0`（命令位置の公開資料なし） · `007986ac`（命令位置の公開資料なし） · `007986b4`（命令位置の公開資料なし）

~~~diff
- 007986a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007986a0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007986a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007986a0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007986a0 bytes 003d45f9
+ 007986a0 bytes 005d45f9
- 007986ac ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007986ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007986ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007986ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007986ac ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007986ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007986ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007986ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007986ac bytes 21203991
+ 007986ac bytes 21603a91
- 007986b4 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007986b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007986b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007986b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007986b4 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007986b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007986b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007986b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007986b4 bytes 42601491
+ 007986b4 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca4de05ea2f74b45df322e421101d686"></a>

### [`00798f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798f70.md) → [`00798f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00798/00798f70.md) FUN_00798f70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 22件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bdafc.md) · 呼出先 22件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.98% / 新版 91.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 7件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00799218",
      "incomplete_value": true,
      "site": "00799218",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00799218",
      "incomplete_value": true,
      "site": "00799218",
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
            "const:128:8"
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
      "definition_site": "00799358",
      "incomplete_value": false,
      "site": "00799358",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "00799358",
      "incomplete_value": false,
      "site": "00799358",
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
                "const:c25000:8"
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
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0079935c",
      "incomplete_value": false,
      "site": "0079935c",
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
      "definition_site": "0079935c",
      "incomplete_value": false,
      "site": "0079935c",
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
      "00798fb0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00798fbc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00798fc4",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00798fb0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00798fbc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00798fc4",
      "PARAM",
      [
        "storage",
        "00bf4568",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00798fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798f70.md#insn-00798fb0) · [`00798fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798f70.md#insn-00798fbc) · [`00798fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00798/00798f70.md#insn-00798fc4)
- 新版 `00798fb0`（命令位置の公開資料なし） · `00798fbc`（命令位置の公開資料なし） · `00798fc4`（命令位置の公開資料なし）

~~~diff
- 00798fb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00798fb0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00798fb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00798fb0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00798fb0 bytes 003d45f9
+ 00798fb0 bytes 005d45f9
- 00798fbc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00798fbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00798fbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00798fbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00798fbc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00798fbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00798fbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00798fbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00798fbc bytes 21203991
+ 00798fbc bytes 21603a91
- 00798fc4 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00798fc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00798fc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00798fc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00798fc4 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00798fc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00798fc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00798fc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00798fc4 bytes 42601491
+ 00798fc4 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-914888c5c4bcf7d02fe7a0144327861b"></a>

### [`0079942c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/0079942c.md) → [`0079942c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/0079942c.md) FUN_0079942c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 20件 [`0044ab84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab84.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`007cc71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc71c.md) [`007cc720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cc/007cc720.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bdafc.md) · 呼出先 20件 [`0044ab84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab84.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`007cc71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc71c.md) [`007cc720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc720.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.60% / 新版 92.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00799764",
      "incomplete_value": true,
      "site": "00799764",
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
      "definition_site": "00799764",
      "incomplete_value": true,
      "site": "00799764",
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
      "definition_site": "007997d4",
      "incomplete_value": false,
      "site": "007997d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007997d4",
      "incomplete_value": false,
      "site": "007997d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "definition_site": "00799854",
      "incomplete_value": true,
      "site": "00799854",
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
      "definition_site": "00799854",
      "incomplete_value": true,
      "site": "00799854",
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
      "00799470",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0079947c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00799484",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00799470",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0079947c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00799484",
      "PARAM",
      [
        "storage",
        "00bf4568",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00799470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/0079942c.md#insn-00799470) · [`0079947c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/0079942c.md#insn-0079947c) · [`00799484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/0079942c.md#insn-00799484)
- 新版 `00799470`（命令位置の公開資料なし） · `0079947c`（命令位置の公開資料なし） · `00799484`（命令位置の公開資料なし）

~~~diff
- 00799470 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00799470 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00799470 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00799470 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00799470 bytes 003d45f9
+ 00799470 bytes 005d45f9
- 0079947c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0079947c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0079947c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0079947c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0079947c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0079947c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0079947c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0079947c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0079947c bytes 21203991
+ 0079947c bytes 21603a91
- 00799484 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00799484 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00799484 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00799484 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00799484 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00799484 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00799484 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00799484 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00799484 bytes 42601491
+ 00799484 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f20d72b0708f482631305a29e6979ada"></a>

### [`007999cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/007999cc.md) → [`007999cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/007999cc.md) FUN_007999cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`006fdbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdbdc.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`007bdafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bdafc.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.38% / 新版 96.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00799c2c",
      "incomplete_value": false,
      "site": "00799c30",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d80:8"
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
      "definition_site": "00799c2c",
      "incomplete_value": false,
      "site": "00799c30",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
      "definition_site": "00799eb8",
      "incomplete_value": false,
      "site": "00799ebc",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d80:8"
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
      "definition_site": "00799eb8",
      "incomplete_value": false,
      "site": "00799ebc",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079a010",
      "incomplete_value": true,
      "site": "0079a014",
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
                "const:d80:8"
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
      "definition_site": "0079a010",
      "incomplete_value": true,
      "site": "0079a014",
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
                "const:d30:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00799a34",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00799a40",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00799a48",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00799a34",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00799a40",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00799a48",
      "PARAM",
      [
        "storage",
        "00bf4568",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00799a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/007999cc.md#insn-00799a34) · [`00799a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/007999cc.md#insn-00799a40) · [`00799a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/007999cc.md#insn-00799a48)
- 新版 `00799a34`（命令位置の公開資料なし） · `00799a40`（命令位置の公開資料なし） · `00799a48`（命令位置の公開資料なし）

~~~diff
- 00799a34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00799a34 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00799a34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00799a34 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00799a34 bytes 003d45f9
+ 00799a34 bytes 005d45f9
- 00799a40 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00799a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00799a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00799a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00799a40 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00799a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00799a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00799a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00799a40 bytes 21203991
+ 00799a40 bytes 21603a91
- 00799a48 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00799a48 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00799a48 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00799a48 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00799a48 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00799a48 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00799a48 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00799a48 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00799a48 bytes 42601491
+ 00799a48 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b5ba709d2133da0251fa1536e7e5a39"></a>

### [`0079a4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079a/0079a4e4.md) → [`0079a4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079a/0079a4e4.md) FUN_0079a4e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 67件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md)
- 新版 呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 67件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.32% / 新版 94.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 10件, `store_value` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079a53c",
      "incomplete_value": true,
      "site": "0079a548",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079a53c",
      "incomplete_value": true,
      "site": "0079a548",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bd3:8"
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
      "definition_site": "0079ab0c",
      "incomplete_value": true,
      "site": "0079ab28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079ab0c",
      "incomplete_value": true,
      "site": "0079ab28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a2b:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0079ab2c",
      "incomplete_value": true,
      "site": "0079ab2c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0079ab2c",
      "incomplete_value": true,
      "site": "0079ab2c",
      "value": [
        "LOAD",
        "8",
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
      "0079a53c",
      "READ",
      [
        "storage",
        "002a6bd3",
        null,
        "string"
      ]
    ],
    [
      "0079a55c",
      "PARAM",
      [
        "storage",
        "00291ec2",
        null,
        "string"
      ]
    ],
    [
      "0079a64c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0079a53c",
      "READ",
      [
        "storage",
        "002a6c6d",
        null,
        "string"
      ]
    ],
    [
      "0079a55c",
      "PARAM",
      [
        "storage",
        "00291e35",
        null,
        "string"
      ]
    ],
    [
      "0079a64c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079a534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079a/0079a4e4.md#insn-0079a534) · [`0079a55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079a/0079a4e4.md#insn-0079a55c) · [`0079a64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079a/0079a4e4.md#insn-0079a64c)
- 新版 `0079a534`（命令位置の公開資料なし） · `0079a55c`（命令位置の公開資料なし） · `0079a64c`（命令位置の公開資料なし）

~~~diff
- 0079a534 ["COPY", "tmp:0:8", ["const:bd3:8"]]
- 0079a534 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079a534 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079a534 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079a534 ["COPY", "tmp:0:8", ["const:c6d:8"]]
+ 0079a534 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079a534 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079a534 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079a534 bytes 294d2f91
+ 0079a534 bytes 29b53191
- 0079a55c ["COPY", "tmp:0:8", ["const:ec2:8"]]
- 0079a55c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0079a55c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0079a55c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0079a55c ["COPY", "tmp:0:8", ["const:e35:8"]]
+ 0079a55c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0079a55c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0079a55c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0079a55c bytes 21083b91
+ 0079a55c bytes 21d43891
- 0079a64c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 0079a64c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0079a64c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 0079a64c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0079a64c bytes 203d45f9
+ 0079a64c bytes 205d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a796d84bcde5a01c2f98cd154929c21"></a>

### [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) → [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) FUN_0079bdf0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 405件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 405件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.49% / 新版 97.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 91件, `call_target` 7件, `store_value` 71件

アドレスに依存する影響 `branch_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079c34c",
      "incomplete_value": true,
      "site": "0079c34c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:e04:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079c34c",
      "incomplete_value": true,
      "site": "0079c34c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:e91:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079c350",
      "incomplete_value": true,
      "site": "0079c350",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0079c350",
      "incomplete_value": true,
      "site": "0079c350",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 65,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079c428",
      "incomplete_value": false,
      "site": "0079c428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079c428",
      "incomplete_value": false,
      "site": "0079c428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "ordinal": 84,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0079c33c",
      "READ",
      [
        "storage",
        "00291e91",
        null,
        "string"
      ]
    ],
    [
      "0079c340",
      "READ",
      [
        "storage",
        "00291e97",
        null,
        "string"
      ]
    ],
    [
      "0079c428",
      "DATA",
      [
        "storage",
        "00bfd628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079c33c",
      "READ",
      [
        "storage",
        "00291e04",
        null,
        "string"
      ]
    ],
    [
      "0079c340",
      "READ",
      [
        "storage",
        "00291e0a",
        null,
        "string"
      ]
    ],
    [
      "0079c428",
      "DATA",
      [
        "storage",
        "00bfd678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079c334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0079b/0079bdf0-0079bdf0-007a724c.md#insn-0079c334) · [`0079c344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0079b/0079bdf0-0079bdf0-007a724c.md#insn-0079c344)
- 新版 `0079c334`（命令位置の公開資料なし） · `0079c344`（命令位置の公開資料なし）

~~~diff
- 0079c334 ["COPY", "tmp:0:8", ["const:e91:8"]]
- 0079c334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079c334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079c334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079c334 ["COPY", "tmp:0:8", ["const:e04:8"]]
+ 0079c334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079c334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079c334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079c334 bytes 29453a91
+ 0079c334 bytes 29113891
- 0079c344 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 0079c344 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 0079c344 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 0079c344 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 0079c344 bytes f6a30a91
+ 0079c344 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 0079c344 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 0079c344 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 0079c344 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 0079c344 bytes f6a30a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dcf0872af2664043586f5ac06224b64"></a>

### [`007ab6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ab/007ab6a0.md) → [`007ab6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ab/007ab6a0.md) FUN_007ab6a0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 31件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 31件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.35% / 新版 91.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `store_destination` 14件, `store_value` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ab994",
      "incomplete_value": true,
      "site": "007ab9a4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:295000:8"
              ],
              [
                "leaf",
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ab994",
      "incomplete_value": true,
      "site": "007ab9a4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:295000:8"
              ],
              [
                "leaf",
                "const:f05:8"
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
      "definition_site": "007ab998",
      "incomplete_value": true,
      "site": "007ab9a8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "007ab998",
      "incomplete_value": true,
      "site": "007ab9a8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007abbc0",
      "incomplete_value": true,
      "site": "007abbcc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:e22:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007abbc0",
      "incomplete_value": true,
      "site": "007abbcc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:eaf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ab6f0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007ab6fc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ab704",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007ab6f0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007ab6fc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ab704",
      "PARAM",
      [
        "storage",
        "00bf4568",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ab6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ab/007ab6a0.md#insn-007ab6f0) · [`007ab6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ab/007ab6a0.md#insn-007ab6fc) · [`007ab704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ab/007ab6a0.md#insn-007ab704)
- 新版 `007ab6f0`（命令位置の公開資料なし） · `007ab6fc`（命令位置の公開資料なし） · `007ab704`（命令位置の公開資料なし）

~~~diff
- 007ab6f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007ab6f0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007ab6f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007ab6f0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007ab6f0 bytes 003d45f9
+ 007ab6f0 bytes 005d45f9
- 007ab6fc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007ab6fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ab6fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ab6fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ab6fc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007ab6fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ab6fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ab6fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ab6fc bytes 21203991
+ 007ab6fc bytes 21603a91
- 007ab704 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007ab704 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007ab704 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007ab704 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007ab704 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007ab704 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007ab704 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007ab704 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007ab704 bytes 42601491
+ 007ab704 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2019d1e4eb135cd758fd2c5da87b9a7"></a>

### [`007ac760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007ac760.md) → [`007ac760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007ac760.md) FUN_007ac760

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.55% / 新版 85.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `store_destination` 21件, `store_value` 10件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ac818",
      "incomplete_value": true,
      "site": "007ac818",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:78f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac818",
      "incomplete_value": true,
      "site": "007ac818",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:704:8"
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
      "definition_site": "007ac830",
      "incomplete_value": true,
      "site": "007ac830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:58e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac830",
      "incomplete_value": true,
      "site": "007ac830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f4:8"
              ]
            ]
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
      "definition_site": "007ac834",
      "incomplete_value": true,
      "site": "007ac834",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ac834",
      "incomplete_value": true,
      "site": "007ac834",
      "value": [
        "LOAD",
        "8",
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
      "007ac794",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007ac7a0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ac7a8",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007ac794",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007ac7a0",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ac7a8",
      "PARAM",
      [
        "storage",
        "00bf4568",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ac794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007ac760.md#insn-007ac794) · [`007ac7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007ac760.md#insn-007ac7a0) · [`007ac7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007ac760.md#insn-007ac7a8)
- 新版 `007ac794`（命令位置の公開資料なし） · `007ac7a0`（命令位置の公開資料なし） · `007ac7a8`（命令位置の公開資料なし）

~~~diff
- 007ac794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007ac794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 007ac794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007ac794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 007ac794 bytes 083d45f9
+ 007ac794 bytes 085d45f9
- 007ac7a0 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007ac7a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ac7a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ac7a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ac7a0 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007ac7a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ac7a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ac7a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ac7a0 bytes 21203991
+ 007ac7a0 bytes 21603a91
- 007ac7a8 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007ac7a8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007ac7a8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007ac7a8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007ac7a8 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007ac7a8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007ac7a8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007ac7a8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007ac7a8 bytes 42601491
+ 007ac7a8 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8360d5d9fb8fffa0db074afc38fb8344"></a>

### [`007bdafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md) → [`007bdafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bdafc.md) FUN_007bdafc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007c9cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9cac.md) [`007c9d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9d9c.md) · 呼出先 33件 [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`005bfb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bf/005bfb9c.md) [`005bfe78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bf/005bfe78.md) [`005c01d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c01d4.md) [`005c3468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3468.md)
- 新版 呼出元 2件 [`007c9cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9cac.md) [`007c9d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9d9c.md) · 呼出先 33件 [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`005bfb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bf/005bfb9c.md) [`005bfe78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bf/005bfe78.md) [`005c01d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c01d4.md) [`005c3468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c3/005c3468.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007bdbd0",
      "incomplete_value": false,
      "site": "007bdbd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:72f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bdbd0",
      "incomplete_value": false,
      "site": "007bdbd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:6a4:8"
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
      "definition_site": "007bdbf8",
      "incomplete_value": false,
      "site": "007bdc04",
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
            "const:a3d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bdbf8",
      "incomplete_value": false,
      "site": "007bdc04",
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
            "const:9a3:8"
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
      "definition_site": "007bdc30",
      "incomplete_value": false,
      "site": "007bdc34",
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
            "const:7bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bdc30",
      "incomplete_value": false,
      "site": "007bdc34",
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
            "const:731:8"
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
      "007bdbd8",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "007bdc04",
      "DATA",
      [
        "storage",
        "002a69a3",
        null,
        "string"
      ]
    ],
    [
      "007bdc34",
      "DATA",
      [
        "storage",
        "002a1731",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007bdbd8",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ],
    [
      "007bdc04",
      "DATA",
      [
        "storage",
        "002a6a3d",
        null,
        "string"
      ]
    ],
    [
      "007bdc34",
      "DATA",
      [
        "storage",
        "002a17bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bdbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md#insn-007bdbd0) · [`007bdbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bdafc.md#insn-007bdbd4)
- 新版 `007bdbd0`（命令位置の公開資料なし） · `007bdbd4`（命令位置の公開資料なし）

~~~diff
- 007bdbd0 ["COPY", "tmp:0:8", ["const:6a4:8"]]
- 007bdbd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bdbd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bdbd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bdbd0 ["COPY", "tmp:0:8", ["const:72f:8"]]
+ 007bdbd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bdbd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bdbd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bdbd0 bytes 08911a91
+ 007bdbd0 bytes 08bd1c91
- 007bdbd4 ["COPY", "tmp:0:8", ["const:18:8"]]
- 007bdbd4 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 007bdbd4 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 007bdbd4 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 007bdbd4 bytes f4630091
+ 007bdbd4 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 007bdbd4 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 007bdbd4 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 007bdbd4 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 007bdbd4 bytes f4630091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb1d5923ae8aa66dc3a534e05dadb0d3"></a>

### [`007be3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007be3c8.md) → [`007be3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007be/007be3c8.md) FUN_007be3c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007999cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00799/007999cc.md) · 呼出先 7件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`009e964c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e964c.md) [`009e9b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9b90.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`007999cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/007999cc.md) · 呼出先 7件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`009e9690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9690.md) [`009e9bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9bd4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "007be47c",
      "incomplete_value": false,
      "site": "007be480",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d80:8"
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
      "definition_site": "007be47c",
      "incomplete_value": false,
      "site": "007be480",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
      "007be440",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "007be454",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "007be480",
      "DATA",
      [
        "storage",
        "00c0bd40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007be440",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "007be454",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "007be480",
      "DATA",
      [
        "storage",
        "00c0bd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007be440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007be3c8.md#insn-007be440) · [`007be474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007be3c8.md#insn-007be474)
- 新版 `007be440`（命令位置の公開資料なし） · `007be474`（命令位置の公開資料なし）

~~~diff
- 007be440 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:520:8"]]
- 007be440 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 007be440 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:570:8"]]
+ 007be440 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 007be440 bytes 189342f9
+ 007be440 bytes 18bb42f9
- 007be474 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 007be474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007be474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007be474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007be474 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 007be474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007be474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007be474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007be474 bytes 08c13491
+ 007be474 bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c07640499a1b1bf666df4bb450198f5"></a>

### [`007be548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007be548.md) → [`007be548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007be/007be548.md) FUN_007be548

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007bea98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007bea98.md) · 呼出先 10件 [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c104.md) [`0064c428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c428.md) [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md)
- 新版 呼出元 1件 [`007bea98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007be/007bea98.md) · 呼出先 10件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`0064c428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c428.md) [`006582c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007be564",
      "incomplete_value": false,
      "site": "007be568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007be564",
      "incomplete_value": false,
      "site": "007be568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "definition_site": "007bea14",
      "incomplete_value": false,
      "site": "007bea18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bea14",
      "incomplete_value": false,
      "site": "007bea18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "definition_site": "007bea50",
      "incomplete_value": false,
      "site": "007bea54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bea50",
      "incomplete_value": false,
      "site": "007bea54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "007be568",
      "DATA",
      [
        "storage",
        "00bfce90",
        null,
        "pointer"
      ]
    ],
    [
      "007bea18",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "007bea54",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007be568",
      "DATA",
      [
        "storage",
        "00bfcee0",
        null,
        "pointer"
      ]
    ],
    [
      "007bea18",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "007bea54",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007be564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007be548.md#insn-007be564) · [`007bea14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007be548.md#insn-007bea14) · [`007bea50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007be548.md#insn-007bea50)
- 新版 `007be564`（命令位置の公開資料なし） · `007bea14`（命令位置の公開資料なし） · `007bea50`（命令位置の公開資料なし）

~~~diff
- 007be564 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 007be564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007be564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007be564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007be564 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 007be564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007be564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007be564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007be564 bytes 08413a91
+ 007be564 bytes 08813b91
- 007bea14 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 007bea14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bea14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bea14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bea14 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 007bea14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bea14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bea14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bea14 bytes 08e13691
+ 007bea14 bytes 08213891
- 007bea50 ["COPY", "tmp:0:8", ["const:298:8"]]
- 007bea50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bea50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bea50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bea50 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 007bea50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bea50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bea50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bea50 bytes 08610a91
+ 007bea50 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fdf4d3795a45437fc4b55747b41b635"></a>

### [`007bebf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007bebf8.md) → [`007bebf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007be/007bebf8.md) FUN_007bebf8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007beabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007beabc.md) [`007bebf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007bebf8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`007beabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007be/007beabc.md) [`007bebf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007be/007bebf8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.83% / 新版 98.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007bed5c",
      "incomplete_value": false,
      "site": "007bed64",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bed5c",
      "incomplete_value": false,
      "site": "007bed64",
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
            "const:30a:8"
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
      "definition_site": "007bed80",
      "incomplete_value": false,
      "site": "007bed8c",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bed80",
      "incomplete_value": false,
      "site": "007bed8c",
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
            "const:919:8"
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
      "definition_site": "007beeb4",
      "incomplete_value": false,
      "site": "007beebc",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007beeb4",
      "incomplete_value": false,
      "site": "007beebc",
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
            "const:2ee:8"
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
      "007bed5c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "007bed80",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "007beeb4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007bed5c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "007bed80",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "007beeb4",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bed5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007bebf8.md#insn-007bed5c) · [`007bed80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007bebf8.md#insn-007bed80) · [`007beeb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007bebf8.md#insn-007beeb4)
- 新版 `007bed5c`（命令位置の公開資料なし） · `007bed80`（命令位置の公開資料なし） · `007beeb4`（命令位置の公開資料なし）

~~~diff
- 007bed5c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007bed5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007bed5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007bed5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007bed5c ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 007bed5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007bed5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007bed5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007bed5c bytes 21280c91
+ 007bed5c bytes 21900e91
- 007bed80 ["COPY", "tmp:0:8", ["const:919:8"]]
- 007bed80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007bed80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007bed80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007bed80 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 007bed80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007bed80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007bed80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007bed80 bytes 21642491
+ 007bed80 bytes 21142291
- 007beeb4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 007beeb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007beeb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007beeb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007beeb4 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 007beeb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007beeb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007beeb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007beeb4 bytes 21b80b91
+ 007beeb4 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40ca2dbba21feeb417e1ece76a778f09"></a>

### [`007bfcb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcb4.md) → [`007bfcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfcb4.md) FUN_007bfcb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007bf6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bf6b8.md) [`008cd26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd26c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`007bf6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bf6b8.md) [`008cd26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cd/008cd26c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007bfcc0",
      "incomplete_value": false,
      "site": "007bfcc4",
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
      "definition_site": "007bfcc0",
      "incomplete_value": false,
      "site": "007bfcc4",
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
      "007bfcc0",
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
      "007bfcc0",
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

- 旧版 [`007bfcc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcb4.md#insn-007bfcc0)
- 新版 `007bfcc0`（命令位置の公開資料なし）

~~~diff
- 007bfcc0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007bfcc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007bfcc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007bfcc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007bfcc0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007bfcc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfcc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfcc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007bfcc0 bytes 000c0c91
+ 007bfcc0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f27f7817cfe8773fa2f33cceea5cc115"></a>

### [`007bfcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcc8.md) → [`007bfcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfcc8.md) FUN_007bfcc8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`007da634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da634.md) [`007dbfcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbfcc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`007da634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da634.md) [`007dbfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007dbfcc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007bfcd4",
      "incomplete_value": false,
      "site": "007bfcd8",
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
      "definition_site": "007bfcd4",
      "incomplete_value": false,
      "site": "007bfcd8",
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
      "007bfcd4",
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
      "007bfcd4",
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

- 旧版 [`007bfcd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcc8.md#insn-007bfcd4)
- 新版 `007bfcd4`（命令位置の公開資料なし）

~~~diff
- 007bfcd4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007bfcd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007bfcd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007bfcd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007bfcd4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007bfcd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfcd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfcd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007bfcd4 bytes 000c0c91
+ 007bfcd4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d1b96a2169f003bba1bb166db5a3718"></a>

### [`007bfcdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcdc.md) → [`007bfcdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfcdc.md) FUN_007bfcdc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`00796d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00796/00796d74.md) [`007da86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da86c.md) [`007dbc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbc94.md) [`007dc0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dc0fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 6件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`00796d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00796/00796d74.md) [`007da86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da86c.md) [`007dbc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007db/007dbc94.md) [`007dc0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dc0fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007bfce8",
      "incomplete_value": false,
      "site": "007bfcec",
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
      "definition_site": "007bfce8",
      "incomplete_value": false,
      "site": "007bfcec",
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
      "007bfce8",
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
      "007bfce8",
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

- 旧版 [`007bfce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcdc.md#insn-007bfce8)
- 新版 `007bfce8`（命令位置の公開資料なし）

~~~diff
- 007bfce8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007bfce8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007bfce8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007bfce8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007bfce8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007bfce8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfce8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007bfce8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007bfce8 bytes 000c0c91
+ 007bfce8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e3ed3ec60ededff49c0aa0668e659b6"></a>

### [`007bfcf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcf4.md) → [`007bfcf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfcf4.md) FUN_007bfcf4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007bfd08",
      "incomplete_value": false,
      "site": "007bfd0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bfd08",
      "incomplete_value": false,
      "site": "007bfd0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "007bfd0c",
      "DATA",
      [
        "storage",
        "00bfceb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007bfd0c",
      "DATA",
      [
        "storage",
        "00bfcf00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bfd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcf4.md#insn-007bfd08)
- 新版 `007bfd08`（命令位置の公開資料なし）

~~~diff
- 007bfd08 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 007bfd08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bfd08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bfd08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bfd08 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 007bfd08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfd08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfd08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bfd08 bytes 08c13a91
+ 007bfd08 bytes 08013c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f55b841b07a6f7f12170c6926a445bdd"></a>

### [`007bfd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfd18.md) → [`007bfd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfd18.md) FUN_007bfd18

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007bfd1c",
      "incomplete_value": false,
      "site": "007bfd20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bfd1c",
      "incomplete_value": false,
      "site": "007bfd20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "007bfd20",
      "DATA",
      [
        "storage",
        "00bfceb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007bfd20",
      "DATA",
      [
        "storage",
        "00bfcf00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bfd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfd18.md#insn-007bfd1c)
- 新版 `007bfd1c`（命令位置の公開資料なし）

~~~diff
- 007bfd1c ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 007bfd1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bfd1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bfd1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bfd1c ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 007bfd1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfd1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfd1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bfd1c bytes 08c13a91
+ 007bfd1c bytes 08013c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad986cc872baa3b49e268380851997ab"></a>

### [`007bfd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfd30.md) → [`007bfd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfd30.md) FUN_007bfd30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007bfe1c",
      "incomplete_value": true,
      "site": "007bfe30",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:85:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bfe1c",
      "incomplete_value": true,
      "site": "007bfe30",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:112:8"
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
      "definition_site": "007bfefc",
      "incomplete_value": false,
      "site": "007bfefc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bfefc",
      "incomplete_value": false,
      "site": "007bfefc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "007bfe1c",
      "READ",
      [
        "storage",
        "00299112",
        null,
        "string"
      ]
    ],
    [
      "007bfe24",
      "READ",
      [
        "storage",
        "0029911f",
        null,
        "string"
      ]
    ],
    [
      "007bfefc",
      "DATA",
      [
        "storage",
        "00bfcf20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007bfe1c",
      "READ",
      [
        "storage",
        "00299085",
        null,
        "string"
      ]
    ],
    [
      "007bfe24",
      "READ",
      [
        "storage",
        "00299092",
        null,
        "string"
      ]
    ],
    [
      "007bfefc",
      "DATA",
      [
        "storage",
        "00bfcf70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bfe18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfd30.md#insn-007bfe18) · [`007bfef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfd30.md#insn-007bfef4)
- 新版 `007bfe18`（命令位置の公開資料なし） · `007bfef4`（命令位置の公開資料なし）

~~~diff
- 007bfe18 ["COPY", "tmp:0:8", ["const:112:8"]]
- 007bfe18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007bfe18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007bfe18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007bfe18 ["COPY", "tmp:0:8", ["const:85:8"]]
+ 007bfe18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007bfe18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007bfe18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007bfe18 bytes 29490491
+ 007bfe18 bytes 29150291
- 007bfef4 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 007bfef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007bfef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007bfef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007bfef4 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 007bfef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007bfef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007bfef4 bytes 08813c91
+ 007bfef4 bytes 08c13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a4f786bb34198b7c4b1ff149fdfd25b"></a>

### [`007c015c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c015c.md) → [`007c015c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c015c.md) FUN_007c015c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007c0170",
      "incomplete_value": false,
      "site": "007c0174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0170",
      "incomplete_value": false,
      "site": "007c0174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "007c0174",
      "DATA",
      [
        "storage",
        "00bfcf20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0174",
      "DATA",
      [
        "storage",
        "00bfcf70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c015c.md#insn-007c0170)
- 新版 `007c0170`（命令位置の公開資料なし）

~~~diff
- 007c0170 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 007c0170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0170 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 007c0170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0170 bytes 08813c91
+ 007c0170 bytes 08c13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-726ce6d68e61ddba78f07525bbb7090e"></a>

### [`007c0180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0180.md) → [`007c0180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0180.md) FUN_007c0180

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007c0184",
      "incomplete_value": false,
      "site": "007c0188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0184",
      "incomplete_value": false,
      "site": "007c0188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "007c0188",
      "DATA",
      [
        "storage",
        "00bfcf20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0188",
      "DATA",
      [
        "storage",
        "00bfcf70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0180.md#insn-007c0184)
- 新版 `007c0184`（命令位置の公開資料なし）

~~~diff
- 007c0184 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 007c0184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0184 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 007c0184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0184 bytes 08813c91
+ 007c0184 bytes 08c13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbca69e39a9e221b53fe22d703d227b3"></a>

### [`007c0198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0198.md) → [`007c0198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0198.md) FUN_007c0198

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.97% / 新版 98.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c0360",
      "incomplete_value": false,
      "site": "007c036c",
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
            "const:5a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0360",
      "incomplete_value": false,
      "site": "007c036c",
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
            "const:50f:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c03d0",
      "incomplete_value": false,
      "site": "007c03dc",
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
            "const:5a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c03d0",
      "incomplete_value": false,
      "site": "007c03dc",
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
            "const:50f:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c0484",
      "incomplete_value": false,
      "site": "007c0490",
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
            "const:9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0484",
      "incomplete_value": false,
      "site": "007c0490",
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
            "const:128:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007c0360",
      "PARAM",
      [
        "storage",
        "002a850f",
        null,
        "string"
      ]
    ],
    [
      "007c03d0",
      "PARAM",
      [
        "storage",
        "002a850f",
        null,
        "string"
      ]
    ],
    [
      "007c0484",
      "PARAM",
      [
        "storage",
        "00299128",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007c0360",
      "PARAM",
      [
        "storage",
        "002a85a9",
        null,
        "string"
      ]
    ],
    [
      "007c03d0",
      "PARAM",
      [
        "storage",
        "002a85a9",
        null,
        "string"
      ]
    ],
    [
      "007c0484",
      "PARAM",
      [
        "storage",
        "0029909b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0198.md#insn-007c0360) · [`007c03d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0198.md#insn-007c03d0) · [`007c0484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0198.md#insn-007c0484)
- 新版 `007c0360`（命令位置の公開資料なし） · `007c03d0`（命令位置の公開資料なし） · `007c0484`（命令位置の公開資料なし）

~~~diff
- 007c0360 ["COPY", "tmp:0:8", ["const:50f:8"]]
- 007c0360 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c0360 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c0360 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c0360 ["COPY", "tmp:0:8", ["const:5a9:8"]]
+ 007c0360 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c0360 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c0360 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c0360 bytes 423c1491
+ 007c0360 bytes 42a41691
- 007c03d0 ["COPY", "tmp:0:8", ["const:50f:8"]]
- 007c03d0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c03d0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c03d0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c03d0 ["COPY", "tmp:0:8", ["const:5a9:8"]]
+ 007c03d0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c03d0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c03d0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c03d0 bytes 423c1491
+ 007c03d0 bytes 42a41691
- 007c0484 ["COPY", "tmp:0:8", ["const:128:8"]]
- 007c0484 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c0484 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c0484 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c0484 ["COPY", "tmp:0:8", ["const:9b:8"]]
+ 007c0484 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c0484 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c0484 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c0484 bytes 42a00491
+ 007c0484 bytes 426c0291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4255039913d72154a0eacfc67abdf7e0"></a>

### [`007c0754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0754.md) → [`007c0754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0754.md) FUN_007c0754

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007c0768",
      "incomplete_value": false,
      "site": "007c076c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0768",
      "incomplete_value": false,
      "site": "007c076c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "007c076c",
      "DATA",
      [
        "storage",
        "00bfcfb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c076c",
      "DATA",
      [
        "storage",
        "00bfd000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0754.md#insn-007c0764) · [`007c0768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0754.md#insn-007c0768)
- 新版 `007c0764`（命令位置の公開資料なし） · `007c0768`（命令位置の公開資料なし）

~~~diff
- 007c0764 ["COPY", "register:4040:8", ["const:bfc000:8"]]
+ 007c0764 ["COPY", "register:4040:8", ["const:bfd000:8"]]
- 007c0764 bytes e8210090
+ 007c0764 bytes e82100b0
- 007c0768 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 007c0768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0768 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 007c0768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0768 bytes 08c13e91
+ 007c0768 bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93065ab6d23e3581f04efd2bf4571d86"></a>

### [`007c0778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0778.md) → [`007c0778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0778.md) FUN_007c0778

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007c077c",
      "incomplete_value": false,
      "site": "007c0780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c077c",
      "incomplete_value": false,
      "site": "007c0780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfc000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "007c0780",
      "DATA",
      [
        "storage",
        "00bfcfb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0780",
      "DATA",
      [
        "storage",
        "00bfd000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0778.md#insn-007c0778) · [`007c077c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0778.md#insn-007c077c)
- 新版 `007c0778`（命令位置の公開資料なし） · `007c077c`（命令位置の公開資料なし）

~~~diff
- 007c0778 ["COPY", "register:4040:8", ["const:bfc000:8"]]
+ 007c0778 ["COPY", "register:4040:8", ["const:bfd000:8"]]
- 007c0778 bytes e8210090
+ 007c0778 bytes e82100b0
- 007c077c ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 007c077c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c077c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c077c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c077c ["COPY", "tmp:0:8", ["const:0:8"]]
+ 007c077c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c077c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c077c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c077c bytes 08c13e91
+ 007c077c bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d165e29c5ba0307408f65503625d5ce2"></a>

### [`007c0834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0834.md) → [`007c0834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0834.md) FUN_007c0834

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
      "definition_site": "007c0858",
      "incomplete_value": false,
      "site": "007c0858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0858",
      "incomplete_value": false,
      "site": "007c0858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c0858",
      "DATA",
      [
        "storage",
        "00bfd030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0858",
      "DATA",
      [
        "storage",
        "00bfd080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0834.md#insn-007c0854)
- 新版 `007c0854`（命令位置の公開資料なし）

~~~diff
- 007c0854 ["COPY", "tmp:0:8", ["const:30:8"]]
- 007c0854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0854 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 007c0854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0854 bytes 08c10091
+ 007c0854 bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b88fc07c3982f41d8fa9040d7a09de0b"></a>

### [`007c0868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0868.md) → [`007c0868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0868.md) FUN_007c0868

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
      "definition_site": "007c0874",
      "incomplete_value": false,
      "site": "007c0874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0874",
      "incomplete_value": false,
      "site": "007c0874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      "007c0874",
      "DATA",
      [
        "storage",
        "00bfd030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0874",
      "DATA",
      [
        "storage",
        "00bfd080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0868.md#insn-007c0870)
- 新版 `007c0870`（命令位置の公開資料なし）

~~~diff
- 007c0870 ["COPY", "tmp:0:8", ["const:30:8"]]
- 007c0870 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c0870 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c0870 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c0870 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 007c0870 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0870 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0870 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c0870 bytes 29c10091
+ 007c0870 bytes 29010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c26c133e2fd2bd231cd6357dc2aa03ed"></a>

### [`007c0884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0884.md) → [`007c0884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0884.md) FUN_007c0884

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.31% / 新版 94.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c0914",
      "incomplete_value": true,
      "site": "007c0928",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fcc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0914",
      "incomplete_value": true,
      "site": "007c0928",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:59:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c0988",
      "incomplete_value": false,
      "site": "007c0988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0988",
      "incomplete_value": false,
      "site": "007c0988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "definition_site": "007c0a64",
      "incomplete_value": false,
      "site": "007c0a68",
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
      "definition_site": "007c0a64",
      "incomplete_value": false,
      "site": "007c0a68",
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
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007c0914",
      "READ",
      [
        "storage",
        "00298059",
        null,
        "string"
      ]
    ],
    [
      "007c0988",
      "DATA",
      [
        "storage",
        "00bfd0a0",
        null,
        "undefined *"
      ]
    ],
    [
      "007c09e0",
      "READ",
      [
        "storage",
        "00bfd0c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c0914",
      "READ",
      [
        "storage",
        "00297fcc",
        null,
        "string"
      ]
    ],
    [
      "007c0988",
      "DATA",
      [
        "storage",
        "00bfd0f0",
        null,
        "undefined *"
      ]
    ],
    [
      "007c09e0",
      "READ",
      [
        "storage",
        "00bfd110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0884.md#insn-007c0908) · [`007c090c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0884.md#insn-007c090c) · [`007c0980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0884.md#insn-007c0980)
- 新版 `007c0908`（命令位置の公開資料なし） · `007c090c`（命令位置の公開資料なし） · `007c0980`（命令位置の公開資料なし）

~~~diff
- 007c0908 ["COPY", "register:4048:8", ["const:298000:8"]]
+ 007c0908 ["COPY", "register:4048:8", ["const:297000:8"]]
- 007c0908 bytes c9d6ff90
+ 007c0908 bytes a9d6fff0
- 007c090c ["COPY", "tmp:0:8", ["const:59:8"]]
- 007c090c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c090c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c090c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c090c ["COPY", "tmp:0:8", ["const:fcc:8"]]
+ 007c090c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c090c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c090c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c090c bytes 29650191
+ 007c090c bytes 29313f91
- 007c0980 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 007c0980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0980 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 007c0980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0980 bytes 08810291
+ 007c0980 bytes 08c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b0a72d000840e28d6d371b6b95e86c1"></a>

### [`007c0b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0b54.md) → [`007c0b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0b54.md) FUN_007c0b54

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007c0b68",
      "incomplete_value": false,
      "site": "007c0b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0b68",
      "incomplete_value": false,
      "site": "007c0b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "007c0b6c",
      "DATA",
      [
        "storage",
        "00bfd0a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0b6c",
      "DATA",
      [
        "storage",
        "00bfd0f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0b54.md#insn-007c0b68)
- 新版 `007c0b68`（命令位置の公開資料なし）

~~~diff
- 007c0b68 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 007c0b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0b68 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 007c0b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0b68 bytes 08810291
+ 007c0b68 bytes 08c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11d49a72c086bef3c42be744fd599434"></a>

### [`007c0b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0b78.md) → [`007c0b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0b78.md) FUN_007c0b78

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007c0b7c",
      "incomplete_value": false,
      "site": "007c0b80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0b7c",
      "incomplete_value": false,
      "site": "007c0b80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "007c0b80",
      "DATA",
      [
        "storage",
        "00bfd0a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0b80",
      "DATA",
      [
        "storage",
        "00bfd0f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0b78.md#insn-007c0b7c)
- 新版 `007c0b7c`（命令位置の公開資料なし）

~~~diff
- 007c0b7c ["COPY", "tmp:0:8", ["const:a0:8"]]
- 007c0b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0b7c ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 007c0b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0b7c bytes 08810291
+ 007c0b7c bytes 08c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f9fbaeb894dcad3a03b047ddc999faf"></a>

### [`007c0c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0c04.md) → [`007c0c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0c04.md) FUN_007c0c04

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
      "definition_site": "007c0c28",
      "incomplete_value": false,
      "site": "007c0c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0c28",
      "incomplete_value": false,
      "site": "007c0c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c0c28",
      "DATA",
      [
        "storage",
        "00bfd130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0c28",
      "DATA",
      [
        "storage",
        "00bfd180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0c04.md#insn-007c0c24)
- 新版 `007c0c24`（命令位置の公開資料なし）

~~~diff
- 007c0c24 ["COPY", "tmp:0:8", ["const:130:8"]]
- 007c0c24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0c24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0c24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0c24 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 007c0c24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0c24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0c24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0c24 bytes 08c10491
+ 007c0c24 bytes 08010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01116f1cfb0ca5c9b34dea7cd5e1f797"></a>

### [`007c0c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0c38.md) → [`007c0c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0c38.md) FUN_007c0c38

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
      "definition_site": "007c0c44",
      "incomplete_value": false,
      "site": "007c0c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0c44",
      "incomplete_value": false,
      "site": "007c0c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:130:8"
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
      "007c0c44",
      "DATA",
      [
        "storage",
        "00bfd130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0c44",
      "DATA",
      [
        "storage",
        "00bfd180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0c38.md#insn-007c0c40)
- 新版 `007c0c40`（命令位置の公開資料なし）

~~~diff
- 007c0c40 ["COPY", "tmp:0:8", ["const:130:8"]]
- 007c0c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c0c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c0c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c0c40 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 007c0c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c0c40 bytes 29c10491
+ 007c0c40 bytes 29010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e46e09dbfeeb3a4648619a51cc841ae"></a>

### [`007c0e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0e24.md) → [`007c0e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0e24.md) FUN_007c0e24

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
      "definition_site": "007c0e48",
      "incomplete_value": false,
      "site": "007c0e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0e48",
      "incomplete_value": false,
      "site": "007c0e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c0e48",
      "DATA",
      [
        "storage",
        "00bfd1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0e48",
      "DATA",
      [
        "storage",
        "00bfd200",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0e24.md#insn-007c0e44)
- 新版 `007c0e44`（命令位置の公開資料なし）

~~~diff
- 007c0e44 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 007c0e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c0e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c0e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c0e44 ["COPY", "tmp:0:8", ["const:200:8"]]
+ 007c0e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c0e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c0e44 bytes 08c10691
+ 007c0e44 bytes 08010891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24ad4e68ff6ca7ceb6e13f697a05d2b3"></a>

### [`007c0e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0e58.md) → [`007c0e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0e58.md) FUN_007c0e58

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
      "definition_site": "007c0e64",
      "incomplete_value": false,
      "site": "007c0e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c0e64",
      "incomplete_value": false,
      "site": "007c0e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "007c0e64",
      "DATA",
      [
        "storage",
        "00bfd1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c0e64",
      "DATA",
      [
        "storage",
        "00bfd200",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c0e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0e58.md#insn-007c0e60)
- 新版 `007c0e60`（命令位置の公開資料なし）

~~~diff
- 007c0e60 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 007c0e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c0e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c0e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c0e60 ["COPY", "tmp:0:8", ["const:200:8"]]
+ 007c0e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c0e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c0e60 bytes 29c10691
+ 007c0e60 bytes 29010891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bbdc76876414731b698b5e577e2e8ad"></a>

### [`007c1068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1068.md) → [`007c1068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1068.md) FUN_007c1068

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
      "definition_site": "007c108c",
      "incomplete_value": false,
      "site": "007c108c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c108c",
      "incomplete_value": false,
      "site": "007c108c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "007c108c",
      "DATA",
      [
        "storage",
        "00bfd230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c108c",
      "DATA",
      [
        "storage",
        "00bfd280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1068.md#insn-007c1088)
- 新版 `007c1088`（命令位置の公開資料なし）

~~~diff
- 007c1088 ["COPY", "tmp:0:8", ["const:230:8"]]
- 007c1088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c1088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c1088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c1088 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 007c1088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c1088 bytes 08c10891
+ 007c1088 bytes 08010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d591b1a6a8142eb7dfcaa93fb0de31e"></a>

### [`007c109c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c109c.md) → [`007c109c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c109c.md) FUN_007c109c

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
      "definition_site": "007c10a8",
      "incomplete_value": false,
      "site": "007c10a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c10a8",
      "incomplete_value": false,
      "site": "007c10a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "007c10a8",
      "DATA",
      [
        "storage",
        "00bfd230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c10a8",
      "DATA",
      [
        "storage",
        "00bfd280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c10a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c109c.md#insn-007c10a4)
- 新版 `007c10a4`（命令位置の公開資料なし）

~~~diff
- 007c10a4 ["COPY", "tmp:0:8", ["const:230:8"]]
- 007c10a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c10a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c10a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c10a4 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 007c10a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c10a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c10a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c10a4 bytes 29c10891
+ 007c10a4 bytes 29010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ecda37c9849bf53e6eb486bd860f96d"></a>

### [`007c10b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c10b8.md) → [`007c10b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c10b8.md) FUN_007c10b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c133c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c133c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007c133c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c133c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c117c",
      "incomplete_value": true,
      "site": "007c1190",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007c117c",
      "incomplete_value": true,
      "site": "007c1190",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c11a8",
      "incomplete_value": false,
      "site": "007c11b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c11a8",
      "incomplete_value": false,
      "site": "007c11b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "007c117c",
      "READ",
      [
        "storage",
        "002a4272",
        null,
        "string"
      ]
    ],
    [
      "007c11b0",
      "DATA",
      [
        "storage",
        "00bfd2a0",
        null,
        "undefined *"
      ]
    ],
    [
      "007c11fc",
      "READ",
      [
        "storage",
        "00bfd2c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c117c",
      "READ",
      [
        "storage",
        "002a42fd",
        null,
        "string"
      ]
    ],
    [
      "007c11b0",
      "DATA",
      [
        "storage",
        "00bfd2f0",
        null,
        "undefined *"
      ]
    ],
    [
      "007c11fc",
      "READ",
      [
        "storage",
        "00bfd310",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c10b8.md#insn-007c1174) · [`007c11a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c10b8.md#insn-007c11a8)
- 新版 `007c1174`（命令位置の公開資料なし） · `007c11a8`（命令位置の公開資料なし）

~~~diff
- 007c1174 ["COPY", "tmp:0:8", ["const:272:8"]]
- 007c1174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c1174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c1174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c1174 ["COPY", "tmp:0:8", ["const:2fd:8"]]
+ 007c1174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c1174 bytes 29c90991
+ 007c1174 bytes 29f50b91
- 007c11a8 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 007c11a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c11a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c11a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c11a8 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 007c11a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c11a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c11a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c11a8 bytes 08810a91
+ 007c11a8 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d346f32c7c3146b1342f18d2ab547165"></a>

### [`007c1308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1308.md) → [`007c1308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1308.md) FUN_007c1308

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007c131c",
      "incomplete_value": false,
      "site": "007c1320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c131c",
      "incomplete_value": false,
      "site": "007c1320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "007c1320",
      "DATA",
      [
        "storage",
        "00bfd2a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c1320",
      "DATA",
      [
        "storage",
        "00bfd2f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c131c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1308.md#insn-007c131c)
- 新版 `007c131c`（命令位置の公開資料なし）

~~~diff
- 007c131c ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 007c131c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c131c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c131c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c131c ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 007c131c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c131c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c131c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c131c bytes 08810a91
+ 007c131c bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02d60a7a551f95ebf815db4550819658"></a>

### [`007c132c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c132c.md) → [`007c132c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c132c.md) FUN_007c132c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007c1330",
      "incomplete_value": false,
      "site": "007c1334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1330",
      "incomplete_value": false,
      "site": "007c1334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "007c1334",
      "DATA",
      [
        "storage",
        "00bfd2a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c1334",
      "DATA",
      [
        "storage",
        "00bfd2f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c132c.md#insn-007c1330)
- 新版 `007c1330`（命令位置の公開資料なし）

~~~diff
- 007c1330 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 007c1330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c1330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c1330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c1330 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 007c1330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c1330 bytes 08810a91
+ 007c1330 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4e354aef927fc3c699e11a0579a6165"></a>

### [`007c1388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1388.md) → [`007c1388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1388.md) FUN_007c1388

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
      "definition_site": "007c13ac",
      "incomplete_value": false,
      "site": "007c13ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c13ac",
      "incomplete_value": false,
      "site": "007c13ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c13ac",
      "DATA",
      [
        "storage",
        "00bfd330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c13ac",
      "DATA",
      [
        "storage",
        "00bfd380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c13a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1388.md#insn-007c13a8)
- 新版 `007c13a8`（命令位置の公開資料なし）

~~~diff
- 007c13a8 ["COPY", "tmp:0:8", ["const:330:8"]]
- 007c13a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c13a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c13a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c13a8 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 007c13a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c13a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c13a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c13a8 bytes 08c10c91
+ 007c13a8 bytes 08010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4812c43403848edb2cf3191a92543447"></a>

### [`007c13bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c13bc.md) → [`007c13bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c13bc.md) FUN_007c13bc

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
      "definition_site": "007c13c8",
      "incomplete_value": false,
      "site": "007c13c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c13c8",
      "incomplete_value": false,
      "site": "007c13c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c13c8",
      "DATA",
      [
        "storage",
        "00bfd330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c13c8",
      "DATA",
      [
        "storage",
        "00bfd380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c13c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c13bc.md#insn-007c13c4)
- 新版 `007c13c4`（命令位置の公開資料なし）

~~~diff
- 007c13c4 ["COPY", "tmp:0:8", ["const:330:8"]]
- 007c13c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c13c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c13c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c13c4 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 007c13c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c13c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c13c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c13c4 bytes 29c10c91
+ 007c13c4 bytes 29010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e2bcc1ad4d1f90015cb6fa25f10820"></a>

### [`007c147c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c147c.md) → [`007c147c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c147c.md) FUN_007c147c

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
      "definition_site": "007c14a0",
      "incomplete_value": false,
      "site": "007c14a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c14a0",
      "incomplete_value": false,
      "site": "007c14a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c14a0",
      "DATA",
      [
        "storage",
        "00bfd3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c14a0",
      "DATA",
      [
        "storage",
        "00bfd400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c149c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c147c.md#insn-007c149c)
- 新版 `007c149c`（命令位置の公開資料なし）

~~~diff
- 007c149c ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 007c149c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c149c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c149c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c149c ["COPY", "tmp:0:8", ["const:400:8"]]
+ 007c149c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c149c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c149c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c149c bytes 08c10e91
+ 007c149c bytes 08011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59b425869a9c2187f263853aff21b073"></a>

### [`007c14b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c14b0.md) → [`007c14b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c14b0.md) FUN_007c14b0

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
      "definition_site": "007c14bc",
      "incomplete_value": false,
      "site": "007c14bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c14bc",
      "incomplete_value": false,
      "site": "007c14bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c14bc",
      "DATA",
      [
        "storage",
        "00bfd3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c14bc",
      "DATA",
      [
        "storage",
        "00bfd400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c14b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c14b0.md#insn-007c14b8)
- 新版 `007c14b8`（命令位置の公開資料なし）

~~~diff
- 007c14b8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 007c14b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c14b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c14b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c14b8 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 007c14b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c14b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c14b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c14b8 bytes 29c10e91
+ 007c14b8 bytes 29011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e0b9efb9ff208437d9a61ef5966a4d5"></a>

### [`007c14cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c14cc.md) → [`007c14cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c14cc.md) FUN_007c14cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c17bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c17bc.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007c17bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c17bc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.09% / 新版 96.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c1590",
      "incomplete_value": true,
      "site": "007c15a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007c1590",
      "incomplete_value": true,
      "site": "007c15a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c15bc",
      "incomplete_value": false,
      "site": "007c15c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c15bc",
      "incomplete_value": false,
      "site": "007c15c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "007c1590",
      "READ",
      [
        "storage",
        "002a4272",
        null,
        "string"
      ]
    ],
    [
      "007c15c4",
      "DATA",
      [
        "storage",
        "00bfd420",
        null,
        "undefined *"
      ]
    ],
    [
      "007c1628",
      "READ",
      [
        "storage",
        "00bfd440",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c1590",
      "READ",
      [
        "storage",
        "002a42fd",
        null,
        "string"
      ]
    ],
    [
      "007c15c4",
      "DATA",
      [
        "storage",
        "00bfd470",
        null,
        "undefined *"
      ]
    ],
    [
      "007c1628",
      "READ",
      [
        "storage",
        "00bfd490",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c14cc.md#insn-007c1588) · [`007c15bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c14cc.md#insn-007c15bc)
- 新版 `007c1588`（命令位置の公開資料なし） · `007c15bc`（命令位置の公開資料なし）

~~~diff
- 007c1588 ["COPY", "tmp:0:8", ["const:272:8"]]
- 007c1588 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c1588 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c1588 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c1588 ["COPY", "tmp:0:8", ["const:2fd:8"]]
+ 007c1588 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1588 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1588 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c1588 bytes 29c90991
+ 007c1588 bytes 29f50b91
- 007c15bc ["COPY", "tmp:0:8", ["const:420:8"]]
- 007c15bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c15bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c15bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c15bc ["COPY", "tmp:0:8", ["const:470:8"]]
+ 007c15bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c15bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c15bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c15bc bytes 08811091
+ 007c15bc bytes 08c11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f244849453ff101d1539b9d6f344a68d"></a>

### [`007c1788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1788.md) → [`007c1788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1788.md) FUN_007c1788

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007c179c",
      "incomplete_value": false,
      "site": "007c17a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c179c",
      "incomplete_value": false,
      "site": "007c17a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "007c17a0",
      "DATA",
      [
        "storage",
        "00bfd420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c17a0",
      "DATA",
      [
        "storage",
        "00bfd470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c179c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1788.md#insn-007c179c)
- 新版 `007c179c`（命令位置の公開資料なし）

~~~diff
- 007c179c ["COPY", "tmp:0:8", ["const:420:8"]]
- 007c179c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c179c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c179c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c179c ["COPY", "tmp:0:8", ["const:470:8"]]
+ 007c179c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c179c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c179c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c179c bytes 08811091
+ 007c179c bytes 08c11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57d88d7534a136852560ba068246b758"></a>

### [`007c17ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c17ac.md) → [`007c17ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c17ac.md) FUN_007c17ac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007c17b0",
      "incomplete_value": false,
      "site": "007c17b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c17b0",
      "incomplete_value": false,
      "site": "007c17b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "007c17b4",
      "DATA",
      [
        "storage",
        "00bfd420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c17b4",
      "DATA",
      [
        "storage",
        "00bfd470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c17b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c17ac.md#insn-007c17b0)
- 新版 `007c17b0`（命令位置の公開資料なし）

~~~diff
- 007c17b0 ["COPY", "tmp:0:8", ["const:420:8"]]
- 007c17b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c17b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c17b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c17b0 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 007c17b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c17b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c17b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c17b0 bytes 08811091
+ 007c17b0 bytes 08c11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-937f5d63af8fe8df1dacfa448eee3f8d"></a>

### [`007c1808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1808.md) → [`007c1808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1808.md) FUN_007c1808

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
      "definition_site": "007c182c",
      "incomplete_value": false,
      "site": "007c182c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c182c",
      "incomplete_value": false,
      "site": "007c182c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c182c",
      "DATA",
      [
        "storage",
        "00bfd4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c182c",
      "DATA",
      [
        "storage",
        "00bfd500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1808.md#insn-007c1828)
- 新版 `007c1828`（命令位置の公開資料なし）

~~~diff
- 007c1828 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 007c1828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c1828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c1828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c1828 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 007c1828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c1828 bytes 08c11291
+ 007c1828 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbfbb384a4a6286cb56daa398ad48d0c"></a>

### [`007c183c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c183c.md) → [`007c183c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c183c.md) FUN_007c183c

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
      "definition_site": "007c1848",
      "incomplete_value": false,
      "site": "007c1848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1848",
      "incomplete_value": false,
      "site": "007c1848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "007c1848",
      "DATA",
      [
        "storage",
        "00bfd4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c1848",
      "DATA",
      [
        "storage",
        "00bfd500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c183c.md#insn-007c1844)
- 新版 `007c1844`（命令位置の公開資料なし）

~~~diff
- 007c1844 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 007c1844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c1844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c1844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c1844 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 007c1844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c1844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c1844 bytes 29c11291
+ 007c1844 bytes 29011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-933409871ee589106c831df421329b9c"></a>

### [`007c1858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1858.md) → [`007c1858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1858.md) FUN_007c1858

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.42% / 新版 95.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c19d0",
      "incomplete_value": false,
      "site": "007c19d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c19d0",
      "incomplete_value": false,
      "site": "007c19d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:520:8"
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
      "definition_site": "007c1ab0",
      "incomplete_value": false,
      "site": "007c1ab4",
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
      "definition_site": "007c1ab0",
      "incomplete_value": false,
      "site": "007c1ab4",
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
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007c195c",
      "READ",
      [
        "storage",
        "0029e860",
        null,
        "string"
      ]
    ],
    [
      "007c195c",
      "READ",
      [
        "storage",
        "002aeef9",
        null,
        "string"
      ]
    ],
    [
      "007c1960",
      "READ",
      [
        "storage",
        "0029e86d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007c195c",
      "READ",
      [
        "storage",
        "0029e8eb",
        null,
        "string"
      ]
    ],
    [
      "007c195c",
      "READ",
      [
        "storage",
        "002aee65",
        null,
        "string"
      ]
    ],
    [
      "007c1960",
      "READ",
      [
        "storage",
        "0029e8f8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c18f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1858.md#insn-007c18f0) · [`007c191c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1858.md#insn-007c191c) · [`007c19c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1858.md#insn-007c19c8)
- 新版 `007c18f0`（命令位置の公開資料なし） · `007c191c`（命令位置の公開資料なし） · `007c19c8`（命令位置の公開資料なし）

~~~diff
- 007c18f0 ["COPY", "tmp:0:8", ["const:860:8"]]
- 007c18f0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 007c18f0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 007c18f0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 007c18f0 ["COPY", "tmp:0:8", ["const:8eb:8"]]
+ 007c18f0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 007c18f0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 007c18f0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 007c18f0 bytes d6822191
+ 007c18f0 bytes d6ae2391
- 007c191c ["COPY", "tmp:0:8", ["const:ef9:8"]]
- 007c191c ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 007c191c ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 007c191c ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 007c191c ["COPY", "tmp:0:8", ["const:e65:8"]]
+ 007c191c ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 007c191c ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 007c191c ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 007c191c bytes f7e63b91
+ 007c191c bytes f7963991
- 007c19c8 ["COPY", "tmp:0:8", ["const:520:8"]]
- 007c19c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c19c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c19c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c19c8 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 007c19c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c19c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c19c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c19c8 bytes 08811491
+ 007c19c8 bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3733963b0d72dc5452a118a2f21f08c"></a>

### [`007c1ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1ba0.md) → [`007c1ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1ba0.md) FUN_007c1ba0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007c1bb4",
      "incomplete_value": false,
      "site": "007c1bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1bb4",
      "incomplete_value": false,
      "site": "007c1bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:520:8"
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
      "007c1bb8",
      "DATA",
      [
        "storage",
        "00bfd520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c1bb8",
      "DATA",
      [
        "storage",
        "00bfd570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1ba0.md#insn-007c1bb4)
- 新版 `007c1bb4`（命令位置の公開資料なし）

~~~diff
- 007c1bb4 ["COPY", "tmp:0:8", ["const:520:8"]]
- 007c1bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c1bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c1bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c1bb4 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 007c1bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c1bb4 bytes 08811491
+ 007c1bb4 bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b32b83ecc99743ea1bbf045e7e6a2d3e"></a>

### [`007c1bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1bc4.md) → [`007c1bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1bc4.md) FUN_007c1bc4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007c1bc8",
      "incomplete_value": false,
      "site": "007c1bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1bc8",
      "incomplete_value": false,
      "site": "007c1bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:520:8"
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
      "007c1bcc",
      "DATA",
      [
        "storage",
        "00bfd520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c1bcc",
      "DATA",
      [
        "storage",
        "00bfd570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1bc4.md#insn-007c1bc8)
- 新版 `007c1bc8`（命令位置の公開資料なし）

~~~diff
- 007c1bc8 ["COPY", "tmp:0:8", ["const:520:8"]]
- 007c1bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c1bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c1bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c1bc8 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 007c1bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c1bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c1bc8 bytes 08811491
+ 007c1bc8 bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a68c1733d3dd4bb119102998460becc4"></a>

### [`007c1c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1c70.md) → [`007c1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1c70.md) FUN_007c1c70

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 10件 [`006ad590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad590.md) [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`006ad8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8e8.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) · 呼出先 10件 [`006ad590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad590.md) [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

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
      "definition_site": "007c1f30",
      "incomplete_value": false,
      "site": "007c1f34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:21:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c1f30",
      "incomplete_value": false,
      "site": "007c1f34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:23:8"
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
      "007c1f30",
      "PARAM",
      [
        "storage",
        "0029a023",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007c1f30",
      "PARAM",
      [
        "storage",
        "0029a021",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1c70.md#insn-007c1f30)
- 新版 `007c1f30`（命令位置の公開資料なし）

~~~diff
- 007c1f30 ["COPY", "tmp:0:8", ["const:23:8"]]
- 007c1f30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007c1f30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007c1f30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007c1f30 ["COPY", "tmp:0:8", ["const:21:8"]]
+ 007c1f30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007c1f30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007c1f30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007c1f30 bytes 008c0091
+ 007c1f30 bytes 00840091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c28ebe6ae7e19cb45bf38ed2248651b5"></a>

### [`007c1f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1f74.md) → [`007c1f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1f74.md) FUN_007c1f74

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) [`006add94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006add94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) [`006add94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006add94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007c231c",
      "incomplete_value": false,
      "site": "007c2320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:ea2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c231c",
      "incomplete_value": false,
      "site": "007c2320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:f2f:8"
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
      "007c231c",
      "PARAM",
      [
        "storage",
        "00297f2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007c231c",
      "PARAM",
      [
        "storage",
        "00297ea2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c231c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1f74.md#insn-007c231c)
- 新版 `007c231c`（命令位置の公開資料なし）

~~~diff
- 007c231c ["COPY", "tmp:0:8", ["const:f2f:8"]]
- 007c231c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007c231c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007c231c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007c231c ["COPY", "tmp:0:8", ["const:ea2:8"]]
+ 007c231c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007c231c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007c231c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007c231c bytes 00bc3c91
+ 007c231c bytes 00883a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b042a5350ab2b3df04a2313289f9511e"></a>

### [`007c238c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c238c.md) → [`007c238c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c238c.md) FUN_007c238c

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
      "definition_site": "007c23b0",
      "incomplete_value": false,
      "site": "007c23b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c23b0",
      "incomplete_value": false,
      "site": "007c23b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "007c23b0",
      "DATA",
      [
        "storage",
        "00bfd628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c23b0",
      "DATA",
      [
        "storage",
        "00bfd678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c23ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c238c.md#insn-007c23ac)
- 新版 `007c23ac`（命令位置の公開資料なし）

~~~diff
- 007c23ac ["COPY", "tmp:0:8", ["const:628:8"]]
- 007c23ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c23ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c23ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c23ac ["COPY", "tmp:0:8", ["const:678:8"]]
+ 007c23ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c23ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c23ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c23ac bytes 08a11891
+ 007c23ac bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf8b9c235f026ce7a7cedcd7be41c635"></a>

### [`007c23c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c23c0.md) → [`007c23c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c23c0.md) FUN_007c23c0

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
      "definition_site": "007c23cc",
      "incomplete_value": false,
      "site": "007c23cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c23cc",
      "incomplete_value": false,
      "site": "007c23cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "007c23cc",
      "DATA",
      [
        "storage",
        "00bfd628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c23cc",
      "DATA",
      [
        "storage",
        "00bfd678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c23c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c23c0.md#insn-007c23c8)
- 新版 `007c23c8`（命令位置の公開資料なし）

~~~diff
- 007c23c8 ["COPY", "tmp:0:8", ["const:628:8"]]
- 007c23c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c23c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c23c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c23c8 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 007c23c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c23c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c23c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c23c8 bytes 29a11891
+ 007c23c8 bytes 29e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fa8471a239b578b66fac706b69659f8"></a>

### [`007c248c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c248c.md) → [`007c248c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c248c.md) FUN_007c248c

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
      "definition_site": "007c24b0",
      "incomplete_value": false,
      "site": "007c24b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c24b0",
      "incomplete_value": false,
      "site": "007c24b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "007c24b0",
      "DATA",
      [
        "storage",
        "00bfd6a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c24b0",
      "DATA",
      [
        "storage",
        "00bfd6f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c24ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c248c.md#insn-007c24ac)
- 新版 `007c24ac`（命令位置の公開資料なし）

~~~diff
- 007c24ac ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 007c24ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c24ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c24ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c24ac ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 007c24ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c24ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c24ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c24ac bytes 08a11a91
+ 007c24ac bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcb3cd6d40c3347b4e9762774742bf9a"></a>

### [`007c24c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c24c0.md) → [`007c24c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c24c0.md) FUN_007c24c0

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
      "definition_site": "007c24cc",
      "incomplete_value": false,
      "site": "007c24cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c24cc",
      "incomplete_value": false,
      "site": "007c24cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "007c24cc",
      "DATA",
      [
        "storage",
        "00bfd6a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c24cc",
      "DATA",
      [
        "storage",
        "00bfd6f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c24c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c24c0.md#insn-007c24c8)
- 新版 `007c24c8`（命令位置の公開資料なし）

~~~diff
- 007c24c8 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 007c24c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c24c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c24c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c24c8 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 007c24c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c24c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c24c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c24c8 bytes 29a11a91
+ 007c24c8 bytes 29e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da4afc7d6867d5de935d6742f18a9bfe"></a>

### [`007c2574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2574.md) → [`007c2574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c2574.md) FUN_007c2574

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
      "definition_site": "007c2598",
      "incomplete_value": false,
      "site": "007c2598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c2598",
      "incomplete_value": false,
      "site": "007c2598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "007c2598",
      "DATA",
      [
        "storage",
        "00bfd728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c2598",
      "DATA",
      [
        "storage",
        "00bfd778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c2594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2574.md#insn-007c2594)
- 新版 `007c2594`（命令位置の公開資料なし）

~~~diff
- 007c2594 ["COPY", "tmp:0:8", ["const:728:8"]]
- 007c2594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c2594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c2594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c2594 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 007c2594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c2594 bytes 08a11c91
+ 007c2594 bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bb41fa6547bd318519f814b2558dfee"></a>

### [`007c25a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c25a8.md) → [`007c25a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c25a8.md) FUN_007c25a8

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
      "definition_site": "007c25b4",
      "incomplete_value": false,
      "site": "007c25b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c25b4",
      "incomplete_value": false,
      "site": "007c25b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "007c25b4",
      "DATA",
      [
        "storage",
        "00bfd728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c25b4",
      "DATA",
      [
        "storage",
        "00bfd778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c25b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c25a8.md#insn-007c25b0)
- 新版 `007c25b0`（命令位置の公開資料なし）

~~~diff
- 007c25b0 ["COPY", "tmp:0:8", ["const:728:8"]]
- 007c25b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c25b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c25b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c25b0 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 007c25b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c25b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c25b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c25b0 bytes 29a11c91
+ 007c25b0 bytes 29e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d692440e766b4c5d1b48f914f0e3471a"></a>

### [`007c267c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c267c.md) → [`007c267c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c267c.md) FUN_007c267c

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
      "definition_site": "007c26a0",
      "incomplete_value": false,
      "site": "007c26a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c26a0",
      "incomplete_value": false,
      "site": "007c26a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "007c26a0",
      "DATA",
      [
        "storage",
        "00bfd7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c26a0",
      "DATA",
      [
        "storage",
        "00bfd7f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c269c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c267c.md#insn-007c269c)
- 新版 `007c269c`（命令位置の公開資料なし）

~~~diff
- 007c269c ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 007c269c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c269c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c269c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c269c ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 007c269c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c269c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c269c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c269c bytes 08a11e91
+ 007c269c bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743243d6819bf80999e5106250b2e358"></a>

### [`007c26b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c26b0.md) → [`007c26b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c26b0.md) FUN_007c26b0

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
      "definition_site": "007c26bc",
      "incomplete_value": false,
      "site": "007c26bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c26bc",
      "incomplete_value": false,
      "site": "007c26bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "007c26bc",
      "DATA",
      [
        "storage",
        "00bfd7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c26bc",
      "DATA",
      [
        "storage",
        "00bfd7f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c26b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c26b0.md#insn-007c26b8)
- 新版 `007c26b8`（命令位置の公開資料なし）

~~~diff
- 007c26b8 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 007c26b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c26b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c26b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c26b8 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 007c26b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c26b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c26b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c26b8 bytes 29a11e91
+ 007c26b8 bytes 29e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c434c240e80e361d7e3992c41d76f85c"></a>

### [`007c27e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c27e8.md) → [`007c27e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c27e8.md) FUN_007c27e8

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
      "definition_site": "007c280c",
      "incomplete_value": false,
      "site": "007c280c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c280c",
      "incomplete_value": false,
      "site": "007c280c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "007c280c",
      "DATA",
      [
        "storage",
        "00bfd828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c280c",
      "DATA",
      [
        "storage",
        "00bfd878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c2808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c27e8.md#insn-007c2808)
- 新版 `007c2808`（命令位置の公開資料なし）

~~~diff
- 007c2808 ["COPY", "tmp:0:8", ["const:828:8"]]
- 007c2808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c2808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c2808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c2808 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 007c2808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c2808 bytes 08a12091
+ 007c2808 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba5c92d4fd857c974429548e36a933b0"></a>

### [`007c281c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c281c.md) → [`007c281c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c281c.md) FUN_007c281c

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
      "definition_site": "007c2828",
      "incomplete_value": false,
      "site": "007c2828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c2828",
      "incomplete_value": false,
      "site": "007c2828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
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
      "007c2828",
      "DATA",
      [
        "storage",
        "00bfd828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c2828",
      "DATA",
      [
        "storage",
        "00bfd878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c2824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c281c.md#insn-007c2824)
- 新版 `007c2824`（命令位置の公開資料なし）

~~~diff
- 007c2824 ["COPY", "tmp:0:8", ["const:828:8"]]
- 007c2824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c2824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c2824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c2824 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 007c2824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c2824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c2824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c2824 bytes 29a12091
+ 007c2824 bytes 29e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18b80c64b7b8fe90cdd7f73892d03d9c"></a>

### [`007c28b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c28b0.md) → [`007c28b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c28b0.md) FUN_007c28b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007c28d4",
      "incomplete_value": false,
      "site": "007c28d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c28d4",
      "incomplete_value": false,
      "site": "007c28d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "007c28d8",
      "DATA",
      [
        "storage",
        "00bfd8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c28d8",
      "DATA",
      [
        "storage",
        "00bfd8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c28d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c28b0.md#insn-007c28d4)
- 新版 `007c28d4`（命令位置の公開資料なし）

~~~diff
- 007c28d4 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 007c28d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c28d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c28d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c28d4 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 007c28d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c28d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c28d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c28d4 bytes 08a12291
+ 007c28d4 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

