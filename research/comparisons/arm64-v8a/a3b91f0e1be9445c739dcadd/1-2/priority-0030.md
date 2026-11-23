# v15.7.3 → v15.7.4 · 最優先の変更候補 (30)

[一覧の目次](README.md)

<a id="compare-f1f830f5ef66c6a3221daf402269c5b9"></a>

### [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) → [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) FUN_006ad854

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`006ad28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad28c.md) [`006ad980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad980.md) [`007c1c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1c70.md) [`007c1f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1f74.md) · 呼出先 4件 [`006ad8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8b8.md) [`00bbaea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 4件 [`006ad28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md) [`006ad980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad980.md) [`007c1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1c70.md) [`007c1f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1f74.md) · 呼出先 4件 [`006ad8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8b8.md) [`00bbaeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeec.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006ad884",
      "incomplete_value": true,
      "site": "006ad88c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
      "definition_site": "006ad884",
      "incomplete_value": true,
      "site": "006ad88c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:700:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006ad888",
      "incomplete_value": true,
      "site": "006ad88c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ad888",
      "incomplete_value": true,
      "site": "006ad88c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:708:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ad884",
      "READ",
      [
        "storage",
        "00c1b700",
        null,
        "pointer"
      ]
    ],
    [
      "006ad884",
      "PARAM",
      [
        "storage",
        "00c16a78",
        "_ZTISt11range_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006ad888",
      "READ",
      [
        "storage",
        "00c1b708",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006ad884",
      "READ",
      [
        "storage",
        "00c1b750",
        null,
        "pointer"
      ]
    ],
    [
      "006ad884",
      "PARAM",
      [
        "storage",
        "00c16ac8",
        "_ZTISt11range_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006ad888",
      "READ",
      [
        "storage",
        "00c1b758",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ad884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md#insn-006ad884) · [`006ad888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md#insn-006ad888)
- 新版 [`006ad884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md#insn-006ad884) · [`006ad888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md#insn-006ad888)

~~~diff
- 006ad884 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:700:8"]]
- 006ad884 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 006ad884 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:750:8"]]
+ 006ad884 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 006ad884 bytes 218043f9
+ 006ad884 bytes 21a843f9
- 006ad888 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:708:8"]]
- 006ad888 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 006ad888 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:758:8"]]
+ 006ad888 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 006ad888 bytes 428443f9
+ 006ad888 bytes 42ac43f9
~~~


<a id="compare-db432934f7b46e248ef523b0557e257f"></a>

### [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) → [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) FUN_006ad8a4

採用 · 移動量 `+0x0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 25件 [`006a6d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a6/006a6d68.md) [`006ad28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad28c.md) [`006ad590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad590.md) [`006ad8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8e8.md) [`007c1c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1c70.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 25件 [`006a6d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a6/006a6d68.md) [`006ad28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md) [`006ad590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad590.md) [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md) [`007c1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1c70.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006ad8b0",
      "incomplete_value": false,
      "site": "006ad8b4",
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
            "const:24c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ad8b0",
      "incomplete_value": false,
      "site": "006ad8b4",
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
            "const:1b2:8"
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
      "006ad8b0",
      "PARAM",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006ad8b0",
      "PARAM",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ad8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md#insn-006ad8b0)
- 新版 [`006ad8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md#insn-006ad8b0)

~~~diff
- 006ad8b0 ["COPY", "tmp:0:8", ["const:1b2:8"]]
- 006ad8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006ad8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006ad8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006ad8b0 ["COPY", "tmp:0:8", ["const:24c:8"]]
+ 006ad8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006ad8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006ad8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006ad8b0 bytes 00c80691
+ 006ad8b0 bytes 00300991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c15722de0db8dc68dbe6d1c972b11aea"></a>

### [`006ad8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8b8.md) → [`006ad8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8b8.md) FUN_006ad8b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) · 呼出先 1件 [`00bdda30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda30.md)
- 新版 呼出元 1件 [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) · 呼出先 1件 [`00bdda80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ad8d4",
      "incomplete_value": true,
      "site": "006ad8d8",
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
      "definition_site": "006ad8d4",
      "incomplete_value": true,
      "site": "006ad8d8",
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
      "006ad8d0",
      "READ",
      [
        "storage",
        "00c1b710",
        null,
        "pointer"
      ]
    ],
    [
      "006ad8d8",
      "DATA",
      [
        "storage",
        "00c16a48",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "006ad8d0",
      "READ",
      [
        "storage",
        "00c1b760",
        null,
        "pointer"
      ]
    ],
    [
      "006ad8d8",
      "DATA",
      [
        "storage",
        "00c16a98",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ad8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8b8.md#insn-006ad8d0)
- 新版 [`006ad8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8b8.md#insn-006ad8d0)

~~~diff
- 006ad8d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:710:8"]]
- 006ad8d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006ad8d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:760:8"]]
+ 006ad8d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006ad8d0 bytes 088943f9
+ 006ad8d0 bytes 08b143f9
~~~


<a id="compare-56bfc04aed48b13d3e5740d2e3598796"></a>

### [`006ad980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad980.md) → [`006ad980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad980.md) FUN_006ad980

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a6/006a6d68.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) [`006add94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006add94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a6/006a6d68.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) [`006add94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006add94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "006add28",
      "incomplete_value": false,
      "site": "006add2c",
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
      "definition_site": "006add28",
      "incomplete_value": false,
      "site": "006add2c",
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
      "006add28",
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
      "006add28",
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

- 旧版 [`006add28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad980.md#insn-006add28)
- 新版 [`006add28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad980.md#insn-006add28)

~~~diff
- 006add28 ["COPY", "tmp:0:8", ["const:f2f:8"]]
- 006add28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006add28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006add28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006add28 ["COPY", "tmp:0:8", ["const:ea2:8"]]
+ 006add28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006add28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006add28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006add28 bytes 00bc3c91
+ 006add28 bytes 00883a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd225c7ce8a86349e25a7e4e0cebbb75"></a>

### [`006ae060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae060.md) → [`006ae060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae060.md) FUN_006ae060

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
      "definition_site": "006ae06c",
      "incomplete_value": false,
      "site": "006ae06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae06c",
      "incomplete_value": false,
      "site": "006ae06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "006ae06c",
      "DATA",
      [
        "storage",
        "00bf8da0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae06c",
      "DATA",
      [
        "storage",
        "00bf8df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae060.md#insn-006ae068)
- 新版 [`006ae068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae060.md#insn-006ae068)

~~~diff
- 006ae068 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 006ae068 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae068 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae068 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ae068 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 006ae068 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae068 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae068 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae068 bytes 29813691
+ 006ae068 bytes 29c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f843a1a7c4e94d76e66f88f78f90460"></a>

### [`006ae40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae40c.md) → [`006ae40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae40c.md) FUN_006ae40c

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
      "definition_site": "006ae430",
      "incomplete_value": false,
      "site": "006ae430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae430",
      "incomplete_value": false,
      "site": "006ae430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "006ae430",
      "DATA",
      [
        "storage",
        "00bf8e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae430",
      "DATA",
      [
        "storage",
        "00bf8e70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae42c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae40c.md#insn-006ae42c)
- 新版 [`006ae42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae40c.md#insn-006ae42c)

~~~diff
- 006ae42c ["COPY", "tmp:0:8", ["const:e20:8"]]
- 006ae42c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ae42c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ae42c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ae42c ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 006ae42c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae42c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae42c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ae42c bytes 08813891
+ 006ae42c bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea508968c91a7fd2de4c3e75af5d240e"></a>

### [`006ae440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae440.md) → [`006ae440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae440.md) FUN_006ae440

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
      "definition_site": "006ae44c",
      "incomplete_value": false,
      "site": "006ae44c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae44c",
      "incomplete_value": false,
      "site": "006ae44c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "006ae44c",
      "DATA",
      [
        "storage",
        "00bf8e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae44c",
      "DATA",
      [
        "storage",
        "00bf8e70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae440.md#insn-006ae448)
- 新版 [`006ae448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae440.md#insn-006ae448)

~~~diff
- 006ae448 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 006ae448 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae448 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae448 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ae448 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 006ae448 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae448 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae448 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae448 bytes 29813891
+ 006ae448 bytes 29c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac63e36741d3cddbab72bc3651fcf8fd"></a>

### [`006ae59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae59c.md) → [`006ae59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae59c.md) FUN_006ae59c

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
      "definition_site": "006ae5c0",
      "incomplete_value": false,
      "site": "006ae5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae5c0",
      "incomplete_value": false,
      "site": "006ae5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "006ae5c0",
      "DATA",
      [
        "storage",
        "00bf8ea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae5c0",
      "DATA",
      [
        "storage",
        "00bf8ef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae59c.md#insn-006ae5bc)
- 新版 [`006ae5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae59c.md#insn-006ae5bc)

~~~diff
- 006ae5bc ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 006ae5bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ae5bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ae5bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ae5bc ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 006ae5bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae5bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae5bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ae5bc bytes 08813a91
+ 006ae5bc bytes 08c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b31f4264a262055c9ba8b9354d7d7b8f"></a>

### [`006ae5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae5d0.md) → [`006ae5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5d0.md) FUN_006ae5d0

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
      "definition_site": "006ae5dc",
      "incomplete_value": false,
      "site": "006ae5dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae5dc",
      "incomplete_value": false,
      "site": "006ae5dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "006ae5dc",
      "DATA",
      [
        "storage",
        "00bf8ea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae5dc",
      "DATA",
      [
        "storage",
        "00bf8ef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae5d0.md#insn-006ae5d8)
- 新版 [`006ae5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5d0.md#insn-006ae5d8)

~~~diff
- 006ae5d8 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 006ae5d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae5d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae5d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ae5d8 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 006ae5d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae5d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae5d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae5d8 bytes 29813a91
+ 006ae5d8 bytes 29c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88210935d1d0d90cf49d3f5af863b170"></a>

### [`006ae91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae91c.md) → [`006ae91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae91c.md) FUN_006ae91c

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
      "definition_site": "006ae940",
      "incomplete_value": false,
      "site": "006ae940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae940",
      "incomplete_value": false,
      "site": "006ae940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "006ae940",
      "DATA",
      [
        "storage",
        "00bf8f20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae940",
      "DATA",
      [
        "storage",
        "00bf8f70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae93c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae91c.md#insn-006ae93c)
- 新版 [`006ae93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae91c.md#insn-006ae93c)

~~~diff
- 006ae93c ["COPY", "tmp:0:8", ["const:f20:8"]]
- 006ae93c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ae93c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ae93c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ae93c ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 006ae93c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae93c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae93c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ae93c bytes 08813c91
+ 006ae93c bytes 08c13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2337f7994c4aac57dc5b7488f1878232"></a>

### [`006ae950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae950.md) → [`006ae950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae950.md) FUN_006ae950

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
      "definition_site": "006ae95c",
      "incomplete_value": false,
      "site": "006ae95c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae95c",
      "incomplete_value": false,
      "site": "006ae95c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
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
      "006ae95c",
      "DATA",
      [
        "storage",
        "00bf8f20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae95c",
      "DATA",
      [
        "storage",
        "00bf8f70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae950.md#insn-006ae958)
- 新版 [`006ae958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae950.md#insn-006ae958)

~~~diff
- 006ae958 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 006ae958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ae958 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 006ae958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae958 bytes 29813c91
+ 006ae958 bytes 29c13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0a73de3cd4245f9100193753404bafe"></a>

### [`006aeeb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006aeeb4.md) → [`006aeeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006aeeb4.md) FUN_006aeeb4

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
      "definition_site": "006aeed8",
      "incomplete_value": false,
      "site": "006aeed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006aeed8",
      "incomplete_value": false,
      "site": "006aeed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
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
      "006aeed8",
      "DATA",
      [
        "storage",
        "00bf8fa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006aeed8",
      "DATA",
      [
        "storage",
        "00bf8ff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006aeed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006aeeb4.md#insn-006aeed4)
- 新版 [`006aeed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006aeeb4.md#insn-006aeed4)

~~~diff
- 006aeed4 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 006aeed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006aeed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006aeed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006aeed4 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 006aeed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006aeed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006aeed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006aeed4 bytes 08813e91
+ 006aeed4 bytes 08c13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b75c2af73946dc64af43e3b80c14a509"></a>

### [`006aeee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006aeee8.md) → [`006aeee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006aeee8.md) FUN_006aeee8

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
      "definition_site": "006aeef4",
      "incomplete_value": false,
      "site": "006aeef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006aeef4",
      "incomplete_value": false,
      "site": "006aeef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
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
      "006aeef4",
      "DATA",
      [
        "storage",
        "00bf8fa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006aeef4",
      "DATA",
      [
        "storage",
        "00bf8ff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006aeef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006aeee8.md#insn-006aeef0)
- 新版 [`006aeef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006aeee8.md#insn-006aeef0)

~~~diff
- 006aeef0 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 006aeef0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006aeef0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006aeef0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006aeef0 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 006aeef0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006aeef0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006aeef0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006aeef0 bytes 29813e91
+ 006aeef0 bytes 29c13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0392373febb3d3ae621c6ad1968336b"></a>

### [`006afa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afa38.md) → [`006afa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afa38.md) FUN_006afa38

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
      "definition_site": "006afa5c",
      "incomplete_value": false,
      "site": "006afa5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afa5c",
      "incomplete_value": false,
      "site": "006afa5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:20:8"
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
      "006afa5c",
      "DATA",
      [
        "storage",
        "00bf9020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afa5c",
      "DATA",
      [
        "storage",
        "00bf9070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afa38.md#insn-006afa58)
- 新版 [`006afa58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afa38.md#insn-006afa58)

~~~diff
- 006afa58 ["COPY", "tmp:0:8", ["const:20:8"]]
- 006afa58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afa58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afa58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006afa58 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 006afa58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006afa58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006afa58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afa58 bytes 08810091
+ 006afa58 bytes 08c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-395944d8a3ed9f54a7be9616f0e21265"></a>

### [`006afa6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afa6c.md) → [`006afa6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afa6c.md) FUN_006afa6c

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
      "definition_site": "006afa78",
      "incomplete_value": false,
      "site": "006afa78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afa78",
      "incomplete_value": false,
      "site": "006afa78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:20:8"
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
      "006afa78",
      "DATA",
      [
        "storage",
        "00bf9020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afa78",
      "DATA",
      [
        "storage",
        "00bf9070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afa6c.md#insn-006afa74)
- 新版 [`006afa74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afa6c.md#insn-006afa74)

~~~diff
- 006afa74 ["COPY", "tmp:0:8", ["const:20:8"]]
- 006afa74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006afa74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006afa74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006afa74 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 006afa74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006afa74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006afa74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006afa74 bytes 29810091
+ 006afa74 bytes 29c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d742ec2fb9e2cabf489faf7f861fd86b"></a>

### [`006afb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afb70.md) → [`006afb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afb70.md) FUN_006afb70

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
      "definition_site": "006afb94",
      "incomplete_value": false,
      "site": "006afb94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afb94",
      "incomplete_value": false,
      "site": "006afb94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "006afb94",
      "DATA",
      [
        "storage",
        "00bf90a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afb94",
      "DATA",
      [
        "storage",
        "00bf90f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afb70.md#insn-006afb90)
- 新版 [`006afb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afb70.md#insn-006afb90)

~~~diff
- 006afb90 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 006afb90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afb90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afb90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006afb90 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 006afb90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006afb90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006afb90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afb90 bytes 08810291
+ 006afb90 bytes 08c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55c5721f090d21673f54b96623f148c4"></a>

### [`006afba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afba4.md) → [`006afba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afba4.md) FUN_006afba4

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
      "definition_site": "006afbb0",
      "incomplete_value": false,
      "site": "006afbb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afbb0",
      "incomplete_value": false,
      "site": "006afbb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006afbb0",
      "DATA",
      [
        "storage",
        "00bf90a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afbb0",
      "DATA",
      [
        "storage",
        "00bf90f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afbac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afba4.md#insn-006afbac)
- 新版 [`006afbac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afba4.md#insn-006afbac)

~~~diff
- 006afbac ["COPY", "tmp:0:8", ["const:a0:8"]]
- 006afbac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006afbac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006afbac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006afbac ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 006afbac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006afbac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006afbac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006afbac bytes 29810291
+ 006afbac bytes 29c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-568fa47775c08e558e245d61eb6c2fe9"></a>

### [`006afc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afc9c.md) → [`006afc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afc9c.md) FUN_006afc9c

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
      "definition_site": "006afcc0",
      "incomplete_value": false,
      "site": "006afcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afcc0",
      "incomplete_value": false,
      "site": "006afcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:120:8"
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
      "006afcc0",
      "DATA",
      [
        "storage",
        "00bf9120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afcc0",
      "DATA",
      [
        "storage",
        "00bf9170",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afcbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afc9c.md#insn-006afcbc)
- 新版 [`006afcbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afc9c.md#insn-006afcbc)

~~~diff
- 006afcbc ["COPY", "tmp:0:8", ["const:120:8"]]
- 006afcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006afcbc ["COPY", "tmp:0:8", ["const:170:8"]]
+ 006afcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006afcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006afcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afcbc bytes 08810491
+ 006afcbc bytes 08c10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-513a732e59b2b07afb057a13c9eab0aa"></a>

### [`006afcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afcd0.md) → [`006afcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afcd0.md) FUN_006afcd0

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
      "definition_site": "006afcdc",
      "incomplete_value": false,
      "site": "006afcdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afcdc",
      "incomplete_value": false,
      "site": "006afcdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:120:8"
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
      "006afcdc",
      "DATA",
      [
        "storage",
        "00bf9120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afcdc",
      "DATA",
      [
        "storage",
        "00bf9170",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afcd0.md#insn-006afcd8)
- 新版 [`006afcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afcd0.md#insn-006afcd8)

~~~diff
- 006afcd8 ["COPY", "tmp:0:8", ["const:120:8"]]
- 006afcd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006afcd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006afcd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006afcd8 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 006afcd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006afcd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006afcd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006afcd8 bytes 29810491
+ 006afcd8 bytes 29c10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e68531007c6fec2ba1fabb38face5746"></a>

### [`006afe68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afe68.md) → [`006afe68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afe68.md) FUN_006afe68

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
      "definition_site": "006afe88",
      "incomplete_value": false,
      "site": "006afe8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afe88",
      "incomplete_value": false,
      "site": "006afe8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
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
      "006afe8c",
      "DATA",
      [
        "storage",
        "00bf91a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afe8c",
      "DATA",
      [
        "storage",
        "00bf91f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afe88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afe68.md#insn-006afe88)
- 新版 [`006afe88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afe68.md#insn-006afe88)

~~~diff
- 006afe88 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 006afe88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afe88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afe88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006afe88 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 006afe88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006afe88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006afe88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afe88 bytes 08810691
+ 006afe88 bytes 08c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf4cafb0799375a939dd77c9cc3ebe8"></a>

### [`006afea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afea0.md) → [`006afea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afea0.md) FUN_006afea0

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
      "definition_site": "006afea4",
      "incomplete_value": false,
      "site": "006afea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afea4",
      "incomplete_value": false,
      "site": "006afea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
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
      "006afea8",
      "DATA",
      [
        "storage",
        "00bf91a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afea8",
      "DATA",
      [
        "storage",
        "00bf91f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afea0.md#insn-006afea4)
- 新版 [`006afea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afea0.md#insn-006afea4)

~~~diff
- 006afea4 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 006afea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006afea4 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 006afea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006afea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006afea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afea4 bytes 08810691
+ 006afea4 bytes 08c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e62437998d10548a83162ac94822e64"></a>

### [`006b0184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0184.md) → [`006b0184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0184.md) FUN_006b0184

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
      "definition_site": "006b01a4",
      "incomplete_value": false,
      "site": "006b01a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b01a4",
      "incomplete_value": false,
      "site": "006b01a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006b01a8",
      "DATA",
      [
        "storage",
        "00bf9220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b01a8",
      "DATA",
      [
        "storage",
        "00bf9270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b01a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0184.md#insn-006b01a4)
- 新版 [`006b01a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0184.md#insn-006b01a4)

~~~diff
- 006b01a4 ["COPY", "tmp:0:8", ["const:220:8"]]
- 006b01a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b01a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b01a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b01a4 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 006b01a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b01a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b01a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b01a4 bytes 08810891
+ 006b01a4 bytes 08c10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4fd89fc415ca5a4d4dcc77a99bef3b4"></a>

### [`006b01bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b01bc.md) → [`006b01bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b01bc.md) FUN_006b01bc

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
      "definition_site": "006b01c0",
      "incomplete_value": false,
      "site": "006b01c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b01c0",
      "incomplete_value": false,
      "site": "006b01c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006b01c4",
      "DATA",
      [
        "storage",
        "00bf9220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b01c4",
      "DATA",
      [
        "storage",
        "00bf9270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b01c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b01bc.md#insn-006b01c0)
- 新版 [`006b01c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b01bc.md#insn-006b01c0)

~~~diff
- 006b01c0 ["COPY", "tmp:0:8", ["const:220:8"]]
- 006b01c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b01c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b01c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b01c0 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 006b01c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b01c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b01c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b01c0 bytes 08810891
+ 006b01c0 bytes 08c10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c339314d22451b94f0d539872c7d2e7b"></a>

### [`006b04cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b04cc.md) → [`006b04cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b04cc.md) FUN_006b04cc

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
      "definition_site": "006b04ec",
      "incomplete_value": false,
      "site": "006b04f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b04ec",
      "incomplete_value": false,
      "site": "006b04f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "006b04f0",
      "DATA",
      [
        "storage",
        "00bf92a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b04f0",
      "DATA",
      [
        "storage",
        "00bf92f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b04ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b04cc.md#insn-006b04ec)
- 新版 [`006b04ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b04cc.md#insn-006b04ec)

~~~diff
- 006b04ec ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 006b04ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b04ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b04ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b04ec ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 006b04ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b04ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b04ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b04ec bytes 08810a91
+ 006b04ec bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a45acd81d9250b9a10fc9ee5a754d0b"></a>

### [`006b0504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0504.md) → [`006b0504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0504.md) FUN_006b0504

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
      "definition_site": "006b0508",
      "incomplete_value": false,
      "site": "006b050c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0508",
      "incomplete_value": false,
      "site": "006b050c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006b050c",
      "DATA",
      [
        "storage",
        "00bf92a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b050c",
      "DATA",
      [
        "storage",
        "00bf92f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b0508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0504.md#insn-006b0508)
- 新版 [`006b0508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0504.md#insn-006b0508)

~~~diff
- 006b0508 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 006b0508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b0508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b0508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b0508 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 006b0508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b0508 bytes 08810a91
+ 006b0508 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dcead98fcb06ec4e83c155a590a3ecb"></a>

### [`006b0824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0824.md) → [`006b0824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0824.md) FUN_006b0824

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
      "definition_site": "006b0848",
      "incomplete_value": false,
      "site": "006b0848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0848",
      "incomplete_value": false,
      "site": "006b0848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "006b0848",
      "DATA",
      [
        "storage",
        "00bf9320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b0848",
      "DATA",
      [
        "storage",
        "00bf9370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b0844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0824.md#insn-006b0844)
- 新版 [`006b0844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0824.md#insn-006b0844)

~~~diff
- 006b0844 ["COPY", "tmp:0:8", ["const:320:8"]]
- 006b0844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b0844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b0844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b0844 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 006b0844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b0844 bytes 08810c91
+ 006b0844 bytes 08c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fceac83b1e6a872787480bb2b827482e"></a>

### [`006b0858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0858.md) → [`006b0858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0858.md) FUN_006b0858

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
      "definition_site": "006b0864",
      "incomplete_value": false,
      "site": "006b0864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0864",
      "incomplete_value": false,
      "site": "006b0864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "006b0864",
      "DATA",
      [
        "storage",
        "00bf9320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b0864",
      "DATA",
      [
        "storage",
        "00bf9370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b0860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0858.md#insn-006b0860)
- 新版 [`006b0860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0858.md#insn-006b0860)

~~~diff
- 006b0860 ["COPY", "tmp:0:8", ["const:320:8"]]
- 006b0860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006b0860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006b0860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006b0860 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 006b0860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006b0860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006b0860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006b0860 bytes 29810c91
+ 006b0860 bytes 29c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f21cb13a723997876201631bf3af9027"></a>

### [`006b0a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0a20.md) → [`006b0a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0a20.md) _INIT_106

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
      "definition_site": "006b0a5c",
      "incomplete_value": true,
      "site": "006b0a78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b0a5c",
      "incomplete_value": true,
      "site": "006b0a78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b0a80",
      "incomplete_value": true,
      "site": "006b0a9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b0a80",
      "incomplete_value": true,
      "site": "006b0a9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b0aa0",
      "incomplete_value": true,
      "site": "006b0abc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b0aa0",
      "incomplete_value": true,
      "site": "006b0abc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006b0a5c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006b0a80",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006b0aa0",
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
      "006b0a5c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006b0a80",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006b0aa0",
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

- 旧版 [`006b0a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0a20.md#insn-006b0a4c) · [`006b0a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0a20.md#insn-006b0a54)
- 新版 [`006b0a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0a20.md#insn-006b0a4c) · [`006b0a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0a20.md#insn-006b0a54)

~~~diff
- 006b0a4c ["COPY", "tmp:0:8", ["const:838:8"]]
- 006b0a4c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006b0a4c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006b0a4c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006b0a4c ["COPY", "tmp:0:8", ["const:878:8"]]
+ 006b0a4c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006b0a4c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006b0a4c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006b0a4c bytes 73e22091
+ 006b0a4c bytes 73e22191
- 006b0a54 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006b0a54 bytes a9dffff0
+ 006b0a54 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006b0a54 bytes a9dffff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e71230926682d621265ca6a4c61849e3"></a>

### [`006b0f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0f78.md) → [`006b0f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0f78.md) FUN_006b0f78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ab1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) · 呼出先 9件 [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`006b0db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0db0.md) [`00ab11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00ab1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) · 呼出先 9件 [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`006b0db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0db0.md) [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.00% / 新版 86.00%

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
      "definition_site": "006b0fac",
      "incomplete_value": false,
      "site": "006b0fb4",
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
      "definition_site": "006b0fac",
      "incomplete_value": false,
      "site": "006b0fb4",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b0fc8",
      "incomplete_value": true,
      "site": "006b0fd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b4a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0fc8",
      "incomplete_value": true,
      "site": "006b0fd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ab0:8"
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
      "definition_site": "006b1068",
      "incomplete_value": true,
      "site": "006b106c",
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
      "definition_site": "006b1068",
      "incomplete_value": true,
      "site": "006b106c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b0fb4",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006b0fc8",
      "READ",
      [
        "storage",
        "002a6ab0",
        null,
        "string"
      ]
    ],
    [
      "006b1058",
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
      "006b0fb4",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006b0fc8",
      "READ",
      [
        "storage",
        "002a6b4a",
        null,
        "string"
      ]
    ],
    [
      "006b1058",
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

- 旧版 [`006b0fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0f78.md#insn-006b0fac) · [`006b0fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0f78.md#insn-006b0fc4) · [`006b1058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0f78.md#insn-006b1058)
- 新版 [`006b0fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0f78.md#insn-006b0fac) · [`006b0fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0f78.md#insn-006b0fc4) · [`006b1058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0f78.md#insn-006b1058)

~~~diff
- 006b0fac ["COPY", "tmp:0:8", ["const:d28:8"]]
- 006b0fac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b0fac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b0fac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b0fac ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 006b0fac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0fac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0fac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b0fac bytes 08a13491
+ 006b0fac bytes 08e13591
- 006b0fc4 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 006b0fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b0fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b0fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b0fc4 ["COPY", "tmp:0:8", ["const:b4a:8"]]
+ 006b0fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b0fc4 bytes 08c12a91
+ 006b0fc4 bytes 08292d91
- 006b1058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 006b1058 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006b1058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 006b1058 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006b1058 bytes 08b946f9
+ 006b1058 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fdcd308cf31ad0e8ed7fa42e1caab0d"></a>

### [`006b12cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b12cc.md) → [`006b12cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b12cc.md) FUN_006b12cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ab1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00ab1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.45% / 新版 90.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006b130c",
      "incomplete_value": false,
      "site": "006b1310",
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
      "definition_site": "006b130c",
      "incomplete_value": false,
      "site": "006b1310",
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
      "definition_site": "006b1328",
      "incomplete_value": true,
      "site": "006b133c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:739:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b1328",
      "incomplete_value": true,
      "site": "006b133c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ae:8"
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
      "definition_site": "006b1328",
      "incomplete_value": true,
      "site": "006b133c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006b1328",
      "incomplete_value": true,
      "site": "006b133c",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b1310",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006b1328",
      "READ",
      [
        "storage",
        "0029d6ae",
        null,
        "string"
      ]
    ],
    [
      "006b1328",
      "READ",
      [
        "storage",
        "0029d6be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b1310",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006b1328",
      "READ",
      [
        "storage",
        "0029d739",
        null,
        "string"
      ]
    ],
    [
      "006b1328",
      "READ",
      [
        "storage",
        "0029d749",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b130c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b12cc.md#insn-006b130c) · [`006b1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b12cc.md#insn-006b1320) · [`006b1324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b12cc.md#insn-006b1324)
- 新版 [`006b130c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b12cc.md#insn-006b130c) · [`006b1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b12cc.md#insn-006b1320)

~~~diff
- 006b130c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 006b130c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b130c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b130c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b130c ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 006b130c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b130c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b130c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b130c bytes 08a13491
+ 006b130c bytes 08e13591
- 006b1320 ["COPY", "tmp:0:8", ["const:6ae:8"]]
- 006b1320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b1320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b1320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b1320 ["COPY", "tmp:0:8", ["const:739:8"]]
+ 006b1320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b1320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b1320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b1320 bytes 08b91a91
+ 006b1320 bytes 08e51c91
- 006b1324 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 006b1324 bytes 09e0ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eff4a3660259d0e7b1d89ae4d6410ee"></a>

### [`006b15e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b15e4.md) → [`006b15e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b15e4.md) FUN_006b15e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068d810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d810.md) · 呼出先 27件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) · 呼出先 27件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.04% / 新版 92.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b177c",
      "incomplete_value": true,
      "site": "006b177c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:764:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b177c",
      "incomplete_value": true,
      "site": "006b177c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006b1824",
      "incomplete_value": false,
      "site": "006b1824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b1824",
      "incomplete_value": false,
      "site": "006b1824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "definition_site": "006b1a18",
      "incomplete_value": false,
      "site": "006b1a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b1a18",
      "incomplete_value": false,
      "site": "006b1a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "006b1660",
      "READ",
      [
        "storage",
        "00c27dd4",
        null,
        "undefined4"
      ]
    ],
    [
      "006b167c",
      "READ",
      [
        "storage",
        "00c27dd0",
        null,
        "undefined4"
      ]
    ],
    [
      "006b1760",
      "READ",
      [
        "storage",
        "002a46d9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b1660",
      "READ",
      [
        "storage",
        "00c27e14",
        null,
        "undefined4"
      ]
    ],
    [
      "006b167c",
      "READ",
      [
        "storage",
        "00c27e10",
        null,
        "undefined4"
      ]
    ],
    [
      "006b1760",
      "READ",
      [
        "storage",
        "002a4764",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b165c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b15e4.md#insn-006b165c) · [`006b1678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b15e4.md#insn-006b1678) · [`006b175c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b15e4.md#insn-006b175c)
- 新版 [`006b165c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b15e4.md#insn-006b165c) · [`006b1678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b15e4.md#insn-006b1678) · [`006b175c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b15e4.md#insn-006b175c)

~~~diff
- 006b165c ["COPY", "tmp:0:8", ["const:dd4:8"]]
- 006b165c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b165c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b165c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b165c ["COPY", "tmp:0:8", ["const:e14:8"]]
+ 006b165c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b165c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b165c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b165c bytes 08513791
+ 006b165c bytes 08513891
- 006b1678 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 006b1678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b1678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b1678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b1678 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 006b1678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b1678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b1678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b1678 bytes 08413791
+ 006b1678 bytes 08413891
- 006b175c ["COPY", "tmp:0:8", ["const:6d9:8"]]
- 006b175c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006b175c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006b175c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006b175c ["COPY", "tmp:0:8", ["const:764:8"]]
+ 006b175c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006b175c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006b175c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006b175c bytes 29651b91
+ 006b175c bytes 29911d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58df5f37809e1656b299f7f9161fcdc4"></a>

### [`006b2b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b2/006b2b44.md) → [`006b2b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2b44.md) FUN_006b2b44

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c6850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c6/006c6850.md) · 呼出先 18件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044c794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c794.md) [`0044c80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md)
- 新版 呼出元 1件 [`006c6850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6850.md) · 呼出先 18件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044c794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c794.md) [`0044c80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c80c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.40% / 新版 89.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 7件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b2b88",
      "incomplete_value": true,
      "site": "006b2b98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b2b88",
      "incomplete_value": true,
      "site": "006b2b98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0f:8"
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
      "definition_site": "006b2b88",
      "incomplete_value": true,
      "site": "006b2b9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b2b88",
      "incomplete_value": true,
      "site": "006b2b9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0f:8"
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
      "definition_site": "006b2bc0",
      "incomplete_value": true,
      "site": "006b2bd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:782:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b2bc0",
      "incomplete_value": true,
      "site": "006b2bd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6f7:8"
              ]
            ]
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
      "006b2b74",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006b2b88",
      "READ",
      [
        "storage",
        "00292c0f",
        null,
        "string"
      ]
    ],
    [
      "006b2bc0",
      "READ",
      [
        "storage",
        "002a26f7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b2b74",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006b2b88",
      "READ",
      [
        "storage",
        "00292b82",
        null,
        "string"
      ]
    ],
    [
      "006b2bc0",
      "READ",
      [
        "storage",
        "002a2782",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b2b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b2/006b2b44.md#insn-006b2b64) · [`006b2b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b2/006b2b44.md#insn-006b2b7c)
- 新版 [`006b2b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2b44.md#insn-006b2b64) · [`006b2b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2b44.md#insn-006b2b7c)

~~~diff
- 006b2b64 ["COPY", "tmp:0:8", ["const:38:8"]]
- 006b2b64 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 006b2b64 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 006b2b64 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 006b2b64 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006b2b64 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 006b2b64 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 006b2b64 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 006b2b64 bytes f7e20091
+ 006b2b64 bytes f7e20191
- 006b2b7c ["COPY", "register:4048:8", ["const:292000:8"]]
- 006b2b7c bytes 09dfff90
+ 006b2b7c ["COPY", "register:4048:8", ["const:292000:8"]]
+ 006b2b7c bytes 09dfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c1421ce1e6014ee39ec810e3def705f"></a>

### [`006b3674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b3/006b3674.md) → [`006b3674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b3/006b3674.md) FUN_006b3674

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.96% / 新版 82.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b36b8",
      "incomplete_value": true,
      "site": "006b36c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b36b8",
      "incomplete_value": true,
      "site": "006b36c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0f:8"
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
      "definition_site": "006b36e8",
      "incomplete_value": true,
      "site": "006b36fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:782:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b36e8",
      "incomplete_value": true,
      "site": "006b36fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6f7:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006b385c",
      "incomplete_value": false,
      "site": "006b385c",
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
      "definition_site": "006b385c",
      "incomplete_value": false,
      "site": "006b385c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b36a4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006b36b8",
      "READ",
      [
        "storage",
        "00292c0f",
        null,
        "string"
      ]
    ],
    [
      "006b36e8",
      "READ",
      [
        "storage",
        "002a26f7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b36a4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006b36b8",
      "READ",
      [
        "storage",
        "00292b82",
        null,
        "string"
      ]
    ],
    [
      "006b36e8",
      "READ",
      [
        "storage",
        "002a2782",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b36a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b3/006b3674.md#insn-006b36a0) · [`006b36ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b3/006b3674.md#insn-006b36ac)
- 新版 [`006b36a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b3/006b3674.md#insn-006b36a0) · [`006b36ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b3/006b3674.md#insn-006b36ac)

~~~diff
- 006b36a0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 006b36a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b36a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b36a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b36a0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006b36a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b36a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b36a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b36a0 bytes 08e10091
+ 006b36a0 bytes 08e10191
- 006b36ac ["COPY", "register:4048:8", ["const:292000:8"]]
- 006b36ac bytes e9defff0
+ 006b36ac ["COPY", "register:4048:8", ["const:292000:8"]]
+ 006b36ac bytes e9defff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84c6bab6e6282afc448fefbbce5b2b0b"></a>

### [`006b408c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b4/006b408c.md) → [`006b408c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b4/006b408c.md) FUN_006b408c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006c0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0060.md) [`006ce8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006ce8d4.md) · 呼出先 14件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446074.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)
- 新版 呼出元 2件 [`006c0060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0060.md) [`006ce8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006ce8d4.md) · 呼出先 14件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00446074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446074.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.63% / 新版 99.63%

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
      "definition_site": "006b40cc",
      "incomplete_value": true,
      "site": "006b40cc",
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
      "definition_site": "006b40cc",
      "incomplete_value": true,
      "site": "006b40cc",
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
      "definition_site": "006b40d4",
      "incomplete_value": false,
      "site": "006b40e8",
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
      "definition_site": "006b40d4",
      "incomplete_value": false,
      "site": "006b40e8",
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
      "definition_site": "006b40dc",
      "incomplete_value": false,
      "site": "006b40e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b40dc",
      "incomplete_value": false,
      "site": "006b40e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "006b40c8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006b40d4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006b40dc",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006b40c8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006b40d4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006b40dc",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b40c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b4/006b408c.md#insn-006b40c8) · [`006b40d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b4/006b408c.md#insn-006b40d4) · [`006b40dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b4/006b408c.md#insn-006b40dc)
- 新版 [`006b40c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b4/006b408c.md#insn-006b40c8) · [`006b40d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b4/006b408c.md#insn-006b40d4) · [`006b40dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b4/006b408c.md#insn-006b40dc)

~~~diff
- 006b40c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006b40c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006b40c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006b40c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006b40c8 bytes 083d45f9
+ 006b40c8 bytes 085d45f9
- 006b40d4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006b40d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006b40d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006b40d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006b40d4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006b40d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006b40d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006b40d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006b40d4 bytes 21203991
+ 006b40d4 bytes 21603a91
- 006b40dc ["COPY", "tmp:0:8", ["const:298:8"]]
- 006b40dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006b40dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006b40dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006b40dc ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006b40dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006b40dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006b40dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006b40dc bytes 42600a91
+ 006b40dc bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da714979e0bee429f629b756fb2faf18"></a>

### [`006b5fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b5/006b5fcc.md) → [`006b5fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5fcc.md) FUN_006b5fcc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ab1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00ab1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 96.56% / 新版 96.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b642c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b6430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b643c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b6028",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006b6108",
      "READ",
      [
        "storage",
        "0029a05b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:006b641c",
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
      "006b6028",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006b6108",
      "READ",
      [
        "storage",
        "0029a059",
        null,
        "string"
      ]
    ],
    [
      "006b641c",
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

- 旧版 [`006b642c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b5/006b5fcc.md#insn-006b642c) · [`006b6430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b5/006b5fcc.md#insn-006b6430)
- 新版 [`006b642c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5fcc.md#insn-006b642c)

~~~diff
- 006b642c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:100:8"]]
- 006b642c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b642c bytes e88300f9
+ 006b642c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:100:8"]]
+ 006b642c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006b642c bytes e88300f9
- 006b6430 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:148:8"]]
- 006b6430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006b6430 bytes e9a700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e32a4734b32f71559ee9b1c227e11b16"></a>

### [`006b6b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6b68.md) → [`006b6b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6b68.md) FUN_006b6b68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006b6c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6c84.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`006b6c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6c84.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006b6b80",
      "incomplete_value": true,
      "site": "006b6b84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c27000:8"
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
    "old": {
      "definition_site": "006b6b80",
      "incomplete_value": true,
      "site": "006b6b84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c27000:8"
              ],
              [
                "leaf",
                "const:c90:8"
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
      "definition_site": "006b6b98",
      "incomplete_value": true,
      "site": "006b6b9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c27000:8"
              ],
              [
                "leaf",
                "const:cb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b6b98",
      "incomplete_value": true,
      "site": "006b6b9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c27000:8"
              ],
              [
                "leaf",
                "const:c78:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006b6bb0",
      "incomplete_value": true,
      "site": "006b6bb4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:ca0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b6bb0",
      "incomplete_value": true,
      "site": "006b6bb4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:c60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b6b74",
      "READ",
      [
        "storage",
        "00c27c80",
        null,
        "undefined1"
      ]
    ],
    [
      "006b6b80",
      "READ",
      [
        "storage",
        "00c27c90",
        null,
        "undefined8"
      ]
    ],
    [
      "006b6b8c",
      "READ",
      [
        "storage",
        "00c27c68",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "006b6b74",
      "READ",
      [
        "storage",
        "00c27cc0",
        null,
        "undefined1"
      ]
    ],
    [
      "006b6b80",
      "READ",
      [
        "storage",
        "00c27cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "006b6b8c",
      "READ",
      [
        "storage",
        "00c27ca8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b6b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6b68.md#insn-006b6b74) · [`006b6b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6b68.md#insn-006b6b80) · [`006b6b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6b68.md#insn-006b6b8c)
- 新版 [`006b6b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6b68.md#insn-006b6b74) · [`006b6b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6b68.md#insn-006b6b80) · [`006b6b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6b68.md#insn-006b6b8c)

~~~diff
- 006b6b74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c80:8"]]
- 006b6b74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 006b6b74 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 006b6b74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
+ 006b6b74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 006b6b74 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 006b6b74 bytes 08017239
+ 006b6b74 bytes 08017339
- 006b6b80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c90:8"]]
- 006b6b80 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006b6b80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
+ 006b6b80 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006b6b80 bytes 004946f9
+ 006b6b80 bytes 006946f9
- 006b6b8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c68:8"]]
- 006b6b8c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 006b6b8c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 006b6b8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ca8:8"]]
+ 006b6b8c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 006b6b8c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 006b6b8c bytes 08a17139
+ 006b6b8c bytes 08a17239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed808081014377817b72eb6378aed4d2"></a>

### [`006b77e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b7/006b77e4.md) → [`006b77e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b77e4.md) FUN_006b77e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md)
- 新版 呼出元 1件 [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.21% / 新版 96.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b7a20",
      "incomplete_value": true,
      "site": "006b7a20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7a20",
      "incomplete_value": true,
      "site": "006b7a20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:16c:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006b7954",
      "incomplete_value": false,
      "site": "006b7968",
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
      "definition_site": "006b7954",
      "incomplete_value": false,
      "site": "006b7968",
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006b7c80",
      "incomplete_value": true,
      "site": "006b7c84",
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
      "definition_site": "006b7c80",
      "incomplete_value": true,
      "site": "006b7c84",
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
    "ordinal": 42,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b7898",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006b7954",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "006b7a08",
      "READ",
      [
        "storage",
        "0029916c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b7898",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006b7954",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "006b7a08",
      "READ",
      [
        "storage",
        "002990df",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b7/006b77e4.md#insn-006b7894) · [`006b7954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b7/006b77e4.md#insn-006b7954) · [`006b7a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b7/006b77e4.md#insn-006b7a04)
- 新版 [`006b7894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b77e4.md#insn-006b7894) · [`006b7954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b77e4.md#insn-006b7954) · [`006b7a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b77e4.md#insn-006b7a04)

~~~diff
- 006b7894 ["COPY", "tmp:0:8", ["const:38:8"]]
- 006b7894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b7894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b7894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b7894 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006b7894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b7894 bytes 08e10091
+ 006b7894 bytes 08e10191
- 006b7954 ["COPY", "tmp:0:8", ["const:0:8"]]
- 006b7954 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006b7954 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006b7954 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006b7954 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 006b7954 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006b7954 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006b7954 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006b7954 bytes 00000091
+ 006b7954 bytes 00000191
- 006b7a04 ["COPY", "tmp:0:8", ["const:16c:8"]]
- 006b7a04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006b7a04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006b7a04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006b7a04 ["COPY", "tmp:0:8", ["const:df:8"]]
+ 006b7a04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006b7a04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006b7a04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006b7a04 bytes 29b10591
+ 006b7a04 bytes 297d0391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6f113806696fedfb9bb6f0cb4dc0bce"></a>

### [`006b8bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8bf4.md) → [`006b8bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8bf4.md) FUN_006b8bf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b8e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8e78.md) · 呼出先 11件 [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ac4.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`006b8e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8e78.md) · 呼出先 11件 [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ac4.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006b8c30",
      "incomplete_value": false,
      "site": "006b8c3c",
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
      "definition_site": "006b8c30",
      "incomplete_value": false,
      "site": "006b8c3c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b8c34",
      "incomplete_value": true,
      "site": "006b8c48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b94:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b8c34",
      "incomplete_value": true,
      "site": "006b8c48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c21:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b8d88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b8c34",
      "READ",
      [
        "storage",
        "00292c21",
        null,
        "string"
      ]
    ],
    [
      "006b8c3c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006b8d78",
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
      "006b8c34",
      "READ",
      [
        "storage",
        "00292b94",
        null,
        "string"
      ]
    ],
    [
      "006b8c3c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006b8d78",
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

- 旧版 [`006b8d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8bf4.md#insn-006b8d88) · [`006b8d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8bf4.md#insn-006b8d8c)
- 新版 [`006b8d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8bf4.md#insn-006b8d88)

~~~diff
- 006b8d88 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 006b8d88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b8d88 bytes e81300f9
+ 006b8d88 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
+ 006b8d88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006b8d88 bytes e81300f9
- 006b8d8c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:68:8"]]
- 006b8d8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006b8d8c bytes e93700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcf1d20e2610ee917d6c504612e5abf6"></a>

### [`006b8e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8e78.md) → [`006b8e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8e78.md) FUN_006b8e78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)
- 新版 呼出元 1件 [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.53% / 新版 93.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b9060",
      "incomplete_value": true,
      "site": "006b9060",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b9060",
      "incomplete_value": true,
      "site": "006b9060",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:16c:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006b92a0",
      "incomplete_value": false,
      "site": "006b92a0",
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
      "definition_site": "006b92a0",
      "incomplete_value": false,
      "site": "006b92a0",
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
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006b92a4",
      "incomplete_value": false,
      "site": "006b92a4",
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
      "definition_site": "006b92a4",
      "incomplete_value": false,
      "site": "006b92a4",
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
    "ordinal": 30,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b8ecc",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006b8f94",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "006b9048",
      "READ",
      [
        "storage",
        "0029916c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b8ecc",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006b8f94",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "006b9048",
      "READ",
      [
        "storage",
        "002990df",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8e78.md#insn-006b8ec4) · [`006b8f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8e78.md#insn-006b8f94) · [`006b9044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8e78.md#insn-006b9044)
- 新版 [`006b8ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8e78.md#insn-006b8ec4) · [`006b8f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8e78.md#insn-006b8f94) · [`006b9044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8e78.md#insn-006b9044)

~~~diff
- 006b8ec4 ["COPY", "tmp:0:8", ["const:38:8"]]
- 006b8ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b8ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b8ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b8ec4 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006b8ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b8ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b8ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b8ec4 bytes 08e10091
+ 006b8ec4 bytes 08e10191
- 006b8f94 ["COPY", "tmp:0:8", ["const:0:8"]]
- 006b8f94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006b8f94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006b8f94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006b8f94 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 006b8f94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006b8f94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006b8f94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006b8f94 bytes 00000091
+ 006b8f94 bytes 00000191
- 006b9044 ["COPY", "tmp:0:8", ["const:16c:8"]]
- 006b9044 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006b9044 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006b9044 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006b9044 ["COPY", "tmp:0:8", ["const:df:8"]]
+ 006b9044 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006b9044 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006b9044 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006b9044 bytes 29b10591
+ 006b9044 bytes 297d0391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3adcfe3b6ee1ad500abff19dbbd483e1"></a>

### [`006ba518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba518.md) → [`006ba518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006ba518.md) FUN_006ba518

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006bbf6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006bbf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bbf6c.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.57% / 新版 90.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ba58c",
      "incomplete_value": true,
      "site": "006ba58c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ba58c",
      "incomplete_value": true,
      "site": "006ba58c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d3a:8"
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
      "definition_site": "006ba584",
      "incomplete_value": true,
      "site": "006ba590",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006ba584",
      "incomplete_value": true,
      "site": "006ba590",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ba580",
      "READ",
      [
        "storage",
        "002aed3a",
        null,
        "string"
      ]
    ],
    [
      "006ba584",
      "READ",
      [
        "storage",
        "002aed41",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006ba580",
      "READ",
      [
        "storage",
        "002aeca6",
        null,
        "string"
      ]
    ],
    [
      "006ba584",
      "READ",
      [
        "storage",
        "002aecad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ba578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba518.md#insn-006ba578)
- 新版 [`006ba578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006ba518.md#insn-006ba578)

~~~diff
- 006ba578 ["COPY", "tmp:0:8", ["const:d3a:8"]]
- 006ba578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ba578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ba578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ba578 ["COPY", "tmp:0:8", ["const:ca6:8"]]
+ 006ba578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ba578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ba578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ba578 bytes 29e93491
+ 006ba578 bytes 29993291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2a24f776f05b432f1d525b2bed52cb1"></a>

### [`006ba6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba6e4.md) → [`006ba6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006ba6e4.md) FUN_006ba6e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006baf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md) [`006bbf6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`006baf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006baf70.md) [`006bbf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bbf6c.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.58% / 新版 85.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 14件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ba7c8",
      "incomplete_value": true,
      "site": "006ba7d4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:7d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ba7c8",
      "incomplete_value": true,
      "site": "006ba7d4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:7f:8"
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
      "definition_site": "006ba7d8",
      "incomplete_value": true,
      "site": "006ba7d8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006ba7d8",
      "incomplete_value": true,
      "site": "006ba7d8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ba828",
      "incomplete_value": true,
      "site": "006ba838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6be:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ba828",
      "incomplete_value": true,
      "site": "006ba838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:633:8"
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
      "006ba7a4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006ba7c8",
      "READ",
      [
        "storage",
        "0029a07f",
        null,
        "string"
      ]
    ],
    [
      "006ba7cc",
      "READ",
      [
        "storage",
        "0029a08e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006ba7a4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006ba7c8",
      "READ",
      [
        "storage",
        "0029a07d",
        null,
        "string"
      ]
    ],
    [
      "006ba7cc",
      "READ",
      [
        "storage",
        "0029a08c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ba7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba6e4.md#insn-006ba7a0) · [`006ba7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba6e4.md#insn-006ba7bc) · [`006ba824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba6e4.md#insn-006ba824)
- 新版 [`006ba7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006ba6e4.md#insn-006ba7a0) · [`006ba7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006ba6e4.md#insn-006ba7bc) · [`006ba824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006ba6e4.md#insn-006ba824)

~~~diff
- 006ba7a0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 006ba7a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ba7a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ba7a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ba7a0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006ba7a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ba7a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ba7a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ba7a0 bytes 08e10091
+ 006ba7a0 bytes 08e10191
- 006ba7bc ["COPY", "tmp:0:8", ["const:7f:8"]]
- 006ba7bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ba7bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ba7bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ba7bc ["COPY", "tmp:0:8", ["const:7d:8"]]
+ 006ba7bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ba7bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ba7bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ba7bc bytes 08fd0191
+ 006ba7bc bytes 08f50191
- 006ba824 ["COPY", "tmp:0:8", ["const:633:8"]]
- 006ba824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ba824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ba824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ba824 ["COPY", "tmp:0:8", ["const:6be:8"]]
+ 006ba824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ba824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ba824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ba824 bytes 08cd1891
+ 006ba824 bytes 08f91a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-999f4d6c0c9b47264db3104425ee4d97"></a>

### [`006baf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md) → [`006baf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006baf70.md) FUN_006baf70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0068c0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c0a8.md) [`0069a970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a970.md) [`0069a9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a9cc.md) [`0069ab88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069ab88.md)
- 新版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0068c0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c0a8.md) [`0069a970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069a970.md) [`0069a9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069a9cc.md) [`0069ab88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069ab88.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.97% / 新版 98.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006bb4e0",
      "incomplete_value": false,
      "site": "006bb4e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb4e0",
      "incomplete_value": false,
      "site": "006bb4e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006bafb4",
      "incomplete_value": true,
      "site": "006bafb4",
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
      "definition_site": "006bafb4",
      "incomplete_value": true,
      "site": "006bafb4",
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
      "006bafb0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bafbc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bafc4",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bafb0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bafbc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bafc4",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md#insn-006bafb0) · [`006bafbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md#insn-006bafbc) · [`006bafc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md#insn-006bafc4)
- 新版 [`006bafb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006baf70.md#insn-006bafb0) · [`006bafbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006baf70.md#insn-006bafbc) · [`006bafc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006baf70.md#insn-006bafc4)

~~~diff
- 006bafb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006bafb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bafb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006bafb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006bafb0 bytes 083d45f9
+ 006bafb0 bytes 085d45f9
- 006bafbc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006bafbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bafbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bafbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bafbc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006bafbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bafbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bafbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bafbc bytes 21203991
+ 006bafbc bytes 21603a91
- 006bafc4 ["COPY", "tmp:0:8", ["const:298:8"]]
- 006bafc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bafc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bafc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bafc4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006bafc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bafc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bafc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bafc4 bytes 42600a91
+ 006bafc4 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-674e4a9074ea91a0a87c65e97bc63057"></a>

### [`006bbf6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md) → [`006bbf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bbf6c.md) FUN_006bbf6c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 59件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 59件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 13件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006bc844",
      "incomplete_value": false,
      "site": "006bc844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bc844",
      "incomplete_value": false,
      "site": "006bc844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006bc918",
      "incomplete_value": false,
      "site": "006bc918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bc918",
      "incomplete_value": false,
      "site": "006bc918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "006bca78",
      "incomplete_value": false,
      "site": "006bca80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bca78",
      "incomplete_value": false,
      "site": "006bca80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "006bbfa8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bbfb4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bbfbc",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bbfa8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bbfb4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bbfbc",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bbfa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md#insn-006bbfa8) · [`006bbfb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md#insn-006bbfb4) · [`006bbfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md#insn-006bbfbc)
- 新版 [`006bbfa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bbf6c.md#insn-006bbfa8) · [`006bbfb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bbf6c.md#insn-006bbfb4) · [`006bbfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bbf6c.md#insn-006bbfbc)

~~~diff
- 006bbfa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006bbfa8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bbfa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006bbfa8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006bbfa8 bytes 003d45f9
+ 006bbfa8 bytes 005d45f9
- 006bbfb4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006bbfb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bbfb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bbfb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bbfb4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006bbfb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bbfb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bbfb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bbfb4 bytes 21203991
+ 006bbfb4 bytes 21603a91
- 006bbfbc ["COPY", "tmp:0:8", ["const:298:8"]]
- 006bbfbc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bbfbc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bbfbc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bbfbc ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006bbfbc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bbfbc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bbfbc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bbfbc bytes 42600a91
+ 006bbfbc bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7bf49f1b0ab5956dce7db3f50290de1"></a>

### [`006bdb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bdb8c.md) → [`006bdb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bd/006bdb8c.md) FUN_006bdb8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006cec14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md) · 呼出先 12件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md)
- 新版 呼出元 1件 [`006cec14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md) · 呼出先 12件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006bdbbc",
      "incomplete_value": true,
      "site": "006bdbbc",
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
      "definition_site": "006bdbbc",
      "incomplete_value": true,
      "site": "006bdbbc",
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
      "definition_site": "006bdbc4",
      "incomplete_value": false,
      "site": "006bdbd4",
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
      "definition_site": "006bdbc4",
      "incomplete_value": false,
      "site": "006bdbd4",
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
      "definition_site": "006bdbcc",
      "incomplete_value": false,
      "site": "006bdbd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bdbcc",
      "incomplete_value": false,
      "site": "006bdbd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "006bdbb8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bdbc4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bdbcc",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bdbb8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bdbc4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bdbcc",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bdbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bdb8c.md#insn-006bdbb8) · [`006bdbc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bdb8c.md#insn-006bdbc4) · [`006bdbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bdb8c.md#insn-006bdbcc)
- 新版 [`006bdbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bd/006bdb8c.md#insn-006bdbb8) · [`006bdbc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bd/006bdb8c.md#insn-006bdbc4) · [`006bdbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bd/006bdb8c.md#insn-006bdbcc)

~~~diff
- 006bdbb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006bdbb8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bdbb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006bdbb8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006bdbb8 bytes 003d45f9
+ 006bdbb8 bytes 005d45f9
- 006bdbc4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006bdbc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bdbc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bdbc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bdbc4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006bdbc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bdbc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bdbc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bdbc4 bytes 21203991
+ 006bdbc4 bytes 21603a91
- 006bdbcc ["COPY", "tmp:0:8", ["const:298:8"]]
- 006bdbcc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bdbcc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bdbcc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bdbcc ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006bdbcc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bdbcc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bdbcc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bdbcc bytes 42600a91
+ 006bdbcc bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-407518d2145b877ff6a51b0b58e442c6"></a>

### [`006bde3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bde3c.md) → [`006bde3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bd/006bde3c.md) FUN_006bde3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006bdb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bdb8c.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md) [`00448040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448040.md)
- 新版 呼出元 1件 [`006bdb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bd/006bdb8c.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00447378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447378.md) [`00448040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.79% / 新版 99.79%

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
      "definition_site": "006bde90",
      "incomplete_value": true,
      "site": "006bde90",
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
      "definition_site": "006bde90",
      "incomplete_value": true,
      "site": "006bde90",
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
      "definition_site": "006bde98",
      "incomplete_value": false,
      "site": "006bdeac",
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
      "definition_site": "006bde98",
      "incomplete_value": false,
      "site": "006bdeac",
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
      "definition_site": "006bdea0",
      "incomplete_value": false,
      "site": "006bdeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bdea0",
      "incomplete_value": false,
      "site": "006bdeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "006bde8c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bde98",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bdea0",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bde8c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bde98",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bdea0",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bde8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bde3c.md#insn-006bde8c) · [`006bde98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bde3c.md#insn-006bde98) · [`006bdea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bde3c.md#insn-006bdea0)
- 新版 [`006bde8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bd/006bde3c.md#insn-006bde8c) · [`006bde98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bd/006bde3c.md#insn-006bde98) · [`006bdea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bd/006bde3c.md#insn-006bdea0)

~~~diff
- 006bde8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006bde8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bde8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006bde8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006bde8c bytes 083d45f9
+ 006bde8c bytes 085d45f9
- 006bde98 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006bde98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bde98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bde98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bde98 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006bde98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bde98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bde98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bde98 bytes 21203991
+ 006bde98 bytes 21603a91
- 006bdea0 ["COPY", "tmp:0:8", ["const:298:8"]]
- 006bdea0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bdea0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bdea0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bdea0 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006bdea0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bdea0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bdea0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bdea0 bytes 42600a91
+ 006bdea0 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f68ddab5d0847cd6170b3b75cc85e4ba"></a>

### [`006bee18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006be/006bee18.md) → [`006bee18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006be/006bee18.md) FUN_006bee18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) · 呼出先 19件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 19件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.93% / 新版 90.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 14件, `store_value` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bf180",
      "incomplete_value": true,
      "site": "006bf194",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6be:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bf180",
      "incomplete_value": true,
      "site": "006bf194",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:633:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bf1dc",
      "incomplete_value": true,
      "site": "006bf1ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:797:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bf1dc",
      "incomplete_value": true,
      "site": "006bf1ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:70c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 51,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006bf448",
      "incomplete_value": false,
      "site": "006bf448",
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
      "definition_site": "006bf448",
      "incomplete_value": false,
      "site": "006bf448",
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
    "ordinal": 62,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006bee54",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bee60",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bee68",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bee54",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bee60",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bee68",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bee54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006be/006bee18.md#insn-006bee54) · [`006bee60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006be/006bee18.md#insn-006bee60) · [`006bee68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006be/006bee18.md#insn-006bee68)
- 新版 [`006bee54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006be/006bee18.md#insn-006bee54) · [`006bee60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006be/006bee18.md#insn-006bee60) · [`006bee68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006be/006bee18.md#insn-006bee68)

~~~diff
- 006bee54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006bee54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bee54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006bee54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006bee54 bytes 083d45f9
+ 006bee54 bytes 085d45f9
- 006bee60 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006bee60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bee60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bee60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bee60 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006bee60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bee60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bee60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bee60 bytes 21203991
+ 006bee60 bytes 21603a91
- 006bee68 ["COPY", "tmp:0:8", ["const:298:8"]]
- 006bee68 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bee68 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bee68 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bee68 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006bee68 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bee68 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bee68 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bee68 bytes 42600a91
+ 006bee68 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67c61fcb89f9f2fa3b4d0e95230b0bbb"></a>

### [`006bf5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bf/006bf5a0.md) → [`006bf5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bf/006bf5a0.md) FUN_006bf5a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md)
- 新版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.78% / 新版 98.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006bf5d4",
      "incomplete_value": true,
      "site": "006bf5d4",
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
      "definition_site": "006bf5d4",
      "incomplete_value": true,
      "site": "006bf5d4",
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
      "definition_site": "006bf5dc",
      "incomplete_value": false,
      "site": "006bf5f0",
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
      "definition_site": "006bf5dc",
      "incomplete_value": false,
      "site": "006bf5f0",
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
      "definition_site": "006bf5e4",
      "incomplete_value": false,
      "site": "006bf5f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bf5e4",
      "incomplete_value": false,
      "site": "006bf5f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "006bf5d0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bf5dc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bf5e4",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bf5d0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bf5dc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bf5e4",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bf5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bf/006bf5a0.md#insn-006bf5d0) · [`006bf5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bf/006bf5a0.md#insn-006bf5dc) · [`006bf5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bf/006bf5a0.md#insn-006bf5e4)
- 新版 [`006bf5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bf/006bf5a0.md#insn-006bf5d0) · [`006bf5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bf/006bf5a0.md#insn-006bf5dc) · [`006bf5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bf/006bf5a0.md#insn-006bf5e4)

~~~diff
- 006bf5d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006bf5d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bf5d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006bf5d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006bf5d0 bytes 083d45f9
+ 006bf5d0 bytes 085d45f9
- 006bf5dc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006bf5dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bf5dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bf5dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bf5dc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006bf5dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bf5dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bf5dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bf5dc bytes 21203991
+ 006bf5dc bytes 21603a91
- 006bf5e4 ["COPY", "tmp:0:8", ["const:298:8"]]
- 006bf5e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bf5e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bf5e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bf5e4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006bf5e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bf5e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bf5e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bf5e4 bytes 42600a91
+ 006bf5e4 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aff6b12a6ca71e94f03f92d9da6f4f8c"></a>

### [`006c0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0060.md) → [`006c0060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0060.md) FUN_006c0060

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006cec14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md) · 呼出先 13件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md)
- 新版 呼出元 1件 [`006cec14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md) · 呼出先 13件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.29% / 新版 99.29%

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
      "definition_site": "006c00a0",
      "incomplete_value": true,
      "site": "006c00a0",
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
      "definition_site": "006c00a0",
      "incomplete_value": true,
      "site": "006c00a0",
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
      "definition_site": "006c00a8",
      "incomplete_value": false,
      "site": "006c00bc",
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
      "definition_site": "006c00a8",
      "incomplete_value": false,
      "site": "006c00bc",
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
      "definition_site": "006c00b0",
      "incomplete_value": false,
      "site": "006c00bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c00b0",
      "incomplete_value": false,
      "site": "006c00bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "006c009c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006c00a8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c00b0",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006c009c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006c00a8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c00b0",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c009c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0060.md#insn-006c009c) · [`006c00a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0060.md#insn-006c00a8) · [`006c00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0060.md#insn-006c00b0)
- 新版 [`006c009c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0060.md#insn-006c009c) · [`006c00a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0060.md#insn-006c00a8) · [`006c00b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0060.md#insn-006c00b0)

~~~diff
- 006c009c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006c009c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c009c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006c009c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006c009c bytes 083d45f9
+ 006c009c bytes 085d45f9
- 006c00a8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006c00a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c00a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c00a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c00a8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006c00a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c00a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c00a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c00a8 bytes 21203991
+ 006c00a8 bytes 21603a91
- 006c00b0 ["COPY", "tmp:0:8", ["const:298:8"]]
- 006c00b0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006c00b0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006c00b0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006c00b0 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006c00b0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006c00b0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006c00b0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006c00b0 bytes 42600a91
+ 006c00b0 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3abe9f118b4456ab0647f97737f7eab6"></a>

### [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) → [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) FUN_006c0784

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 8件 [`0068d810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d810.md) [`006c077c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c077c.md) [`006c7884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md) [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) [`006d1b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1b1c.md) · 呼出先 52件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 8件 [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) [`006c077c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c077c.md) [`006c7884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c7884.md) [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`006d1b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1b1c.md) · 呼出先 52件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.33% / 新版 94.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 50件, `store_destination` 35件, `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c0da8",
      "incomplete_value": true,
      "site": "006c0db8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:74f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c0da8",
      "incomplete_value": true,
      "site": "006c0db8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c4:8"
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
      "definition_site": "006c0dbc",
      "incomplete_value": true,
      "site": "006c0dbc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006c0dbc",
      "incomplete_value": true,
      "site": "006c0dbc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 61,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006c2540",
      "incomplete_value": false,
      "site": "006c2540",
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
      "definition_site": "006c2540",
      "incomplete_value": false,
      "site": "006c2540",
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
    "ordinal": 195,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c0958",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006c09cc",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "006c0ac8",
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
      "006c0958",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006c09cc",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "006c0ac8",
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

- 旧版 [`006c0954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md#insn-006c0954) · [`006c09cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md#insn-006c09cc) · [`006c0ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md#insn-006c0ac4)
- 新版 [`006c0954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md#insn-006c0954) · [`006c09cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md#insn-006c09cc) · [`006c0ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md#insn-006c0ac4)

~~~diff
- 006c0954 ["COPY", "tmp:0:8", ["const:38:8"]]
- 006c0954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c0954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c0954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c0954 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006c0954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c0954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c0954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c0954 bytes 08e10091
+ 006c0954 bytes 08e10191
- 006c09cc ["COPY", "tmp:0:8", ["const:0:8"]]
- 006c09cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006c09cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006c09cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006c09cc ["COPY", "tmp:0:8", ["const:40:8"]]
+ 006c09cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006c09cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006c09cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006c09cc bytes 00000091
+ 006c09cc bytes 00000191
- 006c0ac4 ["COPY", "tmp:0:8", ["const:38:8"]]
- 006c0ac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c0ac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c0ac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c0ac4 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006c0ac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c0ac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c0ac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c0ac4 bytes 08e10091
+ 006c0ac4 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25e53ef5912bcf403c9250dccc58ae0d"></a>

### [`006c2f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c2/006c2f8c.md) → [`006c2f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c2/006c2f8c.md) FUN_006c2f8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00605f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/00605f28.md) [`006f4c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f4c58.md)
- 新版 呼出元 2件 [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00605f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/00605f28.md) [`006f4c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4c58.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.05% / 新版 98.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c34f8",
      "incomplete_value": true,
      "site": "006c34f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c34f8",
      "incomplete_value": true,
      "site": "006c34f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e2:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c34fc",
      "incomplete_value": true,
      "site": "006c34fc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006c34fc",
      "incomplete_value": true,
      "site": "006c34fc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 66,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c304c",
      "incomplete_value": false,
      "site": "006c3054",
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
            "const:3cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c304c",
      "incomplete_value": false,
      "site": "006c3054",
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
            "const:342:8"
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
      "006c304c",
      "PARAM",
      [
        "storage",
        "002a0342",
        null,
        null
      ]
    ],
    [
      "006c30e8",
      "PARAM",
      [
        "storage",
        "0029196e",
        null,
        null
      ]
    ],
    [
      "006c31c0",
      "PARAM",
      [
        "storage",
        "002a0342",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006c304c",
      "PARAM",
      [
        "storage",
        "002a03cd",
        null,
        null
      ]
    ],
    [
      "006c30e8",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        null
      ]
    ],
    [
      "006c31c0",
      "PARAM",
      [
        "storage",
        "002a03cd",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c304c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c2/006c2f8c.md#insn-006c304c) · [`006c30e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c2/006c2f8c.md#insn-006c30e8) · [`006c31c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c2/006c2f8c.md#insn-006c31c0)
- 新版 [`006c304c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c2/006c2f8c.md#insn-006c304c) · [`006c30e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c2/006c2f8c.md#insn-006c30e8) · [`006c31c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c2/006c2f8c.md#insn-006c31c0)

~~~diff
- 006c304c ["COPY", "tmp:0:8", ["const:342:8"]]
- 006c304c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c304c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c304c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c304c ["COPY", "tmp:0:8", ["const:3cd:8"]]
+ 006c304c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c304c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c304c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c304c bytes 21080d91
+ 006c304c bytes 21340f91
- 006c30e8 ["COPY", "tmp:0:8", ["const:96e:8"]]
- 006c30e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c30e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c30e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c30e8 ["COPY", "tmp:0:8", ["const:8e1:8"]]
+ 006c30e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c30e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c30e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c30e8 bytes 21b82591
+ 006c30e8 bytes 21842391
- 006c31c0 ["COPY", "tmp:0:8", ["const:342:8"]]
- 006c31c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c31c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c31c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c31c0 ["COPY", "tmp:0:8", ["const:3cd:8"]]
+ 006c31c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c31c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c31c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c31c0 bytes 21080d91
+ 006c31c0 bytes 21340f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b45fdc5ab7283a1a4a6dc5af8bb431b1"></a>

### [`006c3fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c3/006c3fe0.md) → [`006c3fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c3/006c3fe0.md) FUN_006c3fe0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) [`006d1400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1400.md) [`006d3c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c38.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0069ab88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069ab88.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`006d1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1400.md) [`006d3c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c38.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0069ab88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069ab88.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c48c4",
      "incomplete_value": false,
      "site": "006c48e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c48c4",
      "incomplete_value": false,
      "site": "006c48e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c48e8",
      "incomplete_value": false,
      "site": "006c48ec",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c48e8",
      "incomplete_value": false,
      "site": "006c48ec",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c4740",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006c4784",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "006c4788",
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
      "006c4740",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006c4784",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "006c4788",
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

- 旧版 [`006c473c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c3/006c3fe0.md#insn-006c473c) · [`006c4784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c3/006c3fe0.md#insn-006c4784) · [`006c4788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c3/006c3fe0.md#insn-006c4788)
- 新版 [`006c473c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c3/006c3fe0.md#insn-006c473c) · [`006c4784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c3/006c3fe0.md#insn-006c4784) · [`006c4788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c3/006c3fe0.md#insn-006c4788)

~~~diff
- 006c473c ["COPY", "tmp:0:8", ["const:38:8"]]
- 006c473c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c473c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c473c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c473c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006c473c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c473c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c473c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c473c bytes 08e10091
+ 006c473c bytes 08e10191
- 006c4784 ["COPY", "tmp:0:8", ["const:0:8"]]
- 006c4784 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006c4784 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006c4784 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006c4784 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 006c4784 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006c4784 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006c4784 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006c4784 bytes 00000091
+ 006c4784 bytes 00000191
- 006c4788 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 006c4788 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c4788 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 006c4788 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 006c4788 bytes 423047f9
+ 006c4788 bytes 425847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b003d666ed9612ee3ca9149620ffb19"></a>

### [`006c4ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c4/006c4ea8.md) → [`006c4ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c4/006c4ea8.md) FUN_006c4ea8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 18件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`006b1fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b1fac.md) [`006ba5ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba5ec.md) [`006bacc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006bacc8.md)
- 新版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 18件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`006b1fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1fac.md) [`006ba5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006ba5ec.md) [`006bacc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006bacc8.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c52ac",
      "incomplete_value": false,
      "site": "006c52b4",
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
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c52ac",
      "incomplete_value": false,
      "site": "006c52b4",
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
            "const:e12:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c52f4",
      "incomplete_value": false,
      "site": "006c52fc",
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
            "const:7cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c52f4",
      "incomplete_value": false,
      "site": "006c52fc",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c54ac",
      "incomplete_value": false,
      "site": "006c54b4",
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
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c54ac",
      "incomplete_value": false,
      "site": "006c54b4",
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
            "const:e12:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c4fcc",
      "DATA",
      [
        "storage",
        "00c23f98",
        null,
        null
      ]
    ],
    [
      "006c5270",
      "DATA",
      [
        "storage",
        "00c23f88",
        null,
        null
      ]
    ],
    [
      "006c52b4",
      "DATA",
      [
        "storage",
        "00297e12",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006c4fcc",
      "DATA",
      [
        "storage",
        "00c23fe8",
        null,
        null
      ]
    ],
    [
      "006c5270",
      "DATA",
      [
        "storage",
        "00c23fd8",
        null,
        null
      ]
    ],
    [
      "006c52b4",
      "DATA",
      [
        "storage",
        "00297d85",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c4fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c4/006c4ea8.md#insn-006c4fc0) · [`006c5260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c4/006c4ea8.md#insn-006c5260) · [`006c5264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c4/006c4ea8.md#insn-006c5264)
- 新版 [`006c4fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c4/006c4ea8.md#insn-006c4fc0) · [`006c5260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c4/006c4ea8.md#insn-006c5260) · [`006c5264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c4/006c4ea8.md#insn-006c5264)

~~~diff
- 006c4fc0 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 006c4fc0 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
- 006c4fc0 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
- 006c4fc0 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
+ 006c4fc0 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 006c4fc0 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
+ 006c4fc0 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
+ 006c4fc0 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
- 006c4fc0 bytes 7b633e91
+ 006c4fc0 bytes 7ba33f91
- 006c5260 ["COPY", "register:4048:8", ["const:c23000:8"]]
+ 006c5260 ["COPY", "register:4048:8", ["const:c24000:8"]]
- 006c5260 bytes e92a00d0
+ 006c5260 bytes e92a00f0
- 006c5264 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 006c5264 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006c5264 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006c5264 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006c5264 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 006c5264 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006c5264 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006c5264 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006c5264 bytes 29c13e91
+ 006c5264 bytes 29010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3ffa04d750fe8017e792eab64bb85cc"></a>

### [`006c5940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c5/006c5940.md) → [`006c5940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c5/006c5940.md) FUN_006c5940

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006d4810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4810.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md)
- 新版 呼出元 1件 [`006d4810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4810.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a83e4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.90% / 新版 92.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c59d4",
      "incomplete_value": true,
      "site": "006c59e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c59d4",
      "incomplete_value": true,
      "site": "006c59e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:751:8"
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
      "definition_site": "006c59ec",
      "incomplete_value": true,
      "site": "006c59ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006c59ec",
      "incomplete_value": true,
      "site": "006c59ec",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c5a00",
      "incomplete_value": false,
      "site": "006c5a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c5a00",
      "incomplete_value": false,
      "site": "006c5a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "006c59d4",
      "READ",
      [
        "storage",
        "0029e751",
        null,
        "string"
      ]
    ],
    [
      "006c59dc",
      "READ",
      [
        "storage",
        "0029e75e",
        null,
        "string"
      ]
    ],
    [
      "006c5a08",
      "DATA",
      [
        "storage",
        "00bf9720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006c59d4",
      "READ",
      [
        "storage",
        "0029e7dc",
        null,
        "string"
      ]
    ],
    [
      "006c59dc",
      "READ",
      [
        "storage",
        "0029e7e9",
        null,
        "string"
      ]
    ],
    [
      "006c5a08",
      "DATA",
      [
        "storage",
        "00bf9770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c59d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c5/006c5940.md#insn-006c59d0) · [`006c5a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c5/006c5940.md#insn-006c5a00) · [`006c5a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c5/006c5940.md#insn-006c5a7c)
- 新版 [`006c59d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c5/006c5940.md#insn-006c59d0) · [`006c5a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c5/006c5940.md#insn-006c5a00) · [`006c5a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c5/006c5940.md#insn-006c5a7c)

~~~diff
- 006c59d0 ["COPY", "tmp:0:8", ["const:751:8"]]
- 006c59d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006c59d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006c59d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006c59d0 ["COPY", "tmp:0:8", ["const:7dc:8"]]
+ 006c59d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006c59d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006c59d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006c59d0 bytes 29451d91
+ 006c59d0 bytes 29711f91
- 006c5a00 ["COPY", "tmp:0:8", ["const:720:8"]]
- 006c5a00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c5a00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c5a00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c5a00 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 006c5a00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c5a00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c5a00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c5a00 bytes 08811c91
+ 006c5a00 bytes 08c11d91
- 006c5a7c ["COPY", "tmp:0:8", ["const:d88:8"]]
- 006c5a7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006c5a7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006c5a7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006c5a7c ["COPY", "tmp:0:8", ["const:cfb:8"]]
+ 006c5a7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006c5a7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006c5a7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006c5a7c bytes 29213691
+ 006c5a7c bytes 29ed3391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01af55a15e38dc8a9586429077df0e91"></a>

### [`006c6850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c6/006c6850.md) → [`006c6850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6850.md) FUN_006c6850

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c7884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md) · 呼出先 23件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md)
- 新版 呼出元 1件 [`006c7884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c7884.md) · 呼出先 23件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.46% / 新版 95.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 13件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c68e0",
      "incomplete_value": true,
      "site": "006c68ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7a9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c68e0",
      "incomplete_value": true,
      "site": "006c68ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:71e:8"
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
      "definition_site": "006c68e0",
      "incomplete_value": true,
      "site": "006c68ec",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006c68e0",
      "incomplete_value": true,
      "site": "006c68ec",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006c6994",
      "incomplete_value": true,
      "site": "006c69a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ccc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c6994",
      "incomplete_value": true,
      "site": "006c69a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d60:8"
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
      "006c6888",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006c6894",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c689c",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006c6888",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006c6894",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c689c",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c6888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c6/006c6850.md#insn-006c6888) · [`006c6894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c6/006c6850.md#insn-006c6894) · [`006c689c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c6/006c6850.md#insn-006c689c)
- 新版 [`006c6888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6850.md#insn-006c6888) · [`006c6894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6850.md#insn-006c6894) · [`006c689c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6850.md#insn-006c689c)

~~~diff
- 006c6888 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006c6888 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c6888 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006c6888 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006c6888 bytes 083d45f9
+ 006c6888 bytes 085d45f9
- 006c6894 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006c6894 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c6894 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c6894 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c6894 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006c6894 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c6894 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c6894 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c6894 bytes 21203991
+ 006c6894 bytes 21603a91
- 006c689c ["COPY", "tmp:0:8", ["const:298:8"]]
- 006c689c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006c689c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006c689c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006c689c ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006c689c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006c689c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006c689c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006c689c bytes 42600a91
+ 006c689c bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f34cf8cd762c3604312c02fa1eb45903"></a>

### [`006c7884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md) → [`006c7884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c7884.md) FUN_006c7884

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0068c620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c620.md) · 呼出先 37件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d208.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0069a9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a9cc.md)
- 新版 呼出元 1件 [`0068c620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c620.md) · 呼出先 37件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d208.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0069a9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069a9cc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c7e80",
      "incomplete_value": false,
      "site": "006c7e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c7e80",
      "incomplete_value": false,
      "site": "006c7e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c8424",
      "incomplete_value": false,
      "site": "006c8424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c8424",
      "incomplete_value": false,
      "site": "006c8424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "ordinal": 144,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006c78cc",
      "incomplete_value": true,
      "site": "006c78cc",
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
      "definition_site": "006c78cc",
      "incomplete_value": true,
      "site": "006c78cc",
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
      "006c78c0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006c78d4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c78dc",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006c78c0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006c78d4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c78dc",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c78c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md#insn-006c78c0) · [`006c78d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md#insn-006c78d4) · [`006c78dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md#insn-006c78dc)
- 新版 [`006c78c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c7884.md#insn-006c78c0) · [`006c78d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c7884.md#insn-006c78d4) · [`006c78dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c7884.md#insn-006c78dc)

~~~diff
- 006c78c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006c78c0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c78c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006c78c0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006c78c0 bytes 003d45f9
+ 006c78c0 bytes 005d45f9
- 006c78d4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006c78d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c78d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c78d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c78d4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006c78d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c78d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c78d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c78d4 bytes 21203991
+ 006c78d4 bytes 21603a91
- 006c78dc ["COPY", "tmp:0:8", ["const:298:8"]]
- 006c78dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006c78dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006c78dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006c78dc ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006c78dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006c78dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006c78dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006c78dc bytes 42600a91
+ 006c78dc bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00edf64e9907461733bc2edd3a3875ea"></a>

### [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) → [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) FUN_006c86d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068c7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c7d4.md) · 呼出先 141件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md)
- 新版 呼出元 1件 [`0068c7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c7d4.md) · 呼出先 141件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 49件, `store_value` 8件

アドレスに依存する影響 `branch_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c88f0",
      "incomplete_value": false,
      "site": "006c88f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c88f0",
      "incomplete_value": false,
      "site": "006c88f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "definition_site": "006c99ac",
      "incomplete_value": false,
      "site": "006c99ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c99ac",
      "incomplete_value": false,
      "site": "006c99ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "ordinal": 83,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006cb36c",
      "incomplete_value": false,
      "site": "006cb36c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006cb36c",
      "incomplete_value": false,
      "site": "006cb36c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "ordinal": 170,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c8764",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006c8770",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c8778",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006c8764",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006c8770",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c8778",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c8764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md#insn-006c8764) · [`006c8770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md#insn-006c8770) · [`006c8778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md#insn-006c8778)
- 新版 [`006c8764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md#insn-006c8764) · [`006c8770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md#insn-006c8770) · [`006c8778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md#insn-006c8778)

~~~diff
- 006c8764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006c8764 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c8764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006c8764 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006c8764 bytes 003d45f9
+ 006c8764 bytes 005d45f9
- 006c8770 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006c8770 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c8770 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c8770 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c8770 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006c8770 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c8770 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c8770 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c8770 bytes 21203991
+ 006c8770 bytes 21603a91
- 006c8778 ["COPY", "tmp:0:8", ["const:298:8"]]
- 006c8778 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006c8778 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006c8778 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006c8778 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006c8778 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006c8778 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006c8778 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006c8778 bytes 42600a91
+ 006c8778 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-251f0487150b50ee44aad33db218a817"></a>

### [`006cec14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md) → [`006cec14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md) FUN_006cec14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md) · 呼出先 30件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md)
- 新版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d0f8.md) · 呼出先 30件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.97% / 新版 97.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006cec60",
      "incomplete_value": true,
      "site": "006cec60",
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
      "definition_site": "006cec60",
      "incomplete_value": true,
      "site": "006cec60",
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
      "definition_site": "006cec68",
      "incomplete_value": false,
      "site": "006cec78",
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
      "definition_site": "006cec68",
      "incomplete_value": false,
      "site": "006cec78",
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
      "definition_site": "006cec70",
      "incomplete_value": false,
      "site": "006cec78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006cec70",
      "incomplete_value": false,
      "site": "006cec78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "006cec4c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006cec68",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006cec70",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006cec4c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006cec68",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006cec70",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006cec4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md#insn-006cec4c) · [`006cec68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md#insn-006cec68) · [`006cec70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md#insn-006cec70)
- 新版 [`006cec4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md#insn-006cec4c) · [`006cec68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md#insn-006cec68) · [`006cec70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md#insn-006cec70)

~~~diff
- 006cec4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006cec4c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006cec4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006cec4c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006cec4c bytes 003d45f9
+ 006cec4c bytes 005d45f9
- 006cec68 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006cec68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006cec68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006cec68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006cec68 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006cec68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006cec68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006cec68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006cec68 bytes 21203991
+ 006cec68 bytes 21603a91
- 006cec70 ["COPY", "tmp:0:8", ["const:298:8"]]
- 006cec70 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006cec70 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006cec70 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006cec70 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 006cec70 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006cec70 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006cec70 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006cec70 bytes 42600a91
+ 006cec70 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fb51f09404792d56ed9c6a4b1fcf79a"></a>

### [`006d00e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d00e4.md) → [`006d00e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d00e4.md) FUN_006d00e4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006b0db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0db0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006b0db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0db0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006d00f0",
      "incomplete_value": false,
      "site": "006d00f4",
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
      "definition_site": "006d00f0",
      "incomplete_value": false,
      "site": "006d00f4",
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
      "006d00f0",
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
      "006d00f0",
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

- 旧版 [`006d00f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d00e4.md#insn-006d00f0)
- 新版 [`006d00f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d00e4.md#insn-006d00f0)

~~~diff
- 006d00f0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 006d00f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006d00f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006d00f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006d00f0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006d00f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006d00f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006d00f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006d00f0 bytes 000c0c91
+ 006d00f0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f9eb47d08a1c57d16c55c97abf06279"></a>

### [`006d00fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d00fc.md) → [`006d00fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d00fc.md) FUN_006d00fc

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
      "definition_site": "006d0120",
      "incomplete_value": false,
      "site": "006d0120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d0120",
      "incomplete_value": false,
      "site": "006d0120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "006d0120",
      "DATA",
      [
        "storage",
        "00bf93a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d0120",
      "DATA",
      [
        "storage",
        "00bf93f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d011c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d00fc.md#insn-006d011c)
- 新版 [`006d011c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d00fc.md#insn-006d011c)

~~~diff
- 006d011c ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 006d011c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d011c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d011c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d011c ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 006d011c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d011c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d011c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d011c bytes 08810e91
+ 006d011c bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d4033b14cc74a50b258323556c19b73"></a>

### [`006d0130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d0130.md) → [`006d0130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d0130.md) FUN_006d0130

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
      "definition_site": "006d013c",
      "incomplete_value": false,
      "site": "006d013c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d013c",
      "incomplete_value": false,
      "site": "006d013c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "006d013c",
      "DATA",
      [
        "storage",
        "00bf93a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d013c",
      "DATA",
      [
        "storage",
        "00bf93f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d0130.md#insn-006d0138)
- 新版 [`006d0138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d0130.md#insn-006d0138)

~~~diff
- 006d0138 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 006d0138 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d0138 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d0138 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d0138 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 006d0138 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d0138 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d0138 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d0138 bytes 29810e91
+ 006d0138 bytes 29c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d79cc453aa8bf0276a8d9de899acee2"></a>

### [`006d01e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d01e8.md) → [`006d01e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d01e8.md) FUN_006d01e8

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
      "definition_site": "006d020c",
      "incomplete_value": false,
      "site": "006d020c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d020c",
      "incomplete_value": false,
      "site": "006d020c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "006d020c",
      "DATA",
      [
        "storage",
        "00bf9420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d020c",
      "DATA",
      [
        "storage",
        "00bf9470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d01e8.md#insn-006d0208)
- 新版 [`006d0208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d01e8.md#insn-006d0208)

~~~diff
- 006d0208 ["COPY", "tmp:0:8", ["const:420:8"]]
- 006d0208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d0208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d0208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d0208 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 006d0208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d0208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d0208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d0208 bytes 08811091
+ 006d0208 bytes 08c11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5315f7bcab2a33035908f4a4360b4ec"></a>

### [`006d021c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d021c.md) → [`006d021c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d021c.md) FUN_006d021c

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
      "definition_site": "006d0228",
      "incomplete_value": false,
      "site": "006d0228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d0228",
      "incomplete_value": false,
      "site": "006d0228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d0228",
      "DATA",
      [
        "storage",
        "00bf9420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d0228",
      "DATA",
      [
        "storage",
        "00bf9470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d021c.md#insn-006d0224)
- 新版 [`006d0224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d021c.md#insn-006d0224)

~~~diff
- 006d0224 ["COPY", "tmp:0:8", ["const:420:8"]]
- 006d0224 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d0224 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d0224 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d0224 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 006d0224 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d0224 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d0224 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d0224 bytes 29811091
+ 006d0224 bytes 29c11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a9f42f4cb2c72eea9bb51174a728509"></a>

### [`006d02ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d02ec.md) → [`006d02ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d02ec.md) FUN_006d02ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006b1d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b1d70.md) [`006b1fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b1fac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`006b1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1d70.md) [`006b1fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1fac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006d02f8",
      "incomplete_value": false,
      "site": "006d02fc",
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
      "definition_site": "006d02f8",
      "incomplete_value": false,
      "site": "006d02fc",
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
      "006d02f8",
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
      "006d02f8",
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

- 旧版 [`006d02f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d02ec.md#insn-006d02f8)
- 新版 [`006d02f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d02ec.md#insn-006d02f8)

~~~diff
- 006d02f8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 006d02f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006d02f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006d02f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006d02f8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006d02f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006d02f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006d02f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006d02f8 bytes 000c0c91
+ 006d02f8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-536122aa222913f6d98282f1c8840c8b"></a>

### [`006d12f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d12f4.md) → [`006d12f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d12f4.md) FUN_006d12f4

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
      "definition_site": "006d1308",
      "incomplete_value": false,
      "site": "006d130c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1308",
      "incomplete_value": false,
      "site": "006d130c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "006d130c",
      "DATA",
      [
        "storage",
        "00bf94a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d130c",
      "DATA",
      [
        "storage",
        "00bf94f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d12f4.md#insn-006d1308)
- 新版 [`006d1308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d12f4.md#insn-006d1308)

~~~diff
- 006d1308 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 006d1308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d1308 ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 006d1308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1308 bytes 08811291
+ 006d1308 bytes 08c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-961d3703961f3b94b57ce0e7cdca1858"></a>

### [`006d1318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1318.md) → [`006d1318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1318.md) FUN_006d1318

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
      "definition_site": "006d131c",
      "incomplete_value": false,
      "site": "006d1320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d131c",
      "incomplete_value": false,
      "site": "006d1320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "006d1320",
      "DATA",
      [
        "storage",
        "00bf94a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1320",
      "DATA",
      [
        "storage",
        "00bf94f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d131c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1318.md#insn-006d131c)
- 新版 [`006d131c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1318.md#insn-006d131c)

~~~diff
- 006d131c ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 006d131c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d131c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d131c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d131c ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 006d131c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d131c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d131c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d131c bytes 08811291
+ 006d131c bytes 08c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebc14e0b23f22d04fcda59e3d8a954c6"></a>

### [`006d1398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1398.md) → [`006d1398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1398.md) FUN_006d1398

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
      "definition_site": "006d13bc",
      "incomplete_value": false,
      "site": "006d13c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d13bc",
      "incomplete_value": false,
      "site": "006d13c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:520:8"
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
      "006d13c0",
      "DATA",
      [
        "storage",
        "00bf9520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d13c0",
      "DATA",
      [
        "storage",
        "00bf9570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d13bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1398.md#insn-006d13bc)
- 新版 [`006d13bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1398.md#insn-006d13bc)

~~~diff
- 006d13bc ["COPY", "tmp:0:8", ["const:520:8"]]
- 006d13bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d13bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d13bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d13bc ["COPY", "tmp:0:8", ["const:570:8"]]
+ 006d13bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d13bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d13bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d13bc bytes 08811491
+ 006d13bc bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-261c1c3e5a5782614b32363f2956c971"></a>

### [`006d13d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d13d8.md) → [`006d13d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d13d8.md) FUN_006d13d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006d13dc",
      "incomplete_value": false,
      "site": "006d13e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d13dc",
      "incomplete_value": false,
      "site": "006d13e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d13e0",
      "DATA",
      [
        "storage",
        "00bf9520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d13e0",
      "DATA",
      [
        "storage",
        "00bf9570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d13dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d13d8.md#insn-006d13dc)
- 新版 [`006d13dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d13d8.md#insn-006d13dc)

~~~diff
- 006d13dc ["COPY", "tmp:0:8", ["const:520:8"]]
- 006d13dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d13dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d13dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d13dc ["COPY", "tmp:0:8", ["const:570:8"]]
+ 006d13dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d13dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d13dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d13dc bytes 08811491
+ 006d13dc bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75349b29312f79c69d2db5cab25b735d"></a>

### [`006d1400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1400.md) → [`006d1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1400.md) FUN_006d1400

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d1524",
      "incomplete_value": true,
      "site": "006d1538",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1524",
      "incomplete_value": true,
      "site": "006d1538",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73a:8"
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
      "definition_site": "006d17b0",
      "incomplete_value": false,
      "site": "006d17b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d17b0",
      "incomplete_value": false,
      "site": "006d17b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:590:8"
          ]
        ]
      ]
    },
    "ordinal": 51,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006d1524",
      "READ",
      [
        "storage",
        "002a373a",
        null,
        "string"
      ]
    ],
    [
      "006d17b0",
      "DATA",
      [
        "storage",
        "00bf9590",
        null,
        "undefined *"
      ]
    ],
    [
      "006d1808",
      "READ",
      [
        "storage",
        "00bf95b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006d1524",
      "READ",
      [
        "storage",
        "002a37c5",
        null,
        "string"
      ]
    ],
    [
      "006d17b0",
      "DATA",
      [
        "storage",
        "00bf95e0",
        null,
        "undefined *"
      ]
    ],
    [
      "006d1808",
      "READ",
      [
        "storage",
        "00bf9600",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d151c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1400.md#insn-006d151c) · [`006d17a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1400.md#insn-006d17a0)
- 新版 [`006d151c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1400.md#insn-006d151c) · [`006d17a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1400.md#insn-006d17a0)

~~~diff
- 006d151c ["COPY", "tmp:0:8", ["const:73a:8"]]
- 006d151c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d151c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d151c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d151c ["COPY", "tmp:0:8", ["const:7c5:8"]]
+ 006d151c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d151c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d151c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d151c bytes 29e91c91
+ 006d151c bytes 29151f91
- 006d17a0 ["COPY", "tmp:0:8", ["const:590:8"]]
- 006d17a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d17a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d17a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d17a0 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 006d17a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d17a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d17a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d17a0 bytes 08411691
+ 006d17a0 bytes 08811791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b215d40dd1dac7719ad10e6949433b04"></a>

### [`006d1acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1acc.md) → [`006d1acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1acc.md) FUN_006d1acc

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
      "definition_site": "006d1af0",
      "incomplete_value": false,
      "site": "006d1af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1af0",
      "incomplete_value": false,
      "site": "006d1af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:590:8"
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
      "006d1af0",
      "DATA",
      [
        "storage",
        "00bf9590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1af0",
      "DATA",
      [
        "storage",
        "00bf95e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1acc.md#insn-006d1aec)
- 新版 [`006d1aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1acc.md#insn-006d1aec)

~~~diff
- 006d1aec ["COPY", "tmp:0:8", ["const:590:8"]]
- 006d1aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d1aec ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 006d1aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1aec bytes 08411691
+ 006d1aec bytes 08811791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef7d4799e1e20f3da6092f4f09860bea"></a>

### [`006d1b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1b00.md) → [`006d1b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1b00.md) FUN_006d1b00

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
      "definition_site": "006d1b0c",
      "incomplete_value": false,
      "site": "006d1b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1b0c",
      "incomplete_value": false,
      "site": "006d1b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:590:8"
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
      "006d1b0c",
      "DATA",
      [
        "storage",
        "00bf9590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1b0c",
      "DATA",
      [
        "storage",
        "00bf95e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1b00.md#insn-006d1b08)
- 新版 [`006d1b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1b00.md#insn-006d1b08)

~~~diff
- 006d1b08 ["COPY", "tmp:0:8", ["const:590:8"]]
- 006d1b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d1b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d1b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d1b08 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 006d1b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d1b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d1b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d1b08 bytes 29411691
+ 006d1b08 bytes 29811791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-485a9609afc5dfc36dcce724c8ab1cef"></a>

### [`006d1c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1c44.md) → [`006d1c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1c44.md) FUN_006d1c44

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
      "definition_site": "006d1c64",
      "incomplete_value": false,
      "site": "006d1c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1c64",
      "incomplete_value": false,
      "site": "006d1c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d1c68",
      "DATA",
      [
        "storage",
        "00bf9620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1c68",
      "DATA",
      [
        "storage",
        "00bf9670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1c44.md#insn-006d1c64)
- 新版 [`006d1c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1c44.md#insn-006d1c64)

~~~diff
- 006d1c64 ["COPY", "tmp:0:8", ["const:620:8"]]
- 006d1c64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1c64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1c64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d1c64 ["COPY", "tmp:0:8", ["const:670:8"]]
+ 006d1c64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1c64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1c64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1c64 bytes 08811891
+ 006d1c64 bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48f3b63d4d3aec6328b7b7bdec20b6f5"></a>

### [`006d1c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1c7c.md) → [`006d1c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1c7c.md) FUN_006d1c7c

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
      "definition_site": "006d1c80",
      "incomplete_value": false,
      "site": "006d1c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1c80",
      "incomplete_value": false,
      "site": "006d1c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d1c84",
      "DATA",
      [
        "storage",
        "00bf9620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1c84",
      "DATA",
      [
        "storage",
        "00bf9670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1c7c.md#insn-006d1c80)
- 新版 [`006d1c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1c7c.md#insn-006d1c80)

~~~diff
- 006d1c80 ["COPY", "tmp:0:8", ["const:620:8"]]
- 006d1c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d1c80 ["COPY", "tmp:0:8", ["const:670:8"]]
+ 006d1c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1c80 bytes 08811891
+ 006d1c80 bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd8ae6137376b0470102607a96b316a6"></a>

### [`006d1e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1e68.md) → [`006d1e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1e68.md) FUN_006d1e68

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
      "definition_site": "006d1e8c",
      "incomplete_value": false,
      "site": "006d1e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1e8c",
      "incomplete_value": false,
      "site": "006d1e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d1e8c",
      "DATA",
      [
        "storage",
        "00bf96a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1e8c",
      "DATA",
      [
        "storage",
        "00bf96f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1e68.md#insn-006d1e88)
- 新版 [`006d1e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1e68.md#insn-006d1e88)

~~~diff
- 006d1e88 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 006d1e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d1e88 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 006d1e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1e88 bytes 08811a91
+ 006d1e88 bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1a052a43caa8b9d93454da40c1eb21e"></a>

### [`006d1e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1e9c.md) → [`006d1e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1e9c.md) FUN_006d1e9c

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
      "definition_site": "006d1ea8",
      "incomplete_value": false,
      "site": "006d1ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1ea8",
      "incomplete_value": false,
      "site": "006d1ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d1ea8",
      "DATA",
      [
        "storage",
        "00bf96a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1ea8",
      "DATA",
      [
        "storage",
        "00bf96f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1e9c.md#insn-006d1ea4)
- 新版 [`006d1ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1e9c.md#insn-006d1ea4)

~~~diff
- 006d1ea4 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 006d1ea4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d1ea4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d1ea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d1ea4 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 006d1ea4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d1ea4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d1ea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d1ea4 bytes 29811a91
+ 006d1ea4 bytes 29c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc932d456e837c04299415450787aedb"></a>

### [`006d3b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3b28.md) → [`006d3b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b28.md) FUN_006d3b28

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
      "definition_site": "006d3b3c",
      "incomplete_value": false,
      "site": "006d3b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3b3c",
      "incomplete_value": false,
      "site": "006d3b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "006d3b40",
      "DATA",
      [
        "storage",
        "00bf9720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d3b40",
      "DATA",
      [
        "storage",
        "00bf9770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3b28.md#insn-006d3b3c)
- 新版 [`006d3b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b28.md#insn-006d3b3c)

~~~diff
- 006d3b3c ["COPY", "tmp:0:8", ["const:720:8"]]
- 006d3b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d3b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d3b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d3b3c ["COPY", "tmp:0:8", ["const:770:8"]]
+ 006d3b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d3b3c bytes 08811c91
+ 006d3b3c bytes 08c11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0efca352f587f9f23c33fe8311ff6dc1"></a>

### [`006d3b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3b4c.md) → [`006d3b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b4c.md) FUN_006d3b4c

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
      "definition_site": "006d3b50",
      "incomplete_value": false,
      "site": "006d3b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3b50",
      "incomplete_value": false,
      "site": "006d3b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "006d3b54",
      "DATA",
      [
        "storage",
        "00bf9720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d3b54",
      "DATA",
      [
        "storage",
        "00bf9770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3b4c.md#insn-006d3b50)
- 新版 [`006d3b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b4c.md#insn-006d3b50)

~~~diff
- 006d3b50 ["COPY", "tmp:0:8", ["const:720:8"]]
- 006d3b50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d3b50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d3b50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d3b50 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 006d3b50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3b50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3b50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d3b50 bytes 08811c91
+ 006d3b50 bytes 08c11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5e1b40e1d0308f486423074c3f9f455"></a>

### [`006d3bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3bd0.md) → [`006d3bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3bd0.md) FUN_006d3bd0

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
      "definition_site": "006d3bf4",
      "incomplete_value": false,
      "site": "006d3bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3bf4",
      "incomplete_value": false,
      "site": "006d3bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d3bf8",
      "DATA",
      [
        "storage",
        "00bf97a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d3bf8",
      "DATA",
      [
        "storage",
        "00bf97f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3bd0.md#insn-006d3bf4)
- 新版 [`006d3bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3bd0.md#insn-006d3bf4)

~~~diff
- 006d3bf4 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 006d3bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d3bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d3bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d3bf4 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 006d3bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d3bf4 bytes 08811e91
+ 006d3bf4 bytes 08c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af366b9f3ff082957a92939ef0c0adc8"></a>

### [`006d3c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c10.md) → [`006d3c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c10.md) FUN_006d3c10

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006d3c14",
      "incomplete_value": false,
      "site": "006d3c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3c14",
      "incomplete_value": false,
      "site": "006d3c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d3c18",
      "DATA",
      [
        "storage",
        "00bf97a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d3c18",
      "DATA",
      [
        "storage",
        "00bf97f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c10.md#insn-006d3c14)
- 新版 [`006d3c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c10.md#insn-006d3c14)

~~~diff
- 006d3c14 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 006d3c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d3c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d3c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d3c14 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 006d3c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d3c14 bytes 08811e91
+ 006d3c14 bytes 08c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b43740466aed8c6857eef79d2c1db878"></a>

### [`006d3c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c38.md) → [`006d3c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c38.md) FUN_006d3c38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d3d3c",
      "incomplete_value": true,
      "site": "006d3d50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3d3c",
      "incomplete_value": true,
      "site": "006d3d50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73a:8"
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
      "definition_site": "006d3e78",
      "incomplete_value": true,
      "site": "006d3e78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b86:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3e78",
      "incomplete_value": true,
      "site": "006d3e78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c13:8"
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
      "definition_site": "006d3e6c",
      "incomplete_value": true,
      "site": "006d3e7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006d3e6c",
      "incomplete_value": true,
      "site": "006d3e7c",
      "value": [
        "LOAD",
        "8",
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
      "006d3d3c",
      "READ",
      [
        "storage",
        "002a373a",
        null,
        "string"
      ]
    ],
    [
      "006d3e68",
      "READ",
      [
        "storage",
        "00293c13",
        null,
        "string"
      ]
    ],
    [
      "006d3e6c",
      "READ",
      [
        "storage",
        "00293c1a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006d3d3c",
      "READ",
      [
        "storage",
        "002a37c5",
        null,
        "string"
      ]
    ],
    [
      "006d3e68",
      "READ",
      [
        "storage",
        "00293b86",
        null,
        "string"
      ]
    ],
    [
      "006d3e6c",
      "READ",
      [
        "storage",
        "00293b8d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c38.md#insn-006d3d34) · [`006d3e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c38.md#insn-006d3e60) · [`006d3f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c38.md#insn-006d3f5c)
- 新版 [`006d3d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c38.md#insn-006d3d34) · [`006d3e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c38.md#insn-006d3e60) · [`006d3f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c38.md#insn-006d3f5c)

~~~diff
- 006d3d34 ["COPY", "tmp:0:8", ["const:73a:8"]]
- 006d3d34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d3d34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d3d34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d3d34 ["COPY", "tmp:0:8", ["const:7c5:8"]]
+ 006d3d34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d3d34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d3d34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d3d34 bytes 29e91c91
+ 006d3d34 bytes 29151f91
- 006d3e60 ["COPY", "tmp:0:8", ["const:c13:8"]]
- 006d3e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d3e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d3e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d3e60 ["COPY", "tmp:0:8", ["const:b86:8"]]
+ 006d3e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d3e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d3e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d3e60 bytes 294d3091
+ 006d3e60 bytes 29192e91
- 006d3f5c ["COPY", "tmp:0:8", ["const:74f:8"]]
- 006d3f5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006d3f5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006d3f5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006d3f5c ["COPY", "tmp:0:8", ["const:7da:8"]]
+ 006d3f5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006d3f5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006d3f5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006d3f5c bytes 213c1d91
+ 006d3f5c bytes 21681f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dad2dd0d9015e05ad9bdfa6cb037433a"></a>

### [`006d4344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4344.md) → [`006d4344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4344.md) FUN_006d4344

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
      "definition_site": "006d4364",
      "incomplete_value": false,
      "site": "006d4368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4364",
      "incomplete_value": false,
      "site": "006d4368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "006d4368",
      "DATA",
      [
        "storage",
        "00bf9810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4368",
      "DATA",
      [
        "storage",
        "00bf9860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4344.md#insn-006d4364)
- 新版 [`006d4364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4344.md#insn-006d4364)

~~~diff
- 006d4364 ["COPY", "tmp:0:8", ["const:810:8"]]
- 006d4364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4364 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 006d4364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4364 bytes 08412091
+ 006d4364 bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38e66b40012d22c58b82918c1854dd0e"></a>

### [`006d437c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d437c.md) → [`006d437c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d437c.md) FUN_006d437c

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
      "definition_site": "006d4380",
      "incomplete_value": false,
      "site": "006d4384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4380",
      "incomplete_value": false,
      "site": "006d4384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "006d4384",
      "DATA",
      [
        "storage",
        "00bf9810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4384",
      "DATA",
      [
        "storage",
        "00bf9860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d437c.md#insn-006d4380)
- 新版 [`006d4380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d437c.md#insn-006d4380)

~~~diff
- 006d4380 ["COPY", "tmp:0:8", ["const:810:8"]]
- 006d4380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4380 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 006d4380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4380 bytes 08412091
+ 006d4380 bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a15bfeee8271e278b92943557d15fdfe"></a>

### [`006d447c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d447c.md) → [`006d447c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d447c.md) FUN_006d447c

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
      "definition_site": "006d449c",
      "incomplete_value": false,
      "site": "006d44a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d449c",
      "incomplete_value": false,
      "site": "006d44a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d44a0",
      "DATA",
      [
        "storage",
        "00bf98a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d44a0",
      "DATA",
      [
        "storage",
        "00bf98f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d449c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d447c.md#insn-006d449c)
- 新版 [`006d449c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d447c.md#insn-006d449c)

~~~diff
- 006d449c ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 006d449c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d449c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d449c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d449c ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 006d449c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d449c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d449c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d449c bytes 08812291
+ 006d449c bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68046bcc6dc1a60bd91799a5e8b0178d"></a>

### [`006d44b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d44b4.md) → [`006d44b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d44b4.md) FUN_006d44b4

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
      "definition_site": "006d44b8",
      "incomplete_value": false,
      "site": "006d44bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d44b8",
      "incomplete_value": false,
      "site": "006d44bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d44bc",
      "DATA",
      [
        "storage",
        "00bf98a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d44bc",
      "DATA",
      [
        "storage",
        "00bf98f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d44b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d44b4.md#insn-006d44b8)
- 新版 [`006d44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d44b4.md#insn-006d44b8)

~~~diff
- 006d44b8 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 006d44b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d44b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d44b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d44b8 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 006d44b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d44b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d44b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d44b8 bytes 08812291
+ 006d44b8 bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f005b942a254e08ce9424c3ec030ea5c"></a>

### [`006d46a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d46a0.md) → [`006d46a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d46a0.md) FUN_006d46a0

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
      "definition_site": "006d46c0",
      "incomplete_value": false,
      "site": "006d46c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d46c0",
      "incomplete_value": false,
      "site": "006d46c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "006d46c4",
      "DATA",
      [
        "storage",
        "00bf9920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d46c4",
      "DATA",
      [
        "storage",
        "00bf9970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d46c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d46a0.md#insn-006d46c0)
- 新版 [`006d46c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d46a0.md#insn-006d46c0)

~~~diff
- 006d46c0 ["COPY", "tmp:0:8", ["const:920:8"]]
- 006d46c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d46c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d46c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d46c0 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 006d46c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d46c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d46c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d46c0 bytes 08812491
+ 006d46c0 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bedd70f8929dcbc5742fc1f38fceff67"></a>

### [`006d46d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d46d8.md) → [`006d46d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d46d8.md) FUN_006d46d8

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
      "definition_site": "006d46dc",
      "incomplete_value": false,
      "site": "006d46e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d46dc",
      "incomplete_value": false,
      "site": "006d46e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "006d46e0",
      "DATA",
      [
        "storage",
        "00bf9920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d46e0",
      "DATA",
      [
        "storage",
        "00bf9970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d46dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d46d8.md#insn-006d46dc)
- 新版 [`006d46dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d46d8.md#insn-006d46dc)

~~~diff
- 006d46dc ["COPY", "tmp:0:8", ["const:920:8"]]
- 006d46dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d46dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d46dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d46dc ["COPY", "tmp:0:8", ["const:970:8"]]
+ 006d46dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d46dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d46dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d46dc bytes 08812491
+ 006d46dc bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b2e5e92bbaf7dbced2955a3a0821c88"></a>

### [`006d47b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d47b8.md) → [`006d47b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d47b8.md) FUN_006d47b8

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
      "definition_site": "006d47d8",
      "incomplete_value": false,
      "site": "006d47dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d47d8",
      "incomplete_value": false,
      "site": "006d47dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "006d47dc",
      "DATA",
      [
        "storage",
        "00bf99a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d47dc",
      "DATA",
      [
        "storage",
        "00bf99f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d47d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d47b8.md#insn-006d47d8)
- 新版 [`006d47d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d47b8.md#insn-006d47d8)

~~~diff
- 006d47d8 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 006d47d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d47d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d47d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d47d8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 006d47d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d47d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d47d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d47d8 bytes 08812691
+ 006d47d8 bytes 08c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4124d9b33a0df4dbcedbc0209905a49f"></a>

### [`006d47f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d47f0.md) → [`006d47f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d47f0.md) FUN_006d47f0

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
      "definition_site": "006d47f4",
      "incomplete_value": false,
      "site": "006d47f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d47f4",
      "incomplete_value": false,
      "site": "006d47f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "006d47f8",
      "DATA",
      [
        "storage",
        "00bf99a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d47f8",
      "DATA",
      [
        "storage",
        "00bf99f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d47f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d47f0.md#insn-006d47f4)
- 新版 [`006d47f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d47f0.md#insn-006d47f4)

~~~diff
- 006d47f4 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 006d47f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d47f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d47f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d47f4 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 006d47f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d47f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d47f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d47f4 bytes 08812691
+ 006d47f4 bytes 08c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44f656c985b4dce2b46c1b1224cf6624"></a>

### [`006d4810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4810.md) → [`006d4810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4810.md) FUN_006d4810

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006bb5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bb5d0.md) [`006c5940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c5/006c5940.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006bb5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bb5d0.md) [`006c5940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c5/006c5940.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.29% / 新版 98.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d4940",
      "incomplete_value": false,
      "site": "006d4948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4940",
      "incomplete_value": false,
      "site": "006d4948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "006d4948",
      "DATA",
      [
        "storage",
        "00bf9a10",
        null,
        "undefined *"
      ]
    ],
    [
      "006d4994",
      "READ",
      [
        "storage",
        "00bf9a30",
        null,
        "pointer"
      ]
    ],
    [
      "006d4994",
      "READ",
      [
        "storage",
        "00bf9a38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4948",
      "DATA",
      [
        "storage",
        "00bf9a60",
        null,
        "undefined *"
      ]
    ],
    [
      "006d4994",
      "READ",
      [
        "storage",
        "00bf9a80",
        null,
        "pointer"
      ]
    ],
    [
      "006d4994",
      "READ",
      [
        "storage",
        "00bf9a88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4810.md#insn-006d4940)
- 新版 [`006d4940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4810.md#insn-006d4940)

~~~diff
- 006d4940 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 006d4940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4940 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 006d4940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4940 bytes 08412891
+ 006d4940 bytes 08812991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbfb223785cf827f48ee6aed0426282f"></a>

### [`006d4aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4aa0.md) → [`006d4aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4aa0.md) FUN_006d4aa0

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
      "definition_site": "006d4ab4",
      "incomplete_value": false,
      "site": "006d4ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4ab4",
      "incomplete_value": false,
      "site": "006d4ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "006d4ab8",
      "DATA",
      [
        "storage",
        "00bf9a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4ab8",
      "DATA",
      [
        "storage",
        "00bf9a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4aa0.md#insn-006d4ab4)
- 新版 [`006d4ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4aa0.md#insn-006d4ab4)

~~~diff
- 006d4ab4 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 006d4ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4ab4 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 006d4ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4ab4 bytes 08412891
+ 006d4ab4 bytes 08812991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-089e6d331271c3afbd417a2f2958a200"></a>

### [`006d4ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4ac4.md) → [`006d4ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ac4.md) FUN_006d4ac4

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
      "definition_site": "006d4ac8",
      "incomplete_value": false,
      "site": "006d4acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4ac8",
      "incomplete_value": false,
      "site": "006d4acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "006d4acc",
      "DATA",
      [
        "storage",
        "00bf9a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4acc",
      "DATA",
      [
        "storage",
        "00bf9a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4ac4.md#insn-006d4ac8)
- 新版 [`006d4ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ac4.md#insn-006d4ac8)

~~~diff
- 006d4ac8 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 006d4ac8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ac8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ac8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4ac8 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 006d4ac8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ac8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ac8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4ac8 bytes 08412891
+ 006d4ac8 bytes 08812991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eb9953573ccb788ff4b62da43ec8989"></a>

### [`006d4b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4b48.md) → [`006d4b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4b48.md) FUN_006d4b48

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
      "definition_site": "006d4b68",
      "incomplete_value": false,
      "site": "006d4b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4b68",
      "incomplete_value": false,
      "site": "006d4b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d4b6c",
      "DATA",
      [
        "storage",
        "00bf9aa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4b6c",
      "DATA",
      [
        "storage",
        "00bf9af0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4b48.md#insn-006d4b68)
- 新版 [`006d4b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4b48.md#insn-006d4b68)

~~~diff
- 006d4b68 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 006d4b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4b68 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 006d4b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4b68 bytes 08812a91
+ 006d4b68 bytes 08c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eb667ec04a52a1fa571f7a0ce77406f"></a>

### [`006d4b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4b80.md) → [`006d4b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4b80.md) FUN_006d4b80

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
      "definition_site": "006d4b84",
      "incomplete_value": false,
      "site": "006d4b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4b84",
      "incomplete_value": false,
      "site": "006d4b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d4b88",
      "DATA",
      [
        "storage",
        "00bf9aa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4b88",
      "DATA",
      [
        "storage",
        "00bf9af0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4b80.md#insn-006d4b84)
- 新版 [`006d4b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4b80.md#insn-006d4b84)

~~~diff
- 006d4b84 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 006d4b84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4b84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4b84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4b84 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 006d4b84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4b84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4b84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4b84 bytes 08812a91
+ 006d4b84 bytes 08c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-588f54f5c8ea860ebb8a8f0476997945"></a>

### [`006d4f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4f18.md) → [`006d4f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4f18.md) FUN_006d4f18

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
      "definition_site": "006d4f3c",
      "incomplete_value": false,
      "site": "006d4f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4f3c",
      "incomplete_value": false,
      "site": "006d4f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006d4f3c",
      "DATA",
      [
        "storage",
        "00bf9b10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4f3c",
      "DATA",
      [
        "storage",
        "00bf9b60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4f18.md#insn-006d4f38)
- 新版 [`006d4f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4f18.md#insn-006d4f38)

~~~diff
- 006d4f38 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 006d4f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4f38 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 006d4f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4f38 bytes 08412c91
+ 006d4f38 bytes 08812d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc535f62926df9529c619d3fd5b10d8a"></a>

### [`006d4fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4fd4.md) → [`006d4fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4fd4.md) FUN_006d4fd4

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
      "definition_site": "006d4fe8",
      "incomplete_value": false,
      "site": "006d4fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4fe8",
      "incomplete_value": false,
      "site": "006d4fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "006d4fec",
      "DATA",
      [
        "storage",
        "00bf9ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4fec",
      "DATA",
      [
        "storage",
        "00bf9bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4fd4.md#insn-006d4fe8)
- 新版 [`006d4fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4fd4.md#insn-006d4fe8)

~~~diff
- 006d4fe8 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 006d4fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4fe8 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 006d4fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4fe8 bytes 08812e91
+ 006d4fe8 bytes 08c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af3f5aaec69f041187218543b61c0eae"></a>

### [`006d4ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4ff8.md) → [`006d4ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ff8.md) FUN_006d4ff8

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
      "definition_site": "006d4ffc",
      "incomplete_value": false,
      "site": "006d5000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4ffc",
      "incomplete_value": false,
      "site": "006d5000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "006d5000",
      "DATA",
      [
        "storage",
        "00bf9ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d5000",
      "DATA",
      [
        "storage",
        "00bf9bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4ff8.md#insn-006d4ffc)
- 新版 [`006d4ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ff8.md#insn-006d4ffc)

~~~diff
- 006d4ffc ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 006d4ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4ffc ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 006d4ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4ffc bytes 08812e91
+ 006d4ffc bytes 08c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9e8e8332543bf8a2914238432b63144"></a>

### [`006d507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d507c.md) → [`006d507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d507c.md) FUN_006d507c

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
      "definition_site": "006d5090",
      "incomplete_value": false,
      "site": "006d5094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d5090",
      "incomplete_value": false,
      "site": "006d5094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "006d5094",
      "DATA",
      [
        "storage",
        "00bf9c20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d5094",
      "DATA",
      [
        "storage",
        "00bf9c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d5090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d507c.md#insn-006d5090)
- 新版 [`006d5090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d507c.md#insn-006d5090)

~~~diff
- 006d5090 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 006d5090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d5090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d5090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d5090 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 006d5090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d5090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d5090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d5090 bytes 08813091
+ 006d5090 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd50aa8480efe621a229475dda8578ad"></a>

### [`006d50a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d50a0.md) → [`006d50a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d50a0.md) FUN_006d50a0

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
      "definition_site": "006d50a4",
      "incomplete_value": false,
      "site": "006d50a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d50a4",
      "incomplete_value": false,
      "site": "006d50a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "006d50a8",
      "DATA",
      [
        "storage",
        "00bf9c20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d50a8",
      "DATA",
      [
        "storage",
        "00bf9c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d50a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d50a0.md#insn-006d50a4)
- 新版 [`006d50a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d50a0.md#insn-006d50a4)

~~~diff
- 006d50a4 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 006d50a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d50a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d50a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d50a4 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 006d50a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d50a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d50a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d50a4 bytes 08813091
+ 006d50a4 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f89dbd685e726f98d3d03dcaec682d03"></a>

### [`006d51a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d51a4.md) → [`006d51a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51a4.md) FUN_006d51a4

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
      "definition_site": "006d51c8",
      "incomplete_value": false,
      "site": "006d51c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d51c8",
      "incomplete_value": false,
      "site": "006d51c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "006d51c8",
      "DATA",
      [
        "storage",
        "00bf9ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d51c8",
      "DATA",
      [
        "storage",
        "00bf9cf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d51c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d51a4.md#insn-006d51c4)
- 新版 [`006d51c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51a4.md#insn-006d51c4)

~~~diff
- 006d51c4 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 006d51c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d51c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d51c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d51c4 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 006d51c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d51c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d51c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d51c4 bytes 08813291
+ 006d51c4 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b18ea712005c5ca739377cfda5d14c6f"></a>

### [`006d51d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d51d8.md) → [`006d51d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51d8.md) FUN_006d51d8

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
      "definition_site": "006d51e4",
      "incomplete_value": false,
      "site": "006d51e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d51e4",
      "incomplete_value": false,
      "site": "006d51e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "006d51e4",
      "DATA",
      [
        "storage",
        "00bf9ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d51e4",
      "DATA",
      [
        "storage",
        "00bf9cf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d51e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d51d8.md#insn-006d51e0)
- 新版 [`006d51e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51d8.md#insn-006d51e0)

~~~diff
- 006d51e0 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 006d51e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d51e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d51e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d51e0 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 006d51e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d51e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d51e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d51e0 bytes 29813291
+ 006d51e0 bytes 29c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-446048182516a470f3067fd93c160a65"></a>

### [`006d5298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5298.md) → [`006d5298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5298.md) FUN_006d5298

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
      "definition_site": "006d52ac",
      "incomplete_value": false,
      "site": "006d52b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d52ac",
      "incomplete_value": false,
      "site": "006d52b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "006d52b0",
      "DATA",
      [
        "storage",
        "00bf9d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d52b0",
      "DATA",
      [
        "storage",
        "00bf9d70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d52ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5298.md#insn-006d52ac)
- 新版 [`006d52ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5298.md#insn-006d52ac)

~~~diff
- 006d52ac ["COPY", "tmp:0:8", ["const:d20:8"]]
- 006d52ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d52ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d52ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d52ac ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 006d52ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d52ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d52ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d52ac bytes 08813491
+ 006d52ac bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

