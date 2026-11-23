# v15.7.3 → v15.7.4 · 最優先の変更候補 (49)

[一覧の目次](README.md)

<a id="compare-45d81949251758a000cc6580458a6e02"></a>

### [`009009cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009009cc.md) → [`009009cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009009cc.md) FUN_009009cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982c5c.md) · 呼出先 3件 [`00900ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900ae0.md) [`00a6d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d884.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982c5c.md) · 呼出先 3件 [`00900ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900ae0.md) [`00a6d8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8c8.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "00900a0c",
      "incomplete_value": false,
      "site": "00900a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900a0c",
      "incomplete_value": false,
      "site": "00900a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "00900a14",
      "DATA",
      [
        "storage",
        "00c09920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00900a14",
      "DATA",
      [
        "storage",
        "00c09970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00900a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009009cc.md#insn-00900a0c)
- 新版 `00900a0c`（命令位置の公開資料なし）

~~~diff
- 00900a0c ["COPY", "tmp:0:8", ["const:920:8"]]
- 00900a0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00900a0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00900a0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00900a0c ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00900a0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00900a0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00900a0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00900a0c bytes 08812491
+ 00900a0c bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-008210ef9d8467467d013a5f2528afb0"></a>

### [`00900d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900d80.md) → [`00900d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900d80.md) FUN_00900d80

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00a6d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00a6d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8f8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00900d98",
      "incomplete_value": false,
      "site": "00900da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900d98",
      "incomplete_value": false,
      "site": "00900da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "00900da4",
      "DATA",
      [
        "storage",
        "00c09920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00900da4",
      "DATA",
      [
        "storage",
        "00c09970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00900d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900d80.md#insn-00900d98)
- 新版 `00900d98`（命令位置の公開資料なし）

~~~diff
- 00900d98 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00900d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00900d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00900d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00900d98 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00900d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00900d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00900d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00900d98 bytes 08812491
+ 00900d98 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f94cee8cba74dabcefe6cb04c940ce9"></a>

### [`00900e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900e0c.md) → [`00900e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900e0c.md) FUN_00900e0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00a6d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00a6d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8f8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00900e24",
      "incomplete_value": false,
      "site": "00900e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900e24",
      "incomplete_value": false,
      "site": "00900e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "00900e30",
      "DATA",
      [
        "storage",
        "00c09920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00900e30",
      "DATA",
      [
        "storage",
        "00c09970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00900e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900e0c.md#insn-00900e24)
- 新版 `00900e24`（命令位置の公開資料なし）

~~~diff
- 00900e24 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00900e24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00900e24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00900e24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00900e24 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00900e24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00900e24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00900e24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00900e24 bytes 08812491
+ 00900e24 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe431a921388d30a7afa8fea8b0172c0"></a>

### [`00901338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901338.md) → [`00901338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/00901338.md) FUN_00901338

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
      "definition_site": "0090133c",
      "incomplete_value": false,
      "site": "00901340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0090133c",
      "incomplete_value": false,
      "site": "00901340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "00901340",
      "DATA",
      [
        "storage",
        "00c09970",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00901340",
      "DATA",
      [
        "storage",
        "00c099c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0090133c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901338.md#insn-0090133c)
- 新版 `0090133c`（命令位置の公開資料なし）

~~~diff
- 0090133c ["COPY", "tmp:0:8", ["const:970:8"]]
- 0090133c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0090133c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0090133c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0090133c ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 0090133c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0090133c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0090133c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0090133c bytes 08c12591
+ 0090133c bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08b716ce89e189a2b23abbed5741da36"></a>

### [`00901388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901388.md) → [`00901388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/00901388.md) _INIT_180

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00901428",
      "incomplete_value": true,
      "site": "00901440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901428",
      "incomplete_value": true,
      "site": "00901440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009013c4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "009013e8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00901408",
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
      "009013c4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "009013e8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00901408",
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

- 旧版 [`009013b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901388.md#insn-009013b4) · [`009013bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901388.md#insn-009013bc)
- 新版 `009013b4`（命令位置の公開資料なし） · `009013bc`（命令位置の公開資料なし）

~~~diff
- 009013b4 ["COPY", "tmp:0:8", ["const:840:8"]]
- 009013b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009013b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009013b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009013b4 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 009013b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009013b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009013b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009013b4 bytes 73022191
+ 009013b4 bytes 73022291
- 009013bc ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 009013bc bytes 29cdffd0
+ 009013bc ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 009013bc bytes 29cdffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea7f7bd81aa1a6952d69f42550b7d428"></a>

### [`00901718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901718.md) → [`00901718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/00901718.md) FUN_00901718

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

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
      "definition_site": "00901750",
      "incomplete_value": true,
      "site": "0090175c",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00901750",
      "incomplete_value": true,
      "site": "0090175c",
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
            "const:d28:8"
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
      "definition_site": "0090190c",
      "incomplete_value": true,
      "site": "00901910",
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
      "definition_site": "0090190c",
      "incomplete_value": true,
      "site": "00901910",
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
      "0090175c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00901770",
      "READ",
      [
        "storage",
        "002af0e8",
        null,
        "string"
      ]
    ],
    [
      "009018d8",
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
      "0090175c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00901770",
      "READ",
      [
        "storage",
        "002af054",
        null,
        "string"
      ]
    ],
    [
      "009018d8",
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

- 旧版 [`00901750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901718.md#insn-00901750) · [`00901768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901718.md#insn-00901768) · [`009018d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901718.md#insn-009018d8)
- 新版 `00901750`（命令位置の公開資料なし） · `00901768`（命令位置の公開資料なし） · `009018d8`（命令位置の公開資料なし）

~~~diff
- 00901750 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00901750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00901750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00901750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00901750 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00901750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00901750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00901750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00901750 bytes 08a13491
+ 00901750 bytes 08e13591
- 00901768 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00901768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00901768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00901768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00901768 ["COPY", "tmp:0:8", ["const:54:8"]]
+ 00901768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00901768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00901768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00901768 bytes 29a10391
+ 00901768 bytes 29510191
- 009018d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 009018d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 009018d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 009018d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 009018d8 bytes 08b946f9
+ 009018d8 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-567e6b9ac7135cbecb0118d085949f57"></a>

### [`00901d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901d24.md) → [`00901d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/00901d24.md) _INIT_181

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
      "definition_site": "00901d60",
      "incomplete_value": true,
      "site": "00901d7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901d60",
      "incomplete_value": true,
      "site": "00901d7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901d84",
      "incomplete_value": true,
      "site": "00901da0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901d84",
      "incomplete_value": true,
      "site": "00901da0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901da4",
      "incomplete_value": true,
      "site": "00901dc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901da4",
      "incomplete_value": true,
      "site": "00901dc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00901d60",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00901d84",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00901da4",
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
      "00901d60",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00901d84",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00901da4",
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

- 旧版 [`00901d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901d24.md#insn-00901d50) · [`00901d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901d24.md#insn-00901d58)
- 新版 `00901d50`（命令位置の公開資料なし） · `00901d58`（命令位置の公開資料なし）

~~~diff
- 00901d50 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00901d50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00901d50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00901d50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00901d50 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00901d50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00901d50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00901d50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00901d50 bytes 73622191
+ 00901d50 bytes 73622291
- 00901d58 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00901d58 bytes 29cdffd0
+ 00901d58 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00901d58 bytes 29cdffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e9325b89abe3854e6b493b25a216a8f"></a>

### [`009020e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00902/009020e4.md) → [`009020e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00902/009020e4.md) FUN_009020e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.06% / 新版 96.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00902128",
      "incomplete_value": false,
      "site": "00902134",
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
      "definition_site": "00902128",
      "incomplete_value": false,
      "site": "00902134",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00902148",
      "incomplete_value": true,
      "site": "00902164",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
              ],
              [
                "leaf",
                "const:eb9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00902148",
      "incomplete_value": true,
      "site": "00902164",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
              ],
              [
                "leaf",
                "const:f46:8"
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
      "definition_site": "00902878",
      "incomplete_value": true,
      "site": "00902888",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b93:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00902878",
      "incomplete_value": true,
      "site": "00902888",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 111,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00902134",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00902148",
      "READ",
      [
        "storage",
        "00292f46",
        null,
        "string"
      ]
    ],
    [
      "009022d8",
      "READ",
      [
        "storage",
        "002a5a3b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00902134",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00902148",
      "READ",
      [
        "storage",
        "00292eb9",
        null,
        "string"
      ]
    ],
    [
      "009022d8",
      "READ",
      [
        "storage",
        "002a5ac6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00902128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00902/009020e4.md#insn-00902128) · [`0090213c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00902/009020e4.md#insn-0090213c)
- 新版 `00902128`（命令位置の公開資料なし） · `0090213c`（命令位置の公開資料なし）

~~~diff
- 00902128 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00902128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00902128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00902128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00902128 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00902128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00902128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00902128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00902128 bytes 08a13491
+ 00902128 bytes 08e13591
- 0090213c ["COPY", "register:4048:8", ["const:292000:8"]]
- 0090213c bytes 89ccff90
+ 0090213c ["COPY", "register:4048:8", ["const:292000:8"]]
+ 0090213c bytes 89ccff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0e9a483bb0317b73b09aebf4193d6ce"></a>

### [`00904150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/00904150.md) → [`00904150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00904/00904150.md) _INIT_182

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009041b0",
      "incomplete_value": true,
      "site": "009041cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009041b0",
      "incomplete_value": true,
      "site": "009041cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009041d0",
      "incomplete_value": true,
      "site": "009041ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009041d0",
      "incomplete_value": true,
      "site": "009041ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009041f0",
      "incomplete_value": true,
      "site": "00904208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009041f0",
      "incomplete_value": true,
      "site": "00904208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0090418c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "009041b0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "009041d0",
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
      "0090418c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "009041b0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "009041d0",
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

- 旧版 [`0090417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/00904150.md#insn-0090417c) · [`00904184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/00904150.md#insn-00904184)
- 新版 `0090417c`（命令位置の公開資料なし） · `00904184`（命令位置の公開資料なし）

~~~diff
- 0090417c ["COPY", "tmp:0:8", ["const:870:8"]]
- 0090417c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0090417c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0090417c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0090417c ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 0090417c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0090417c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0090417c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0090417c bytes 73c22191
+ 0090417c bytes 73c22291
- 00904184 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00904184 bytes 09cdfff0
+ 00904184 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00904184 bytes 09cdfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdc59d1cf4f3d0e7a0141c85c4a58dc8"></a>

### [`009044e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/009044e0.md) → [`009044e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00904/009044e0.md) FUN_009044e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.12% / 新版 98.12%

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
      "definition_site": "00904524",
      "incomplete_value": false,
      "site": "00904530",
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
      "definition_site": "00904524",
      "incomplete_value": false,
      "site": "00904530",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00904544",
      "incomplete_value": true,
      "site": "0090455c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bad:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00904544",
      "incomplete_value": true,
      "site": "0090455c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b22:8"
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
      "definition_site": "00904560",
      "incomplete_value": true,
      "site": "00904560",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00904560",
      "incomplete_value": true,
      "site": "00904560",
      "value": [
        "LOAD",
        "8",
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
      "00904530",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00904544",
      "READ",
      [
        "storage",
        "0029cb22",
        null,
        "string"
      ]
    ],
    [
      "0090454c",
      "READ",
      [
        "storage",
        "0029cb2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00904530",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00904544",
      "READ",
      [
        "storage",
        "0029cbad",
        null,
        "string"
      ]
    ],
    [
      "0090454c",
      "READ",
      [
        "storage",
        "0029cbba",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00904524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/009044e0.md#insn-00904524) · [`00904540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/009044e0.md#insn-00904540) · [`009046b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/009044e0.md#insn-009046b8)
- 新版 `00904524`（命令位置の公開資料なし） · `00904540`（命令位置の公開資料なし） · `009046b8`（命令位置の公開資料なし）

~~~diff
- 00904524 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00904524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00904524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00904524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00904524 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00904524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00904524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00904524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00904524 bytes 08a13491
+ 00904524 bytes 08e13591
- 00904540 ["COPY", "tmp:0:8", ["const:b22:8"]]
- 00904540 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00904540 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00904540 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00904540 ["COPY", "tmp:0:8", ["const:bad:8"]]
+ 00904540 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00904540 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00904540 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00904540 bytes 29892c91
+ 00904540 bytes 29b52e91
- 009046b8 ["COPY", "tmp:0:8", ["const:c46:8"]]
- 009046b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009046b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009046b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009046b8 ["COPY", "tmp:0:8", ["const:cd1:8"]]
+ 009046b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009046b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009046b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009046b8 bytes 4a193191
+ 009046b8 bytes 4a453391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d7ed7168e94b767d3e32ab96d35b4c2"></a>

### [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) → [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) FUN_00906b9c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 51件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md)
- 新版 呼出元 1件 [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 51件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md)

変更の種類 call, call_argument_candidate, call_target, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00906c3c",
      "incomplete_value": true,
      "site": "00906c58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bc3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00906c3c",
      "incomplete_value": true,
      "site": "00906c58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b38:8"
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
      "definition_site": "00906c5c",
      "incomplete_value": true,
      "site": "00906c5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00906c5c",
      "incomplete_value": true,
      "site": "00906c5c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00906f9c",
      "incomplete_value": true,
      "site": "00906fac",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
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
      "definition_site": "00906f9c",
      "incomplete_value": true,
      "site": "00906fac",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:a29:8"
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
      "00906c3c",
      "READ",
      [
        "storage",
        "0029cb38",
        null,
        "string"
      ]
    ],
    [
      "00906c40",
      "READ",
      [
        "storage",
        "0029cb45",
        null,
        "string"
      ]
    ],
    [
      "00906e38",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00906c3c",
      "READ",
      [
        "storage",
        "0029cbc3",
        null,
        "string"
      ]
    ],
    [
      "00906c40",
      "READ",
      [
        "storage",
        "0029cbd0",
        null,
        "string"
      ]
    ],
    [
      "00906e38",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00907034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md#insn-00907034) · [`00906c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md#insn-00906c2c) · [`00906cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md#insn-00906cf4)
- 新版 `00907034`（命令位置の公開資料なし） · `00906c2c`（命令位置の公開資料なし） · `00906cf4`（命令位置の公開資料なし）

~~~diff
- 00907034 ["INT_ADD", "register:40f0:8", ["const:907034:8", "const:4:8"]]
- 00907034 ["CALL", null, ["ram:a09924:8"]]
+ 00907034 ["INT_ADD", "register:40f0:8", ["const:907034:8", "const:4:8"]]
+ 00907034 ["CALL", null, ["ram:a09968:8"]]
- 00907034 bytes 3c0a0494
+ 00907034 bytes 4d0a0494
- 00906c2c ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00906c2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00906c2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00906c2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00906c2c ["COPY", "tmp:0:8", ["const:bc3:8"]]
+ 00906c2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00906c2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00906c2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00906c2c bytes 29e12c91
+ 00906c2c bytes 290d2f91
- 00906cf4 ["COPY", "tmp:0:8", ["const:25c:8"]]
- 00906cf4 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
- 00906cf4 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
- 00906cf4 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
+ 00906cf4 ["COPY", "tmp:0:8", ["const:1cf:8"]]
+ 00906cf4 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
+ 00906cf4 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
+ 00906cf4 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
- 00906cf4 bytes 7b730991
+ 00906cf4 bytes 7b3f0791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94b689778e992812a8a95a7f74f04a67"></a>

### [`0090a308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090a/0090a308.md) → [`0090a308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090a/0090a308.md) FUN_0090a308

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0090a130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090a/0090a130.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0090a130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090a/0090a130.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0090a314",
      "incomplete_value": false,
      "site": "0090a318",
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
      "definition_site": "0090a314",
      "incomplete_value": false,
      "site": "0090a318",
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
      "0090a314",
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
      "0090a314",
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

- 旧版 [`0090a314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090a/0090a308.md#insn-0090a314)
- 新版 `0090a314`（命令位置の公開資料なし）

~~~diff
- 0090a314 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0090a314 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0090a314 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0090a314 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0090a314 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0090a314 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0090a314 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0090a314 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0090a314 bytes 000c0c91
+ 0090a314 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8be4062c44229b0c4c00e9c5dcc77bac"></a>

### [`0090f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f6f4.md) → [`0090f6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090f/0090f6f4.md) FUN_0090f6f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0090f700",
      "incomplete_value": false,
      "site": "0090f704",
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
      "definition_site": "0090f700",
      "incomplete_value": false,
      "site": "0090f704",
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
      "0090f700",
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
      "0090f700",
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

- 旧版 [`0090f700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f6f4.md#insn-0090f700)
- 新版 `0090f700`（命令位置の公開資料なし）

~~~diff
- 0090f700 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0090f700 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0090f700 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0090f700 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0090f700 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0090f700 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0090f700 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0090f700 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0090f700 bytes 000c0c91
+ 0090f700 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf3de07fde7b34ba810bda56f29f8b0"></a>

### [`0090f708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f708.md) → [`0090f708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090f/0090f708.md) FUN_0090f708

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) [`0090f708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f708.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) [`0090f708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090f/0090f708.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0090f860",
      "incomplete_value": true,
      "site": "0090f868",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0090f860",
      "incomplete_value": true,
      "site": "0090f868",
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
      "definition_site": "0090f884",
      "incomplete_value": false,
      "site": "0090f890",
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
      "definition_site": "0090f884",
      "incomplete_value": false,
      "site": "0090f890",
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
      "definition_site": "0090f9b8",
      "incomplete_value": false,
      "site": "0090f9c0",
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
      "definition_site": "0090f9b8",
      "incomplete_value": false,
      "site": "0090f9c0",
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
      "0090f860",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0090f884",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0090f9b8",
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
      "0090f860",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0090f884",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0090f9b8",
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

- 旧版 [`0090f860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f708.md#insn-0090f860) · [`0090f884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f708.md#insn-0090f884) · [`0090f9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f708.md#insn-0090f9b8)
- 新版 `0090f860`（命令位置の公開資料なし） · `0090f884`（命令位置の公開資料なし） · `0090f9b8`（命令位置の公開資料なし）

~~~diff
- 0090f860 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0090f860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0090f860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0090f860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0090f860 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0090f860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0090f860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0090f860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0090f860 bytes 21280c91
+ 0090f860 bytes 21900e91
- 0090f884 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0090f884 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0090f884 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0090f884 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0090f884 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0090f884 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0090f884 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0090f884 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0090f884 bytes 21642491
+ 0090f884 bytes 21142291
- 0090f9b8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0090f9b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0090f9b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0090f9b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0090f9b8 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0090f9b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0090f9b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0090f9b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0090f9b8 bytes 21b80b91
+ 0090f9b8 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5e6d342af1154ce18484049a630506c"></a>

### [`009101cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00910/009101cc.md) → [`009101cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00910/009101cc.md) FUN_009101cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "009101d8",
      "incomplete_value": false,
      "site": "009101dc",
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
      "definition_site": "009101d8",
      "incomplete_value": false,
      "site": "009101dc",
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
      "009101d8",
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
      "009101d8",
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

- 旧版 [`009101d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00910/009101cc.md#insn-009101d8)
- 新版 `009101d8`（命令位置の公開資料なし）

~~~diff
- 009101d8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 009101d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009101d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009101d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009101d8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 009101d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009101d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009101d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009101d8 bytes 000c0c91
+ 009101d8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2b0673449d8dbb1f85ef4b6c0de5fb2"></a>

### [`00911e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00911/00911e34.md) → [`00911e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00911/00911e34.md) _INIT_183

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
      "definition_site": "00911e70",
      "incomplete_value": true,
      "site": "00911e8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00911e70",
      "incomplete_value": true,
      "site": "00911e8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00911e94",
      "incomplete_value": true,
      "site": "00911eb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00911e94",
      "incomplete_value": true,
      "site": "00911eb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00911eb4",
      "incomplete_value": true,
      "site": "00911ed0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00911eb4",
      "incomplete_value": true,
      "site": "00911ed0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00911e70",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00911e94",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00911eb4",
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
      "00911e70",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00911e94",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00911eb4",
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

- 旧版 [`00911e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00911/00911e34.md#insn-00911e60) · [`00911e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00911/00911e34.md#insn-00911e68)
- 新版 `00911e60`（命令位置の公開資料なし） · `00911e68`（命令位置の公開資料なし）

~~~diff
- 00911e60 ["COPY", "tmp:0:8", ["const:888:8"]]
- 00911e60 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00911e60 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00911e60 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00911e60 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 00911e60 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00911e60 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00911e60 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00911e60 bytes 73222291
+ 00911e60 bytes 73222391
- 00911e68 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00911e68 bytes a9ccffd0
+ 00911e68 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00911e68 bytes a9ccffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b97a7659e58d78232742d0ab515ccf10"></a>

### [`009121c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00912/009121c4.md) → [`009121c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00912/009121c4.md) FUN_009121c4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 112件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 112件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 96.24% / 新版 96.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 115件, `call_target` 4件, `store_condition` 2件, `store_destination` 35件, `store_value` 12件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "009139d4",
      "incomplete_value": false,
      "site": "009139d4",
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
      "definition_site": "009139d4",
      "incomplete_value": false,
      "site": "009139d4",
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
    "ordinal": 124,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "009139d8",
      "incomplete_value": false,
      "site": "009139d8",
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
      "definition_site": "009139d8",
      "incomplete_value": false,
      "site": "009139d8",
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
    "ordinal": 125,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009139d4",
      "incomplete_value": false,
      "site": "009139d8",
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
      "definition_site": "009139d4",
      "incomplete_value": false,
      "site": "009139d8",
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
    "ordinal": 125,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00912220",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00912234",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0091223c",
      "PARAM",
      [
        "storage",
        "00bf3d00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00912220",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00912234",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0091223c",
      "PARAM",
      [
        "storage",
        "00bf3d50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00912220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/00912/009121c4-009121c4-0092b720.md#insn-00912220) · [`00912234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/00912/009121c4-009121c4-0092b720.md#insn-00912234) · [`0091223c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/00912/009121c4-009121c4-0092b720.md#insn-0091223c)
- 新版 `00912220`（命令位置の公開資料なし） · `00912234`（命令位置の公開資料なし） · `0091223c`（命令位置の公開資料なし）

~~~diff
- 00912220 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00912220 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00912220 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00912220 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00912220 bytes 003d45f9
+ 00912220 bytes 005d45f9
- 00912234 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00912234 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00912234 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00912234 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00912234 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00912234 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00912234 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00912234 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00912234 bytes 21203991
+ 00912234 bytes 21603a91
- 0091223c ["COPY", "tmp:0:8", ["const:d00:8"]]
- 0091223c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0091223c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0091223c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0091223c ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 0091223c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0091223c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0091223c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0091223c bytes 42003491
+ 0091223c bytes 42403591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c3cb3e3825450dd2384ea3112ab7c04"></a>

### [`0092bc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md) → [`0092bc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0092b/0092bc08.md) FUN_0092bc08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 25件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`005a7c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7c94.md) [`005dfeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005df/005dfeb0.md) [`0063e6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e6d4.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`005a7c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7c94.md) [`005dfeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005df/005dfeb0.md) [`0063e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e6d4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.74% / 新版 97.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 14件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c71c",
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
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c71c",
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
    "ordinal": 38,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0092c720",
      "incomplete_value": false,
      "site": "0092c720",
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
      "definition_site": "0092c720",
      "incomplete_value": false,
      "site": "0092c720",
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
    "ordinal": 39,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c720",
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
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c720",
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
      "0092c464",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0092c484",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "0092c4f8",
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
      "0092c464",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0092c484",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "0092c4f8",
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

- 旧版 [`0092c45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md#insn-0092c45c) · [`0092c484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md#insn-0092c484) · [`0092c4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md#insn-0092c4f8)
- 新版 `0092c45c`（命令位置の公開資料なし） · `0092c484`（命令位置の公開資料なし） · `0092c4f8`（命令位置の公開資料なし）

~~~diff
- 0092c45c ["COPY", "tmp:0:8", ["const:38:8"]]
- 0092c45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0092c45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0092c45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0092c45c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0092c45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0092c45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0092c45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0092c45c bytes 08e10091
+ 0092c45c bytes 08e10191
- 0092c484 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0092c484 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0092c484 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0092c484 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0092c484 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0092c484 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0092c484 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0092c484 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0092c484 bytes 00000091
+ 0092c484 bytes 00000191
- 0092c4f8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 0092c4f8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 0092c4f8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 0092c4f8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 0092c4f8 bytes 423047f9
+ 0092c4f8 bytes 425847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aae82036a5ab722ec0f08d44e6ca1bd1"></a>

### [`009428a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md) → [`009428a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00942/009428a4.md) FUN_009428a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00942564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/00942564.md) [`009428a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00942564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00942/00942564.md) [`009428a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00942/009428a4.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00942a38",
      "incomplete_value": false,
      "site": "00942a40",
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
      "definition_site": "00942a38",
      "incomplete_value": false,
      "site": "00942a40",
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
      "definition_site": "00942af0",
      "incomplete_value": false,
      "site": "00942af8",
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
      "definition_site": "00942af0",
      "incomplete_value": false,
      "site": "00942af8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00942bc0",
      "incomplete_value": false,
      "site": "00942bcc",
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
      "definition_site": "00942bc0",
      "incomplete_value": false,
      "site": "00942bcc",
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
      "00942a38",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00942af0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00942b0c",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00942a38",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00942af0",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00942b0c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00942a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md#insn-00942a38) · [`00942af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md#insn-00942af0) · [`00942b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md#insn-00942b0c)
- 新版 `00942a38`（命令位置の公開資料なし） · `00942af0`（命令位置の公開資料なし） · `00942b0c`（命令位置の公開資料なし）

~~~diff
- 00942a38 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00942a38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00942a38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00942a38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00942a38 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00942a38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00942a38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00942a38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00942a38 bytes 21280c91
+ 00942a38 bytes 21900e91
- 00942af0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00942af0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00942af0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00942af0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00942af0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00942af0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00942af0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00942af0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00942af0 bytes 21b80b91
+ 00942af0 bytes 21e40d91
- 00942b0c ["COPY", "tmp:0:8", ["const:919:8"]]
- 00942b0c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00942b0c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00942b0c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00942b0c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00942b0c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00942b0c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00942b0c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00942b0c bytes 21642491
+ 00942b0c bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be3cc882f69df1140b00de1fa1141007"></a>

### [`00943aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md) → [`00943aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00943/00943aa0.md) FUN_00943aa0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009428a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md) [`00943aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`009428a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00942/009428a4.md) [`00943aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00943/00943aa0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00943c28",
      "incomplete_value": false,
      "site": "00943c30",
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
      "definition_site": "00943c28",
      "incomplete_value": false,
      "site": "00943c30",
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
      "definition_site": "00943ce0",
      "incomplete_value": false,
      "site": "00943ce8",
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
      "definition_site": "00943ce0",
      "incomplete_value": false,
      "site": "00943ce8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00943cfc",
      "incomplete_value": false,
      "site": "00943d08",
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
      "definition_site": "00943cfc",
      "incomplete_value": false,
      "site": "00943d08",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00943c28",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00943ce0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00943cfc",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00943c28",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00943ce0",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00943cfc",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00943c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md#insn-00943c28) · [`00943ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md#insn-00943ce0) · [`00943cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md#insn-00943cfc)
- 新版 `00943c28`（命令位置の公開資料なし） · `00943ce0`（命令位置の公開資料なし） · `00943cfc`（命令位置の公開資料なし）

~~~diff
- 00943c28 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00943c28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00943c28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00943c28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00943c28 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00943c28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00943c28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00943c28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00943c28 bytes 21280c91
+ 00943c28 bytes 21900e91
- 00943ce0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00943ce0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00943ce0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00943ce0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00943ce0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00943ce0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00943ce0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00943ce0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00943ce0 bytes 21b80b91
+ 00943ce0 bytes 21e40d91
- 00943cfc ["COPY", "tmp:0:8", ["const:919:8"]]
- 00943cfc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00943cfc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00943cfc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00943cfc ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00943cfc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00943cfc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00943cfc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00943cfc bytes 21642491
+ 00943cfc bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4765e89d3fea65ed9fb3fa3bc51ca3d6"></a>

### [`00944ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md) → [`00944ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00944/00944ab4.md) FUN_00944ab4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00943aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md) [`00944ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00943aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00943/00943aa0.md) [`00944ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00944/00944ab4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.13% / 新版 99.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00944c20",
      "incomplete_value": false,
      "site": "00944c28",
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
      "definition_site": "00944c20",
      "incomplete_value": false,
      "site": "00944c28",
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
      "definition_site": "00944c74",
      "incomplete_value": true,
      "site": "00944c80",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00944c74",
      "incomplete_value": true,
      "site": "00944c80",
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
      "definition_site": "00944db0",
      "incomplete_value": false,
      "site": "00944db8",
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
      "definition_site": "00944db0",
      "incomplete_value": false,
      "site": "00944db8",
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
      "00944c20",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00944c74",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00944db0",
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
      "00944c20",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00944c74",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00944db0",
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

- 旧版 [`00944c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md#insn-00944c20) · [`00944c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md#insn-00944c74) · [`00944db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md#insn-00944db0)
- 新版 `00944c20`（命令位置の公開資料なし） · `00944c74`（命令位置の公開資料なし） · `00944db0`（命令位置の公開資料なし）

~~~diff
- 00944c20 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00944c20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00944c20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00944c20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00944c20 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00944c20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00944c20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00944c20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00944c20 bytes 21280c91
+ 00944c20 bytes 21900e91
- 00944c74 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00944c74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00944c74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00944c74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00944c74 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00944c74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00944c74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00944c74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00944c74 bytes 21642491
+ 00944c74 bytes 21142291
- 00944db0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00944db0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00944db0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00944db0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00944db0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00944db0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00944db0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00944db0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00944db0 bytes 21b80b91
+ 00944db0 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d75e240fba98a72dc486146c989fff7e"></a>

### [`00945a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md) → [`00945a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00945/00945a50.md) FUN_00945a50

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00944ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md) [`00945a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00944ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00944/00944ab4.md) [`00945a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00945/00945a50.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00945bc8",
      "incomplete_value": false,
      "site": "00945bd0",
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
      "definition_site": "00945bc8",
      "incomplete_value": false,
      "site": "00945bd0",
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
      "definition_site": "00945c80",
      "incomplete_value": false,
      "site": "00945c88",
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
      "definition_site": "00945c80",
      "incomplete_value": false,
      "site": "00945c88",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00945c9c",
      "incomplete_value": false,
      "site": "00945ca8",
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
      "definition_site": "00945c9c",
      "incomplete_value": false,
      "site": "00945ca8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00945bc8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00945c80",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00945c9c",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00945bc8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00945c80",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00945c9c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00945bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md#insn-00945bc8) · [`00945c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md#insn-00945c80) · [`00945c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md#insn-00945c9c)
- 新版 `00945bc8`（命令位置の公開資料なし） · `00945c80`（命令位置の公開資料なし） · `00945c9c`（命令位置の公開資料なし）

~~~diff
- 00945bc8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00945bc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00945bc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00945bc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00945bc8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00945bc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00945bc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00945bc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00945bc8 bytes 21280c91
+ 00945bc8 bytes 21900e91
- 00945c80 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00945c80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00945c80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00945c80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00945c80 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00945c80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00945c80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00945c80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00945c80 bytes 21b80b91
+ 00945c80 bytes 21e40d91
- 00945c9c ["COPY", "tmp:0:8", ["const:919:8"]]
- 00945c9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00945c9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00945c9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00945c9c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00945c9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00945c9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00945c9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00945c9c bytes 21642491
+ 00945c9c bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b694bed6784bc6b7a052deb031c29432"></a>

### [`00946864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00946/00946864.md) → [`00946864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00946/00946864.md) FUN_00946864

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00945a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md) [`00946864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00946/00946864.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00945a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00945/00945a50.md) [`00946864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00946/00946864.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.98% / 新版 98.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00946bc8",
      "incomplete_value": false,
      "site": "00946bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00946bc8",
      "incomplete_value": false,
      "site": "00946bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:867:8"
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
      "definition_site": "0094704c",
      "incomplete_value": false,
      "site": "00947054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094704c",
      "incomplete_value": false,
      "site": "00947054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:866:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009469c8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "009469ec",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00946b20",
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
      "009469c8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "009469ec",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00946b20",
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

- 旧版 [`009469c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00946/00946864.md#insn-009469c8) · [`009469ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00946/00946864.md#insn-009469ec) · [`00946b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00946/00946864.md#insn-00946b20)
- 新版 `009469c8`（命令位置の公開資料なし） · `009469ec`（命令位置の公開資料なし） · `00946b20`（命令位置の公開資料なし）

~~~diff
- 009469c8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 009469c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009469c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009469c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009469c8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 009469c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009469c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009469c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009469c8 bytes 21280c91
+ 009469c8 bytes 21900e91
- 009469ec ["COPY", "tmp:0:8", ["const:919:8"]]
- 009469ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009469ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009469ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009469ec ["COPY", "tmp:0:8", ["const:885:8"]]
+ 009469ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009469ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009469ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009469ec bytes 21642491
+ 009469ec bytes 21142291
- 00946b20 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00946b20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00946b20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00946b20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00946b20 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00946b20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00946b20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00946b20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00946b20 bytes 21b80b91
+ 00946b20 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48007c6c3185763b360bfb6735e38fec"></a>

### [`0094757c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/0094757c.md) → [`0094757c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/0094757c.md) FUN_0094757c

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
      "definition_site": "00947590",
      "incomplete_value": false,
      "site": "00947594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947590",
      "incomplete_value": false,
      "site": "00947594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00947594",
      "DATA",
      [
        "storage",
        "00c099c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00947594",
      "DATA",
      [
        "storage",
        "00c09a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00947590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/0094757c.md#insn-00947590)
- 新版 `00947590`（命令位置の公開資料なし）

~~~diff
- 00947590 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00947590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00947590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00947590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00947590 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 00947590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00947590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00947590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00947590 bytes 08012791
+ 00947590 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6694ee917dbf71d6db2370ab825ec886"></a>

### [`009475a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/009475a0.md) → [`009475a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/009475a0.md) FUN_009475a0

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
      "definition_site": "009475a4",
      "incomplete_value": false,
      "site": "009475a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009475a4",
      "incomplete_value": false,
      "site": "009475a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "009475a8",
      "DATA",
      [
        "storage",
        "00c099c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009475a8",
      "DATA",
      [
        "storage",
        "00c09a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009475a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/009475a0.md#insn-009475a4)
- 新版 `009475a4`（命令位置の公開資料なし）

~~~diff
- 009475a4 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 009475a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009475a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009475a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009475a4 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 009475a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009475a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009475a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009475a4 bytes 08012791
+ 009475a4 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b2cb48b7c455d7662b7f861544c3c4d"></a>

### [`0094762c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/0094762c.md) → [`0094762c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/0094762c.md) FUN_0094762c

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
      "definition_site": "0094764c",
      "incomplete_value": false,
      "site": "00947650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094764c",
      "incomplete_value": false,
      "site": "00947650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "00947650",
      "DATA",
      [
        "storage",
        "00c09a40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00947650",
      "DATA",
      [
        "storage",
        "00c09a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0094764c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/0094762c.md#insn-0094764c)
- 新版 `0094764c`（命令位置の公開資料なし）

~~~diff
- 0094764c ["COPY", "tmp:0:8", ["const:a40:8"]]
- 0094764c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0094764c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0094764c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0094764c ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 0094764c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0094764c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0094764c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0094764c bytes 08012991
+ 0094764c bytes 08412a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-562a86f968da51dea710dafb40dbe768"></a>

### [`00947684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947684.md) → [`00947684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/00947684.md) FUN_00947684

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`0065ec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ec80.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`0065ec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ec80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094771c",
      "incomplete_value": true,
      "site": "0094772c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a01:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094771c",
      "incomplete_value": true,
      "site": "0094772c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:976:8"
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
      "definition_site": "00947774",
      "incomplete_value": false,
      "site": "00947774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947774",
      "incomplete_value": false,
      "site": "00947774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "0094771c",
      "READ",
      [
        "storage",
        "002a2976",
        null,
        "string"
      ]
    ],
    [
      "00947774",
      "DATA",
      [
        "storage",
        "00c09ab0",
        null,
        "undefined *"
      ]
    ],
    [
      "009477cc",
      "READ",
      [
        "storage",
        "00c09ad0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0094771c",
      "READ",
      [
        "storage",
        "002a2a01",
        null,
        "string"
      ]
    ],
    [
      "00947774",
      "DATA",
      [
        "storage",
        "00c09b00",
        null,
        "undefined *"
      ]
    ],
    [
      "009477cc",
      "READ",
      [
        "storage",
        "00c09b20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00947714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947684.md#insn-00947714) · [`0094776c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947684.md#insn-0094776c) · [`00947770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947684.md#insn-00947770)
- 新版 `00947714`（命令位置の公開資料なし） · `0094776c`（命令位置の公開資料なし）

~~~diff
- 00947714 ["COPY", "tmp:0:8", ["const:976:8"]]
- 00947714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00947714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00947714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00947714 ["COPY", "tmp:0:8", ["const:a01:8"]]
+ 00947714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00947714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00947714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00947714 bytes 29d92591
+ 00947714 bytes 29052891
- 0094776c ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 0094776c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0094776c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0094776c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0094776c ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 0094776c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0094776c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0094776c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0094776c bytes 08c12a91
+ 0094776c bytes 08012c91
- 00947770 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:40:8"]]
- 00947770 bytes b40301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84e5f60eaa94ab632cbd6eda78f76f42"></a>

### [`00947964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947964.md) → [`00947964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/00947964.md) FUN_00947964

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
      "definition_site": "00947988",
      "incomplete_value": false,
      "site": "00947988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947988",
      "incomplete_value": false,
      "site": "00947988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "00947988",
      "DATA",
      [
        "storage",
        "00c09ab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00947988",
      "DATA",
      [
        "storage",
        "00c09b00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00947984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947964.md#insn-00947984)
- 新版 `00947984`（命令位置の公開資料なし）

~~~diff
- 00947984 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00947984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00947984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00947984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00947984 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 00947984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00947984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00947984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00947984 bytes 08c12a91
+ 00947984 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3504b9e4cd30c88d026f18fe1d43c3bc"></a>

### [`00947998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947998.md) → [`00947998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/00947998.md) FUN_00947998

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
      "definition_site": "009479a4",
      "incomplete_value": false,
      "site": "009479a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009479a4",
      "incomplete_value": false,
      "site": "009479a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "009479a4",
      "DATA",
      [
        "storage",
        "00c09ab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009479a4",
      "DATA",
      [
        "storage",
        "00c09b00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009479a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947998.md#insn-009479a0)
- 新版 `009479a0`（命令位置の公開資料なし）

~~~diff
- 009479a0 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 009479a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009479a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009479a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009479a0 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 009479a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009479a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009479a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009479a0 bytes 29c12a91
+ 009479a0 bytes 29012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-716fa6a984aab001b5dcb6467a53f759"></a>

### [`00947c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947c00.md) → [`00947c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/00947c00.md) FUN_00947c00

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
      "definition_site": "00947c14",
      "incomplete_value": false,
      "site": "00947c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947c14",
      "incomplete_value": false,
      "site": "00947c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "00947c18",
      "DATA",
      [
        "storage",
        "00c09b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00947c18",
      "DATA",
      [
        "storage",
        "00c09b90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00947c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947c00.md#insn-00947c14)
- 新版 `00947c14`（命令位置の公開資料なし）

~~~diff
- 00947c14 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 00947c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00947c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00947c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00947c14 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00947c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00947c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00947c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00947c14 bytes 08012d91
+ 00947c14 bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2f91ac32d4d25fd7d3a136fa08bbc30"></a>

### [`00947d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947d34.md) → [`00947d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/00947d34.md) FUN_00947d34

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00947d48",
      "incomplete_value": true,
      "site": "00947d4c",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947d48",
      "incomplete_value": true,
      "site": "00947d4c",
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
            "const:bc0:8"
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
      "00947d4c",
      "DATA",
      [
        "storage",
        "00c09bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00947d4c",
      "DATA",
      [
        "storage",
        "00c09c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00947d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947d34.md#insn-00947d48)
- 新版 `00947d48`（命令位置の公開資料なし）

~~~diff
- 00947d48 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00947d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00947d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00947d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00947d48 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00947d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00947d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00947d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00947d48 bytes 08012f91
+ 00947d48 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e54a7cd0d4f912685e42fdb2e303725"></a>

### [`00948440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948440.md) → [`00948440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00948/00948440.md) FUN_00948440

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
      "definition_site": "00948454",
      "incomplete_value": false,
      "site": "00948458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00948454",
      "incomplete_value": false,
      "site": "00948458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "00948458",
      "DATA",
      [
        "storage",
        "00c09c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00948458",
      "DATA",
      [
        "storage",
        "00c09c90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00948454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948440.md#insn-00948454)
- 新版 `00948454`（命令位置の公開資料なし）

~~~diff
- 00948454 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00948454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00948454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00948454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00948454 ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 00948454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00948454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00948454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00948454 bytes 08013191
+ 00948454 bytes 08413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67ffc267b17bfb660af749934564f3af"></a>

### [`0094847c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/0094847c.md) → [`0094847c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00948/0094847c.md) FUN_0094847c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`00447a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447a10.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.43% / 新版 99.43%

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
      "definition_site": "00948884",
      "incomplete_value": true,
      "site": "00948884",
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
      "definition_site": "00948884",
      "incomplete_value": true,
      "site": "00948884",
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0094888c",
      "incomplete_value": false,
      "site": "0094889c",
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
      "definition_site": "0094888c",
      "incomplete_value": false,
      "site": "0094889c",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00948894",
      "incomplete_value": false,
      "site": "0094889c",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00948894",
      "incomplete_value": false,
      "site": "0094889c",
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
            "const:d00:8"
          ]
        ]
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
      "00948880",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0094888c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00948894",
      "PARAM",
      [
        "storage",
        "00bf3d00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00948880",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0094888c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00948894",
      "PARAM",
      [
        "storage",
        "00bf3d50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00948880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/0094847c.md#insn-00948880) · [`0094888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/0094847c.md#insn-0094888c) · [`00948894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/0094847c.md#insn-00948894)
- 新版 `00948880`（命令位置の公開資料なし） · `0094888c`（命令位置の公開資料なし） · `00948894`（命令位置の公開資料なし）

~~~diff
- 00948880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00948880 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00948880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00948880 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00948880 bytes 003d45f9
+ 00948880 bytes 005d45f9
- 0094888c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0094888c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0094888c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0094888c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0094888c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0094888c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0094888c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0094888c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0094888c bytes 21203991
+ 0094888c bytes 21603a91
- 00948894 ["COPY", "tmp:0:8", ["const:d00:8"]]
- 00948894 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00948894 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00948894 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00948894 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00948894 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00948894 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00948894 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00948894 bytes 42003491
+ 00948894 bytes 42403591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2e71321d96fd532edaf542477488566"></a>

### [`00948a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948a24.md) → [`00948a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00948/00948a24.md) _INIT_184

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00948aa4",
      "incomplete_value": true,
      "site": "00948ac0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00948aa4",
      "incomplete_value": true,
      "site": "00948ac0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00948ac4",
      "incomplete_value": true,
      "site": "00948adc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00948ac4",
      "incomplete_value": true,
      "site": "00948adc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00948ae0",
      "incomplete_value": true,
      "site": "00948afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00948ae0",
      "incomplete_value": true,
      "site": "00948afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00948a60",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00948a84",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00948aa4",
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
      "00948a60",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00948a84",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00948aa4",
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

- 旧版 [`00948a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948a24.md#insn-00948a50) · [`00948a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948a24.md#insn-00948a5c) · [`00948a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948a24.md#insn-00948a78)
- 新版 `00948a50`（命令位置の公開資料なし） · `00948a5c`（命令位置の公開資料なし） · `00948a78`（命令位置の公開資料なし）

~~~diff
- 00948a50 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00948a50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00948a50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00948a50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00948a50 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 00948a50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00948a50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00948a50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00948a50 bytes 73822291
+ 00948a50 bytes 73822391
- 00948a5c ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00948a5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00948a5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00948a5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00948a5c ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00948a5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00948a5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00948a5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00948a5c bytes 29750b91
+ 00948a5c bytes 29dd0d91
- 00948a78 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 00948a78 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00948a78 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00948a78 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00948a78 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 00948a78 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00948a78 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00948a78 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00948a78 bytes 4ac10b91
+ 00948a78 bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55f430a2f826306d5599a97b0835fb6e"></a>

### [`00948db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948db4.md) → [`00948db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00948/00948db4.md) FUN_00948db4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00949ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949ed8.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`005748e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005748e4.md) [`00574bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bb4.md) [`009496f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/009496f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00949ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00949/00949ed8.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`005748e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748e4.md) [`00574bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bb4.md) [`009496f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00949/009496f0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.93% / 新版 97.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009491d0",
      "incomplete_value": true,
      "site": "009491d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009491d0",
      "incomplete_value": true,
      "site": "009491d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:74e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00949328",
      "incomplete_value": true,
      "site": "00949328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:85c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00949328",
      "incomplete_value": true,
      "site": "00949328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 68,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009494c4",
      "incomplete_value": true,
      "site": "009494c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:744:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009494c4",
      "incomplete_value": true,
      "site": "009494c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:6b9:8"
              ]
            ]
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
      "00948ff8",
      "READ",
      [
        "storage",
        "002a770a",
        null,
        "string"
      ]
    ],
    [
      "009491c4",
      "READ",
      [
        "storage",
        "0029374e",
        null,
        "string"
      ]
    ],
    [
      "00949314",
      "READ",
      [
        "storage",
        "002a57d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00948ff8",
      "READ",
      [
        "storage",
        "002a77a4",
        null,
        "string"
      ]
    ],
    [
      "009491c4",
      "READ",
      [
        "storage",
        "002936c1",
        null,
        "string"
      ]
    ],
    [
      "00949314",
      "READ",
      [
        "storage",
        "002a585c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00948ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948db4.md#insn-00948ff0) · [`009491b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948db4.md#insn-009491b8) · [`0094930c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948db4.md#insn-0094930c)
- 新版 `00948ff0`（命令位置の公開資料なし） · `009491b8`（命令位置の公開資料なし） · `0094930c`（命令位置の公開資料なし）

~~~diff
- 00948ff0 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 00948ff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00948ff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00948ff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00948ff0 ["COPY", "tmp:0:8", ["const:7a4:8"]]
+ 00948ff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00948ff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00948ff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00948ff0 bytes 29291c91
+ 00948ff0 bytes 29911e91
- 009491b8 ["COPY", "tmp:0:8", ["const:74e:8"]]
- 009491b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009491b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009491b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009491b8 ["COPY", "tmp:0:8", ["const:6c1:8"]]
+ 009491b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009491b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009491b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009491b8 bytes 29391d91
+ 009491b8 bytes 29051b91
- 0094930c ["COPY", "tmp:0:8", ["const:7d1:8"]]
- 0094930c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0094930c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0094930c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0094930c ["COPY", "tmp:0:8", ["const:85c:8"]]
+ 0094930c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0094930c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0094930c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0094930c bytes 29451f91
+ 0094930c bytes 29712191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccb1c775c2fdba430fcff74dc5e2c83e"></a>

### [`00949c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949c4c.md) → [`00949c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00949/00949c4c.md) FUN_00949c4c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) · 呼出先 11件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`00428cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428cb4.md) [`00428e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428e88.md) [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`0053f0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f0f8.md)
- 新版 呼出元 1件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) · 呼出先 11件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00428cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428cb4.md) [`00428e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428e88.md) [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) [`0053f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00949d00",
      "incomplete_value": false,
      "site": "00949d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00949d00",
      "incomplete_value": false,
      "site": "00949d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
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
      "definition_site": "00949cd8",
      "incomplete_value": true,
      "site": "00949ce0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00949cd8",
      "incomplete_value": true,
      "site": "00949ce0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00949cd8",
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      "00949cd8",
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "00949d00",
      "DATA",
      [
        "storage",
        "00c09cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00949cd8",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00949cd8",
      "PARAM",
      [
        "storage",
        "00c25e10",
        null,
        "undefined1"
      ]
    ],
    [
      "00949d00",
      "DATA",
      [
        "storage",
        "00c09d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00949cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949c4c.md#insn-00949cd8) · [`00949cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949c4c.md#insn-00949cf8)
- 新版 `00949cd8`（命令位置の公開資料なし） · `00949cf8`（命令位置の公開資料なし）

~~~diff
- 00949cd8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
- 00949cd8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00949cd8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:dd8:8"]]
+ 00949cd8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00949cd8 bytes 00c446f9
+ 00949cd8 bytes 00ec46f9
- 00949cf8 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 00949cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00949cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00949cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00949cf8 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00949cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00949cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00949cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00949cf8 bytes 08613391
+ 00949cf8 bytes 08a13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29efb9c2ab386f4ab49ee14717eaea1b"></a>

### [`00949ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949ed8.md) → [`00949ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00949/00949ed8.md) FUN_00949ed8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0094bc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc30.md) [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0045e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md) [`0045f0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f0ac.md)
- 新版 呼出元 2件 [`0094bc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094b/0094bc30.md) [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0045e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md) [`0045f0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f0ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00949f44",
      "incomplete_value": true,
      "site": "00949f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:84f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00949f44",
      "incomplete_value": true,
      "site": "00949f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c4:8"
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
      "definition_site": "0094a010",
      "incomplete_value": true,
      "site": "0094a010",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094a010",
      "incomplete_value": true,
      "site": "0094a010",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:952:8"
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
      "definition_site": "0094a254",
      "incomplete_value": true,
      "site": "0094a264",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7a4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094a254",
      "incomplete_value": true,
      "site": "0094a264",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:70a:8"
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
      "00949f30",
      "READ",
      [
        "storage",
        "002a57c4",
        null,
        "string"
      ]
    ],
    [
      "00949f58",
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      "0094a000",
      "READ",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00949f30",
      "READ",
      [
        "storage",
        "002a584f",
        null,
        "string"
      ]
    ],
    [
      "00949f58",
      "PARAM",
      [
        "storage",
        "002a9259",
        null,
        null
      ]
    ],
    [
      "0094a000",
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00949f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949ed8.md#insn-00949f24) · [`00949f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949ed8.md#insn-00949f58) · [`00949ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949ed8.md#insn-00949ff8)
- 新版 `00949f24`（命令位置の公開資料なし） · `00949f58`（命令位置の公開資料なし） · `00949ff8`（命令位置の公開資料なし）

~~~diff
- 00949f24 ["COPY", "tmp:0:8", ["const:7c4:8"]]
- 00949f24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00949f24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00949f24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00949f24 ["COPY", "tmp:0:8", ["const:84f:8"]]
+ 00949f24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00949f24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00949f24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00949f24 bytes 29111f91
+ 00949f24 bytes 293d2191
- 00949f58 ["COPY", "tmp:0:8", ["const:1bf:8"]]
- 00949f58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00949f58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00949f58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00949f58 ["COPY", "tmp:0:8", ["const:259:8"]]
+ 00949f58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00949f58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00949f58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00949f58 bytes 21fc0691
+ 00949f58 bytes 21640991
- 00949ff8 ["COPY", "tmp:0:8", ["const:952:8"]]
- 00949ff8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00949ff8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00949ff8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00949ff8 ["COPY", "tmp:0:8", ["const:8c5:8"]]
+ 00949ff8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00949ff8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00949ff8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00949ff8 bytes 29492591
+ 00949ff8 bytes 29152391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b5c9163b9ab9d61ab2e830704658770"></a>

### [`0094bbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bbe0.md) → [`0094bbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094b/0094bbe0.md) FUN_0094bbe0

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
      "definition_site": "0094bc04",
      "incomplete_value": false,
      "site": "0094bc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094bc04",
      "incomplete_value": false,
      "site": "0094bc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
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
      "0094bc04",
      "DATA",
      [
        "storage",
        "00c09cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0094bc04",
      "DATA",
      [
        "storage",
        "00c09d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0094bc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bbe0.md#insn-0094bc00)
- 新版 `0094bc00`（命令位置の公開資料なし）

~~~diff
- 0094bc00 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 0094bc00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0094bc00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0094bc00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0094bc00 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 0094bc00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0094bc00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0094bc00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0094bc00 bytes 08613391
+ 0094bc00 bytes 08a13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec3945349be2c18ff3677651cbc4116"></a>

### [`0094bc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc14.md) → [`0094bc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094b/0094bc14.md) FUN_0094bc14

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
      "definition_site": "0094bc20",
      "incomplete_value": false,
      "site": "0094bc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094bc20",
      "incomplete_value": false,
      "site": "0094bc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
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
      "0094bc20",
      "DATA",
      [
        "storage",
        "00c09cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0094bc20",
      "DATA",
      [
        "storage",
        "00c09d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0094bc1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc14.md#insn-0094bc1c)
- 新版 `0094bc1c`（命令位置の公開資料なし）

~~~diff
- 0094bc1c ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 0094bc1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0094bc1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0094bc1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0094bc1c ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 0094bc1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bc1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bc1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0094bc1c bytes 29613391
+ 0094bc1c bytes 29a13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4523062cc3c315a92837c0c4a888633b"></a>

### [`0094bc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc30.md) → [`0094bc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094b/0094bc30.md) FUN_0094bc30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0045e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md) [`0045f524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f524.md) [`0045f660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f660.md) [`0045f6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f6d8.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0045e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md) [`0045f524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f524.md) [`0045f660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f660.md) [`0045f6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f6d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.97% / 新版 95.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094bd0c",
      "incomplete_value": true,
      "site": "0094bd0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:84f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094bd0c",
      "incomplete_value": true,
      "site": "0094bd0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c4:8"
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
      "definition_site": "0094bdd4",
      "incomplete_value": true,
      "site": "0094bdd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094bdd4",
      "incomplete_value": true,
      "site": "0094bdd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:952:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0094bec8",
      "incomplete_value": false,
      "site": "0094becc",
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
                "const:be8000:8"
              ],
              [
                "leaf",
                "const:570:8"
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
      "definition_site": "0094bec8",
      "incomplete_value": false,
      "site": "0094becc",
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
                "const:be8000:8"
              ],
              [
                "leaf",
                "const:520:8"
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
      "0094bcf8",
      "READ",
      [
        "storage",
        "002a57c4",
        null,
        "string"
      ]
    ],
    [
      "0094bd20",
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      "0094bdc4",
      "READ",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0094bcf8",
      "READ",
      [
        "storage",
        "002a584f",
        null,
        "string"
      ]
    ],
    [
      "0094bd20",
      "PARAM",
      [
        "storage",
        "002a9259",
        null,
        null
      ]
    ],
    [
      "0094bdc4",
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0094bcec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc30.md#insn-0094bcec) · [`0094bd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc30.md#insn-0094bd20) · [`0094bdbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc30.md#insn-0094bdbc)
- 新版 `0094bcec`（命令位置の公開資料なし） · `0094bd20`（命令位置の公開資料なし） · `0094bdbc`（命令位置の公開資料なし）

~~~diff
- 0094bcec ["COPY", "tmp:0:8", ["const:7c4:8"]]
- 0094bcec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0094bcec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0094bcec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0094bcec ["COPY", "tmp:0:8", ["const:84f:8"]]
+ 0094bcec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bcec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bcec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0094bcec bytes 29111f91
+ 0094bcec bytes 293d2191
- 0094bd20 ["COPY", "tmp:0:8", ["const:1bf:8"]]
- 0094bd20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0094bd20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0094bd20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0094bd20 ["COPY", "tmp:0:8", ["const:259:8"]]
+ 0094bd20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0094bd20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0094bd20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0094bd20 bytes 21fc0691
+ 0094bd20 bytes 21640991
- 0094bdbc ["COPY", "tmp:0:8", ["const:952:8"]]
- 0094bdbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0094bdbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0094bdbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0094bdbc ["COPY", "tmp:0:8", ["const:8c5:8"]]
+ 0094bdbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bdbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bdbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0094bdbc bytes 29492591
+ 0094bdbc bytes 29152391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d77687cef361a9b42f9ab300ab43c99f"></a>

### [`0094c570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094c570.md) → [`0094c570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094c/0094c570.md) FUN_0094c570

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0094c174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094c174.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0094c174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094c/0094c174.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0094c57c",
      "incomplete_value": false,
      "site": "0094c580",
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
      "definition_site": "0094c57c",
      "incomplete_value": false,
      "site": "0094c580",
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
      "0094c57c",
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
      "0094c57c",
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

- 旧版 [`0094c57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094c570.md#insn-0094c57c)
- 新版 `0094c57c`（命令位置の公開資料なし）

~~~diff
- 0094c57c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0094c57c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0094c57c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0094c57c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0094c57c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0094c57c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0094c57c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0094c57c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0094c57c bytes 000c0c91
+ 0094c57c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e53a272e310e9210b69f848f370c1fe"></a>

### [`0094cd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094cd94.md) → [`0094cd94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094c/0094cd94.md) _INIT_185

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094cdd0",
      "incomplete_value": true,
      "site": "0094cdec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0094cdd0",
      "incomplete_value": true,
      "site": "0094cdec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0094cdf4",
      "incomplete_value": true,
      "site": "0094ce10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0094cdf4",
      "incomplete_value": true,
      "site": "0094ce10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0094ce14",
      "incomplete_value": true,
      "site": "0094ce30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0094ce14",
      "incomplete_value": true,
      "site": "0094ce30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0094cdd0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0094cdf4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0094ce14",
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
      "0094cdd0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0094cdf4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0094ce14",
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

- 旧版 [`0094cdc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094cd94.md#insn-0094cdc0) · [`0094cdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094cd94.md#insn-0094cdc8)
- 新版 `0094cdc0`（命令位置の公開資料なし） · `0094cdc8`（命令位置の公開資料なし）

~~~diff
- 0094cdc0 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 0094cdc0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0094cdc0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0094cdc0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0094cdc0 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 0094cdc0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0094cdc0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0094cdc0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0094cdc0 bytes 73e22291
+ 0094cdc0 bytes 73e22391
- 0094cdc8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0094cdc8 bytes c9cafff0
+ 0094cdc8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0094cdc8 bytes c9cafff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8cc95ae133dd98ff326c84696677a59"></a>

### [`0094d124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094d/0094d124.md) → [`0094d124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094d/0094d124.md) FUN_0094d124

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 22件 [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`004752f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004752f8.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md)
- 新版 呼出元 2件 [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) · 呼出先 22件 [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`004752f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004752f8.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 91.91% / 新版 91.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 36件, `store_condition` 2件, `store_destination` 31件, `store_value` 14件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0094d178",
      "incomplete_value": true,
      "site": "0094d178",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094d178",
      "incomplete_value": true,
      "site": "0094d178",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094dca4",
      "incomplete_value": true,
      "site": "0094dcb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094dca4",
      "incomplete_value": true,
      "site": "0094dcb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c44:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 86,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094df6c",
      "incomplete_value": true,
      "site": "0094df80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094df6c",
      "incomplete_value": true,
      "site": "0094df80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 99,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0094d168",
      "READ",
      [
        "storage",
        "00c246e0",
        null,
        "undefined4"
      ]
    ],
    [
      "0094d178",
      "WRITE",
      [
        "storage",
        "00c246e0",
        null,
        "undefined4"
      ]
    ],
    [
      "0094d17c",
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
      "0094d168",
      "READ",
      [
        "storage",
        "00c24730",
        null,
        "undefined4"
      ]
    ],
    [
      "0094d178",
      "WRITE",
      [
        "storage",
        "00c24730",
        null,
        "undefined4"
      ]
    ],
    [
      "0094d17c",
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

- 旧版 [`0094d178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094d/0094d124.md#insn-0094d178) · [`0094d168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094d/0094d124.md#insn-0094d168) · [`0094d17c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094d/0094d124.md#insn-0094d17c)
- 新版 `0094d178`（命令位置の公開資料なし） · `0094d168`（命令位置の公開資料なし） · `0094d17c`（命令位置の公開資料なし）

~~~diff
- 0094d178 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6e0:8"]]
- 0094d178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
+ 0094d178 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:730:8"]]
+ 0094d178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
- 0094d178 bytes 18e106b9
+ 0094d178 bytes 183107b9
- 0094d168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6e0:8"]]
- 0094d168 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 0094d168 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 0094d168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:730:8"]]
+ 0094d168 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 0094d168 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 0094d168 bytes 09e146b9
+ 0094d168 bytes 093147b9
- 0094d17c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 0094d17c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0094d17c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 0094d17c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0094d17c bytes 203d45f9
+ 0094d17c bytes 205d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76032d669919c5447e2fe2447e3f850b"></a>

### [`0094efec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094e/0094efec.md) → [`0094efec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094e/0094efec.md) FUN_0094efec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00680c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/00680c84.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 14件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00640490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640490.md) [`0066f824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f824.md) [`0094f64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f64c.md)
- 新版 呼出元 2件 [`00680c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00680/00680c84.md) [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) · 呼出先 14件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00640490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640490.md) [`0066f824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f824.md) [`0094f64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f64c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 91.41% / 新版 91.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3dc",
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
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3dc",
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
    "ordinal": 25,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0094f3e0",
      "incomplete_value": false,
      "site": "0094f3e0",
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
      "definition_site": "0094f3e0",
      "incomplete_value": false,
      "site": "0094f3e0",
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
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3e0",
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
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3e0",
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
      "0094f034",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0094f048",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0094f050",
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0094f034",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0094f048",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0094f050",
      "PARAM",
      [
        "storage",
        "00bf3d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0094f034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094e/0094efec.md#insn-0094f034) · [`0094f048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094e/0094efec.md#insn-0094f048) · [`0094f050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094e/0094efec.md#insn-0094f050)
- 新版 `0094f034`（命令位置の公開資料なし） · `0094f048`（命令位置の公開資料なし） · `0094f050`（命令位置の公開資料なし）

~~~diff
- 0094f034 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0094f034 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0094f034 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0094f034 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0094f034 bytes 003d45f9
+ 0094f034 bytes 005d45f9
- 0094f048 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0094f048 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0094f048 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0094f048 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0094f048 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0094f048 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0094f048 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0094f048 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0094f048 bytes 21203991
+ 0094f048 bytes 21603a91
- 0094f050 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 0094f050 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0094f050 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0094f050 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0094f050 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 0094f050 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0094f050 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0094f050 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0094f050 bytes 42203591
+ 0094f050 bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3dec4355c49173c33153d2e650e170c"></a>

### [`00957320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957320.md) → [`00957320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957320.md) FUN_00957320

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00680c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/00680c84.md) [`0092bc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md) [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 18件 [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`005bdd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bd/005bdd1c.md) [`005dfeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005df/005dfeb0.md)
- 新版 呼出元 4件 [`00680c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00680/00680c84.md) [`0092bc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0092b/0092bc08.md) [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) · 呼出先 18件 [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`0044b660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b660.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`005bdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bdd1c.md) [`005dfeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005df/005dfeb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009573ac",
      "incomplete_value": true,
      "site": "009573ac",
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
      "definition_site": "009573ac",
      "incomplete_value": true,
      "site": "009573ac",
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009573b4",
      "incomplete_value": false,
      "site": "009573c4",
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
      "definition_site": "009573b4",
      "incomplete_value": false,
      "site": "009573c4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009573bc",
      "incomplete_value": false,
      "site": "009573c4",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009573bc",
      "incomplete_value": false,
      "site": "009573c4",
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
            "const:d48:8"
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
      "009573a8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009573b4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009573bc",
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009573a8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "009573b4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009573bc",
      "PARAM",
      [
        "storage",
        "00bf3d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009573a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957320.md#insn-009573a8) · [`009573b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957320.md#insn-009573b4) · [`009573bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957320.md#insn-009573bc)
- 新版 `009573a8`（命令位置の公開資料なし） · `009573b4`（命令位置の公開資料なし） · `009573bc`（命令位置の公開資料なし）

~~~diff
- 009573a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 009573a8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 009573a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 009573a8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 009573a8 bytes 003d45f9
+ 009573a8 bytes 005d45f9
- 009573b4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 009573b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009573b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009573b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009573b4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 009573b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009573b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009573b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009573b4 bytes 21203991
+ 009573b4 bytes 21603a91
- 009573bc ["COPY", "tmp:0:8", ["const:d48:8"]]
- 009573bc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 009573bc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 009573bc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 009573bc ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 009573bc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 009573bc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 009573bc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 009573bc bytes 42203591
+ 009573bc bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4639d5c786689bb255825ea0dae0cf46"></a>

### [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) → [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) FUN_00957f9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 128件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 128件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0044b660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b660.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 67件, `store_condition` 2件, `store_destination` 40件, `store_value` 18件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009583ec",
      "incomplete_value": true,
      "site": "009583fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:24f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009583ec",
      "incomplete_value": true,
      "site": "009583fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dc:8"
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
      "definition_site": "009583f0",
      "incomplete_value": true,
      "site": "00958400",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009583f0",
      "incomplete_value": true,
      "site": "00958400",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00958424",
      "incomplete_value": false,
      "site": "00958424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00958424",
      "incomplete_value": false,
      "site": "00958424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:68:8"
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
      "009583ec",
      "READ",
      [
        "storage",
        "002982dc",
        null,
        "string"
      ]
    ],
    [
      "009583f0",
      "READ",
      [
        "storage",
        "002982e9",
        null,
        "string"
      ]
    ],
    [
      "00958424",
      "DATA",
      [
        "storage",
        "00c0a068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009583ec",
      "READ",
      [
        "storage",
        "0029824f",
        null,
        "string"
      ]
    ],
    [
      "009583f0",
      "READ",
      [
        "storage",
        "0029825c",
        null,
        "string"
      ]
    ],
    [
      "00958424",
      "DATA",
      [
        "storage",
        "00c0a0b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009583e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/00957/00957f9c-00957f9c-00960c98.md#insn-009583e4) · [`009583e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/00957/00957f9c-00957f9c-00960c98.md#insn-009583e8)
- 新版 `009583e4`（命令位置の公開資料なし） · `009583e8`（命令位置の公開資料なし）

~~~diff
- 009583e4 ["COPY", "tmp:0:8", ["const:2dc:8"]]
- 009583e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009583e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009583e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009583e4 ["COPY", "tmp:0:8", ["const:24f:8"]]
+ 009583e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009583e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009583e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009583e4 bytes 08710b91
+ 009583e4 bytes 083d0991
- 009583e8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 009583e8 bytes c9caffb0
+ 009583e8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 009583e8 bytes c9caffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf345ccbca3c80dd71badd62d73c086d"></a>

### [`00960d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00960/00960d40.md) → [`00960d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00960/00960d40.md) FUN_00960d40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/008879f4.md) [`0096dfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfdc.md) [`0096dfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfe0.md)
- 新版 呼出元 1件 [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`008865b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879f4.md) [`0096dfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096dfdc.md) [`0096dfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096dfe0.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00960d7c",
      "incomplete_value": true,
      "site": "00960d7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:26d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00960d7c",
      "incomplete_value": true,
      "site": "00960d7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fa:8"
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
      "definition_site": "00960d74",
      "incomplete_value": true,
      "site": "00960d80",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00960d74",
      "incomplete_value": true,
      "site": "00960d80",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00960d98",
      "incomplete_value": false,
      "site": "00960da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00960d98",
      "incomplete_value": false,
      "site": "00960da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "00960d64",
      "READ",
      [
        "storage",
        "002982fa",
        null,
        "string"
      ]
    ],
    [
      "00960d74",
      "READ",
      [
        "storage",
        "00298301",
        null,
        "string"
      ]
    ],
    [
      "00960da0",
      "DATA",
      [
        "storage",
        "00c0a268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00960d64",
      "READ",
      [
        "storage",
        "0029826d",
        null,
        "string"
      ]
    ],
    [
      "00960d74",
      "READ",
      [
        "storage",
        "00298274",
        null,
        "string"
      ]
    ],
    [
      "00960da0",
      "DATA",
      [
        "storage",
        "00c0a2b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00960d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00960/00960d40.md#insn-00960d5c) · [`00960d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00960/00960d40.md#insn-00960d98) · [`00960d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00960/00960d40.md#insn-00960d9c)
- 新版 `00960d5c`（命令位置の公開資料なし） · `00960d98`（命令位置の公開資料なし）

~~~diff
- 00960d5c ["COPY", "tmp:0:8", ["const:2fa:8"]]
- 00960d5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00960d5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00960d5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00960d5c ["COPY", "tmp:0:8", ["const:26d:8"]]
+ 00960d5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00960d5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00960d5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00960d5c bytes 29e90b91
+ 00960d5c bytes 29b50991
- 00960d98 ["COPY", "tmp:0:8", ["const:268:8"]]
- 00960d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00960d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00960d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00960d98 ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 00960d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00960d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00960d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00960d98 bytes 08a10991
+ 00960d98 bytes 08e10a91
- 00960d9c ["COPY", "tmp:0:8", ["const:30:8"]]
- 00960d9c ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00960d9c ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00960d9c ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00960d9c bytes f5c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01fbf5ca898ad7a60e701fe4e95d61f4"></a>

### [`009613bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00961/009613bc.md) → [`009613bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00961/009613bc.md) FUN_009613bc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 35件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 35件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00961444",
      "incomplete_value": true,
      "site": "00961444",
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
      "definition_site": "00961444",
      "incomplete_value": true,
      "site": "00961444",
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
      "definition_site": "0096149c",
      "incomplete_value": true,
      "site": "0096149c",
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
      "definition_site": "0096149c",
      "incomplete_value": true,
      "site": "0096149c",
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096144c",
      "incomplete_value": false,
      "site": "0096145c",
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
      "definition_site": "0096144c",
      "incomplete_value": false,
      "site": "0096145c",
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
      "00961420",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0096144c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00961454",
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00961420",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0096144c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00961454",
      "PARAM",
      [
        "storage",
        "00bf3d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00961420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00961/009613bc.md#insn-00961420) · [`0096144c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00961/009613bc.md#insn-0096144c) · [`00961454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00961/009613bc.md#insn-00961454)
- 新版 `00961420`（命令位置の公開資料なし） · `0096144c`（命令位置の公開資料なし） · `00961454`（命令位置の公開資料なし）

~~~diff
- 00961420 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:a78:8"]]
- 00961420 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00961420 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ab8:8"]]
+ 00961420 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00961420 bytes 403d45f9
+ 00961420 bytes 405d45f9
- 0096144c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0096144c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0096144c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0096144c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0096144c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0096144c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0096144c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0096144c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0096144c bytes 21203991
+ 0096144c bytes 21603a91
- 00961454 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00961454 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00961454 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00961454 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00961454 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00961454 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00961454 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00961454 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00961454 bytes 42203591
+ 00961454 bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-272e7b6f5af48b83746f6dad5fa09546"></a>

### [`00965df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00965/00965df0.md) → [`00965df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00965/00965df0.md) FUN_00965df0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009613bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00961/009613bc.md) [`0096de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096de04.md) · 呼出先 33件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)
- 新版 呼出元 2件 [`009613bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00961/009613bc.md) [`0096de04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096de04.md) · 呼出先 33件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.57% / 新版 98.57%

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
      "definition_site": "00965e48",
      "incomplete_value": true,
      "site": "00965e48",
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
      "definition_site": "00965e48",
      "incomplete_value": true,
      "site": "00965e48",
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
      "definition_site": "00965e50",
      "incomplete_value": false,
      "site": "00965e60",
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
      "definition_site": "00965e50",
      "incomplete_value": false,
      "site": "00965e60",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00965e58",
      "incomplete_value": false,
      "site": "00965e60",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00965e58",
      "incomplete_value": false,
      "site": "00965e60",
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
            "const:d48:8"
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
      "00965e3c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00965e50",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00965e58",
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00965e3c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00965e50",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00965e58",
      "PARAM",
      [
        "storage",
        "00bf3d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00965e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00965/00965df0.md#insn-00965e3c) · [`00965e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00965/00965df0.md#insn-00965e50) · [`00965e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00965/00965df0.md#insn-00965e58)
- 新版 `00965e3c`（命令位置の公開資料なし） · `00965e50`（命令位置の公開資料なし） · `00965e58`（命令位置の公開資料なし）

~~~diff
- 00965e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00965e3c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00965e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00965e3c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00965e3c bytes 003d45f9
+ 00965e3c bytes 005d45f9
- 00965e50 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00965e50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00965e50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00965e50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00965e50 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00965e50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00965e50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00965e50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00965e50 bytes 21203991
+ 00965e50 bytes 21603a91
- 00965e58 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00965e58 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00965e58 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00965e58 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00965e58 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00965e58 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00965e58 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00965e58 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00965e58 bytes 42203591
+ 00965e58 bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b0f9677fb5dc9539073edb7873a865e"></a>

### [`0096b7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096b/0096b7d8.md) → [`0096b7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096b/0096b7d8.md) FUN_0096b7d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00963004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00963/00963004.md) · 呼出先 6件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00963004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00963/00963004.md) · 呼出先 6件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00447a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447a10.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "definition_site": "0096b81c",
      "incomplete_value": true,
      "site": "0096b81c",
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
      "definition_site": "0096b81c",
      "incomplete_value": true,
      "site": "0096b81c",
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
      "definition_site": "0096b824",
      "incomplete_value": false,
      "site": "0096b838",
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
      "definition_site": "0096b824",
      "incomplete_value": false,
      "site": "0096b838",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096b82c",
      "incomplete_value": false,
      "site": "0096b838",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096b82c",
      "incomplete_value": false,
      "site": "0096b838",
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
            "const:d48:8"
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
      "0096b818",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0096b824",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0096b82c",
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0096b818",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0096b824",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0096b82c",
      "PARAM",
      [
        "storage",
        "00bf3d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096b818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096b/0096b7d8.md#insn-0096b818) · [`0096b824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096b/0096b7d8.md#insn-0096b824) · [`0096b82c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096b/0096b7d8.md#insn-0096b82c)
- 新版 `0096b818`（命令位置の公開資料なし） · `0096b824`（命令位置の公開資料なし） · `0096b82c`（命令位置の公開資料なし）

~~~diff
- 0096b818 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0096b818 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0096b818 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0096b818 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0096b818 bytes 083d45f9
+ 0096b818 bytes 085d45f9
- 0096b824 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0096b824 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0096b824 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0096b824 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0096b824 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0096b824 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0096b824 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0096b824 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0096b824 bytes 21203991
+ 0096b824 bytes 21603a91
- 0096b82c ["COPY", "tmp:0:8", ["const:d48:8"]]
- 0096b82c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0096b82c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0096b82c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0096b82c ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 0096b82c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0096b82c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0096b82c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0096b82c bytes 42203591
+ 0096b82c bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6c3b5379e6e4449110c7623447ae5ee"></a>

### [`0096d13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d13c.md) → [`0096d13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096d13c.md) FUN_0096d13c

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
      "definition_site": "0096d160",
      "incomplete_value": false,
      "site": "0096d160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d160",
      "incomplete_value": false,
      "site": "0096d160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:d58:8"
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
      "0096d160",
      "DATA",
      [
        "storage",
        "00c09d58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096d160",
      "DATA",
      [
        "storage",
        "00c09da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096d15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d13c.md#insn-0096d15c)
- 新版 `0096d15c`（命令位置の公開資料なし）

~~~diff
- 0096d15c ["COPY", "tmp:0:8", ["const:d58:8"]]
- 0096d15c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096d15c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096d15c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096d15c ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 0096d15c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d15c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d15c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096d15c bytes 08613591
+ 0096d15c bytes 08a13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7926f370db0392efeb0295c27a0d009"></a>

### [`0096d530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d530.md) → [`0096d530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096d530.md) FUN_0096d530

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
      "definition_site": "0096d554",
      "incomplete_value": false,
      "site": "0096d554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d554",
      "incomplete_value": false,
      "site": "0096d554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "0096d554",
      "DATA",
      [
        "storage",
        "00c09de8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096d554",
      "DATA",
      [
        "storage",
        "00c09e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096d550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d530.md#insn-0096d550)
- 新版 `0096d550`（命令位置の公開資料なし）

~~~diff
- 0096d550 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 0096d550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096d550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096d550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096d550 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 0096d550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096d550 bytes 08a13791
+ 0096d550 bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ac72fcb919584ab8b23ed4cb9b811a6"></a>

### [`0096d668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d668.md) → [`0096d668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096d668.md) FUN_0096d668

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
      "definition_site": "0096d68c",
      "incomplete_value": false,
      "site": "0096d68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d68c",
      "incomplete_value": false,
      "site": "0096d68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "0096d68c",
      "DATA",
      [
        "storage",
        "00c09e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096d68c",
      "DATA",
      [
        "storage",
        "00c09eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096d688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d668.md#insn-0096d688)
- 新版 `0096d688`（命令位置の公開資料なし）

~~~diff
- 0096d688 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 0096d688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096d688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096d688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096d688 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 0096d688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096d688 bytes 08a13991
+ 0096d688 bytes 08e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc4866efe5f1c30721cfa34bb8102a53"></a>

### [`0096d6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d6b8.md) → [`0096d6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096d6b8.md) FUN_0096d6b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00666298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00666/00666298.md) [`006a8e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00666298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00666/00666298.md) [`006a8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8e60.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096d7c0",
      "incomplete_value": true,
      "site": "0096d7d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0096d7c0",
      "incomplete_value": true,
      "site": "0096d7d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096d7bc",
      "incomplete_value": false,
      "site": "0096d7d4",
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
      "definition_site": "0096d7bc",
      "incomplete_value": false,
      "site": "0096d7d4",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096d7c8",
      "incomplete_value": false,
      "site": "0096d7d4",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d7c8",
      "incomplete_value": false,
      "site": "0096d7d4",
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
            "const:d48:8"
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
      "0096d7bc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0096d7c0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0096d7c8",
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0096d7bc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0096d7c0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0096d7c8",
      "PARAM",
      [
        "storage",
        "00bf3d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096d7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d6b8.md#insn-0096d7bc) · [`0096d7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d6b8.md#insn-0096d7c0) · [`0096d7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d6b8.md#insn-0096d7c8)
- 新版 `0096d7bc`（命令位置の公開資料なし） · `0096d7c0`（命令位置の公開資料なし） · `0096d7c8`（命令位置の公開資料なし）

~~~diff
- 0096d7bc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0096d7bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0096d7bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0096d7bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0096d7bc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0096d7bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0096d7bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0096d7bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0096d7bc bytes 21203991
+ 0096d7bc bytes 21603a91
- 0096d7c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0096d7c0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0096d7c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0096d7c0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0096d7c0 bytes 003d45f9
+ 0096d7c0 bytes 005d45f9
- 0096d7c8 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 0096d7c8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0096d7c8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0096d7c8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0096d7c8 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 0096d7c8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0096d7c8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0096d7c8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0096d7c8 bytes 42203591
+ 0096d7c8 bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8a110a489fb5764e6b0763865a13dd9"></a>

### [`0096d8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d8d4.md) → [`0096d8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096d8d4.md) FUN_0096d8d4

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
      "definition_site": "0096d8f4",
      "incomplete_value": false,
      "site": "0096d8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d8f4",
      "incomplete_value": false,
      "site": "0096d8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "0096d8f8",
      "DATA",
      [
        "storage",
        "00c09ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096d8f8",
      "DATA",
      [
        "storage",
        "00c09f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096d8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d8d4.md#insn-0096d8f4)
- 新版 `0096d8f4`（命令位置の公開資料なし）

~~~diff
- 0096d8f4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 0096d8f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096d8f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096d8f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096d8f4 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0096d8f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d8f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d8f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096d8f4 bytes 08a13b91
+ 0096d8f4 bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936bb76e3efd71c2b2ab338d98650fcc"></a>

### [`0096da04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096da04.md) → [`0096da04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096da04.md) FUN_0096da04

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
      "definition_site": "0096da28",
      "incomplete_value": false,
      "site": "0096da28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096da28",
      "incomplete_value": false,
      "site": "0096da28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "0096da28",
      "DATA",
      [
        "storage",
        "00c09f68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096da28",
      "DATA",
      [
        "storage",
        "00c09fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096da24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096da04.md#insn-0096da24)
- 新版 `0096da24`（命令位置の公開資料なし）

~~~diff
- 0096da24 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 0096da24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096da24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096da24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096da24 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0096da24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096da24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096da24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096da24 bytes 08a13d91
+ 0096da24 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9464599934709355775ea61779e5699e"></a>

### [`0096dc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dc00.md) → [`0096dc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096dc00.md) FUN_0096dc00

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
      "definition_site": "0096dc24",
      "incomplete_value": false,
      "site": "0096dc24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096dc24",
      "incomplete_value": false,
      "site": "0096dc24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "0096dc24",
      "DATA",
      [
        "storage",
        "00c09fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096dc24",
      "DATA",
      [
        "storage",
        "00c0a038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096dc1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dc00.md#insn-0096dc1c) · [`0096dc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dc00.md#insn-0096dc20)
- 新版 `0096dc1c`（命令位置の公開資料なし） · `0096dc20`（命令位置の公開資料なし）

~~~diff
- 0096dc1c ["COPY", "register:4040:8", ["const:c09000:8"]]
+ 0096dc1c ["COPY", "register:4040:8", ["const:c0a000:8"]]
- 0096dc1c bytes e8140090
+ 0096dc1c bytes e81400b0
- 0096dc20 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0096dc20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096dc20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096dc20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096dc20 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0096dc20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dc20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dc20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096dc20 bytes 08a13f91
+ 0096dc20 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db7712e112ac3abf666db6ce84b6a692"></a>

### [`0096dc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dc34.md) → [`0096dc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096dc34.md) FUN_0096dc34

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
      "definition_site": "0096dc40",
      "incomplete_value": false,
      "site": "0096dc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096dc40",
      "incomplete_value": false,
      "site": "0096dc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "0096dc40",
      "DATA",
      [
        "storage",
        "00c09fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096dc40",
      "DATA",
      [
        "storage",
        "00c0a038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096dc38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dc34.md#insn-0096dc38) · [`0096dc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dc34.md#insn-0096dc3c)
- 新版 `0096dc38`（命令位置の公開資料なし） · `0096dc3c`（命令位置の公開資料なし）

~~~diff
- 0096dc38 ["COPY", "register:4048:8", ["const:c09000:8"]]
+ 0096dc38 ["COPY", "register:4048:8", ["const:c0a000:8"]]
- 0096dc38 bytes e9140090
+ 0096dc38 bytes e91400b0
- 0096dc3c ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0096dc3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0096dc3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0096dc3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0096dc3c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0096dc3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0096dc3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0096dc3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0096dc3c bytes 29a13f91
+ 0096dc3c bytes 29e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbcd9259ce48d44f50d2d78949829b07"></a>

### [`0096dcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dcd8.md) → [`0096dcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096dcd8.md) FUN_0096dcd8

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
      "definition_site": "0096dcfc",
      "incomplete_value": false,
      "site": "0096dcfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096dcfc",
      "incomplete_value": false,
      "site": "0096dcfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
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
      "0096dcfc",
      "DATA",
      [
        "storage",
        "00c0a068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096dcfc",
      "DATA",
      [
        "storage",
        "00c0a0b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096dcf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dcd8.md#insn-0096dcf8)
- 新版 `0096dcf8`（命令位置の公開資料なし）

~~~diff
- 0096dcf8 ["COPY", "tmp:0:8", ["const:68:8"]]
- 0096dcf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096dcf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096dcf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096dcf8 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 0096dcf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dcf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dcf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096dcf8 bytes 08a10191
+ 0096dcf8 bytes 08e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d9d0c1c3c7e33144221642fb27b1071"></a>

### [`0096dd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dd0c.md) → [`0096dd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096dd0c.md) FUN_0096dd0c

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
      "definition_site": "0096dd18",
      "incomplete_value": true,
      "site": "0096dd18",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096dd18",
      "incomplete_value": true,
      "site": "0096dd18",
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
      "0096dd18",
      "DATA",
      [
        "storage",
        "00c0a068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096dd18",
      "DATA",
      [
        "storage",
        "00c0a0b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096dd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dd0c.md#insn-0096dd14)
- 新版 `0096dd14`（命令位置の公開資料なし）

~~~diff
- 0096dd14 ["COPY", "tmp:0:8", ["const:68:8"]]
- 0096dd14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0096dd14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0096dd14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0096dd14 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 0096dd14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0096dd14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0096dd14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0096dd14 bytes 29a10191
+ 0096dd14 bytes 29e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89db433fdb9d94814e89677384ed6f1e"></a>

### [`0096ddb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096ddb4.md) → [`0096ddb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096ddb4.md) FUN_0096ddb4

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
      "definition_site": "0096ddd8",
      "incomplete_value": false,
      "site": "0096ddd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096ddd8",
      "incomplete_value": false,
      "site": "0096ddd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
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
      "0096ddd8",
      "DATA",
      [
        "storage",
        "00c0a0e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096ddd8",
      "DATA",
      [
        "storage",
        "00c0a138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096ddd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096ddb4.md#insn-0096ddd4)
- 新版 `0096ddd4`（命令位置の公開資料なし）

~~~diff
- 0096ddd4 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0096ddd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096ddd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096ddd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096ddd4 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0096ddd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096ddd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096ddd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096ddd4 bytes 08a10391
+ 0096ddd4 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0124589014a36c9259e0e022e3a902fa"></a>

### [`0096dde8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dde8.md) → [`0096dde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096dde8.md) FUN_0096dde8

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
      "definition_site": "0096ddf4",
      "incomplete_value": false,
      "site": "0096ddf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096ddf4",
      "incomplete_value": false,
      "site": "0096ddf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
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
      "0096ddf4",
      "DATA",
      [
        "storage",
        "00c0a0e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096ddf4",
      "DATA",
      [
        "storage",
        "00c0a138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096ddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dde8.md#insn-0096ddf0)
- 新版 `0096ddf0`（命令位置の公開資料なし）

~~~diff
- 0096ddf0 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0096ddf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0096ddf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0096ddf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0096ddf0 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0096ddf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0096ddf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0096ddf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0096ddf0 bytes 29a10391
+ 0096ddf0 bytes 29e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5c21a7eaf816f45533ed91652f120d2"></a>

### [`0096de48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096de48.md) → [`0096de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096de48.md) FUN_0096de48

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
      "definition_site": "0096de5c",
      "incomplete_value": false,
      "site": "0096de60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096de5c",
      "incomplete_value": false,
      "site": "0096de60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:168:8"
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
      "0096de60",
      "DATA",
      [
        "storage",
        "00c0a168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096de60",
      "DATA",
      [
        "storage",
        "00c0a1b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096de5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096de48.md#insn-0096de5c)
- 新版 `0096de5c`（命令位置の公開資料なし）

~~~diff
- 0096de5c ["COPY", "tmp:0:8", ["const:168:8"]]
- 0096de5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096de5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096de5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096de5c ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 0096de5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096de5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096de5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096de5c bytes 08a10591
+ 0096de5c bytes 08e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a006cb88950c96951c148e5e2cabf48b"></a>

### [`0096de6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096de6c.md) → [`0096de6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096de6c.md) FUN_0096de6c

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
      "definition_site": "0096de70",
      "incomplete_value": false,
      "site": "0096de74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096de70",
      "incomplete_value": false,
      "site": "0096de74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:168:8"
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
      "0096de74",
      "DATA",
      [
        "storage",
        "00c0a168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096de74",
      "DATA",
      [
        "storage",
        "00c0a1b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096de70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096de6c.md#insn-0096de70)
- 新版 `0096de70`（命令位置の公開資料なし）

~~~diff
- 0096de70 ["COPY", "tmp:0:8", ["const:168:8"]]
- 0096de70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096de70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096de70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096de70 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 0096de70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096de70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096de70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096de70 bytes 08a10591
+ 0096de70 bytes 08e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4118a098f388f0d500ab76af444c9625"></a>

### [`0096df1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096df1c.md) → [`0096df1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096df1c.md) FUN_0096df1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0096df20",
      "incomplete_value": true,
      "site": "0096df24",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096df20",
      "incomplete_value": true,
      "site": "0096df24",
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
            "const:1e8:8"
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
      "0096df24",
      "DATA",
      [
        "storage",
        "00c0a1e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096df24",
      "DATA",
      [
        "storage",
        "00c0a238",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096df20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096df1c.md#insn-0096df20)
- 新版 `0096df20`（命令位置の公開資料なし）

~~~diff
- 0096df20 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0096df20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096df20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096df20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096df20 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 0096df20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096df20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096df20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096df20 bytes 08a10791
+ 0096df20 bytes 08e10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a09910c7aead7d8bdf809358c22232a"></a>

### [`0096dfa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfa8.md) → [`0096dfa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096dfa8.md) FUN_0096dfa8

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
      "definition_site": "0096dfbc",
      "incomplete_value": false,
      "site": "0096dfc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096dfbc",
      "incomplete_value": false,
      "site": "0096dfc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "0096dfc0",
      "DATA",
      [
        "storage",
        "00c0a268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096dfc0",
      "DATA",
      [
        "storage",
        "00c0a2b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096dfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfa8.md#insn-0096dfbc)
- 新版 `0096dfbc`（命令位置の公開資料なし）

~~~diff
- 0096dfbc ["COPY", "tmp:0:8", ["const:268:8"]]
- 0096dfbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096dfbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096dfbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096dfbc ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 0096dfbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dfbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dfbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096dfbc bytes 08a10991
+ 0096dfbc bytes 08e10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a00e38dbfdd562c9004ae32a011238f2"></a>

### [`0096dfcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfcc.md) → [`0096dfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096dfcc.md) FUN_0096dfcc

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
      "definition_site": "0096dfd0",
      "incomplete_value": false,
      "site": "0096dfd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096dfd0",
      "incomplete_value": false,
      "site": "0096dfd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "0096dfd4",
      "DATA",
      [
        "storage",
        "00c0a268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096dfd4",
      "DATA",
      [
        "storage",
        "00c0a2b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096dfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfcc.md#insn-0096dfd0)
- 新版 `0096dfd0`（命令位置の公開資料なし）

~~~diff
- 0096dfd0 ["COPY", "tmp:0:8", ["const:268:8"]]
- 0096dfd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096dfd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096dfd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096dfd0 ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 0096dfd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dfd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dfd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096dfd0 bytes 08a10991
+ 0096dfd0 bytes 08e10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0664ad7546b72ecf86e92d8ec22b3bf9"></a>

### [`0096e054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096e054.md) → [`0096e054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096e/0096e054.md) _INIT_186

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
      "definition_site": "0096e0b4",
      "incomplete_value": true,
      "site": "0096e0d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096e0b4",
      "incomplete_value": true,
      "site": "0096e0d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096e150",
      "incomplete_value": true,
      "site": "0096e194",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:526:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096e150",
      "incomplete_value": true,
      "site": "0096e194",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5b3:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096e27c",
      "incomplete_value": false,
      "site": "0096e288",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096e27c",
      "incomplete_value": false,
      "site": "0096e288",
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
            "const:8d0:8"
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
      "0096e090",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0096e0b4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0096e0d4",
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
      "0096e090",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0096e0b4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0096e0d4",
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

- 旧版 [`0096e080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096e054.md#insn-0096e080) · [`0096e088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096e054.md#insn-0096e088)
- 新版 `0096e080`（命令位置の公開資料なし） · `0096e088`（命令位置の公開資料なし）

~~~diff
- 0096e080 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 0096e080 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0096e080 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0096e080 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0096e080 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 0096e080 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0096e080 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0096e080 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0096e080 bytes 73422391
+ 0096e080 bytes 73422491
- 0096e088 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0096e088 bytes c9c9ffb0
+ 0096e088 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0096e088 bytes c9c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5def7304f90a4f991749781e3aaaf64d"></a>

### [`0096eab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096eab4.md) → [`0096eab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096e/0096eab4.md) _INIT_187

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
      "definition_site": "0096eaf0",
      "incomplete_value": true,
      "site": "0096eb0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eaf0",
      "incomplete_value": true,
      "site": "0096eb0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eb14",
      "incomplete_value": true,
      "site": "0096eb30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eb14",
      "incomplete_value": true,
      "site": "0096eb30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eb34",
      "incomplete_value": true,
      "site": "0096eb50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eb34",
      "incomplete_value": true,
      "site": "0096eb50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0096eaf0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0096eb14",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0096eb34",
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
      "0096eaf0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0096eb14",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0096eb34",
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

- 旧版 [`0096eae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096eab4.md#insn-0096eae0) · [`0096eae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096eab4.md#insn-0096eae8)
- 新版 `0096eae0`（命令位置の公開資料なし） · `0096eae8`（命令位置の公開資料なし）

~~~diff
- 0096eae0 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0096eae0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0096eae0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0096eae0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0096eae0 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 0096eae0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0096eae0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0096eae0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0096eae0 bytes 73a22391
+ 0096eae0 bytes 73a22491
- 0096eae8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0096eae8 bytes c9c9ffb0
+ 0096eae8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0096eae8 bytes c9c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55f4fb9b0bc4a589d345465c9a64b555"></a>

### [`0096ee44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096ee44.md) → [`0096ee44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096e/0096ee44.md) _INIT_188

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
      "definition_site": "0096ee80",
      "incomplete_value": true,
      "site": "0096ee9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096ee80",
      "incomplete_value": true,
      "site": "0096ee9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eea4",
      "incomplete_value": true,
      "site": "0096eec0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eea4",
      "incomplete_value": true,
      "site": "0096eec0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eec4",
      "incomplete_value": true,
      "site": "0096eee0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eec4",
      "incomplete_value": true,
      "site": "0096eee0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0096ee80",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0096eea4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0096eec4",
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
      "0096ee80",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0096eea4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0096eec4",
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

- 旧版 [`0096ee70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096ee44.md#insn-0096ee70) · [`0096ee78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096ee44.md#insn-0096ee78)
- 新版 `0096ee70`（命令位置の公開資料なし） · `0096ee78`（命令位置の公開資料なし）

~~~diff
- 0096ee70 ["COPY", "tmp:0:8", ["const:900:8"]]
- 0096ee70 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0096ee70 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0096ee70 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0096ee70 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 0096ee70 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0096ee70 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0096ee70 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0096ee70 bytes 73022491
+ 0096ee70 bytes 73022591
- 0096ee78 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0096ee78 bytes c9c9ffb0
+ 0096ee78 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0096ee78 bytes c9c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-646f8b21fbd682294e11000382d57c17"></a>

### [`0096f1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f1dc.md) → [`0096f1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f1dc.md) FUN_0096f1dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) · 呼出先 1件 [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md)
- 新版 呼出元 1件 [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) · 呼出先 1件 [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096f1ec",
      "incomplete_value": false,
      "site": "0096f1f4",
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
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096f1ec",
      "incomplete_value": false,
      "site": "0096f1f4",
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
            "const:930:8"
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
      "0096f1ec",
      "PARAM",
      [
        "storage",
        "0109e930",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0096f1ec",
      "PARAM",
      [
        "storage",
        "0109e970",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096f1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f1dc.md#insn-0096f1ec)
- 新版 `0096f1ec`（命令位置の公開資料なし）

~~~diff
- 0096f1ec ["COPY", "tmp:0:8", ["const:930:8"]]
- 0096f1ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0096f1ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0096f1ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0096f1ec ["COPY", "tmp:0:8", ["const:970:8"]]
+ 0096f1ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0096f1ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0096f1ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0096f1ec bytes 21c02491
+ 0096f1ec bytes 21c02591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fc4d31f73a126d9afcc5866f97b33d8"></a>

### [`0096f208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f208.md) → [`0096f208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f208.md) FUN_0096f208

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) · 呼出先 1件 [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md)
- 新版 呼出元 1件 [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) · 呼出先 1件 [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096f218",
      "incomplete_value": false,
      "site": "0096f220",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096f218",
      "incomplete_value": false,
      "site": "0096f220",
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
            "const:950:8"
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
      "0096f218",
      "PARAM",
      [
        "storage",
        "0109e950",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0096f218",
      "PARAM",
      [
        "storage",
        "0109e990",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096f218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f208.md#insn-0096f218)
- 新版 `0096f218`（命令位置の公開資料なし）

~~~diff
- 0096f218 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0096f218 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0096f218 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0096f218 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0096f218 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 0096f218 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0096f218 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0096f218 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0096f218 bytes 21402591
+ 0096f218 bytes 21402691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8874e5b995e831f496e1b999a5cf0e29"></a>

### [`0096f234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f234.md) → [`0096f234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f234.md) FUN_0096f234

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) · 呼出先 12件 [`0046b2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b2bc.md) [`00470da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470da0.md) [`00470da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470da8.md) [`00470e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470e10.md) [`0096f440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f440.md)
- 新版 呼出元 1件 [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) · 呼出先 12件 [`0046b2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b2bc.md) [`00470da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470da0.md) [`00470da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470da8.md) [`00470e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470e10.md) [`0096f440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096f2d8",
      "incomplete_value": false,
      "site": "0096f2dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096f2d8",
      "incomplete_value": false,
      "site": "0096f2dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "0096f2c0",
      "DATA",
      [
        "storage",
        "00c0a2e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f2dc",
      "DATA",
      [
        "storage",
        "00c0a378",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f314",
      "READ",
      [
        "storage",
        "00c0a398",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0096f2c0",
      "DATA",
      [
        "storage",
        "00c0a338",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f2dc",
      "DATA",
      [
        "storage",
        "00c0a3c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f314",
      "READ",
      [
        "storage",
        "00c0a3e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096f2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f234.md#insn-0096f2b8) · [`0096f2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f234.md#insn-0096f2d8)
- 新版 `0096f2b8`（命令位置の公開資料なし） · `0096f2d8`（命令位置の公開資料なし）

~~~diff
- 0096f2b8 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 0096f2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f2b8 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 0096f2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f2b8 bytes 08a10b91
+ 0096f2b8 bytes 08e10c91
- 0096f2d8 ["COPY", "tmp:0:8", ["const:378:8"]]
- 0096f2d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f2d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f2d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f2d8 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0096f2d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f2d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f2d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f2d8 bytes 08e10d91
+ 0096f2d8 bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04095a586cb921eccf235ab69a389cbd"></a>

### [`0096f440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f440.md) → [`0096f440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f440.md) FUN_0096f440

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0096f234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f234.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00582d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582d1c.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b948.md)
- 新版 呼出元 1件 [`0096f234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f234.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576268.md) [`00582d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582d1c.md) [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b948.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.01% / 新版 98.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096f4b0",
      "incomplete_value": false,
      "site": "0096f4b4",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a50:8"
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
      "definition_site": "0096f4b0",
      "incomplete_value": false,
      "site": "0096f4b4",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "0096f4b4",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f584",
      "DATA",
      [
        "storage",
        "00c0a508",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f638",
      "READ",
      [
        "storage",
        "00c0a530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096f4b4",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f584",
      "DATA",
      [
        "storage",
        "00c0a558",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f638",
      "READ",
      [
        "storage",
        "00c0a580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096f4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f440.md#insn-0096f4a8) · [`0096f57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f440.md#insn-0096f57c)
- 新版 `0096f4a8`（命令位置の公開資料なし） · `0096f57c`（命令位置の公開資料なし）

~~~diff
- 0096f4a8 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0096f4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f4a8 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0096f4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f4a8 bytes 08012891
+ 0096f4a8 bytes 08412991
- 0096f57c ["COPY", "tmp:0:8", ["const:508:8"]]
- 0096f57c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f57c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f57c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f57c ["COPY", "tmp:0:8", ["const:558:8"]]
+ 0096f57c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f57c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f57c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f57c bytes 08211491
+ 0096f57c bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c8617c9a04fbfeb9a38ea9192dd8ca7"></a>

### [`0096f888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f888.md) → [`0096f888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f888.md) FUN_0096f888

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) · 呼出先 12件 [`0046b2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b2bc.md) [`00470da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470da0.md) [`00470da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470da8.md) [`00470e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470e10.md) [`0096fb34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096fb34.md)
- 新版 呼出元 1件 [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) · 呼出先 12件 [`0046b2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b2bc.md) [`00470da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470da0.md) [`00470da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470da8.md) [`00470e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470e10.md) [`0096fb34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096fb34.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096f97c",
      "incomplete_value": false,
      "site": "0096f97c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096f97c",
      "incomplete_value": false,
      "site": "0096f97c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "definition_site": "0096f998",
      "incomplete_value": false,
      "site": "0096f99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096f998",
      "incomplete_value": false,
      "site": "0096f99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "0096f97c",
      "DATA",
      [
        "storage",
        "00c0a3f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f99c",
      "DATA",
      [
        "storage",
        "00c0a488",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f9d4",
      "READ",
      [
        "storage",
        "00c0a4a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0096f97c",
      "DATA",
      [
        "storage",
        "00c0a448",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f99c",
      "DATA",
      [
        "storage",
        "00c0a4d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f9d4",
      "READ",
      [
        "storage",
        "00c0a4f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096f974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f888.md#insn-0096f974) · [`0096f998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f888.md#insn-0096f998)
- 新版 `0096f974`（命令位置の公開資料なし） · `0096f998`（命令位置の公開資料なし）

~~~diff
- 0096f974 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 0096f974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f974 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 0096f974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f974 bytes 08e10f91
+ 0096f974 bytes 08211191
- 0096f998 ["COPY", "tmp:0:8", ["const:488:8"]]
- 0096f998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f998 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 0096f998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f998 bytes 08211291
+ 0096f998 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bde5c2d82e07cf7f2aceaa68fb59bf8"></a>

### [`0096fb34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096fb34.md) → [`0096fb34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096fb34.md) FUN_0096fb34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0096f888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f888.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00583d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583d20.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b948.md)
- 新版 呼出元 1件 [`0096f888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f888.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576268.md) [`00583d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583d20.md) [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b948.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.54% / 新版 97.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096fbac",
      "incomplete_value": false,
      "site": "0096fbb0",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a50:8"
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
      "definition_site": "0096fbac",
      "incomplete_value": false,
      "site": "0096fbb0",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096fc80",
      "incomplete_value": false,
      "site": "0096fc80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096fc80",
      "incomplete_value": false,
      "site": "0096fc80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "0096fbb0",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0096fc80",
      "DATA",
      [
        "storage",
        "00c0a588",
        null,
        "undefined *"
      ]
    ],
    [
      "0096fd34",
      "READ",
      [
        "storage",
        "00c0a5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096fbb0",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ],
    [
      "0096fc80",
      "DATA",
      [
        "storage",
        "00c0a5d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0096fd34",
      "READ",
      [
        "storage",
        "00c0a600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096fba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096fb34.md#insn-0096fba4) · [`0096fc78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096fb34.md#insn-0096fc78)
- 新版 `0096fba4`（命令位置の公開資料なし） · `0096fc78`（命令位置の公開資料なし）

~~~diff
- 0096fba4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0096fba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096fba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096fba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096fba4 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0096fba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096fba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096fba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096fba4 bytes 08012891
+ 0096fba4 bytes 08412991
- 0096fc78 ["COPY", "tmp:0:8", ["const:588:8"]]
- 0096fc78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096fc78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096fc78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096fc78 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 0096fc78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096fc78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096fc78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096fc78 bytes 08211691
+ 0096fc78 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c34321d9dd777a94b68d109b83202327"></a>

### [`0096ff84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096ff84.md) → [`0096ff84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096ff84.md) FUN_0096ff84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00970720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970720.md) [`0097107c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/0097107c.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004512c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00451/004512c0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fdf4.md) [`0071edcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071edcc.md)
- 新版 呼出元 2件 [`00970720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/00970720.md) [`0097107c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/0097107c.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004512c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fdf4.md) [`0071edcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071edcc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.13% / 新版 95.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097023c",
      "incomplete_value": true,
      "site": "0097023c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a12:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097023c",
      "incomplete_value": true,
      "site": "0097023c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:987:8"
              ]
            ]
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
      "definition_site": "00970240",
      "incomplete_value": true,
      "site": "00970240",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00970240",
      "incomplete_value": true,
      "site": "00970240",
      "value": [
        "LOAD",
        "8",
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
      "0096ffd4",
      "READ",
      [
        "storage",
        "002a9cdb",
        null,
        "string"
      ]
    ],
    [
      "009700b4",
      "READ",
      [
        "storage",
        "002af124",
        null,
        "string"
      ]
    ],
    [
      "009700cc",
      "READ",
      [
        "storage",
        "002af130",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0096ffd4",
      "READ",
      [
        "storage",
        "002a9cea",
        null,
        "string"
      ]
    ],
    [
      "009700b4",
      "READ",
      [
        "storage",
        "002af090",
        null,
        "string"
      ]
    ],
    [
      "009700cc",
      "READ",
      [
        "storage",
        "002af09c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096ffd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096ff84.md#insn-0096ffd0) · [`0097003c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096ff84.md#insn-0097003c) · [`00970044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096ff84.md#insn-00970044)
- 新版 `0096ffd0`（命令位置の公開資料なし） · `0097003c`（命令位置の公開資料なし）

~~~diff
- 0096ffd0 ["COPY", "tmp:0:8", ["const:cdb:8"]]
- 0096ffd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0096ffd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0096ffd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0096ffd0 ["COPY", "tmp:0:8", ["const:cea:8"]]
+ 0096ffd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0096ffd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0096ffd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0096ffd0 bytes 296d3391
+ 0096ffd0 bytes 29a93391
- 0097003c ["COPY", "tmp:0:8", ["const:124:8"]]
- 0097003c ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 0097003c ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 0097003c ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 0097003c ["COPY", "tmp:0:8", ["const:90:8"]]
+ 0097003c ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 0097003c ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 0097003c ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 0097003c bytes 9c930491
+ 0097003c bytes 9c430291
- 00970044 ["COPY", "register:40b0:8", ["const:299000:8"]]
- 00970044 bytes 56c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d307ffbe368fdcb1c3023ca9dd425668"></a>

### [`009706c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/009706c8.md) → [`009706c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/009706c8.md) FUN_009706c8

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
      "definition_site": "009706e8",
      "incomplete_value": false,
      "site": "009706ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009706e8",
      "incomplete_value": false,
      "site": "009706ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
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
      "009706ec",
      "DATA",
      [
        "storage",
        "00c0a2e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009706ec",
      "DATA",
      [
        "storage",
        "00c0a338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009706e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/009706c8.md#insn-009706e8)
- 新版 `009706e8`（命令位置の公開資料なし）

~~~diff
- 009706e8 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 009706e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009706e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009706e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009706e8 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 009706e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009706e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009706e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009706e8 bytes 08a10b91
+ 009706e8 bytes 08e10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbac909f7919785cc0cf5a383d9dd4ed"></a>

### [`00970700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970700.md) → [`00970700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/00970700.md) FUN_00970700

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
      "definition_site": "00970708",
      "incomplete_value": false,
      "site": "0097070c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00970708",
      "incomplete_value": false,
      "site": "0097070c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
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
      "0097070c",
      "DATA",
      [
        "storage",
        "00c0a2e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097070c",
      "DATA",
      [
        "storage",
        "00c0a338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00970708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970700.md#insn-00970708)
- 新版 `00970708`（命令位置の公開資料なし）

~~~diff
- 00970708 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 00970708 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00970708 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00970708 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00970708 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 00970708 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00970708 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00970708 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00970708 bytes 29a10b91
+ 00970708 bytes 29e10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4cb0cabd78ca0b626c447d73a55b06e"></a>

### [`00970d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970d64.md) → [`00970d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/00970d64.md) FUN_00970d64

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00970c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970c1c.md) [`00970dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970dcc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00970c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/00970c1c.md) [`00970dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/00970dcc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00970d70",
      "incomplete_value": false,
      "site": "00970d74",
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
      "definition_site": "00970d70",
      "incomplete_value": false,
      "site": "00970d74",
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
      "00970d70",
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
      "00970d70",
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

- 旧版 [`00970d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970d64.md#insn-00970d70)
- 新版 `00970d70`（命令位置の公開資料なし）

~~~diff
- 00970d70 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00970d70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00970d70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00970d70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00970d70 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00970d70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00970d70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00970d70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00970d70 bytes 000c0c91
+ 00970d70 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ef97ebcf6b963b92806a519aec71ab9"></a>

### [`00970fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970fb4.md) → [`00970fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/00970fb4.md) FUN_00970fb4

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
      "definition_site": "00970fc8",
      "incomplete_value": false,
      "site": "00970fcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00970fc8",
      "incomplete_value": false,
      "site": "00970fcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00970fcc",
      "DATA",
      [
        "storage",
        "00c0a378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00970fcc",
      "DATA",
      [
        "storage",
        "00c0a3c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00970fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970fb4.md#insn-00970fc8)
- 新版 `00970fc8`（命令位置の公開資料なし）

~~~diff
- 00970fc8 ["COPY", "tmp:0:8", ["const:378:8"]]
- 00970fc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00970fc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00970fc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00970fc8 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 00970fc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00970fc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00970fc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00970fc8 bytes 08e10d91
+ 00970fc8 bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba21a2f2bdcf1a8088ef1d6f7b98ebda"></a>

### [`00970fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970fd8.md) → [`00970fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/00970fd8.md) FUN_00970fd8

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
      "definition_site": "00970fdc",
      "incomplete_value": false,
      "site": "00970fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00970fdc",
      "incomplete_value": false,
      "site": "00970fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00970fe0",
      "DATA",
      [
        "storage",
        "00c0a378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00970fe0",
      "DATA",
      [
        "storage",
        "00c0a3c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00970fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970fd8.md#insn-00970fdc)
- 新版 `00970fdc`（命令位置の公開資料なし）

~~~diff
- 00970fdc ["COPY", "tmp:0:8", ["const:378:8"]]
- 00970fdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00970fdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00970fdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00970fdc ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 00970fdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00970fdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00970fdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00970fdc bytes 08e10d91
+ 00970fdc bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1673eba43c0079997f64b14e82457d4"></a>

### [`00971024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971024.md) → [`00971024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/00971024.md) FUN_00971024

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
      "definition_site": "00971044",
      "incomplete_value": false,
      "site": "00971048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971044",
      "incomplete_value": false,
      "site": "00971048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "00971048",
      "DATA",
      [
        "storage",
        "00c0a3f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00971048",
      "DATA",
      [
        "storage",
        "00c0a448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00971044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971024.md#insn-00971044)
- 新版 `00971044`（命令位置の公開資料なし）

~~~diff
- 00971044 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 00971044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00971044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00971044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00971044 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 00971044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00971044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00971044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00971044 bytes 08e10f91
+ 00971044 bytes 08211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-071716372c0e2762d75c548bf037f826"></a>

### [`0097105c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/0097105c.md) → [`0097105c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/0097105c.md) FUN_0097105c

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
      "definition_site": "00971064",
      "incomplete_value": false,
      "site": "00971068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971064",
      "incomplete_value": false,
      "site": "00971068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "00971068",
      "DATA",
      [
        "storage",
        "00c0a3f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00971068",
      "DATA",
      [
        "storage",
        "00c0a448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00971064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/0097105c.md#insn-00971064)
- 新版 `00971064`（命令位置の公開資料なし）

~~~diff
- 00971064 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 00971064 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00971064 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00971064 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00971064 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 00971064 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00971064 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00971064 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00971064 bytes 29e10f91
+ 00971064 bytes 29211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4e716c49472ecdab99b3aa8142c550d"></a>

### [`00971200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971200.md) → [`00971200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/00971200.md) FUN_00971200

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
      "definition_site": "00971214",
      "incomplete_value": false,
      "site": "00971218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971214",
      "incomplete_value": false,
      "site": "00971218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "00971218",
      "DATA",
      [
        "storage",
        "00c0a488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00971218",
      "DATA",
      [
        "storage",
        "00c0a4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00971214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971200.md#insn-00971214)
- 新版 `00971214`（命令位置の公開資料なし）

~~~diff
- 00971214 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00971214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00971214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00971214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00971214 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00971214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00971214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00971214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00971214 bytes 08211291
+ 00971214 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db5bc2015ee8a8d31ebd9502b0f0690c"></a>

### [`00971224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971224.md) → [`00971224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/00971224.md) FUN_00971224

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
      "definition_site": "00971228",
      "incomplete_value": false,
      "site": "0097122c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971228",
      "incomplete_value": false,
      "site": "0097122c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "0097122c",
      "DATA",
      [
        "storage",
        "00c0a488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097122c",
      "DATA",
      [
        "storage",
        "00c0a4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00971228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971224.md#insn-00971228)
- 新版 `00971228`（命令位置の公開資料なし）

~~~diff
- 00971228 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00971228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00971228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00971228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00971228 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00971228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00971228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00971228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00971228 bytes 08211291
+ 00971228 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d24dd9acdb5de42d25ad652f017008b8"></a>

### [`00971268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971268.md) → [`00971268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/00971268.md) FUN_00971268

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0096ff84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096ff84.md) [`00971268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971268.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0096ff84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096ff84.md) [`00971268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/00971268.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009713bc",
      "incomplete_value": false,
      "site": "009713c4",
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
      "definition_site": "009713bc",
      "incomplete_value": false,
      "site": "009713c4",
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
      "definition_site": "009713e0",
      "incomplete_value": false,
      "site": "009713ec",
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
      "definition_site": "009713e0",
      "incomplete_value": false,
      "site": "009713ec",
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
      "definition_site": "00971514",
      "incomplete_value": false,
      "site": "0097151c",
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
      "definition_site": "00971514",
      "incomplete_value": false,
      "site": "0097151c",
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
      "009713bc",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "009713e0",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00971514",
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
      "009713bc",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "009713e0",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00971514",
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

- 旧版 [`009713bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971268.md#insn-009713bc) · [`009713e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971268.md#insn-009713e0) · [`00971514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971268.md#insn-00971514)
- 新版 `009713bc`（命令位置の公開資料なし） · `009713e0`（命令位置の公開資料なし） · `00971514`（命令位置の公開資料なし）

~~~diff
- 009713bc ["COPY", "tmp:0:8", ["const:30a:8"]]
- 009713bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009713bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009713bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009713bc ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 009713bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009713bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009713bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009713bc bytes 21280c91
+ 009713bc bytes 21900e91
- 009713e0 ["COPY", "tmp:0:8", ["const:919:8"]]
- 009713e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009713e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009713e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009713e0 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 009713e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009713e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009713e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009713e0 bytes 21642491
+ 009713e0 bytes 21142291
- 00971514 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00971514 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00971514 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00971514 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00971514 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00971514 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00971514 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00971514 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00971514 bytes 21b80b91
+ 00971514 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2ffdd5b8c95723d48f3209ab537bed1"></a>

### [`00971a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971a68.md) → [`00971a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/00971a68.md) FUN_00971a68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0096ff84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096ff84.md) [`00971a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971a68.md) [`0097a888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a888.md) [`00aaea38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaea38.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`0096ff84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096ff84.md) [`00971a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/00971a68.md) [`0097a888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a888.md) [`00aaea7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaea7c.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00971bbc",
      "incomplete_value": true,
      "site": "00971bc4",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971bbc",
      "incomplete_value": true,
      "site": "00971bc4",
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
      "definition_site": "00971c78",
      "incomplete_value": true,
      "site": "00971c80",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971c78",
      "incomplete_value": true,
      "site": "00971c80",
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
            "const:2ee:8"
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
      "definition_site": "00971c90",
      "incomplete_value": false,
      "site": "00971c9c",
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
      "definition_site": "00971c90",
      "incomplete_value": false,
      "site": "00971c9c",
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
      "00971bbc",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00971c78",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00971c90",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00971bbc",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00971c78",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00971c90",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00971bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971a68.md#insn-00971bbc) · [`00971c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971a68.md#insn-00971c78) · [`00971c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971a68.md#insn-00971c90)
- 新版 `00971bbc`（命令位置の公開資料なし） · `00971c78`（命令位置の公開資料なし） · `00971c90`（命令位置の公開資料なし）

~~~diff
- 00971bbc ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00971bbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00971bbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00971bbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00971bbc ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00971bbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00971bbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00971bbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00971bbc bytes 21280c91
+ 00971bbc bytes 21900e91
- 00971c78 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00971c78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00971c78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00971c78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00971c78 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00971c78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00971c78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00971c78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00971c78 bytes 21b80b91
+ 00971c78 bytes 21e40d91
- 00971c90 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00971c90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00971c90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00971c90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00971c90 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00971c90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00971c90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00971c90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00971c90 bytes 21642491
+ 00971c90 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23f112fadc484d6e3f3bb68563c997c3"></a>

### [`0097239c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/0097239c.md) → [`0097239c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/0097239c.md) FUN_0097239c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0096f440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f440.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0096f440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f440.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "009723d4",
      "incomplete_value": false,
      "site": "009723dc",
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
      "definition_site": "009723d4",
      "incomplete_value": false,
      "site": "009723dc",
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
      "009723dc",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00972494",
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
      "009723dc",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00972494",
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

- 旧版 [`009723d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/0097239c.md#insn-009723d4) · [`009723d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/0097239c.md#insn-009723d8)
- 新版 `009723d4`（命令位置の公開資料なし） · `009723d8`（命令位置の公開資料なし）

~~~diff
- 009723d4 ["COPY", "tmp:0:8", ["const:148:8"]]
- 009723d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009723d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009723d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009723d4 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 009723d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009723d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009723d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009723d4 bytes 08210591
+ 009723d4 bytes 08610691
- 009723d8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 009723d8 bytes f30300aa
+ 009723d8 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 009723d8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22811174500306c57613b232af1781d6"></a>

### [`00972514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972514.md) → [`00972514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972514.md) FUN_00972514

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097252c",
      "incomplete_value": true,
      "site": "0097253c",
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
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097252c",
      "incomplete_value": true,
      "site": "0097253c",
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
            "const:508:8"
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
      "0097253c",
      "DATA",
      [
        "storage",
        "00c0a508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097253c",
      "DATA",
      [
        "storage",
        "00c0a558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097252c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972514.md#insn-0097252c)
- 新版 `0097252c`（命令位置の公開資料なし）

~~~diff
- 0097252c ["COPY", "tmp:0:8", ["const:508:8"]]
- 0097252c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097252c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097252c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097252c ["COPY", "tmp:0:8", ["const:558:8"]]
+ 0097252c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097252c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097252c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097252c bytes 08211491
+ 0097252c bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2855713857d886a900b3508c8a391358"></a>

### [`009725a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/009725a4.md) → [`009725a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/009725a4.md) FUN_009725a4

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
      "definition_site": "009725bc",
      "incomplete_value": false,
      "site": "009725cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009725bc",
      "incomplete_value": false,
      "site": "009725cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "009725cc",
      "DATA",
      [
        "storage",
        "00c0a508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009725cc",
      "DATA",
      [
        "storage",
        "00c0a558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009725bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/009725a4.md#insn-009725bc)
- 新版 `009725bc`（命令位置の公開資料なし）

~~~diff
- 009725bc ["COPY", "tmp:0:8", ["const:508:8"]]
- 009725bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009725bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009725bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009725bc ["COPY", "tmp:0:8", ["const:558:8"]]
+ 009725bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009725bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009725bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009725bc bytes 08211491
+ 009725bc bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-991a6329a6cc29ecec7fa643cd9ef9a5"></a>

### [`00972630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972630.md) → [`00972630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972630.md) FUN_00972630

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
      "definition_site": "00972660",
      "incomplete_value": false,
      "site": "00972660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972660",
      "incomplete_value": false,
      "site": "00972660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "00972660",
      "DATA",
      [
        "storage",
        "00c0a508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972660",
      "DATA",
      [
        "storage",
        "00c0a558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972630.md#insn-00972658)
- 新版 `00972658`（命令位置の公開資料なし）

~~~diff
- 00972658 ["COPY", "tmp:0:8", ["const:508:8"]]
- 00972658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972658 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00972658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972658 bytes 08211491
+ 00972658 bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52cb0e633ec35f13eba8adf3c3249f3a"></a>

### [`00972738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972738.md) → [`00972738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972738.md) FUN_00972738

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
      "definition_site": "00972760",
      "incomplete_value": false,
      "site": "00972760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972760",
      "incomplete_value": false,
      "site": "00972760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "00972760",
      "DATA",
      [
        "storage",
        "00c0a508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972760",
      "DATA",
      [
        "storage",
        "00c0a558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972738.md#insn-00972758) · [`0097275c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972738.md#insn-0097275c)
- 新版 `00972758`（命令位置の公開資料なし） · `0097275c`（命令位置の公開資料なし）

~~~diff
- 00972758 ["COPY", "tmp:0:8", ["const:508:8"]]
- 00972758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972758 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00972758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972758 bytes 08211491
+ 00972758 bytes 08611591
- 0097275c ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0097275c bytes f40301aa
+ 0097275c ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 0097275c bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d99c530a577576ecfc2b765e0ea7038f"></a>

### [`00972af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972af8.md) → [`00972af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972af8.md) FUN_00972af8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0096fb34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096fb34.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0096fb34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096fb34.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00972b30",
      "incomplete_value": false,
      "site": "00972b38",
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
      "definition_site": "00972b30",
      "incomplete_value": false,
      "site": "00972b38",
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
      "00972b38",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00972bf0",
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
      "00972b38",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00972bf0",
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

- 旧版 [`00972b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972af8.md#insn-00972b30) · [`00972b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972af8.md#insn-00972b34)
- 新版 `00972b30`（命令位置の公開資料なし） · `00972b34`（命令位置の公開資料なし）

~~~diff
- 00972b30 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00972b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972b30 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00972b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972b30 bytes 08210591
+ 00972b30 bytes 08610691
- 00972b34 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00972b34 bytes f30300aa
+ 00972b34 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00972b34 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3032b7b45a5b1b9e4421dbd5aacaca8"></a>

### [`00972c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972c70.md) → [`00972c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972c70.md) FUN_00972c70

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
      "definition_site": "00972c88",
      "incomplete_value": false,
      "site": "00972c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972c88",
      "incomplete_value": false,
      "site": "00972c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "00972c98",
      "DATA",
      [
        "storage",
        "00c0a588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972c98",
      "DATA",
      [
        "storage",
        "00c0a5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972c70.md#insn-00972c88)
- 新版 `00972c88`（命令位置の公開資料なし）

~~~diff
- 00972c88 ["COPY", "tmp:0:8", ["const:588:8"]]
- 00972c88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972c88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972c88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972c88 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00972c88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972c88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972c88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972c88 bytes 08211691
+ 00972c88 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ff71d72622fb18c228290ffd49f54b0"></a>

### [`00972d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972d00.md) → [`00972d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972d00.md) FUN_00972d00

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
      "definition_site": "00972d18",
      "incomplete_value": false,
      "site": "00972d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972d18",
      "incomplete_value": false,
      "site": "00972d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "00972d28",
      "DATA",
      [
        "storage",
        "00c0a588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972d28",
      "DATA",
      [
        "storage",
        "00c0a5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972d00.md#insn-00972d18)
- 新版 `00972d18`（命令位置の公開資料なし）

~~~diff
- 00972d18 ["COPY", "tmp:0:8", ["const:588:8"]]
- 00972d18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972d18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972d18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972d18 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00972d18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972d18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972d18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972d18 bytes 08211691
+ 00972d18 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2b735eedb5c3559a21203845cffac24"></a>

### [`00972d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972d8c.md) → [`00972d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972d8c.md) FUN_00972d8c

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00972dbc",
      "incomplete_value": true,
      "site": "00972dbc",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972dbc",
      "incomplete_value": true,
      "site": "00972dbc",
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
            "const:588:8"
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
      "00972dbc",
      "DATA",
      [
        "storage",
        "00c0a588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972dbc",
      "DATA",
      [
        "storage",
        "00c0a5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972d8c.md#insn-00972db4)
- 新版 `00972db4`（命令位置の公開資料なし）

~~~diff
- 00972db4 ["COPY", "tmp:0:8", ["const:588:8"]]
- 00972db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972db4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00972db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972db4 bytes 08211691
+ 00972db4 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7951731310d04ff5ae4e5e0cf3eed6e7"></a>

### [`00972e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972e94.md) → [`00972e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972e94.md) FUN_00972e94

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
      "definition_site": "00972ebc",
      "incomplete_value": false,
      "site": "00972ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972ebc",
      "incomplete_value": false,
      "site": "00972ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "00972ebc",
      "DATA",
      [
        "storage",
        "00c0a588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972ebc",
      "DATA",
      [
        "storage",
        "00c0a5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972e94.md#insn-00972eb4) · [`00972eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972e94.md#insn-00972eb8)
- 新版 `00972eb4`（命令位置の公開資料なし） · `00972eb8`（命令位置の公開資料なし）

~~~diff
- 00972eb4 ["COPY", "tmp:0:8", ["const:588:8"]]
- 00972eb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972eb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972eb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972eb4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00972eb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972eb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972eb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972eb4 bytes 08211691
+ 00972eb4 bytes 08611791
- 00972eb8 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 00972eb8 bytes f40301aa
+ 00972eb8 ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 00972eb8 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be4d800282d662d959e7aa800135ab00"></a>

### [`00973254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973254.md) → [`00973254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973254.md) _INIT_189

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00973290",
      "incomplete_value": true,
      "site": "009732ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00973290",
      "incomplete_value": true,
      "site": "009732ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009732f4",
      "incomplete_value": true,
      "site": "0097330c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009732f4",
      "incomplete_value": true,
      "site": "0097330c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009734a4",
      "incomplete_value": true,
      "site": "009734bc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:c32:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009734a4",
      "incomplete_value": true,
      "site": "009734bc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:ba7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00973290",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "009732b4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "009732d4",
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
      "00973290",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "009732b4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "009732d4",
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

- 旧版 [`00973280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973254.md#insn-00973280) · [`00973288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973254.md#insn-00973288)
- 新版 `00973280`（命令位置の公開資料なし） · `00973288`（命令位置の公開資料なし）

~~~diff
- 00973280 ["COPY", "tmp:0:8", ["const:918:8"]]
- 00973280 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00973280 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00973280 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00973280 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00973280 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00973280 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00973280 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00973280 bytes 73622491
+ 00973280 bytes 73622591
- 00973288 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00973288 bytes a9c9ff90
+ 00973288 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00973288 bytes a9c9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72bc83dd19439fdcefc6d1f638df1cd9"></a>

### [`00973680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973680.md) → [`00973680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973680.md) FUN_00973680

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0073a198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a198.md) [`00976fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976fb0.md) [`0097ff3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097ff3c.md) [`0097ffb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097ffb0.md) · 呼出先 2件 [`009d6a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6a64.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 4件 [`0073a198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a198.md) [`00976fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976fb0.md) [`0097ff3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097ff3c.md) [`0097ffb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097ffb0.md) · 呼出先 2件 [`009d6aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6aa8.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009736a0",
      "incomplete_value": false,
      "site": "009736a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009736a0",
      "incomplete_value": false,
      "site": "009736a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:866:8"
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
      "009736a0",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "009736a0",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009736a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973680.md#insn-009736a0)
- 新版 `009736a0`（命令位置の公開資料なし）

~~~diff
- 009736a0 ["COPY", "tmp:0:8", ["const:866:8"]]
- 009736a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009736a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009736a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009736a0 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 009736a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009736a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009736a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009736a0 bytes 21982191
+ 009736a0 bytes 21641f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

