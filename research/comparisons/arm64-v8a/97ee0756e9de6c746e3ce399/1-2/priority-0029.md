# v15.7.3 → v15.7.4 · 最優先の変更候補 (29)

[一覧の目次](README.md)

<a id="compare-99292a125ca196e678e3b069e7b68e00"></a>

### [`00672c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672c74.md) → [`00672c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672c74.md) FUN_00672c74

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
      "definition_site": "00672c98",
      "incomplete_value": false,
      "site": "00672c98",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672c98",
      "incomplete_value": false,
      "site": "00672c98",
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
            "const:288:8"
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
      "00672c98",
      "DATA",
      [
        "storage",
        "00bf8288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672c98",
      "DATA",
      [
        "storage",
        "00bf82d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672c74.md#insn-00672c94)
- 新版 `00672c94`（命令位置の公開資料なし）

~~~diff
- 00672c94 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00672c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672c94 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 00672c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672c94 bytes 08210a91
+ 00672c94 bytes 08610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e762947ea1ddd3c2850cb3f904ac55f4"></a>

### [`00672ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ca8.md) → [`00672ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ca8.md) FUN_00672ca8

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
      "definition_site": "00672cb4",
      "incomplete_value": false,
      "site": "00672cb4",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672cb4",
      "incomplete_value": false,
      "site": "00672cb4",
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
            "const:288:8"
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
      "00672cb4",
      "DATA",
      [
        "storage",
        "00bf8288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672cb4",
      "DATA",
      [
        "storage",
        "00bf82d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ca8.md#insn-00672cb0)
- 新版 `00672cb0`（命令位置の公開資料なし）

~~~diff
- 00672cb0 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00672cb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00672cb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00672cb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00672cb0 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 00672cb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00672cb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00672cb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00672cb0 bytes 29210a91
+ 00672cb0 bytes 29610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fe628a6380cc0761f227f220a15c20d"></a>

### [`00672ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ea4.md) → [`00672ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ea4.md) FUN_00672ea4

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
      "definition_site": "00672ec8",
      "incomplete_value": false,
      "site": "00672ec8",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672ec8",
      "incomplete_value": false,
      "site": "00672ec8",
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
            "const:308:8"
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
      "00672ec8",
      "DATA",
      [
        "storage",
        "00bf8308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672ec8",
      "DATA",
      [
        "storage",
        "00bf8358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ea4.md#insn-00672ec4)
- 新版 `00672ec4`（命令位置の公開資料なし）

~~~diff
- 00672ec4 ["COPY", "tmp:0:8", ["const:308:8"]]
- 00672ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672ec4 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00672ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672ec4 bytes 08210c91
+ 00672ec4 bytes 08610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b837000d7c14e70b379e8f039563e45"></a>

### [`00672ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ed8.md) → [`00672ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ed8.md) FUN_00672ed8

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
      "definition_site": "00672ee4",
      "incomplete_value": false,
      "site": "00672ee4",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672ee4",
      "incomplete_value": false,
      "site": "00672ee4",
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
            "const:308:8"
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
      "00672ee4",
      "DATA",
      [
        "storage",
        "00bf8308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672ee4",
      "DATA",
      [
        "storage",
        "00bf8358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ed8.md#insn-00672ee0)
- 新版 `00672ee0`（命令位置の公開資料なし）

~~~diff
- 00672ee0 ["COPY", "tmp:0:8", ["const:308:8"]]
- 00672ee0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00672ee0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00672ee0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00672ee0 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00672ee0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00672ee0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00672ee0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00672ee0 bytes 29210c91
+ 00672ee0 bytes 29610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-080ab5f190c20048d6a877f955895118"></a>

### [`00672ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ef4.md) → [`00672ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ef4.md) FUN_00672ef4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`0066181c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/0066181c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`0066181c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/0066181c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.19% / 新版 94.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00672f44",
      "incomplete_value": true,
      "site": "00672f54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00672f44",
      "incomplete_value": true,
      "site": "00672f54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00672f40",
      "incomplete_value": false,
      "site": "00672f54",
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
      "definition_site": "00672f40",
      "incomplete_value": false,
      "site": "00672f54",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00672f4c",
      "incomplete_value": false,
      "site": "00672f54",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672f4c",
      "incomplete_value": false,
      "site": "00672f54",
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
            "const:a60:8"
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
      "00672f40",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00672f44",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00672f4c",
      "PARAM",
      [
        "storage",
        "00bf7a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00672f40",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00672f44",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00672f4c",
      "PARAM",
      [
        "storage",
        "00bf7ab0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ef4.md#insn-00672f40) · [`00672f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ef4.md#insn-00672f44) · [`00672f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ef4.md#insn-00672f4c)
- 新版 `00672f40`（命令位置の公開資料なし） · `00672f44`（命令位置の公開資料なし） · `00672f4c`（命令位置の公開資料なし）

~~~diff
- 00672f40 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00672f40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00672f40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00672f40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00672f40 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00672f40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00672f40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00672f40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00672f40 bytes 21203991
+ 00672f40 bytes 21603a91
- 00672f44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a78:8"]]
- 00672f44 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00672f44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
+ 00672f44 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00672f44 bytes 603e45f9
+ 00672f44 bytes 605e45f9
- 00672f4c ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00672f4c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00672f4c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00672f4c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00672f4c ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 00672f4c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00672f4c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00672f4c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00672f4c bytes 42802991
+ 00672f4c bytes 42c02a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44e5d517d15be6e983f27a3232abc8af"></a>

### [`006731f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00673/006731f0.md) → [`006731f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/006731f0.md) _INIT_98

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
      "definition_site": "0067322c",
      "incomplete_value": true,
      "site": "00673248",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067322c",
      "incomplete_value": true,
      "site": "00673248",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00673250",
      "incomplete_value": true,
      "site": "0067326c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00673250",
      "incomplete_value": true,
      "site": "0067326c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00673270",
      "incomplete_value": true,
      "site": "0067328c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00673270",
      "incomplete_value": true,
      "site": "0067328c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0067322c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00673250",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00673270",
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
      "0067322c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00673250",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00673270",
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

- 旧版 [`0067321c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00673/006731f0.md#insn-0067321c) · [`00673224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00673/006731f0.md#insn-00673224)
- 新版 `0067321c`（命令位置の公開資料なし） · `00673224`（命令位置の公開資料なし）

~~~diff
- 0067321c ["COPY", "tmp:0:8", ["const:778:8"]]
- 0067321c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0067321c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0067321c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0067321c ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 0067321c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0067321c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0067321c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0067321c bytes 73e21d91
+ 0067321c bytes 73e21e91
- 00673224 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00673224 bytes a9e1ff90
+ 00673224 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00673224 bytes a9e1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd61214523b1d96469ef91b1ec599add"></a>

### [`00673580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00673/00673580.md) → [`00673580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/00673580.md) FUN_00673580

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0067417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00674/0067417c.md) · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.37% / 新版 96.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00673680",
      "incomplete_value": true,
      "site": "00673690",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:8dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00673680",
      "incomplete_value": true,
      "site": "00673690",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:852:8"
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
      "definition_site": "00673968",
      "incomplete_value": true,
      "site": "00673978",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:844:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00673968",
      "incomplete_value": true,
      "site": "00673978",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:7aa:8"
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
      "definition_site": "0067397c",
      "incomplete_value": true,
      "site": "0067397c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0067397c",
      "incomplete_value": true,
      "site": "0067397c",
      "value": [
        "LOAD",
        "8",
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
      "006735cc",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00673680",
      "READ",
      [
        "storage",
        "0029f852",
        null,
        "string"
      ]
    ],
    [
      "00673968",
      "READ",
      [
        "storage",
        "002a77aa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006735cc",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00673680",
      "READ",
      [
        "storage",
        "0029f8dd",
        null,
        "string"
      ]
    ],
    [
      "00673968",
      "READ",
      [
        "storage",
        "002a7844",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006735c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00673/00673580.md#insn-006735c0) · [`00673678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00673/00673580.md#insn-00673678) · [`00673960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00673/00673580.md#insn-00673960)
- 新版 `006735c0`（命令位置の公開資料なし） · `00673678`（命令位置の公開資料なし） · `00673960`（命令位置の公開資料なし）

~~~diff
- 006735c0 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 006735c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006735c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006735c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006735c0 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 006735c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006735c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006735c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006735c0 bytes 08a13491
+ 006735c0 bytes 08e13591
- 00673678 ["COPY", "tmp:0:8", ["const:852:8"]]
- 00673678 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00673678 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00673678 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00673678 ["COPY", "tmp:0:8", ["const:8dd:8"]]
+ 00673678 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00673678 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00673678 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00673678 bytes 29492191
+ 00673678 bytes 29752391
- 00673960 ["COPY", "tmp:0:8", ["const:7aa:8"]]
- 00673960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00673960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00673960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00673960 ["COPY", "tmp:0:8", ["const:844:8"]]
+ 00673960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00673960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00673960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00673960 bytes 29a91e91
+ 00673960 bytes 29112191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2951637986b5da8911c4bc1a8ce7adca"></a>

### [`00678728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678728.md) → [`00678728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678728.md) FUN_00678728

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00678d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678d74.md) · 呼出先 5件 [`0052dadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dadc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0b0.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00678d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678d74.md) · 呼出先 5件 [`0052dadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dadc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.57% / 新版 98.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00678758",
      "incomplete_value": false,
      "site": "00678764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:729:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00678758",
      "incomplete_value": false,
      "site": "00678764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:69e:8"
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
      "00678758",
      "PARAM",
      [
        "storage",
        "0029d69e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00678758",
      "PARAM",
      [
        "storage",
        "0029d729",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00678758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678728.md#insn-00678758)
- 新版 `00678758`（命令位置の公開資料なし）

~~~diff
- 00678758 ["COPY", "tmp:0:8", ["const:69e:8"]]
- 00678758 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00678758 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00678758 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00678758 ["COPY", "tmp:0:8", ["const:729:8"]]
+ 00678758 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00678758 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00678758 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00678758 bytes 42781a91
+ 00678758 bytes 42a41c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-553b421aa8d617e53da04509c6d7a3b9"></a>

### [`00678894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678894.md) → [`00678894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678894.md) FUN_00678894

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 6件 [`00596128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596128.md) [`00821cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cbc.md) [`008226b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/008226b4.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`00868124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) · 呼出先 16件 [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c7f0.md) [`0067c988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c988.md) [`0067c98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c98c.md)
- 新版 呼出元 6件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) [`00821cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cbc.md) [`008226b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/008226b4.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00868124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) · 呼出先 16件 [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c7f0.md) [`0067c988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c988.md) [`0067c98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c98c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006788dc",
      "incomplete_value": false,
      "site": "006788dc",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006788dc",
      "incomplete_value": false,
      "site": "006788dc",
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
            "const:388:8"
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
      "definition_site": "00678a58",
      "incomplete_value": false,
      "site": "00678a58",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00678a58",
      "incomplete_value": false,
      "site": "00678a58",
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
            "const:408:8"
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
      "006788dc",
      "DATA",
      [
        "storage",
        "00bf8388",
        null,
        "undefined *"
      ]
    ],
    [
      "00678998",
      "PARAM",
      [
        "storage",
        "0029d69e",
        null,
        "string"
      ]
    ],
    [
      "00678a58",
      "DATA",
      [
        "storage",
        "00bf8408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006788dc",
      "DATA",
      [
        "storage",
        "00bf83d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00678998",
      "PARAM",
      [
        "storage",
        "0029d729",
        null,
        "string"
      ]
    ],
    [
      "00678a58",
      "DATA",
      [
        "storage",
        "00bf8458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006788d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678894.md#insn-006788d8) · [`00678958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678894.md#insn-00678958) · [`00678a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678894.md#insn-00678a54)
- 新版 `006788d8`（命令位置の公開資料なし） · `00678958`（命令位置の公開資料なし） · `00678a54`（命令位置の公開資料なし）

~~~diff
- 006788d8 ["COPY", "tmp:0:8", ["const:388:8"]]
- 006788d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006788d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006788d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006788d8 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 006788d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006788d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006788d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006788d8 bytes 08210e91
+ 006788d8 bytes 08610f91
- 00678958 ["COPY", "tmp:0:8", ["const:69e:8"]]
- 00678958 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00678958 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00678958 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00678958 ["COPY", "tmp:0:8", ["const:729:8"]]
+ 00678958 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00678958 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00678958 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00678958 bytes d67a1a91
+ 00678958 bytes d6a61c91
- 00678a54 ["COPY", "tmp:0:8", ["const:408:8"]]
- 00678a54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00678a54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00678a54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00678a54 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 00678a54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00678a54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00678a54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00678a54 bytes 08211091
+ 00678a54 bytes 08611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-877449e957c8c7c66484840016a32123"></a>

### [`00678d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678d74.md) → [`00678d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678d74.md) FUN_00678d74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0067c990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c990.md) [`0067d64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067d64c.md) · 呼出先 26件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`0067c990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c990.md) [`0067d64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067d/0067d64c.md) · 呼出先 26件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00679258",
      "incomplete_value": true,
      "site": "00679268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:76f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00679258",
      "incomplete_value": true,
      "site": "00679268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e4:8"
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
      "definition_site": "00679510",
      "incomplete_value": true,
      "site": "00679528",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00679510",
      "incomplete_value": true,
      "site": "00679528",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c2d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 91,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067952c",
      "incomplete_value": true,
      "site": "0067952c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0067952c",
      "incomplete_value": true,
      "site": "0067952c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 92,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00678f04",
      "PARAM",
      [
        "storage",
        "0029b286",
        null,
        null
      ]
    ],
    [
      "00678fa0",
      "PARAM",
      [
        "storage",
        "002a42a8",
        null,
        null
      ]
    ],
    [
      "006790e0",
      "READ",
      [
        "storage",
        "002a186c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00678f04",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ],
    [
      "00678fa0",
      "PARAM",
      [
        "storage",
        "002a4333",
        null,
        null
      ]
    ],
    [
      "006790e0",
      "READ",
      [
        "storage",
        "002a18f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00678f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678d74.md#insn-00678f04) · [`00678fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678d74.md#insn-00678fa0) · [`006790d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678d74.md#insn-006790d8)
- 新版 `00678f04`（命令位置の公開資料なし） · `00678fa0`（命令位置の公開資料なし） · `006790d8`（命令位置の公開資料なし）

~~~diff
- 00678f04 ["COPY", "tmp:0:8", ["const:286:8"]]
- 00678f04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00678f04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00678f04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00678f04 ["COPY", "tmp:0:8", ["const:284:8"]]
+ 00678f04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00678f04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00678f04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00678f04 bytes 21180a91
+ 00678f04 bytes 21100a91
- 00678fa0 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00678fa0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00678fa0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00678fa0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00678fa0 ["COPY", "tmp:0:8", ["const:333:8"]]
+ 00678fa0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00678fa0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00678fa0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00678fa0 bytes 21a00a91
+ 00678fa0 bytes 21cc0c91
- 006790d8 ["COPY", "tmp:0:8", ["const:86c:8"]]
- 006790d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006790d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006790d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006790d8 ["COPY", "tmp:0:8", ["const:8f7:8"]]
+ 006790d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006790d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006790d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006790d8 bytes 4ab12191
+ 006790d8 bytes 4add2391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f54c9898337b9bb1ec22c6841201669d"></a>

### [`00679c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00679/00679c54.md) → [`00679c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679c54.md) FUN_00679c54

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006799c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00679/006799c0.md) [`0067d250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067d250.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`006799c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/006799c0.md) [`0067d250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067d/0067d250.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00679c60",
      "incomplete_value": false,
      "site": "00679c64",
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
      "definition_site": "00679c60",
      "incomplete_value": false,
      "site": "00679c64",
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
      "00679c60",
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
      "00679c60",
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

- 旧版 [`00679c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00679/00679c54.md#insn-00679c60)
- 新版 `00679c60`（命令位置の公開資料なし）

~~~diff
- 00679c60 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00679c60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00679c60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00679c60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00679c60 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00679c60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00679c60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00679c60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00679c60 bytes 000c0c91
+ 00679c60 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56ffe21659c8238af80449b9d0aa3f75"></a>

### [`0067a2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067a/0067a2d8.md) → [`0067a2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2d8.md) FUN_0067a2d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00679f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00679/00679f0c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00679f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679f0c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0067a2e4",
      "incomplete_value": false,
      "site": "0067a2e8",
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
      "definition_site": "0067a2e4",
      "incomplete_value": false,
      "site": "0067a2e8",
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
      "0067a2e4",
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
      "0067a2e4",
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

- 旧版 [`0067a2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067a/0067a2d8.md#insn-0067a2e4)
- 新版 `0067a2e4`（命令位置の公開資料なし）

~~~diff
- 0067a2e4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0067a2e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067a2e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067a2e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0067a2e4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0067a2e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0067a2e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0067a2e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067a2e4 bytes 000c0c91
+ 0067a2e4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf331b7a20a0da523e3e91b88f485f46"></a>

### [`0067a2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067a/0067a2ec.md) → [`0067a2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2ec.md) FUN_0067a2ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00673580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00673/00673580.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 2件 [`00673580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/00673580.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "0067a2f8",
      "incomplete_value": false,
      "site": "0067a2fc",
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
      "definition_site": "0067a2f8",
      "incomplete_value": false,
      "site": "0067a2fc",
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
      "0067a2f8",
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
      "0067a2f8",
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

- 旧版 [`0067a2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067a/0067a2ec.md#insn-0067a2f8)
- 新版 `0067a2f8`（命令位置の公開資料なし）

~~~diff
- 0067a2f8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0067a2f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067a2f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067a2f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0067a2f8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0067a2f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0067a2f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0067a2f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067a2f8 bytes 000c0c91
+ 0067a2f8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-137e305cb051a6096a594314ce479f9b"></a>

### [`0067b1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067b/0067b1c0.md) → [`0067b1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b1c0.md) FUN_0067b1c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0067417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00674/0067417c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0067b1cc",
      "incomplete_value": false,
      "site": "0067b1d0",
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
      "definition_site": "0067b1cc",
      "incomplete_value": false,
      "site": "0067b1d0",
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
      "0067b1cc",
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
      "0067b1cc",
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

- 旧版 [`0067b1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067b/0067b1c0.md#insn-0067b1cc)
- 新版 `0067b1cc`（命令位置の公開資料なし）

~~~diff
- 0067b1cc ["COPY", "tmp:0:8", ["const:303:8"]]
- 0067b1cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067b1cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067b1cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0067b1cc ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0067b1cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0067b1cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0067b1cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067b1cc bytes 000c0c91
+ 0067b1cc bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3df3244b818030ce3d6c189fb5e8e88a"></a>

### [`0067c940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c940.md) → [`0067c940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c940.md) FUN_0067c940

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
      "definition_site": "0067c964",
      "incomplete_value": false,
      "site": "0067c964",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067c964",
      "incomplete_value": false,
      "site": "0067c964",
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
            "const:388:8"
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
      "0067c964",
      "DATA",
      [
        "storage",
        "00bf8388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0067c964",
      "DATA",
      [
        "storage",
        "00bf83d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067c960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c940.md#insn-0067c960)
- 新版 `0067c960`（命令位置の公開資料なし）

~~~diff
- 0067c960 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0067c960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067c960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067c960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067c960 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 0067c960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067c960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067c960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067c960 bytes 08210e91
+ 0067c960 bytes 08610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-355805419c50f8b28d6eb345e69863cc"></a>

### [`0067c974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c974.md) → [`0067c974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c974.md) FUN_0067c974

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
      "definition_site": "0067c980",
      "incomplete_value": false,
      "site": "0067c980",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067c980",
      "incomplete_value": false,
      "site": "0067c980",
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
            "const:388:8"
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
      "0067c980",
      "DATA",
      [
        "storage",
        "00bf8388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0067c980",
      "DATA",
      [
        "storage",
        "00bf83d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067c97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c974.md#insn-0067c97c)
- 新版 `0067c97c`（命令位置の公開資料なし）

~~~diff
- 0067c97c ["COPY", "tmp:0:8", ["const:388:8"]]
- 0067c97c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0067c97c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0067c97c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0067c97c ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 0067c97c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0067c97c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0067c97c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0067c97c bytes 29210e91
+ 0067c97c bytes 29610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5500c49c9623f100537404d7e14e7e29"></a>

### [`0067c9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c4.md) → [`0067c9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c9c4.md) FUN_0067c9c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00678894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678894.md) [`00690d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00690/00690d9c.md) [`008220d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/008220d0.md) [`0082233c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/0082233c.md) [`00857194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857194.md) · 呼出先 6件 [`0067d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067d4f0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb260.md) [`00bdb270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb270.md)
- 新版 呼出元 6件 [`00678894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678894.md) [`00690d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00690/00690d9c.md) [`008220d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/008220d0.md) [`0082233c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/0082233c.md) [`00857194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857194.md) · 呼出先 6件 [`0067d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067d/0067d4f0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) [`00bdb2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0067ca78",
      "incomplete_value": false,
      "site": "0067ca7c",
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
      "definition_site": "0067ca78",
      "incomplete_value": false,
      "site": "0067ca7c",
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
      "0067ca78",
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
      "0067ca78",
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

- 旧版 [`0067ca78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c4.md#insn-0067ca78)
- 新版 `0067ca78`（命令位置の公開資料なし）

~~~diff
- 0067ca78 ["COPY", "tmp:0:8", ["const:5d1:8"]]
- 0067ca78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0067ca78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0067ca78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0067ca78 ["COPY", "tmp:0:8", ["const:544:8"]]
+ 0067ca78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0067ca78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0067ca78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0067ca78 bytes 21441791
+ 0067ca78 bytes 21101591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04aa52fde033a55c6a9ad04f2cf3ecf6"></a>

### [`0067d5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067d5fc.md) → [`0067d5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067d/0067d5fc.md) FUN_0067d5fc

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
      "definition_site": "0067d620",
      "incomplete_value": false,
      "site": "0067d620",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067d620",
      "incomplete_value": false,
      "site": "0067d620",
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
            "const:408:8"
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
      "0067d620",
      "DATA",
      [
        "storage",
        "00bf8408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0067d620",
      "DATA",
      [
        "storage",
        "00bf8458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067d61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067d5fc.md#insn-0067d61c)
- 新版 `0067d61c`（命令位置の公開資料なし）

~~~diff
- 0067d61c ["COPY", "tmp:0:8", ["const:408:8"]]
- 0067d61c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067d61c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067d61c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067d61c ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0067d61c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067d61c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067d61c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067d61c bytes 08211091
+ 0067d61c bytes 08611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60e7d0a595856f8f2b4d91bd2980c1cb"></a>

### [`0067d67c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067d67c.md) → [`0067d67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067d/0067d67c.md) _INIT_99

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
      "definition_site": "0067d6b8",
      "incomplete_value": true,
      "site": "0067d6d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067d6b8",
      "incomplete_value": true,
      "site": "0067d6d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067d6dc",
      "incomplete_value": true,
      "site": "0067d6f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067d6dc",
      "incomplete_value": true,
      "site": "0067d6f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067d6fc",
      "incomplete_value": true,
      "site": "0067d718",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067d6fc",
      "incomplete_value": true,
      "site": "0067d718",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0067d6b8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0067d6dc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0067d6fc",
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
      "0067d6b8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0067d6dc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0067d6fc",
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

- 旧版 [`0067d6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067d67c.md#insn-0067d6a8) · [`0067d6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067d67c.md#insn-0067d6b0)
- 新版 `0067d6a8`（命令位置の公開資料なし） · `0067d6b0`（命令位置の公開資料なし）

~~~diff
- 0067d6a8 ["COPY", "tmp:0:8", ["const:790:8"]]
- 0067d6a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0067d6a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0067d6a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0067d6a8 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 0067d6a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0067d6a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0067d6a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0067d6a8 bytes 73421e91
+ 0067d6a8 bytes 73421f91
- 0067d6b0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0067d6b0 bytes 49e1ffd0
+ 0067d6b0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0067d6b0 bytes 49e1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3254e19ae11a73e63197976bfb18d52"></a>

### [`0067da3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067da3c.md) → [`0067da3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067d/0067da3c.md) FUN_0067da3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/0046555c.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046555c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.47% / 新版 97.47%

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
      "definition_site": "0067da80",
      "incomplete_value": false,
      "site": "0067da8c",
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
      "definition_site": "0067da80",
      "incomplete_value": false,
      "site": "0067da8c",
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
      "definition_site": "0067dab4",
      "incomplete_value": true,
      "site": "0067dac4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067dab4",
      "incomplete_value": true,
      "site": "0067dac4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d3:8"
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
      "definition_site": "0067dab8",
      "incomplete_value": true,
      "site": "0067dac8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0067dab8",
      "incomplete_value": true,
      "site": "0067dac8",
      "value": [
        "LOAD",
        "16",
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
      "0067da8c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0067dab4",
      "READ",
      [
        "storage",
        "002990d3",
        null,
        "string"
      ]
    ],
    [
      "0067dab8",
      "READ",
      [
        "storage",
        "002990dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0067da8c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0067dab4",
      "READ",
      [
        "storage",
        "00299046",
        null,
        "string"
      ]
    ],
    [
      "0067dab8",
      "READ",
      [
        "storage",
        "0029904f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067da80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067da3c.md#insn-0067da80) · [`0067daac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067da3c.md#insn-0067daac) · [`0067dab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067da3c.md#insn-0067dab0)
- 新版 `0067da80`（命令位置の公開資料なし） · `0067daac`（命令位置の公開資料なし）

~~~diff
- 0067da80 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0067da80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067da80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067da80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067da80 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0067da80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067da80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067da80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067da80 bytes 08a13491
+ 0067da80 bytes 08e13591
- 0067daac ["COPY", "tmp:0:8", ["const:d3:8"]]
- 0067daac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067daac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067daac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067daac ["COPY", "tmp:0:8", ["const:46:8"]]
+ 0067daac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067daac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067daac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067daac bytes 084d0391
+ 0067daac bytes 08190191
- 0067dab0 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0067dab0 bytes a9e1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c2c0faa0f547c367a6ec4952c88f799"></a>

### [`0067f378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067f/0067f378.md) → [`0067f378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067f/0067f378.md) FUN_0067f378

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0067f3bc",
      "incomplete_value": false,
      "site": "0067f3c8",
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
      "definition_site": "0067f3bc",
      "incomplete_value": false,
      "site": "0067f3c8",
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
      "definition_site": "0067f6a0",
      "incomplete_value": true,
      "site": "0067f6a4",
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
      "definition_site": "0067f6a0",
      "incomplete_value": true,
      "site": "0067f6a4",
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
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067f6c4",
      "incomplete_value": true,
      "site": "0067f6c8",
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
      "definition_site": "0067f6c4",
      "incomplete_value": true,
      "site": "0067f6c8",
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
    "ordinal": 55,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0067f3c8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0067f690",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "0067f694",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0067f3c8",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0067f690",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "0067f694",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067f3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067f/0067f378.md#insn-0067f3bc) · [`0067f690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067f/0067f378.md#insn-0067f690) · [`0067f694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067f/0067f378.md#insn-0067f694)
- 新版 `0067f3bc`（命令位置の公開資料なし） · `0067f690`（命令位置の公開資料なし） · `0067f694`（命令位置の公開資料なし）

~~~diff
- 0067f3bc ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0067f3bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067f3bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067f3bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067f3bc ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0067f3bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067f3bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067f3bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067f3bc bytes 08a13491
+ 0067f3bc bytes 08e13591
- 0067f690 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0067f690 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0067f690 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0067f690 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0067f690 bytes 08b946f9
+ 0067f690 bytes 08e146f9
- 0067f694 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
- 0067f694 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0067f694 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
+ 0067f694 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0067f694 bytes b5be46f9
+ 0067f694 bytes b5e646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c48960a432f7fdeb899bcc96ef6ff972"></a>

### [`0067fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067f/0067fdf0.md) → [`0067fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067f/0067fdf0.md) FUN_0067fdf0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0067da3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067d/0067da3c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0067da3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067d/0067da3c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0067fdfc",
      "incomplete_value": false,
      "site": "0067fe00",
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
      "definition_site": "0067fdfc",
      "incomplete_value": false,
      "site": "0067fe00",
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
      "0067fdfc",
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
      "0067fdfc",
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

- 旧版 [`0067fdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067f/0067fdf0.md#insn-0067fdfc)
- 新版 `0067fdfc`（命令位置の公開資料なし）

~~~diff
- 0067fdfc ["COPY", "tmp:0:8", ["const:303:8"]]
- 0067fdfc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067fdfc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067fdfc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0067fdfc ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0067fdfc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0067fdfc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0067fdfc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067fdfc bytes 000c0c91
+ 0067fdfc bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b52fee033e0c8671f1a0d32cfec0c9e3"></a>

### [`0067fea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067f/0067fea4.md) → [`0067fea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067f/0067fea4.md) _INIT_100

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
      "definition_site": "0067fee0",
      "incomplete_value": true,
      "site": "0067fefc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067fee0",
      "incomplete_value": true,
      "site": "0067fefc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067ff04",
      "incomplete_value": true,
      "site": "0067ff20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067ff04",
      "incomplete_value": true,
      "site": "0067ff20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067ff24",
      "incomplete_value": true,
      "site": "0067ff40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067ff24",
      "incomplete_value": true,
      "site": "0067ff40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0067fee0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0067ff04",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0067ff24",
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
      "0067fee0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0067ff04",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0067ff24",
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

- 旧版 [`0067fed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067f/0067fea4.md#insn-0067fed0) · [`0067fed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067f/0067fea4.md#insn-0067fed8)
- 新版 `0067fed0`（命令位置の公開資料なし） · `0067fed8`（命令位置の公開資料なし）

~~~diff
- 0067fed0 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 0067fed0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0067fed0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0067fed0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0067fed0 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 0067fed0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0067fed0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0067fed0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0067fed0 bytes 73a21e91
+ 0067fed0 bytes 73a21f91
- 0067fed8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0067fed8 bytes 49e1ff90
+ 0067fed8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0067fed8 bytes 49e1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59038e480d0f4e7983f7699fe5564731"></a>

### [`006806cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/006806cc.md) → [`006806cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00680/006806cc.md) FUN_006806cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00689014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689014.md) [`006892e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006892e4.md) [`00689734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689734.md) · 呼出先 18件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md) [`00687ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00687/00687ba0.md)
- 新版 呼出元 3件 [`00689014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689014.md) [`006892e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006892e4.md) [`00689734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689734.md) · 呼出先 18件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a83e4.md) [`00687ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00687/00687ba0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.76% / 新版 95.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00680708",
      "incomplete_value": true,
      "site": "00680720",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:baf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00680708",
      "incomplete_value": true,
      "site": "00680720",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c3c:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "006807b0",
      "incomplete_value": false,
      "site": "006807b0",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006807b0",
      "incomplete_value": false,
      "site": "006807b0",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00680898",
      "incomplete_value": false,
      "site": "006808a4",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00680898",
      "incomplete_value": false,
      "site": "006808a4",
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
            "const:688:8"
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
      "00680708",
      "READ",
      [
        "storage",
        "00294c3c",
        null,
        "string"
      ]
    ],
    [
      "006807b0",
      "DATA",
      [
        "storage",
        "00bf8488",
        null,
        "undefined *"
      ]
    ],
    [
      "00680814",
      "READ",
      [
        "storage",
        "00bf84a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00680708",
      "READ",
      [
        "storage",
        "00294baf",
        null,
        "string"
      ]
    ],
    [
      "006807b0",
      "DATA",
      [
        "storage",
        "00bf84d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00680814",
      "READ",
      [
        "storage",
        "00bf84f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00680700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/006806cc.md#insn-00680700) · [`006807ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/006806cc.md#insn-006807ac) · [`00680898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/006806cc.md#insn-00680898)
- 新版 `00680700`（命令位置の公開資料なし） · `006807ac`（命令位置の公開資料なし） · `00680898`（命令位置の公開資料なし）

~~~diff
- 00680700 ["COPY", "tmp:0:8", ["const:c3c:8"]]
- 00680700 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00680700 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00680700 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00680700 ["COPY", "tmp:0:8", ["const:baf:8"]]
+ 00680700 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00680700 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00680700 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00680700 bytes 29f13091
+ 00680700 bytes 29bd2e91
- 006807ac ["COPY", "tmp:0:8", ["const:488:8"]]
- 006807ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006807ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006807ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006807ac ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 006807ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006807ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006807ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006807ac bytes 08211291
+ 006807ac bytes 08611391
- 00680898 ["COPY", "tmp:0:8", ["const:688:8"]]
- 00680898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00680898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00680898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00680898 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00680898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00680898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00680898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00680898 bytes 08211a91
+ 00680898 bytes 08611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-502d6cf33e7943bef603130974ff10a8"></a>

### [`00681138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00681/00681138.md) → [`00681138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00681/00681138.md) FUN_00681138

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 46件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) · 呼出先 46件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `store_destination` 7件, `store_value` 15件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00681a98",
      "incomplete_value": false,
      "site": "00681a98",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00681a98",
      "incomplete_value": false,
      "site": "00681a98",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00681be8",
      "incomplete_value": false,
      "site": "00681be8",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00681be8",
      "incomplete_value": false,
      "site": "00681be8",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "ordinal": 80,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00681c84",
      "incomplete_value": true,
      "site": "00681c84",
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
      "definition_site": "00681c84",
      "incomplete_value": true,
      "site": "00681c84",
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
      "006814b0",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006814b8",
      "READ",
      [
        "storage",
        "0029e6c4",
        null,
        "string"
      ]
    ],
    [
      "006814bc",
      "READ",
      [
        "storage",
        "0029e6d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006814b0",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006814b8",
      "READ",
      [
        "storage",
        "0029e74f",
        null,
        "string"
      ]
    ],
    [
      "006814bc",
      "READ",
      [
        "storage",
        "0029e75c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00681470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00681/00681138.md#insn-00681470) · [`00681474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00681/00681138.md#insn-00681474)
- 新版 `00681470`（命令位置の公開資料なし） · `00681474`（命令位置の公開資料なし）

~~~diff
- 00681470 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00681470 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00681470 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00681470 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00681470 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00681470 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00681470 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00681470 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00681470 bytes 94e20091
+ 00681470 bytes 94e20191
- 00681474 ["COPY", "register:40a8:8", ["const:c25000:8"]]
- 00681474 bytes 352d0090
+ 00681474 ["COPY", "register:40a8:8", ["const:c25000:8"]]
+ 00681474 bytes 352d0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-add219d9b4aa7c1411080cc5a5ed9e94"></a>

### [`006847cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00684/006847cc.md) → [`006847cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00684/006847cc.md) FUN_006847cc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00686590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686590.md) · 呼出先 11件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00686590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686590.md) · 呼出先 11件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.33% / 新版 87.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `store_destination` 9件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00684b20",
      "incomplete_value": true,
      "site": "00684b20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00684b20",
      "incomplete_value": true,
      "site": "00684b20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf4:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00684c48",
      "incomplete_value": false,
      "site": "00684c48",
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
      "definition_site": "00684c48",
      "incomplete_value": false,
      "site": "00684c48",
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
    "ordinal": 50,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00684c4c",
      "incomplete_value": false,
      "site": "00684c4c",
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
      "definition_site": "00684c4c",
      "incomplete_value": false,
      "site": "00684c4c",
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
    "ordinal": 51,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006847f4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00684800",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00684808",
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
      "006847f4",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00684800",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00684808",
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

- 旧版 [`006847f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00684/006847cc.md#insn-006847f4) · [`00684800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00684/006847cc.md#insn-00684800) · [`00684808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00684/006847cc.md#insn-00684808)
- 新版 `006847f4`（命令位置の公開資料なし） · `00684800`（命令位置の公開資料なし） · `00684808`（命令位置の公開資料なし）

~~~diff
- 006847f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006847f4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006847f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006847f4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006847f4 bytes 003d45f9
+ 006847f4 bytes 005d45f9
- 00684800 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00684800 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00684800 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00684800 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00684800 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00684800 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00684800 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00684800 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00684800 bytes 21203991
+ 00684800 bytes 21603a91
- 00684808 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00684808 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00684808 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00684808 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00684808 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00684808 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00684808 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00684808 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00684808 bytes 42203591
+ 00684808 bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7252a5daecc06856eb99993ae9dcbd5"></a>

### [`00684ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00684/00684ffc.md) → [`00684ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00684/00684ffc.md) FUN_00684ffc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00686590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686590.md) · 呼出先 32件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a0.md) [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md)
- 新版 呼出元 1件 [`00686590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686590.md) · 呼出先 32件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a0.md) [`0044b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.20% / 新版 92.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `store_destination` 28件, `store_value` 16件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00685508",
      "incomplete_value": false,
      "site": "00685508",
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
      "definition_site": "00685508",
      "incomplete_value": false,
      "site": "00685508",
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
    "ordinal": 46,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0068550c",
      "incomplete_value": false,
      "site": "0068550c",
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
      "definition_site": "0068550c",
      "incomplete_value": false,
      "site": "0068550c",
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
    "ordinal": 47,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00685508",
      "incomplete_value": false,
      "site": "0068550c",
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
      "definition_site": "00685508",
      "incomplete_value": false,
      "site": "0068550c",
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
      "0068503c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0068506c",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "0068506c",
      "PARAM",
      [
        "storage",
        "00c250d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0068503c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0068506c",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "0068506c",
      "PARAM",
      [
        "storage",
        "00c25118",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00685038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00684/00684ffc.md#insn-00685038) · [`0068506c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00684/00684ffc.md#insn-0068506c) · [`0068507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00684/00684ffc.md#insn-0068507c)
- 新版 `00685038`（命令位置の公開資料なし） · `0068506c`（命令位置の公開資料なし） · `0068507c`（命令位置の公開資料なし）

~~~diff
- 00685038 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00685038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00685038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00685038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00685038 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00685038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00685038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00685038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00685038 bytes 08e10091
+ 00685038 bytes 08e10191
- 0068506c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 0068506c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 0068506c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 0068506c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 0068506c bytes 423047f9
+ 0068506c bytes 425847f9
- 0068507c ["COPY", "tmp:0:8", ["const:0:8"]]
- 0068507c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0068507c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0068507c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0068507c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0068507c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0068507c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0068507c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0068507c bytes 00000091
+ 0068507c bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab0e313a6018d262cf719f77419fb023"></a>

### [`006864e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/006864e4.md) → [`006864e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/006864e4.md) FUN_006864e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) · 呼出先 5件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0069aa30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069aa30.md) [`0069ab88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069ab88.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 1件 [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) · 呼出先 5件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0069aa30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069aa30.md) [`0069ab88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069ab88.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00686500",
      "incomplete_value": true,
      "site": "00686500",
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
      "definition_site": "00686500",
      "incomplete_value": true,
      "site": "00686500",
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
      "006864fc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00686508",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00686510",
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
      "006864fc",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00686508",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00686510",
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

- 旧版 [`006864fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/006864e4.md#insn-006864fc) · [`00686508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/006864e4.md#insn-00686508) · [`00686510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/006864e4.md#insn-00686510)
- 新版 `006864fc`（命令位置の公開資料なし） · `00686508`（命令位置の公開資料なし） · `00686510`（命令位置の公開資料なし）

~~~diff
- 006864fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006864fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006864fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 006864fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006864fc bytes 083d45f9
+ 006864fc bytes 085d45f9
- 00686508 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00686508 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00686508 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00686508 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00686508 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00686508 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00686508 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00686508 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00686508 bytes 21203991
+ 00686508 bytes 21603a91
- 00686510 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00686510 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00686510 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00686510 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00686510 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00686510 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00686510 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00686510 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00686510 bytes 42203591
+ 00686510 bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9667bce565e555d37b42e1e5f0c9bd"></a>

### [`00686764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686764.md) → [`00686764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686764.md) FUN_00686764

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00963004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00963/00963004.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`004459e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/004459e0.md)
- 新版 呼出元 1件 [`00963004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00963/00963004.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`004459e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/004459e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.30% / 新版 99.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0068679c",
      "incomplete_value": true,
      "site": "0068679c",
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
      "definition_site": "0068679c",
      "incomplete_value": true,
      "site": "0068679c",
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
      "definition_site": "006867ac",
      "incomplete_value": true,
      "site": "006867b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006867ac",
      "incomplete_value": true,
      "site": "006867b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
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
      "00686798",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006867a4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006867ac",
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
      "00686798",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006867a4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006867ac",
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

- 旧版 [`00686798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686764.md#insn-00686798) · [`006867a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686764.md#insn-006867a4) · [`006867ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686764.md#insn-006867ac)
- 新版 `00686798`（命令位置の公開資料なし） · `006867a4`（命令位置の公開資料なし） · `006867ac`（命令位置の公開資料なし）

~~~diff
- 00686798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00686798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00686798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00686798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00686798 bytes 083d45f9
+ 00686798 bytes 085d45f9
- 006867a4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 006867a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006867a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006867a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006867a4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006867a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006867a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006867a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006867a4 bytes 21203991
+ 006867a4 bytes 21603a91
- 006867ac ["COPY", "tmp:0:8", ["const:d48:8"]]
- 006867ac ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006867ac ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006867ac ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006867ac ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 006867ac ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006867ac ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006867ac ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006867ac bytes 42203591
+ 006867ac bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0651ff228517725f7b1b251002f73ee6"></a>

### [`00686bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686bd4.md) → [`00686bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686bd4.md) FUN_00686bd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00686764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686764.md) · 呼出先 13件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md)
- 新版 呼出元 1件 [`00686764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686764.md) · 呼出先 13件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00445d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "definition_site": "00686c0c",
      "incomplete_value": true,
      "site": "00686c0c",
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
      "definition_site": "00686c0c",
      "incomplete_value": true,
      "site": "00686c0c",
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
      "definition_site": "00686c14",
      "incomplete_value": false,
      "site": "00686c24",
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
      "definition_site": "00686c14",
      "incomplete_value": false,
      "site": "00686c24",
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
      "definition_site": "00686c1c",
      "incomplete_value": false,
      "site": "00686c24",
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
      "definition_site": "00686c1c",
      "incomplete_value": false,
      "site": "00686c24",
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
      "00686c08",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00686c14",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00686c1c",
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
      "00686c08",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00686c14",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00686c1c",
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

- 旧版 [`00686c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686bd4.md#insn-00686c08) · [`00686c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686bd4.md#insn-00686c14) · [`00686c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686bd4.md#insn-00686c1c)
- 新版 `00686c08`（命令位置の公開資料なし） · `00686c14`（命令位置の公開資料なし） · `00686c1c`（命令位置の公開資料なし）

~~~diff
- 00686c08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00686c08 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00686c08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00686c08 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00686c08 bytes 003d45f9
+ 00686c08 bytes 005d45f9
- 00686c14 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00686c14 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00686c14 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00686c14 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00686c14 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00686c14 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00686c14 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00686c14 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00686c14 bytes 21203991
+ 00686c14 bytes 21603a91
- 00686c1c ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00686c1c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00686c1c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00686c1c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00686c1c ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00686c1c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00686c1c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00686c1c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00686c1c bytes 42203591
+ 00686c1c bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eecbdfeb0e2ed086adc981290087c1c9"></a>

### [`00687b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00687/00687b50.md) → [`00687b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00687/00687b50.md) FUN_00687b50

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
      "definition_site": "00687b70",
      "incomplete_value": false,
      "site": "00687b74",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00687b70",
      "incomplete_value": false,
      "site": "00687b74",
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
            "const:488:8"
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
      "00687b74",
      "DATA",
      [
        "storage",
        "00bf8488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00687b74",
      "DATA",
      [
        "storage",
        "00bf84d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00687b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00687/00687b50.md#insn-00687b70)
- 新版 `00687b70`（命令位置の公開資料なし）

~~~diff
- 00687b70 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00687b70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00687b70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00687b70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00687b70 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00687b70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00687b70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00687b70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00687b70 bytes 08211291
+ 00687b70 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f619eb68fb49742b7a40a6e8289a9fdf"></a>

### [`00687b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00687/00687b88.md) → [`00687b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00687/00687b88.md) FUN_00687b88

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
      "definition_site": "00687b8c",
      "incomplete_value": false,
      "site": "00687b90",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00687b8c",
      "incomplete_value": false,
      "site": "00687b90",
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
      "00687b90",
      "DATA",
      [
        "storage",
        "00bf8488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00687b90",
      "DATA",
      [
        "storage",
        "00bf84d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00687b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00687/00687b88.md#insn-00687b8c)
- 新版 `00687b8c`（命令位置の公開資料なし）

~~~diff
- 00687b8c ["COPY", "tmp:0:8", ["const:488:8"]]
- 00687b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00687b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00687b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00687b8c ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00687b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00687b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00687b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00687b8c bytes 08211291
+ 00687b8c bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b91125f27c2fcdb64937c61da5cc7fc5"></a>

### [`00687ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00687/00687ba8.md) → [`00687ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00687/00687ba8.md) FUN_00687ba8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 32件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 32件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.85% / 新版 95.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00687c8c",
      "incomplete_value": true,
      "site": "00687c8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a5e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00687c8c",
      "incomplete_value": true,
      "site": "00687c8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aeb:8"
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
      "definition_site": "00687cac",
      "incomplete_value": true,
      "site": "00687cbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00687cac",
      "incomplete_value": true,
      "site": "00687cbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:903:8"
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
      "definition_site": "00687cc0",
      "incomplete_value": true,
      "site": "00687cc0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00687cc0",
      "incomplete_value": true,
      "site": "00687cc0",
      "value": [
        "LOAD",
        "8",
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
      "00687c7c",
      "READ",
      [
        "storage",
        "00293aeb",
        null,
        "string"
      ]
    ],
    [
      "00687cac",
      "READ",
      [
        "storage",
        "002a5903",
        null,
        "string"
      ]
    ],
    [
      "00687cb0",
      "READ",
      [
        "storage",
        "002a5910",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00687c7c",
      "READ",
      [
        "storage",
        "00293a5e",
        null,
        "string"
      ]
    ],
    [
      "00687cac",
      "READ",
      [
        "storage",
        "002a598e",
        null,
        "string"
      ]
    ],
    [
      "00687cb0",
      "READ",
      [
        "storage",
        "002a599b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00687c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00687/00687ba8.md#insn-00687c78) · [`00687ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00687/00687ba8.md#insn-00687ca8) · [`00687ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00687/00687ba8.md#insn-00687ce4)
- 新版 `00687c78`（命令位置の公開資料なし） · `00687ca8`（命令位置の公開資料なし） · `00687ce4`（命令位置の公開資料なし）

~~~diff
- 00687c78 ["COPY", "tmp:0:8", ["const:aeb:8"]]
- 00687c78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00687c78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00687c78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00687c78 ["COPY", "tmp:0:8", ["const:a5e:8"]]
+ 00687c78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00687c78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00687c78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00687c78 bytes 08ad2b91
+ 00687c78 bytes 08792991
- 00687ca8 ["COPY", "tmp:0:8", ["const:903:8"]]
- 00687ca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00687ca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00687ca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00687ca8 ["COPY", "tmp:0:8", ["const:98e:8"]]
+ 00687ca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00687ca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00687ca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00687ca8 bytes 080d2491
+ 00687ca8 bytes 08392691
- 00687ce4 ["COPY", "tmp:0:8", ["const:830:8"]]
- 00687ce4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00687ce4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00687ce4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00687ce4 ["COPY", "tmp:0:8", ["const:8bb:8"]]
+ 00687ce4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00687ce4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00687ce4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00687ce4 bytes 08c12091
+ 00687ce4 bytes 08ed2291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deccfb2540fef2de131fae16f1c7757d"></a>

### [`00688fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00688/00688fbc.md) → [`00688fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00688/00688fbc.md) FUN_00688fbc

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
      "definition_site": "00688fdc",
      "incomplete_value": false,
      "site": "00688fe0",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00688fdc",
      "incomplete_value": false,
      "site": "00688fe0",
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
            "const:4f8:8"
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
      "00688fe0",
      "DATA",
      [
        "storage",
        "00bf84f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00688fe0",
      "DATA",
      [
        "storage",
        "00bf8548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00688fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00688/00688fbc.md#insn-00688fdc)
- 新版 `00688fdc`（命令位置の公開資料なし）

~~~diff
- 00688fdc ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00688fdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00688fdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00688fdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00688fdc ["COPY", "tmp:0:8", ["const:548:8"]]
+ 00688fdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00688fdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00688fdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00688fdc bytes 08e11391
+ 00688fdc bytes 08211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae6287a54d5a4b3bdd43f50abc8665bd"></a>

### [`00688ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00688/00688ff4.md) → [`00688ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00688/00688ff4.md) FUN_00688ff4

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
      "definition_site": "00688ff8",
      "incomplete_value": false,
      "site": "00688ffc",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00688ff8",
      "incomplete_value": false,
      "site": "00688ffc",
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
            "const:4f8:8"
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
      "00688ffc",
      "DATA",
      [
        "storage",
        "00bf84f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00688ffc",
      "DATA",
      [
        "storage",
        "00bf8548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00688ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00688/00688ff4.md#insn-00688ff8)
- 新版 `00688ff8`（命令位置の公開資料なし）

~~~diff
- 00688ff8 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00688ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00688ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00688ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00688ff8 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 00688ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00688ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00688ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00688ff8 bytes 08e11391
+ 00688ff8 bytes 08211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3f6e8cfd9612e7fde6521be4976bf8c"></a>

### [`00689014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689014.md) → [`00689014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689014.md) FUN_00689014

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`006806cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/006806cc.md) [`006891f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006891f8.md) [`006891fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006891fc.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`006806cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00680/006806cc.md) [`006891f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006891f8.md) [`006891fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006891fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006890a4",
      "incomplete_value": true,
      "site": "006890a4",
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
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006890a4",
      "incomplete_value": true,
      "site": "006890a4",
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
            "const:568:8"
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
      "006890a4",
      "DATA",
      [
        "storage",
        "00bf8568",
        null,
        "undefined *"
      ]
    ],
    [
      "0068910c",
      "READ",
      [
        "storage",
        "00bf8588",
        null,
        "pointer"
      ]
    ],
    [
      "0068910c",
      "READ",
      [
        "storage",
        "00bf8590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006890a4",
      "DATA",
      [
        "storage",
        "00bf85b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0068910c",
      "READ",
      [
        "storage",
        "00bf85d8",
        null,
        "pointer"
      ]
    ],
    [
      "0068910c",
      "READ",
      [
        "storage",
        "00bf85e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006890a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689014.md#insn-006890a0)
- 新版 `006890a0`（命令位置の公開資料なし）

~~~diff
- 006890a0 ["COPY", "tmp:0:8", ["const:568:8"]]
- 006890a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006890a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006890a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006890a0 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 006890a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006890a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006890a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006890a0 bytes 08a11591
+ 006890a0 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e8a2442a3994c253c965ea48dd3ad5f"></a>

### [`006891b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006891b0.md) → [`006891b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006891b0.md) FUN_006891b0

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
      "definition_site": "006891d4",
      "incomplete_value": false,
      "site": "006891d4",
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
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006891d4",
      "incomplete_value": false,
      "site": "006891d4",
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
            "const:568:8"
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
      "006891d4",
      "DATA",
      [
        "storage",
        "00bf8568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006891d4",
      "DATA",
      [
        "storage",
        "00bf85b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006891d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006891b0.md#insn-006891d0)
- 新版 `006891d0`（命令位置の公開資料なし）

~~~diff
- 006891d0 ["COPY", "tmp:0:8", ["const:568:8"]]
- 006891d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006891d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006891d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006891d0 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 006891d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006891d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006891d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006891d0 bytes 08a11591
+ 006891d0 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee047b7c5aa4bf83c85a93bb529ecd9b"></a>

### [`006891e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006891e4.md) → [`006891e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006891e4.md) FUN_006891e4

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
      "definition_site": "006891f0",
      "incomplete_value": false,
      "site": "006891f0",
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
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006891f0",
      "incomplete_value": false,
      "site": "006891f0",
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
            "const:568:8"
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
      "006891f0",
      "DATA",
      [
        "storage",
        "00bf8568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006891f0",
      "DATA",
      [
        "storage",
        "00bf85b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006891ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006891e4.md#insn-006891ec)
- 新版 `006891ec`（命令位置の公開資料なし）

~~~diff
- 006891ec ["COPY", "tmp:0:8", ["const:568:8"]]
- 006891ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006891ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006891ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006891ec ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 006891ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006891ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006891ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006891ec bytes 29a11591
+ 006891ec bytes 29e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-effcd4a8972a976f94d547a8fe35f78a"></a>

### [`0068928c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/0068928c.md) → [`0068928c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/0068928c.md) FUN_0068928c

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
      "definition_site": "006892ac",
      "incomplete_value": false,
      "site": "006892b0",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006892ac",
      "incomplete_value": false,
      "site": "006892b0",
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
            "const:5f8:8"
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
      "006892b0",
      "DATA",
      [
        "storage",
        "00bf85f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006892b0",
      "DATA",
      [
        "storage",
        "00bf8648",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006892ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/0068928c.md#insn-006892ac)
- 新版 `006892ac`（命令位置の公開資料なし）

~~~diff
- 006892ac ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 006892ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006892ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006892ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006892ac ["COPY", "tmp:0:8", ["const:648:8"]]
+ 006892ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006892ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006892ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006892ac bytes 08e11791
+ 006892ac bytes 08211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e35c8810ca414e1eb9c2c7074fa555f6"></a>

### [`006892c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006892c4.md) → [`006892c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006892c4.md) FUN_006892c4

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
      "definition_site": "006892c8",
      "incomplete_value": false,
      "site": "006892cc",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006892c8",
      "incomplete_value": false,
      "site": "006892cc",
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
            "const:5f8:8"
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
      "006892cc",
      "DATA",
      [
        "storage",
        "00bf85f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006892cc",
      "DATA",
      [
        "storage",
        "00bf8648",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006892c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006892c4.md#insn-006892c8)
- 新版 `006892c8`（命令位置の公開資料なし）

~~~diff
- 006892c8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 006892c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006892c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006892c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006892c8 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 006892c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006892c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006892c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006892c8 bytes 08e11791
+ 006892c8 bytes 08211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43a84bd40678d65ae602bb713d211be6"></a>

### [`00689370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689370.md) → [`00689370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689370.md) FUN_00689370

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
      "definition_site": "00689394",
      "incomplete_value": false,
      "site": "00689394",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00689394",
      "incomplete_value": false,
      "site": "00689394",
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
            "const:688:8"
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
      "00689394",
      "DATA",
      [
        "storage",
        "00bf8688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00689394",
      "DATA",
      [
        "storage",
        "00bf86d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00689390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689370.md#insn-00689390)
- 新版 `00689390`（命令位置の公開資料なし）

~~~diff
- 00689390 ["COPY", "tmp:0:8", ["const:688:8"]]
- 00689390 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00689390 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00689390 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00689390 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00689390 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00689390 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00689390 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00689390 bytes 08211a91
+ 00689390 bytes 08611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2441865f0f4ede6caed561de67f2374a"></a>

### [`006893a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006893a4.md) → [`006893a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006893a4.md) FUN_006893a4

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
      "definition_site": "006893b0",
      "incomplete_value": false,
      "site": "006893b0",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006893b0",
      "incomplete_value": false,
      "site": "006893b0",
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
            "const:688:8"
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
      "006893b0",
      "DATA",
      [
        "storage",
        "00bf8688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006893b0",
      "DATA",
      [
        "storage",
        "00bf86d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006893ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006893a4.md#insn-006893ac)
- 新版 `006893ac`（命令位置の公開資料なし）

~~~diff
- 006893ac ["COPY", "tmp:0:8", ["const:688:8"]]
- 006893ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006893ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006893ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006893ac ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 006893ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006893ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006893ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006893ac bytes 29211a91
+ 006893ac bytes 29611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48502c5ac1d3ceec79a478e1990d46a6"></a>

### [`006893c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006893c0.md) → [`006893c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006893c0.md) FUN_006893c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md) [`00886068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/00886068.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md) [`00886068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886068.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.94% / 新版 98.94%

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
      "definition_site": "0068940c",
      "incomplete_value": true,
      "site": "0068940c",
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
      "definition_site": "0068940c",
      "incomplete_value": true,
      "site": "0068940c",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00689414",
      "incomplete_value": false,
      "site": "00689424",
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
      "definition_site": "00689414",
      "incomplete_value": false,
      "site": "00689424",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0068941c",
      "incomplete_value": false,
      "site": "00689424",
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
      "definition_site": "0068941c",
      "incomplete_value": false,
      "site": "00689424",
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
      "00689408",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00689414",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0068941c",
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
      "00689408",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00689414",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0068941c",
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

- 旧版 [`00689408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006893c0.md#insn-00689408) · [`00689414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006893c0.md#insn-00689414) · [`0068941c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006893c0.md#insn-0068941c)
- 新版 `00689408`（命令位置の公開資料なし） · `00689414`（命令位置の公開資料なし） · `0068941c`（命令位置の公開資料なし）

~~~diff
- 00689408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00689408 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00689408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00689408 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00689408 bytes 003d45f9
+ 00689408 bytes 005d45f9
- 00689414 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00689414 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00689414 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00689414 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00689414 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00689414 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00689414 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00689414 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00689414 bytes 21203991
+ 00689414 bytes 21603a91
- 0068941c ["COPY", "tmp:0:8", ["const:d48:8"]]
- 0068941c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0068941c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0068941c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0068941c ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 0068941c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0068941c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0068941c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0068941c bytes 42203591
+ 0068941c bytes 42603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70dd670d72d7aacffcaf2875b80a7111"></a>

### [`006896dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006896dc.md) → [`006896dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006896dc.md) FUN_006896dc

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
      "definition_site": "006896fc",
      "incomplete_value": false,
      "site": "00689700",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006896fc",
      "incomplete_value": false,
      "site": "00689700",
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
            "const:708:8"
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
      "00689700",
      "DATA",
      [
        "storage",
        "00bf8708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00689700",
      "DATA",
      [
        "storage",
        "00bf8758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006896fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006896dc.md#insn-006896fc)
- 新版 `006896fc`（命令位置の公開資料なし）

~~~diff
- 006896fc ["COPY", "tmp:0:8", ["const:708:8"]]
- 006896fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006896fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006896fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006896fc ["COPY", "tmp:0:8", ["const:758:8"]]
+ 006896fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006896fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006896fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006896fc bytes 08211c91
+ 006896fc bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d3ef1c4fd575a5259b2e943f4967997"></a>

### [`00689714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689714.md) → [`00689714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689714.md) FUN_00689714

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
      "definition_site": "00689718",
      "incomplete_value": false,
      "site": "0068971c",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00689718",
      "incomplete_value": false,
      "site": "0068971c",
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
            "const:708:8"
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
      "0068971c",
      "DATA",
      [
        "storage",
        "00bf8708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0068971c",
      "DATA",
      [
        "storage",
        "00bf8758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00689718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689714.md#insn-00689718)
- 新版 `00689718`（命令位置の公開資料なし）

~~~diff
- 00689718 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00689718 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00689718 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00689718 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00689718 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00689718 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00689718 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00689718 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00689718 bytes 08211c91
+ 00689718 bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2354d139472ee8ee3046e13d124ae927"></a>

### [`00689848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689848.md) → [`00689848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689848.md) FUN_00689848

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
      "definition_site": "0068986c",
      "incomplete_value": false,
      "site": "0068986c",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068986c",
      "incomplete_value": false,
      "site": "0068986c",
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
            "const:788:8"
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
      "0068986c",
      "DATA",
      [
        "storage",
        "00bf8788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0068986c",
      "DATA",
      [
        "storage",
        "00bf87d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00689868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689848.md#insn-00689868)
- 新版 `00689868`（命令位置の公開資料なし）

~~~diff
- 00689868 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00689868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00689868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00689868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00689868 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00689868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00689868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00689868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00689868 bytes 08211e91
+ 00689868 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d29882b034f8e0b68da815314840c66"></a>

### [`0068987c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/0068987c.md) → [`0068987c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/0068987c.md) FUN_0068987c

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
      "definition_site": "00689888",
      "incomplete_value": false,
      "site": "00689888",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00689888",
      "incomplete_value": false,
      "site": "00689888",
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
            "const:788:8"
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
      "00689888",
      "DATA",
      [
        "storage",
        "00bf8788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00689888",
      "DATA",
      [
        "storage",
        "00bf87d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00689884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/0068987c.md#insn-00689884)
- 新版 `00689884`（命令位置の公開資料なし）

~~~diff
- 00689884 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00689884 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00689884 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00689884 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00689884 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00689884 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00689884 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00689884 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00689884 bytes 29211e91
+ 00689884 bytes 29611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00b1b29dc6c5f6ce6e93b8a6c497ff70"></a>

### [`0068991c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/0068991c.md) → [`0068991c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/0068991c.md) FUN_0068991c

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
      "definition_site": "00689940",
      "incomplete_value": false,
      "site": "00689940",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00689940",
      "incomplete_value": false,
      "site": "00689940",
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
            "const:808:8"
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
      "00689940",
      "DATA",
      [
        "storage",
        "00bf8808",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00689940",
      "DATA",
      [
        "storage",
        "00bf8858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068993c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/0068991c.md#insn-0068993c)
- 新版 `0068993c`（命令位置の公開資料なし）

~~~diff
- 0068993c ["COPY", "tmp:0:8", ["const:808:8"]]
- 0068993c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0068993c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0068993c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0068993c ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0068993c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0068993c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0068993c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0068993c bytes 08212091
+ 0068993c bytes 08612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3729ab55d88ca579cd9296f7861bfcc9"></a>

### [`00689950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689950.md) → [`00689950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689950.md) FUN_00689950

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
      "definition_site": "0068995c",
      "incomplete_value": false,
      "site": "0068995c",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068995c",
      "incomplete_value": false,
      "site": "0068995c",
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
            "const:808:8"
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
      "0068995c",
      "DATA",
      [
        "storage",
        "00bf8808",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0068995c",
      "DATA",
      [
        "storage",
        "00bf8858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00689958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689950.md#insn-00689958)
- 新版 `00689958`（命令位置の公開資料なし）

~~~diff
- 00689958 ["COPY", "tmp:0:8", ["const:808:8"]]
- 00689958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00689958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00689958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00689958 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 00689958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00689958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00689958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00689958 bytes 29212091
+ 00689958 bytes 29612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e2e72ba49fcd747d8da3517fd2c36cd"></a>

### [`00689b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689b20.md) → [`00689b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689b20.md) _INIT_101

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00689b5c",
      "incomplete_value": true,
      "site": "00689b78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00689b5c",
      "incomplete_value": true,
      "site": "00689b78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00689b80",
      "incomplete_value": true,
      "site": "00689b9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00689b80",
      "incomplete_value": true,
      "site": "00689b9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00689ba0",
      "incomplete_value": true,
      "site": "00689bbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00689ba0",
      "incomplete_value": true,
      "site": "00689bbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00689b5c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00689b80",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00689ba0",
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
      "00689b5c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00689b80",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00689ba0",
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

- 旧版 [`00689b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689b20.md#insn-00689b4c) · [`00689b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689b20.md#insn-00689b54)
- 新版 `00689b4c`（命令位置の公開資料なし） · `00689b54`（命令位置の公開資料なし）

~~~diff
- 00689b4c ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 00689b4c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00689b4c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00689b4c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00689b4c ["COPY", "tmp:0:8", ["const:800:8"]]
+ 00689b4c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00689b4c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00689b4c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00689b4c bytes 73021f91
+ 00689b4c bytes 73022091
- 00689b54 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00689b54 bytes e9e0ffd0
+ 00689b54 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00689b54 bytes e9e0ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb3682dd339ec61d5eacd7b9b1fff98"></a>

### [`00689eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689eb0.md) → [`00689eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689eb0.md) FUN_00689eb0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) · 呼出先 23件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`0068d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) · 呼出先 23件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.91% / 新版 88.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 66件, `store_destination` 21件, `store_value` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0068a0ac",
      "incomplete_value": true,
      "site": "0068a0ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:777:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068a0ac",
      "incomplete_value": true,
      "site": "0068a0ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0068a0c4",
      "incomplete_value": true,
      "site": "0068a0c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068a0c4",
      "incomplete_value": true,
      "site": "0068a0c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d41:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0068a0c8",
      "incomplete_value": true,
      "site": "0068a0c8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0068a0c8",
      "incomplete_value": true,
      "site": "0068a0c8",
      "value": [
        "LOAD",
        "8",
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
      "00689f0c",
      "DATA",
      [
        "storage",
        "00bf8888",
        null,
        "pointer"
      ]
    ],
    [
      "00689f24",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00689f38",
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
      "00689f0c",
      "DATA",
      [
        "storage",
        "00bf88d8",
        null,
        "pointer"
      ]
    ],
    [
      "00689f24",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00689f38",
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

- 旧版 [`00689ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689eb0.md#insn-00689ef8) · [`00689f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689eb0.md#insn-00689f20) · [`00689f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689eb0.md#insn-00689f30)
- 新版 `00689ef8`（命令位置の公開資料なし） · `00689f20`（命令位置の公開資料なし） · `00689f30`（命令位置の公開資料なし）

~~~diff
- 00689ef8 ["COPY", "tmp:0:8", ["const:888:8"]]
- 00689ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00689ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00689ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00689ef8 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00689ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00689ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00689ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00689ef8 bytes 08212291
+ 00689ef8 bytes 08612391
- 00689f20 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00689f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00689f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00689f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00689f20 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00689f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00689f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00689f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00689f20 bytes 08e10091
+ 00689f20 bytes 08e10191
- 00689f30 ["COPY", "tmp:0:8", ["const:895:8"]]
- 00689f30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00689f30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00689f30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00689f30 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00689f30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00689f30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00689f30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00689f30 bytes 29552291
+ 00689f30 bytes 29812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dd0718baf21e2ac92a09bdc3d6ffe2e"></a>

### [`0068d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md) → [`0068d0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d0f8.md) FUN_0068d0f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0068f070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068f/0068f070.md) · 呼出先 20件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)
- 新版 呼出元 1件 [`0068f070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068f/0068f070.md) · 呼出先 20件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0068d120",
      "incomplete_value": true,
      "site": "0068d120",
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
      "definition_site": "0068d120",
      "incomplete_value": true,
      "site": "0068d120",
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
      "definition_site": "0068d128",
      "incomplete_value": false,
      "site": "0068d13c",
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
      "definition_site": "0068d128",
      "incomplete_value": false,
      "site": "0068d13c",
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
      "definition_site": "0068d130",
      "incomplete_value": false,
      "site": "0068d13c",
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
      "definition_site": "0068d130",
      "incomplete_value": false,
      "site": "0068d13c",
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
      "0068d11c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0068d128",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0068d130",
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
      "0068d11c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0068d128",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0068d130",
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

- 旧版 [`0068d11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md#insn-0068d11c) · [`0068d128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md#insn-0068d128) · [`0068d130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md#insn-0068d130)
- 新版 `0068d11c`（命令位置の公開資料なし） · `0068d128`（命令位置の公開資料なし） · `0068d130`（命令位置の公開資料なし）

~~~diff
- 0068d11c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0068d11c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0068d11c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0068d11c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0068d11c bytes 083d45f9
+ 0068d11c bytes 085d45f9
- 0068d128 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0068d128 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0068d128 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0068d128 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0068d128 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0068d128 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0068d128 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0068d128 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0068d128 bytes 21203991
+ 0068d128 bytes 21603a91
- 0068d130 ["COPY", "tmp:0:8", ["const:298:8"]]
- 0068d130 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0068d130 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0068d130 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0068d130 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 0068d130 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0068d130 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0068d130 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0068d130 bytes 42600a91
+ 0068d130 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0b4ef082647d8942880b784a9397280"></a>

### [`0068d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) → [`0068d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) FUN_0068d484

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 19件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005be404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be404.md) [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 19件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`005be404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) [`00646dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646dc4.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0068d6e8",
      "incomplete_value": false,
      "site": "0068d6e8",
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
      "definition_site": "0068d6e8",
      "incomplete_value": false,
      "site": "0068d6e8",
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
    "ordinal": 74,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0068d6e0",
      "incomplete_value": true,
      "site": "0068d6e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0068d6e0",
      "incomplete_value": true,
      "site": "0068d6e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 74,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0068d6ec",
      "incomplete_value": false,
      "site": "0068d6ec",
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
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068d6ec",
      "incomplete_value": false,
      "site": "0068d6ec",
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "ordinal": 75,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0068d6e0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0068d6e4",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "0068d6e8",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0068d6e0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0068d6e4",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "0068d6e8",
      "WRITE",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068d6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md#insn-0068d6e8) · [`0068d6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md#insn-0068d6ec) · [`0068d704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md#insn-0068d704)
- 新版 `0068d6e8`（命令位置の公開資料なし） · `0068d6ec`（命令位置の公開資料なし） · `0068d704`（命令位置の公開資料なし）

~~~diff
- 0068d6e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 0068d6e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0068d6e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 0068d6e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0068d6e8 bytes 093505f9
+ 0068d6e8 bytes 095505f9
- 0068d6ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 0068d6ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0068d6ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 0068d6ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0068d6ec bytes aa3e05f9
+ 0068d6ec bytes aa5e05f9
- 0068d704 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 0068d704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 0068d704 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 0068d704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 0068d704 bytes b43e05f9
+ 0068d704 bytes b45e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6602b5ae5fac6015fb750c0cc51574e"></a>

### [`0068d810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d810.md) → [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) FUN_0068d810

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 59件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`00429060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429060.md) [`0042d878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d878.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 59件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`00429060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429060.md) [`0042d878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d878.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0068d9b0",
      "incomplete_value": false,
      "site": "0068d9b8",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068d9b0",
      "incomplete_value": false,
      "site": "0068d9b8",
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
            "const:9a8:8"
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
      "definition_site": "0068def8",
      "incomplete_value": false,
      "site": "0068def8",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068def8",
      "incomplete_value": false,
      "site": "0068def8",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0068ea7c",
      "incomplete_value": false,
      "site": "0068ea7c",
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
      "definition_site": "0068ea7c",
      "incomplete_value": false,
      "site": "0068ea7c",
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
    "ordinal": 144,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0068d848",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0068d854",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ],
    [
      "0068d878",
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
      "0068d848",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0068d854",
      "READ",
      [
        "storage",
        "00c25070",
        null,
        "undefined8"
      ]
    ],
    [
      "0068d878",
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

- 旧版 [`0068d844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d810.md#insn-0068d844) · [`0068d854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d810.md#insn-0068d854) · [`0068d878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d810.md#insn-0068d878)
- 新版 `0068d844`（命令位置の公開資料なし） · `0068d854`（命令位置の公開資料なし） · `0068d878`（命令位置の公開資料なし）

~~~diff
- 0068d844 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0068d844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0068d844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0068d844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0068d844 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0068d844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0068d844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0068d844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0068d844 bytes 08e10091
+ 0068d844 bytes 08e10191
- 0068d854 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 0068d854 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0068d854 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:70:8"]]
+ 0068d854 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0068d854 bytes 001940f9
+ 0068d854 bytes 003940f9
- 0068d878 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 0068d878 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0068d878 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 0068d878 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0068d878 bytes 203d45f9
+ 0068d878 bytes 205d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6a7a3f15f1e3d051bbad0083f9a8ce6"></a>

### [`0068f070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068f/0068f070.md) → [`0068f070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068f/0068f070.md) FUN_0068f070

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 31件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 31件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00445d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d88.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0068fe00",
      "incomplete_value": false,
      "site": "0068fe00",
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
      "definition_site": "0068fe00",
      "incomplete_value": false,
      "site": "0068fe00",
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
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0068fe04",
      "incomplete_value": false,
      "site": "0068fe04",
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
      "definition_site": "0068fe04",
      "incomplete_value": false,
      "site": "0068fe04",
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
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0068fe00",
      "incomplete_value": false,
      "site": "0068fe04",
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
      "definition_site": "0068fe00",
      "incomplete_value": false,
      "site": "0068fe04",
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
      "0068f0ac",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0068f0b8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0068f0c0",
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
      "0068f0ac",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0068f0b8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0068f0c0",
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

- 旧版 [`0068f0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068f/0068f070.md#insn-0068f0ac) · [`0068f0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068f/0068f070.md#insn-0068f0b8) · [`0068f0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068f/0068f070.md#insn-0068f0c0)
- 新版 `0068f0ac`（命令位置の公開資料なし） · `0068f0b8`（命令位置の公開資料なし） · `0068f0c0`（命令位置の公開資料なし）

~~~diff
- 0068f0ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0068f0ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0068f0ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0068f0ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0068f0ac bytes 083d45f9
+ 0068f0ac bytes 085d45f9
- 0068f0b8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0068f0b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0068f0b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0068f0b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0068f0b8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0068f0b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0068f0b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0068f0b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0068f0b8 bytes 21203991
+ 0068f0b8 bytes 21603a91
- 0068f0c0 ["COPY", "tmp:0:8", ["const:298:8"]]
- 0068f0c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0068f0c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0068f0c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0068f0c0 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 0068f0c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0068f0c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0068f0c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0068f0c0 bytes 42600a91
+ 0068f0c0 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c0f9ba55fe2dce92757202c24a2afa9"></a>

### [`00690d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00690/00690d9c.md) → [`00690d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00690/00690d9c.md) FUN_00690d9c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`00625684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00625/00625684.md) [`006280a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00628/006280a4.md) [`00629194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00629/00629194.md) [`006321e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/006321e8.md) [`006bf5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bf/006bf5a0.md) · 呼出先 15件 [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c4.md)
- 新版 呼出元 11件 [`00625684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00625/00625684.md) [`006280a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00628/006280a4.md) [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) [`006321e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/006321e8.md) [`006bf5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bf/006bf5a0.md) · 呼出先 15件 [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c9c4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.71% / 新版 94.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00690de4",
      "incomplete_value": false,
      "site": "00690de4",
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
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00690de4",
      "incomplete_value": false,
      "site": "00690de4",
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
            "const:aa8:8"
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
      "definition_site": "00690e70",
      "incomplete_value": true,
      "site": "00690e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b77:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00690e70",
      "incomplete_value": true,
      "site": "00690e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c04:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00690e9c",
      "incomplete_value": false,
      "site": "00690e9c",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00690e9c",
      "incomplete_value": false,
      "site": "00690e9c",
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
            "const:ba8:8"
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
      "00690de4",
      "DATA",
      [
        "storage",
        "00bf8aa8",
        null,
        "undefined *"
      ]
    ],
    [
      "00690e60",
      "READ",
      [
        "storage",
        "00292c04",
        null,
        "string"
      ]
    ],
    [
      "00690e9c",
      "DATA",
      [
        "storage",
        "00bf8ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00690de4",
      "DATA",
      [
        "storage",
        "00bf8af8",
        null,
        "undefined *"
      ]
    ],
    [
      "00690e60",
      "READ",
      [
        "storage",
        "00292b77",
        null,
        "string"
      ]
    ],
    [
      "00690e9c",
      "DATA",
      [
        "storage",
        "00bf8bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00690ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00690/00690d9c.md#insn-00690ddc) · [`00690e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00690/00690d9c.md#insn-00690e58) · [`00690e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00690/00690d9c.md#insn-00690e90)
- 新版 `00690ddc`（命令位置の公開資料なし） · `00690e58`（命令位置の公開資料なし） · `00690e90`（命令位置の公開資料なし）

~~~diff
- 00690ddc ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 00690ddc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00690ddc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00690ddc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00690ddc ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00690ddc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00690ddc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00690ddc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00690ddc bytes 08a12a91
+ 00690ddc bytes 08e12b91
- 00690e58 ["COPY", "tmp:0:8", ["const:c04:8"]]
- 00690e58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00690e58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00690e58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00690e58 ["COPY", "tmp:0:8", ["const:b77:8"]]
+ 00690e58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00690e58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00690e58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00690e58 bytes 29113091
+ 00690e58 bytes 29dd2d91
- 00690e90 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 00690e90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00690e90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00690e90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00690e90 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00690e90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00690e90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00690e90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00690e90 bytes 08a12e91
+ 00690e90 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64843201ef128adc9c8f6ed100c0b908"></a>

### [`00691178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691178.md) → [`00691178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691178.md) FUN_00691178

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006912dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006912dc.md) · 呼出先 6件 [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`0068be5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068b/0068be5c.md) [`00691300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691300.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`006912dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/006912dc.md) · 呼出先 6件 [`006582c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`0068be5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068b/0068be5c.md) [`00691300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691300.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00691190",
      "incomplete_value": false,
      "site": "00691198",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691190",
      "incomplete_value": false,
      "site": "00691198",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00691294",
      "incomplete_value": false,
      "site": "00691298",
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
      "definition_site": "00691294",
      "incomplete_value": false,
      "site": "00691298",
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
      "00691198",
      "DATA",
      [
        "storage",
        "00bf8888",
        null,
        "pointer"
      ]
    ],
    [
      "00691298",
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
      "00691198",
      "DATA",
      [
        "storage",
        "00bf88d8",
        null,
        "pointer"
      ]
    ],
    [
      "00691298",
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

- 旧版 [`00691190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691178.md#insn-00691190) · [`00691294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691178.md#insn-00691294)
- 新版 `00691190`（命令位置の公開資料なし） · `00691294`（命令位置の公開資料なし）

~~~diff
- 00691190 ["COPY", "tmp:0:8", ["const:888:8"]]
- 00691190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691190 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00691190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691190 bytes 08212291
+ 00691190 bytes 08612391
- 00691294 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00691294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691294 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00691294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691294 bytes 08610a91
+ 00691294 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-805e16405eecb309d5f9f49e29e36562"></a>

### [`006913d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006913d4.md) → [`006913d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/006913d4.md) FUN_006913d4

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
      "definition_site": "006913e8",
      "incomplete_value": false,
      "site": "006913ec",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006913e8",
      "incomplete_value": false,
      "site": "006913ec",
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
            "const:8a8:8"
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
      "006913ec",
      "DATA",
      [
        "storage",
        "00bf88a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006913ec",
      "DATA",
      [
        "storage",
        "00bf88f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006913e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006913d4.md#insn-006913e8)
- 新版 `006913e8`（命令位置の公開資料なし）

~~~diff
- 006913e8 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 006913e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006913e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006913e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006913e8 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 006913e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006913e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006913e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006913e8 bytes 08a12291
+ 006913e8 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1901cf7508e3f8e7ff4169ad5df65296"></a>

### [`006913f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006913f8.md) → [`006913f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/006913f8.md) FUN_006913f8

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
      "definition_site": "006913fc",
      "incomplete_value": false,
      "site": "00691400",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006913fc",
      "incomplete_value": false,
      "site": "00691400",
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
            "const:8a8:8"
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
      "00691400",
      "DATA",
      [
        "storage",
        "00bf88a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691400",
      "DATA",
      [
        "storage",
        "00bf88f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006913fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006913f8.md#insn-006913fc)
- 新版 `006913fc`（命令位置の公開資料なし）

~~~diff
- 006913fc ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 006913fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006913fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006913fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006913fc ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 006913fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006913fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006913fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006913fc bytes 08a12291
+ 006913fc bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a2c7d1d0018258196c748387f6aa335"></a>

### [`00691410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691410.md) → [`00691410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691410.md) FUN_00691410

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0069164c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/0069164c.md) [`00691650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691650.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0069164c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/0069164c.md) [`00691650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691650.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.59% / 新版 97.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006914b8",
      "incomplete_value": false,
      "site": "006914c0",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006914b8",
      "incomplete_value": false,
      "site": "006914c0",
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
            "const:918:8"
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
      "006914c0",
      "DATA",
      [
        "storage",
        "00bf8918",
        null,
        "undefined *"
      ]
    ],
    [
      "0069150c",
      "READ",
      [
        "storage",
        "00bf8938",
        null,
        "pointer"
      ]
    ],
    [
      "0069150c",
      "READ",
      [
        "storage",
        "00bf8940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006914c0",
      "DATA",
      [
        "storage",
        "00bf8968",
        null,
        "undefined *"
      ]
    ],
    [
      "0069150c",
      "READ",
      [
        "storage",
        "00bf8988",
        null,
        "pointer"
      ]
    ],
    [
      "0069150c",
      "READ",
      [
        "storage",
        "00bf8990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006914b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691410.md#insn-006914b8)
- 新版 `006914b8`（命令位置の公開資料なし）

~~~diff
- 006914b8 ["COPY", "tmp:0:8", ["const:918:8"]]
- 006914b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006914b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006914b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006914b8 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 006914b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006914b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006914b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006914b8 bytes 08612491
+ 006914b8 bytes 08a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e8bb01fb6e80c3f635be54de98315ae"></a>

### [`00691618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691618.md) → [`00691618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691618.md) FUN_00691618

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
      "definition_site": "0069162c",
      "incomplete_value": false,
      "site": "00691630",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0069162c",
      "incomplete_value": false,
      "site": "00691630",
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
            "const:918:8"
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
      "00691630",
      "DATA",
      [
        "storage",
        "00bf8918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691630",
      "DATA",
      [
        "storage",
        "00bf8968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069162c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691618.md#insn-0069162c)
- 新版 `0069162c`（命令位置の公開資料なし）

~~~diff
- 0069162c ["COPY", "tmp:0:8", ["const:918:8"]]
- 0069162c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0069162c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0069162c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0069162c ["COPY", "tmp:0:8", ["const:968:8"]]
+ 0069162c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0069162c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0069162c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0069162c bytes 08612491
+ 0069162c bytes 08a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-484707a14b1f9c3ade98fda2a62e7f12"></a>

### [`0069163c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/0069163c.md) → [`0069163c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/0069163c.md) FUN_0069163c

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
      "definition_site": "00691640",
      "incomplete_value": false,
      "site": "00691644",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691640",
      "incomplete_value": false,
      "site": "00691644",
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
            "const:918:8"
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
      "00691644",
      "DATA",
      [
        "storage",
        "00bf8918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691644",
      "DATA",
      [
        "storage",
        "00bf8968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/0069163c.md#insn-00691640)
- 新版 `00691640`（命令位置の公開資料なし）

~~~diff
- 00691640 ["COPY", "tmp:0:8", ["const:918:8"]]
- 00691640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691640 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00691640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691640 bytes 08612491
+ 00691640 bytes 08a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c201abd8dd712f7a5dd43983a7dab466"></a>

### [`006916f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006916f4.md) → [`006916f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/006916f4.md) FUN_006916f4

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
      "definition_site": "00691708",
      "incomplete_value": false,
      "site": "0069170c",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691708",
      "incomplete_value": false,
      "site": "0069170c",
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
      "0069170c",
      "DATA",
      [
        "storage",
        "00bf89a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069170c",
      "DATA",
      [
        "storage",
        "00bf89f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006916f4.md#insn-00691708)
- 新版 `00691708`（命令位置の公開資料なし）

~~~diff
- 00691708 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 00691708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691708 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00691708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691708 bytes 08a12691
+ 00691708 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c70765b34ba81c0ceef52bb58781576"></a>

### [`00691718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691718.md) → [`00691718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691718.md) FUN_00691718

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
      "definition_site": "0069171c",
      "incomplete_value": false,
      "site": "00691720",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0069171c",
      "incomplete_value": false,
      "site": "00691720",
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
      "00691720",
      "DATA",
      [
        "storage",
        "00bf89a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691720",
      "DATA",
      [
        "storage",
        "00bf89f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069171c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691718.md#insn-0069171c)
- 新版 `0069171c`（命令位置の公開資料なし）

~~~diff
- 0069171c ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 0069171c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0069171c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0069171c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0069171c ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 0069171c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0069171c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0069171c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0069171c bytes 08a12691
+ 0069171c bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b9d14d68b08fa343d59656151012f61"></a>

### [`0069179c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/0069179c.md) → [`0069179c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/0069179c.md) FUN_0069179c

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
      "definition_site": "006917b0",
      "incomplete_value": false,
      "site": "006917b4",
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006917b0",
      "incomplete_value": false,
      "site": "006917b4",
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
            "const:a28:8"
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
      "006917b4",
      "DATA",
      [
        "storage",
        "00bf8a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006917b4",
      "DATA",
      [
        "storage",
        "00bf8a78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006917b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/0069179c.md#insn-006917b0)
- 新版 `006917b0`（命令位置の公開資料なし）

~~~diff
- 006917b0 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 006917b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006917b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006917b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006917b0 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 006917b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006917b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006917b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006917b0 bytes 08a12891
+ 006917b0 bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b6b5744ef07b383567356eef14c923c"></a>

### [`006917c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006917c0.md) → [`006917c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/006917c0.md) FUN_006917c0

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
      "definition_site": "006917c4",
      "incomplete_value": false,
      "site": "006917c8",
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006917c4",
      "incomplete_value": false,
      "site": "006917c8",
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
            "const:a28:8"
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
      "006917c8",
      "DATA",
      [
        "storage",
        "00bf8a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006917c8",
      "DATA",
      [
        "storage",
        "00bf8a78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006917c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006917c0.md#insn-006917c4)
- 新版 `006917c4`（命令位置の公開資料なし）

~~~diff
- 006917c4 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 006917c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006917c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006917c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006917c4 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 006917c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006917c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006917c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006917c4 bytes 08a12891
+ 006917c4 bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-271414a091800bf710a585ee856733dd"></a>

### [`00691844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691844.md) → [`00691844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691844.md) FUN_00691844

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
      "definition_site": "00691868",
      "incomplete_value": false,
      "site": "00691868",
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
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691868",
      "incomplete_value": false,
      "site": "00691868",
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
            "const:aa8:8"
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
      "00691868",
      "DATA",
      [
        "storage",
        "00bf8aa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691868",
      "DATA",
      [
        "storage",
        "00bf8af8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691844.md#insn-00691864)
- 新版 `00691864`（命令位置の公開資料なし）

~~~diff
- 00691864 ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 00691864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691864 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00691864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691864 bytes 08a12a91
+ 00691864 bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a1528075bba77376ee9c5374f12ea82"></a>

### [`00691878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691878.md) → [`00691878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691878.md) FUN_00691878

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
      "definition_site": "0069187c",
      "incomplete_value": false,
      "site": "00691880",
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
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0069187c",
      "incomplete_value": false,
      "site": "00691880",
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
            "const:aa8:8"
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
      "00691880",
      "DATA",
      [
        "storage",
        "00bf8aa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691880",
      "DATA",
      [
        "storage",
        "00bf8af8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069187c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691878.md#insn-0069187c)
- 新版 `0069187c`（命令位置の公開資料なし）

~~~diff
- 0069187c ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 0069187c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0069187c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0069187c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0069187c ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 0069187c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0069187c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0069187c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0069187c bytes 08a12a91
+ 0069187c bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64213037880a4b95bc77a88566731f49"></a>

### [`006918c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006918c8.md) → [`006918c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/006918c8.md) FUN_006918c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00691898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691898.md) [`00691d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691d54.md) [`00691ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691ddc.md) [`00691e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691e64.md) · 呼出先 10件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md) [`0052dae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dae4.md) [`00574ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 4件 [`00691898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691898.md) [`00691d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691d54.md) [`00691ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691ddc.md) [`00691e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691e64.md) · 呼出先 10件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md) [`0052dae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dae4.md) [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.48% / 新版 95.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00691934",
      "incomplete_value": true,
      "site": "00691934",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b77:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691934",
      "incomplete_value": true,
      "site": "00691934",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c04:8"
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
      "definition_site": "00691a9c",
      "incomplete_value": true,
      "site": "00691aac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c8c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691a9c",
      "incomplete_value": true,
      "site": "00691aac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d20:8"
              ]
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
    "kind": "store_value",
    "new": {
      "definition_site": "00691aa0",
      "incomplete_value": true,
      "site": "00691ab0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00691aa0",
      "incomplete_value": true,
      "site": "00691ab0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00691920",
      "READ",
      [
        "storage",
        "00292c04",
        null,
        "string"
      ]
    ],
    [
      "00691a9c",
      "READ",
      [
        "storage",
        "002aed20",
        null,
        "string"
      ]
    ],
    [
      "00691aa0",
      "READ",
      [
        "storage",
        "002aed29",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00691920",
      "READ",
      [
        "storage",
        "00292b77",
        null,
        "string"
      ]
    ],
    [
      "00691a9c",
      "READ",
      [
        "storage",
        "002aec8c",
        null,
        "string"
      ]
    ],
    [
      "00691aa0",
      "READ",
      [
        "storage",
        "002aec95",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069191c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006918c8.md#insn-0069191c) · [`00691a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006918c8.md#insn-00691a94) · [`00691a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/006918c8.md#insn-00691a98)
- 新版 `0069191c`（命令位置の公開資料なし） · `00691a94`（命令位置の公開資料なし）

~~~diff
- 0069191c ["COPY", "tmp:0:8", ["const:c04:8"]]
- 0069191c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0069191c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0069191c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0069191c ["COPY", "tmp:0:8", ["const:b77:8"]]
+ 0069191c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0069191c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0069191c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0069191c bytes 29113091
+ 0069191c bytes 29dd2d91
- 00691a94 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00691a94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691a94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691a94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691a94 ["COPY", "tmp:0:8", ["const:c8c:8"]]
+ 00691a94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691a94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691a94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691a94 bytes 08813491
+ 00691a94 bytes 08313291
- 00691a98 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00691a98 bytes 09e1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0187439b2898ff629dc8eb4efd3a8891"></a>

### [`00691d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691d00.md) → [`00691d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691d00.md) FUN_00691d00

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
      "definition_site": "00691d24",
      "incomplete_value": false,
      "site": "00691d24",
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
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691d24",
      "incomplete_value": false,
      "site": "00691d24",
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
            "const:b28:8"
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
      "00691d24",
      "DATA",
      [
        "storage",
        "00bf8b28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691d24",
      "DATA",
      [
        "storage",
        "00bf8b78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691d00.md#insn-00691d20)
- 新版 `00691d20`（命令位置の公開資料なし）

~~~diff
- 00691d20 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00691d20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691d20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691d20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691d20 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00691d20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691d20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691d20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691d20 bytes 08a12c91
+ 00691d20 bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60404ba05fd68f53063f0cfe0e4dbc9b"></a>

### [`00691d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691d34.md) → [`00691d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691d34.md) FUN_00691d34

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
      "definition_site": "00691d38",
      "incomplete_value": false,
      "site": "00691d3c",
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
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691d38",
      "incomplete_value": false,
      "site": "00691d3c",
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
            "const:b28:8"
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
      "00691d3c",
      "DATA",
      [
        "storage",
        "00bf8b28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691d3c",
      "DATA",
      [
        "storage",
        "00bf8b78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691d34.md#insn-00691d38)
- 新版 `00691d38`（命令位置の公開資料なし）

~~~diff
- 00691d38 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00691d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691d38 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00691d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691d38 bytes 08a12c91
+ 00691d38 bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08047b7cc8afe4210d2275730e60f3e1"></a>

### [`00691d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691d88.md) → [`00691d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691d88.md) FUN_00691d88

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
      "definition_site": "00691dac",
      "incomplete_value": false,
      "site": "00691dac",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691dac",
      "incomplete_value": false,
      "site": "00691dac",
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
            "const:ba8:8"
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
      "00691dac",
      "DATA",
      [
        "storage",
        "00bf8ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691dac",
      "DATA",
      [
        "storage",
        "00bf8bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691d88.md#insn-00691da8)
- 新版 `00691da8`（命令位置の公開資料なし）

~~~diff
- 00691da8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 00691da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691da8 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00691da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691da8 bytes 08a12e91
+ 00691da8 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc6db573a533228abb548735486486d5"></a>

### [`00691dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691dbc.md) → [`00691dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691dbc.md) FUN_00691dbc

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
      "definition_site": "00691dc0",
      "incomplete_value": false,
      "site": "00691dc4",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691dc0",
      "incomplete_value": false,
      "site": "00691dc4",
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
      "00691dc4",
      "DATA",
      [
        "storage",
        "00bf8ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691dc4",
      "DATA",
      [
        "storage",
        "00bf8bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691dbc.md#insn-00691dc0)
- 新版 `00691dc0`（命令位置の公開資料なし）

~~~diff
- 00691dc0 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 00691dc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691dc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691dc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691dc0 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00691dc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691dc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691dc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691dc0 bytes 08a12e91
+ 00691dc0 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d9b20de214923ab39755fdf9833c528"></a>

### [`00691e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691e10.md) → [`00691e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691e10.md) FUN_00691e10

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
      "definition_site": "00691e34",
      "incomplete_value": false,
      "site": "00691e34",
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
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691e34",
      "incomplete_value": false,
      "site": "00691e34",
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
            "const:c28:8"
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
      "00691e34",
      "DATA",
      [
        "storage",
        "00bf8c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691e34",
      "DATA",
      [
        "storage",
        "00bf8c78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691e10.md#insn-00691e30)
- 新版 `00691e30`（命令位置の公開資料なし）

~~~diff
- 00691e30 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00691e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691e30 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00691e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691e30 bytes 08a13091
+ 00691e30 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d573e51b90a04824d5251b43557d350f"></a>

### [`00691e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691e44.md) → [`00691e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691e44.md) FUN_00691e44

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
      "definition_site": "00691e48",
      "incomplete_value": false,
      "site": "00691e4c",
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
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00691e48",
      "incomplete_value": false,
      "site": "00691e4c",
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
      "00691e4c",
      "DATA",
      [
        "storage",
        "00bf8c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00691e4c",
      "DATA",
      [
        "storage",
        "00bf8c78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00691e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691e44.md#insn-00691e48)
- 新版 `00691e48`（命令位置の公開資料なし）

~~~diff
- 00691e48 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00691e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00691e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00691e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00691e48 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00691e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00691e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00691e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00691e48 bytes 08a13091
+ 00691e48 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2af2b3f906c12857134d5753589716d5"></a>

### [`00691e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691e94.md) → [`00691e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691e94.md) _INIT_102

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00691ef4",
      "incomplete_value": true,
      "site": "00691f10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00691ef4",
      "incomplete_value": true,
      "site": "00691f10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00691f14",
      "incomplete_value": true,
      "site": "00691f30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00691f14",
      "incomplete_value": true,
      "site": "00691f30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00691f50",
      "incomplete_value": true,
      "site": "00691f6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00691f50",
      "incomplete_value": true,
      "site": "00691f6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00691ed0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00691ef4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00691f14",
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
      "00691ed0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00691ef4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00691f14",
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

- 旧版 [`00691ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691e94.md#insn-00691ec0) · [`00691ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691e94.md#insn-00691ec8)
- 新版 `00691ec0`（命令位置の公開資料なし） · `00691ec8`（命令位置の公開資料なし）

~~~diff
- 00691ec0 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00691ec0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00691ec0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00691ec0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00691ec0 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00691ec0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00691ec0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00691ec0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00691ec0 bytes 73621f91
+ 00691ec0 bytes 73622091
- 00691ec8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00691ec8 bytes a9e0ffd0
+ 00691ec8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00691ec8 bytes a9e0ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7225d83d31673c5e33ffe7574c0b970"></a>

### [`00692224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/00692224.md) → [`00692224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/00692224.md) FUN_00692224

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ab1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) · 呼出先 20件 [`0041e03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e03c.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ab1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) · 呼出先 20件 [`0041e03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e03c.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.64% / 新版 95.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00692264",
      "incomplete_value": false,
      "site": "0069226c",
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
      "definition_site": "00692264",
      "incomplete_value": false,
      "site": "0069226c",
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
      "definition_site": "00692538",
      "incomplete_value": true,
      "site": "0069253c",
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
      "definition_site": "00692538",
      "incomplete_value": true,
      "site": "0069253c",
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
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00692534",
      "incomplete_value": true,
      "site": "00692540",
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
      "definition_site": "00692534",
      "incomplete_value": true,
      "site": "00692540",
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
    "ordinal": 44,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0069226c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006924b8",
      "READ",
      [
        "storage",
        "00c1b6d8",
        null,
        "pointer"
      ]
    ],
    [
      "00692528",
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
      "0069226c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006924b8",
      "READ",
      [
        "storage",
        "00c1b728",
        null,
        "pointer"
      ]
    ],
    [
      "00692528",
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

- 旧版 [`00692264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/00692224.md#insn-00692264) · [`006924b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/00692224.md#insn-006924b8) · [`00692528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/00692224.md#insn-00692528)
- 新版 `00692264`（命令位置の公開資料なし） · `006924b8`（命令位置の公開資料なし） · `00692528`（命令位置の公開資料なし）

~~~diff
- 00692264 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00692264 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00692264 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00692264 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00692264 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00692264 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00692264 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00692264 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00692264 bytes 08a13491
+ 00692264 bytes 08e13591
- 006924b8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:6d8:8"]]
- 006924b8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 006924b8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
+ 006924b8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 006924b8 bytes f76e43f9
+ 006924b8 bytes f79643f9
- 00692528 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 00692528 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00692528 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00692528 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00692528 bytes 08b946f9
+ 00692528 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4db6ae9e1939810e3174895723fba6e"></a>

### [`006928b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/006928b0.md) → [`006928b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/006928b0.md) FUN_006928b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 16件 [`00692224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/00692224.md) [`006928c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/006928c4.md) [`00692bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/00692bcc.md) [`00693650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00693/00693650.md) [`006941ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00694/006941ac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 15件 [`00692224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/00692224.md) [`006928c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/006928c4.md) [`00692bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/00692bcc.md) [`00693650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00693/00693650.md) [`006941ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00694/006941ac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "006928bc",
      "incomplete_value": false,
      "site": "006928c0",
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
      "definition_site": "006928bc",
      "incomplete_value": false,
      "site": "006928c0",
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
      "006928bc",
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
      "006928bc",
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

- 旧版 [`006928bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/006928b0.md#insn-006928bc)
- 新版 `006928bc`（命令位置の公開資料なし）

~~~diff
- 006928bc ["COPY", "tmp:0:8", ["const:303:8"]]
- 006928bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006928bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006928bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006928bc ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 006928bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006928bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006928bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006928bc bytes 000c0c91
+ 006928bc bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c45fe01647c7c917762090cf706dcbcb"></a>

### [`00692bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/00692bb8.md) → [`00692bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/00692bb8.md) FUN_00692bb8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006928c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/006928c4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006928c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/006928c4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00692bc4",
      "incomplete_value": false,
      "site": "00692bc8",
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
      "definition_site": "00692bc4",
      "incomplete_value": false,
      "site": "00692bc8",
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
      "00692bc4",
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
      "00692bc4",
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

- 旧版 [`00692bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/00692bb8.md#insn-00692bc4)
- 新版 `00692bc4`（命令位置の公開資料なし）

~~~diff
- 00692bc4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00692bc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00692bc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00692bc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692bc4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00692bc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692bc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692bc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00692bc4 bytes 000c0c91
+ 00692bc4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de86d24d271334a00e644d55ba93014a"></a>

### [`00694fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00694/00694fd0.md) → [`00694fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00694/00694fd0.md) _INIT_103

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
      "definition_site": "0069500c",
      "incomplete_value": true,
      "site": "00695028",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0069500c",
      "incomplete_value": true,
      "site": "00695028",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00695030",
      "incomplete_value": true,
      "site": "0069504c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00695030",
      "incomplete_value": true,
      "site": "0069504c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00695050",
      "incomplete_value": true,
      "site": "0069506c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00695050",
      "incomplete_value": true,
      "site": "0069506c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0069500c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00695030",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00695050",
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
      "0069500c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00695030",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00695050",
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

- 旧版 [`00694ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00694/00694fd0.md#insn-00694ffc) · [`00695004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00694/00694fd0.md#insn-00695004)
- 新版 `00694ffc`（命令位置の公開資料なし） · `00695004`（命令位置の公開資料なし）

~~~diff
- 00694ffc ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00694ffc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00694ffc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00694ffc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00694ffc ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00694ffc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00694ffc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00694ffc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00694ffc bytes 73c21f91
+ 00694ffc bytes 73c22091
- 00695004 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00695004 bytes 89e0ffd0
+ 00695004 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00695004 bytes 89e0ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ce43c3be1f90baa484dc0e298c38687"></a>

### [`00695574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695574.md) → [`00695574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695574.md) _INIT_104

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
      "definition_site": "006955f4",
      "incomplete_value": true,
      "site": "00695610",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006955f4",
      "incomplete_value": true,
      "site": "00695610",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00695630",
      "incomplete_value": true,
      "site": "0069564c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00695630",
      "incomplete_value": true,
      "site": "0069564c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069579c",
      "incomplete_value": false,
      "site": "006957a8",
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
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0069579c",
      "incomplete_value": false,
      "site": "006957a8",
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
            "const:808:8"
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
      "006955b0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006955d4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006955f4",
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
      "006955b0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006955d4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006955f4",
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

- 旧版 [`006955a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695574.md#insn-006955a0) · [`006955a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695574.md#insn-006955a8)
- 新版 `006955a0`（命令位置の公開資料なし） · `006955a8`（命令位置の公開資料なし）

~~~diff
- 006955a0 ["COPY", "tmp:0:8", ["const:808:8"]]
- 006955a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006955a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006955a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006955a0 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 006955a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006955a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006955a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006955a0 bytes 73222091
+ 006955a0 bytes 73222191
- 006955a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006955a8 bytes 89e0ffd0
+ 006955a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006955a8 bytes 89e0ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebb6e6106e7227cd13ba47537a005edc"></a>

### [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) → [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) FUN_00695904

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`006525c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00652/006525c0.md) [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`008f06a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f0/008f06a0.md) · 呼出先 105件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md)
- 新版 呼出元 4件 [`006525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`008f06a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f0/008f06a0.md) · 呼出先 105件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 98.99% / 新版 98.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 7件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00697dc0",
      "incomplete_value": false,
      "site": "00697dc0",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00697dc0",
      "incomplete_value": false,
      "site": "00697dc0",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "ordinal": 372,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00698434",
      "incomplete_value": false,
      "site": "00698434",
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
      "definition_site": "00698434",
      "incomplete_value": false,
      "site": "00698434",
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
    "ordinal": 442,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00698438",
      "incomplete_value": false,
      "site": "00698438",
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
      "definition_site": "00698438",
      "incomplete_value": false,
      "site": "00698438",
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
    "ordinal": 443,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00695b08",
      "PARAM",
      [
        "storage",
        "00299112",
        null,
        "string"
      ]
    ],
    [
      "00695db4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00695dc0",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00695b08",
      "PARAM",
      [
        "storage",
        "00299085",
        null,
        "string"
      ]
    ],
    [
      "00695db4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00695dc0",
      "READ",
      [
        "storage",
        "00c25070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00695b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md#insn-00695b08) · [`00695db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md#insn-00695db0) · [`00695dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md#insn-00695dc0)
- 新版 `00695b08`（命令位置の公開資料なし） · `00695db0`（命令位置の公開資料なし） · `00695dc0`（命令位置の公開資料なし）

~~~diff
- 00695b08 ["COPY", "tmp:0:8", ["const:112:8"]]
- 00695b08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00695b08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00695b08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00695b08 ["COPY", "tmp:0:8", ["const:85:8"]]
+ 00695b08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00695b08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00695b08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00695b08 bytes 21480491
+ 00695b08 bytes 21140291
- 00695db0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00695db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00695db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00695db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00695db0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00695db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00695db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00695db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00695db0 bytes 08e10091
+ 00695db0 bytes 08e10191
- 00695dc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 00695dc0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00695dc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:70:8"]]
+ 00695dc0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00695dc0 bytes 001940f9
+ 00695dc0 bytes 003940f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05649b8a2187e847b4f0bd850455e630"></a>

### [`00698648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/00698648.md) → [`00698648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00698/00698648.md) FUN_00698648

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 5件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00699d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00699/00699d04.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 2件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 5件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00699d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/00699d04.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00698658",
      "incomplete_value": true,
      "site": "00698658",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00698658",
      "incomplete_value": true,
      "site": "00698658",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00698690",
      "incomplete_value": false,
      "site": "00698694",
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
      "definition_site": "00698690",
      "incomplete_value": false,
      "site": "00698694",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006986b4",
      "incomplete_value": true,
      "site": "006986d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006986b4",
      "incomplete_value": true,
      "site": "006986d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "00698654",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00698658",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00698674",
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
      "00698654",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00698658",
      "WRITE",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00698674",
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

- 旧版 [`00698658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/00698648.md#insn-00698658) · [`00698654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/00698648.md#insn-00698654) · [`00698670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/00698648.md#insn-00698670)
- 新版 `00698658`（命令位置の公開資料なし） · `00698654`（命令位置の公開資料なし） · `00698670`（命令位置の公開資料なし）

~~~diff
- 00698658 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00698658 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00698658 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00698658 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 00698658 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00698658 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00698658 bytes 1f3505f9
+ 00698658 bytes 1f5505f9
- 00698654 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00698654 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00698654 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 00698654 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00698654 bytes 003545f9
+ 00698654 bytes 005545f9
- 00698670 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00698670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00698670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00698670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00698670 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00698670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00698670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00698670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00698670 bytes 08e10091
+ 00698670 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-387e74fbfebf967ae07fe454099b008f"></a>

### [`006989b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/006989b8.md) → [`006989b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00698/006989b8.md) FUN_006989b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) · 呼出先 24件 [`005bfb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bf/005bfb9c.md) [`005c0108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c0/005c0108.md) [`005c3468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3468.md) [`00699c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00699/00699c78.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md)
- 新版 呼出元 1件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 24件 [`005bfb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bf/005bfb9c.md) [`005c0108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c0108.md) [`005c3468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c3/005c3468.md) [`00699c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/00699c78.md) [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.70% / 新版 92.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 15件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00698a38",
      "incomplete_value": false,
      "site": "00698a40",
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
      "definition_site": "00698a38",
      "incomplete_value": false,
      "site": "00698a40",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00698a60",
      "incomplete_value": false,
      "site": "00698a6c",
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
      "definition_site": "00698a60",
      "incomplete_value": false,
      "site": "00698a6c",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00698a98",
      "incomplete_value": false,
      "site": "00698a9c",
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
      "definition_site": "00698a98",
      "incomplete_value": false,
      "site": "00698a9c",
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
      "00698a40",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "00698a6c",
      "DATA",
      [
        "storage",
        "002a69a3",
        null,
        "string"
      ]
    ],
    [
      "00698a9c",
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
      "00698a40",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ],
    [
      "00698a6c",
      "DATA",
      [
        "storage",
        "002a6a3d",
        null,
        "string"
      ]
    ],
    [
      "00698a9c",
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

- 旧版 [`00698a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/006989b8.md#insn-00698a38) · [`00698a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/006989b8.md#insn-00698a60) · [`00698a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/006989b8.md#insn-00698a98)
- 新版 `00698a38`（命令位置の公開資料なし） · `00698a60`（命令位置の公開資料なし） · `00698a98`（命令位置の公開資料なし）

~~~diff
- 00698a38 ["COPY", "tmp:0:8", ["const:6a4:8"]]
- 00698a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00698a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00698a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00698a38 ["COPY", "tmp:0:8", ["const:72f:8"]]
+ 00698a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00698a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00698a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00698a38 bytes 08911a91
+ 00698a38 bytes 08bd1c91
- 00698a60 ["COPY", "tmp:0:8", ["const:9a3:8"]]
- 00698a60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00698a60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00698a60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00698a60 ["COPY", "tmp:0:8", ["const:a3d:8"]]
+ 00698a60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00698a60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00698a60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00698a60 bytes 088d2691
+ 00698a60 bytes 08f52891
- 00698a98 ["COPY", "tmp:0:8", ["const:731:8"]]
- 00698a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00698a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00698a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00698a98 ["COPY", "tmp:0:8", ["const:7bc:8"]]
+ 00698a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00698a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00698a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00698a98 bytes 08c51c91
+ 00698a98 bytes 08f11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-011974ca62c181422a0c4c9d271858f1"></a>

### [`006994e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00699/006994e8.md) → [`006994e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/006994e8.md) FUN_006994e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`006534e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00653/006534e0.md) [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) [`008f17a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f1/008f17a8.md) · 呼出先 10件 [`00444c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c24.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00445124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445124.md)
- 新版 呼出元 4件 [`006534e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00653/006534e0.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) [`008f17a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f1/008f17a8.md) · 呼出先 10件 [`00444c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c24.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00445124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445124.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.14% / 新版 98.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00699654",
      "incomplete_value": false,
      "site": "00699658",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00699654",
      "incomplete_value": false,
      "site": "00699658",
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
            "const:d70:8"
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
      "definition_site": "006996c4",
      "incomplete_value": false,
      "site": "006996c8",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006996c4",
      "incomplete_value": false,
      "site": "006996c8",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00699724",
      "incomplete_value": false,
      "site": "00699728",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00699724",
      "incomplete_value": false,
      "site": "00699728",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00699520",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00699534",
      "READ",
      [
        "storage",
        "00c24d94",
        null,
        "undefined4"
      ]
    ],
    [
      "00699654",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00699520",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00699534",
      "READ",
      [
        "storage",
        "00c24dd4",
        null,
        "undefined4"
      ]
    ],
    [
      "00699654",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00699520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00699/006994e8.md#insn-00699520) · [`00699654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00699/006994e8.md#insn-00699654) · [`006996c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00699/006994e8.md#insn-006996c4)
- 新版 `00699520`（命令位置の公開資料なし） · `00699654`（命令位置の公開資料なし） · `006996c4`（命令位置の公開資料なし）

~~~diff
- 00699520 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d28:8"]]
- 00699520 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00699520 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d78:8"]]
+ 00699520 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00699520 bytes 089546f9
+ 00699520 bytes 08bd46f9
- 00699654 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 00699654 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00699654 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00699654 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00699654 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 00699654 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00699654 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00699654 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00699654 bytes 00c03591
+ 00699654 bytes 00c03691
- 006996c4 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 006996c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006996c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006996c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006996c4 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 006996c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006996c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006996c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006996c4 bytes 00c03591
+ 006996c4 bytes 00c03691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28818a5dd4190a161a773ff1c5620d58"></a>

### [`00699fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00699/00699fcc.md) → [`00699fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/00699fcc.md) FUN_00699fcc

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
      "definition_site": "00699fe0",
      "incomplete_value": false,
      "site": "00699fe4",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00699fe0",
      "incomplete_value": false,
      "site": "00699fe4",
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
            "const:ca8:8"
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
      "00699fe4",
      "DATA",
      [
        "storage",
        "00bf8ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00699fe4",
      "DATA",
      [
        "storage",
        "00bf8cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00699fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00699/00699fcc.md#insn-00699fe0)
- 新版 `00699fe0`（命令位置の公開資料なし）

~~~diff
- 00699fe0 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 00699fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00699fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00699fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00699fe0 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00699fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00699fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00699fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00699fe0 bytes 08a13291
+ 00699fe0 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a72b3f824cee5609777dfa03b6e39ad7"></a>

### [`00699ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00699/00699ff0.md) → [`00699ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/00699ff0.md) FUN_00699ff0

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
      "definition_site": "00699ff4",
      "incomplete_value": false,
      "site": "00699ff8",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00699ff4",
      "incomplete_value": false,
      "site": "00699ff8",
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
      "00699ff8",
      "DATA",
      [
        "storage",
        "00bf8ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00699ff8",
      "DATA",
      [
        "storage",
        "00bf8cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00699ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00699/00699ff0.md#insn-00699ff4)
- 新版 `00699ff4`（命令位置の公開資料なし）

~~~diff
- 00699ff4 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 00699ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00699ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00699ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00699ff4 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00699ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00699ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00699ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00699ff4 bytes 08a13291
+ 00699ff4 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4480a1ebdf7cbf3bfe3efc76cd97f516"></a>

### [`0069a008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a008.md) → [`0069a008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069a008.md) FUN_0069a008

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.99% / 新版 98.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069a210",
      "incomplete_value": false,
      "site": "0069a21c",
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
      "definition_site": "0069a210",
      "incomplete_value": false,
      "site": "0069a21c",
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
    "ordinal": 19,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069a280",
      "incomplete_value": false,
      "site": "0069a28c",
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
      "definition_site": "0069a280",
      "incomplete_value": false,
      "site": "0069a28c",
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
    "ordinal": 24,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069a334",
      "incomplete_value": false,
      "site": "0069a340",
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
      "definition_site": "0069a334",
      "incomplete_value": false,
      "site": "0069a340",
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
    "ordinal": 31,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0069a210",
      "PARAM",
      [
        "storage",
        "002a850f",
        null,
        "string"
      ]
    ],
    [
      "0069a280",
      "PARAM",
      [
        "storage",
        "002a850f",
        null,
        "string"
      ]
    ],
    [
      "0069a334",
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
      "0069a210",
      "PARAM",
      [
        "storage",
        "002a85a9",
        null,
        "string"
      ]
    ],
    [
      "0069a280",
      "PARAM",
      [
        "storage",
        "002a85a9",
        null,
        "string"
      ]
    ],
    [
      "0069a334",
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

- 旧版 [`0069a210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a008.md#insn-0069a210) · [`0069a280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a008.md#insn-0069a280) · [`0069a334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a008.md#insn-0069a334)
- 新版 `0069a210`（命令位置の公開資料なし） · `0069a280`（命令位置の公開資料なし） · `0069a334`（命令位置の公開資料なし）

~~~diff
- 0069a210 ["COPY", "tmp:0:8", ["const:50f:8"]]
- 0069a210 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0069a210 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0069a210 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0069a210 ["COPY", "tmp:0:8", ["const:5a9:8"]]
+ 0069a210 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0069a210 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0069a210 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0069a210 bytes 423c1491
+ 0069a210 bytes 42a41691
- 0069a280 ["COPY", "tmp:0:8", ["const:50f:8"]]
- 0069a280 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0069a280 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0069a280 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0069a280 ["COPY", "tmp:0:8", ["const:5a9:8"]]
+ 0069a280 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0069a280 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0069a280 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0069a280 bytes 423c1491
+ 0069a280 bytes 42a41691
- 0069a334 ["COPY", "tmp:0:8", ["const:128:8"]]
- 0069a334 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0069a334 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0069a334 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0069a334 ["COPY", "tmp:0:8", ["const:9b:8"]]
+ 0069a334 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0069a334 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0069a334 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0069a334 bytes 42a00491
+ 0069a334 bytes 426c0291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da7bbd4bf6820690fce92963861b9639"></a>

### [`0069a5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a5d8.md) → [`0069a5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069a5d8.md) _INIT_105

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
      "definition_site": "0069a614",
      "incomplete_value": true,
      "site": "0069a630",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0069a614",
      "incomplete_value": true,
      "site": "0069a630",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0069a638",
      "incomplete_value": true,
      "site": "0069a654",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0069a638",
      "incomplete_value": true,
      "site": "0069a654",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0069a658",
      "incomplete_value": true,
      "site": "0069a674",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0069a658",
      "incomplete_value": true,
      "site": "0069a674",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0069a614",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0069a638",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0069a658",
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
      "0069a614",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0069a638",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0069a658",
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

- 旧版 [`0069a604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a5d8.md#insn-0069a604) · [`0069a60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a5d8.md#insn-0069a60c)
- 新版 `0069a604`（命令位置の公開資料なし） · `0069a60c`（命令位置の公開資料なし）

~~~diff
- 0069a604 ["COPY", "tmp:0:8", ["const:820:8"]]
- 0069a604 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0069a604 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0069a604 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0069a604 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 0069a604 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0069a604 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0069a604 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0069a604 bytes 73822091
+ 0069a604 bytes 73822191
- 0069a60c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0069a60c bytes 69e0ffb0
+ 0069a60c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0069a60c bytes 69e0ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeb230866b3ceaf7af5f132eb9f9e350"></a>

### [`0069ced4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069c/0069ced4.md) → [`0069ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ced4.md) FUN_0069ced4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`00629194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00629/00629194.md) [`0069cd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069c/0069cd18.md) [`0069cd4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069c/0069cd4c.md) [`0069cd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069c/0069cd74.md) [`0069ce10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069c/0069ce10.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 10件 [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) [`0069cd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069cd18.md) [`0069cd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069cd4c.md) [`0069cd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069cd74.md) [`0069ce10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069c/0069ce10.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.99% / 新版 97.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069d140",
      "incomplete_value": false,
      "site": "0069d158",
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
      "definition_site": "0069d140",
      "incomplete_value": false,
      "site": "0069d158",
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
    "ordinal": 14,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069d668",
      "incomplete_value": false,
      "site": "0069d680",
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
      "definition_site": "0069d668",
      "incomplete_value": false,
      "site": "0069d680",
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
    "ordinal": 36,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0069d010",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "0069d068",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0069d078",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0069d010",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "0069d068",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0069d078",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069d00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069c/0069ced4.md#insn-0069d00c) · [`0069d010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069c/0069ced4.md#insn-0069d010) · [`0069d014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069c/0069ced4.md#insn-0069d014)
- 新版 `0069d00c`（命令位置の公開資料なし） · `0069d010`（命令位置の公開資料なし）

~~~diff
- 0069d00c ["COPY", "tmp:0:8", ["const:38:8"]]
- 0069d00c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0069d00c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0069d00c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0069d00c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0069d00c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0069d00c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0069d00c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0069d00c bytes b5e20091
+ 0069d00c bytes b5e20191
- 0069d010 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e60:8"]]
- 0069d010 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0069d010 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:eb0:8"]]
+ 0069d010 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0069d010 bytes 183347f9
+ 0069d010 bytes 185b47f9
- 0069d014 ["COPY", "register:40b0:8", ["const:c25000:8"]]
- 0069d014 bytes 562c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-119e7af726079672361eb4cb066cae42"></a>

### [`006a4e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a4/006a4e9c.md) → [`006a4e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a4/006a4e9c.md) FUN_006a4e9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) [`007c80a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c80a0.md) [`00963004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00963/00963004.md) [`00a82394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md)
- 新版 呼出元 4件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`007c80a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c80a0.md) [`00963004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00963/00963004.md) [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.58% / 新版 99.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006a6638",
      "incomplete_value": true,
      "site": "006a6638",
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
      "definition_site": "006a6638",
      "incomplete_value": true,
      "site": "006a6638",
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
    "ordinal": 135,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006a6638",
      "incomplete_value": true,
      "site": "006a6638",
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
      "definition_site": "006a6638",
      "incomplete_value": true,
      "site": "006a6638",
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
    "ordinal": 136,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006a5cd8",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ],
    [
      "006a5cdc",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "006a5cf8",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006a5cd8",
      "READ",
      [
        "storage",
        "00c1b578",
        null,
        "pointer"
      ]
    ],
    [
      "006a5cdc",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "006a5cf8",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a5cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a4/006a4e9c.md#insn-006a5cd8) · [`006a5cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a4/006a4e9c.md#insn-006a5cdc) · [`006a6614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a4/006a4e9c.md#insn-006a6614)
- 新版 `006a5cd8`（命令位置の公開資料なし） · `006a5cdc`（命令位置の公開資料なし） · `006a6614`（命令位置の公開資料なし）

~~~diff
- 006a5cd8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:528:8"]]
- 006a5cd8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 006a5cd8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:578:8"]]
+ 006a5cd8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 006a5cd8 bytes 189742f9
+ 006a5cd8 bytes 18bf42f9
- 006a5cdc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:520:8"]]
- 006a5cdc ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 006a5cdc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:570:8"]]
+ 006a5cdc ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 006a5cdc bytes f79242f9
+ 006a5cdc bytes f7ba42f9
- 006a6614 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:528:8"]]
- 006a6614 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006a6614 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
+ 006a6614 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006a6614 bytes 089542f9
+ 006a6614 bytes 08bd42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb077f0ce4440a8f535088d98c9e91c1"></a>

### [`006a6d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a6/006a6d68.md) → [`006a6d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a6/006a6d68.md) FUN_006a6d68

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`006a7120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7120.md) [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 9件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad268.md) [`006ad28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad28c.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`006ad980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad980.md)
- 新版 呼出元 3件 [`006a7120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a7120.md) [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 9件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad268.md) [`006ad28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`006ad980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad980.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.43% / 新版 98.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006a6dc0",
      "incomplete_value": true,
      "site": "006a6dc8",
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
      "definition_site": "006a6dc0",
      "incomplete_value": true,
      "site": "006a6dc8",
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
      "006a6db0",
      "READ",
      [
        "storage",
        "00c1b6f8",
        null,
        "pointer"
      ]
    ],
    [
      "006a6dc8",
      "DATA",
      [
        "storage",
        "00bf8d28",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "006a6fc4",
      "READ",
      [
        "storage",
        "00bf8d30",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "006a6db0",
      "READ",
      [
        "storage",
        "00c1b748",
        null,
        "pointer"
      ]
    ],
    [
      "006a6dc8",
      "DATA",
      [
        "storage",
        "00bf8d78",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "006a6fc4",
      "READ",
      [
        "storage",
        "00bf8d80",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a6db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a6/006a6d68.md#insn-006a6db0)
- 新版 `006a6db0`（命令位置の公開資料なし）

~~~diff
- 006a6db0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6f8:8"]]
- 006a6db0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006a6db0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:748:8"]]
+ 006a6db0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006a6db0 bytes 087d43f9
+ 006a6db0 bytes 08a543f9
~~~


<a id="compare-7d5e8655d444ab8eaea4b1786ff596cf"></a>

### [`006a7898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7898.md) → [`006a7898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a7898.md) FUN_006a7898

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006a8e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md) · 呼出先 13件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`006ae074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae074.md) [`006ae078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae078.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006a8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8e60.md) · 呼出先 13件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`006ae074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae074.md) [`006ae078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae078.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006a7934",
      "incomplete_value": false,
      "site": "006a7934",
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
      "definition_site": "006a7934",
      "incomplete_value": false,
      "site": "006a7934",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006a79e4",
      "incomplete_value": false,
      "site": "006a79e8",
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
      "definition_site": "006a79e4",
      "incomplete_value": false,
      "site": "006a79e8",
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
      "006a7934",
      "DATA",
      [
        "storage",
        "00bf8da0",
        null,
        "undefined *"
      ]
    ],
    [
      "006a7998",
      "READ",
      [
        "storage",
        "00bf8dc0",
        null,
        "pointer"
      ]
    ],
    [
      "006a7998",
      "READ",
      [
        "storage",
        "00bf8dc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006a7934",
      "DATA",
      [
        "storage",
        "00bf8df0",
        null,
        "undefined *"
      ]
    ],
    [
      "006a7998",
      "READ",
      [
        "storage",
        "00bf8e10",
        null,
        "pointer"
      ]
    ],
    [
      "006a7998",
      "READ",
      [
        "storage",
        "00bf8e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a7930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7898.md#insn-006a7930) · [`006a79a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7898.md#insn-006a79a8) · [`006a79dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7898.md#insn-006a79dc)
- 新版 `006a7930`（命令位置の公開資料なし） · `006a79a8`（命令位置の公開資料なし） · `006a79dc`（命令位置の公開資料なし）

~~~diff
- 006a7930 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 006a7930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006a7930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006a7930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006a7930 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 006a7930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006a7930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006a7930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006a7930 bytes 08813691
+ 006a7930 bytes 08c13791
- 006a79a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:520:8"]]
- 006a79a8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 006a79a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:570:8"]]
+ 006a79a8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 006a79a8 bytes b59242f9
+ 006a79a8 bytes b5ba42f9
- 006a79dc ["COPY", "tmp:0:8", ["const:d30:8"]]
- 006a79dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006a79dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006a79dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006a79dc ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 006a79dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006a79dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006a79dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006a79dc bytes 08c13491
+ 006a79dc bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0d8b80a1b584e71cb3a39b7b2f88da5"></a>

### [`006a7abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7abc.md) → [`006a7abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a7abc.md) FUN_006a7abc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006a8e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md) · 呼出先 13件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`006ae454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae454.md) [`006ae458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae458.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006a8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8e60.md) · 呼出先 13件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`006ae454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae454.md) [`006ae458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae458.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006a7c38",
      "incomplete_value": false,
      "site": "006a7c38",
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
      "definition_site": "006a7c38",
      "incomplete_value": false,
      "site": "006a7c38",
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
      "006a7b9c",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "006a7bb0",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "006a7bc8",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006a7b9c",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "006a7bb0",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "006a7bc8",
      "READ",
      [
        "storage",
        "00c1b578",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a7b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7abc.md#insn-006a7b9c) · [`006a7bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7abc.md#insn-006a7bc8) · [`006a7c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7abc.md#insn-006a7c34)
- 新版 `006a7b9c`（命令位置の公開資料なし） · `006a7bc8`（命令位置の公開資料なし） · `006a7c34`（命令位置の公開資料なし）

~~~diff
- 006a7b9c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:520:8"]]
- 006a7b9c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 006a7b9c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:570:8"]]
+ 006a7b9c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 006a7b9c bytes 189342f9
+ 006a7b9c bytes 18bb42f9
- 006a7bc8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:528:8"]]
- 006a7bc8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 006a7bc8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:578:8"]]
+ 006a7bc8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 006a7bc8 bytes 399742f9
+ 006a7bc8 bytes 39bf42f9
- 006a7c34 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 006a7c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006a7c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006a7c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006a7c34 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 006a7c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006a7c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006a7c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006a7c34 bytes 08813891
+ 006a7c34 bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c24db906b52e74f10ba590b1f359da85"></a>

### [`006a7dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7dc8.md) → [`006a7dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a7dc8.md) FUN_006a7dc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006a8e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md) · 呼出先 13件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`006ae5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae5e4.md) [`006ae5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae5e8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006a8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8e60.md) · 呼出先 13件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`006ae5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5e4.md) [`006ae5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5e8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006a7f44",
      "incomplete_value": true,
      "site": "006a7f44",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006a7f44",
      "incomplete_value": true,
      "site": "006a7f44",
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
            "const:ea0:8"
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
      "006a7ea8",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "006a7ebc",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "006a7ed4",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006a7ea8",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "006a7ebc",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "006a7ed4",
      "READ",
      [
        "storage",
        "00c1b578",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a7ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7dc8.md#insn-006a7ea8) · [`006a7ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7dc8.md#insn-006a7ed4) · [`006a7f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a7/006a7dc8.md#insn-006a7f40)
- 新版 `006a7ea8`（命令位置の公開資料なし） · `006a7ed4`（命令位置の公開資料なし） · `006a7f40`（命令位置の公開資料なし）

~~~diff
- 006a7ea8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:520:8"]]
- 006a7ea8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 006a7ea8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:570:8"]]
+ 006a7ea8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 006a7ea8 bytes 189342f9
+ 006a7ea8 bytes 18bb42f9
- 006a7ed4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:528:8"]]
- 006a7ed4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 006a7ed4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:578:8"]]
+ 006a7ed4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 006a7ed4 bytes 399742f9
+ 006a7ed4 bytes 39bf42f9
- 006a7f40 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 006a7f40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006a7f40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006a7f40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006a7f40 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 006a7f40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006a7f40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006a7f40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006a7f40 bytes 08813a91
+ 006a7f40 bytes 08c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8740d1765e4ee15cc111315b5833e3b"></a>

### [`006a8334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8334.md) → [`006a8334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8334.md) FUN_006a8334

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`008bf94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md) [`008c2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md) [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00a72648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a72648.md) · 呼出先 6件 [`00650740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/00650740.md) [`0069eac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069eac8.md) [`006ae0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae0f8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 5件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`008bf94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bf/008bf94c.md) [`008c2a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2a7c.md) [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 6件 [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`0069eac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069eac8.md) [`006ae0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae0f8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.54% / 新版 99.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006a864c",
      "incomplete_value": false,
      "site": "006a8654",
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
      "definition_site": "006a864c",
      "incomplete_value": false,
      "site": "006a8654",
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006a864c",
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
      "006a864c",
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

- 旧版 [`006a864c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8334.md#insn-006a864c)
- 新版 `006a864c`（命令位置の公開資料なし）

~~~diff
- 006a864c ["COPY", "tmp:0:8", ["const:866:8"]]
- 006a864c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006a864c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006a864c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006a864c ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 006a864c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006a864c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006a864c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006a864c bytes 21982191
+ 006a864c bytes 21641f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a16da4c95f4ae131379c814a05a9ed1"></a>

### [`006a86c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a86c4.md) → [`006a86c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a86c4.md) FUN_006a86c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`007802c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00780/007802c0.md) [`008c2634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md) [`009a1cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a1/009a1cd4.md) · 呼出先 11件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`00650740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/00650740.md) [`0069eac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069eac8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 4件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`007802c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00780/007802c0.md) [`008c2634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2634.md) [`009a1cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a1/009a1cd4.md) · 呼出先 11件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`0069eac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069eac8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.77% / 新版 99.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006a8708",
      "incomplete_value": false,
      "site": "006a8710",
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
      "definition_site": "006a8708",
      "incomplete_value": false,
      "site": "006a8710",
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
      "006a8708",
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
      "006a8708",
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

- 旧版 [`006a8708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a86c4.md#insn-006a8708)
- 新版 `006a8708`（命令位置の公開資料なし）

~~~diff
- 006a8708 ["COPY", "tmp:0:8", ["const:866:8"]]
- 006a8708 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006a8708 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006a8708 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006a8708 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 006a8708 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006a8708 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006a8708 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006a8708 bytes 21982191
+ 006a8708 bytes 21641f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a53407328f2c6f3fb0800e4aa2eb4693"></a>

### [`006a8e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md) → [`006a8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8e60.md) FUN_006a8e60

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`0066e148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e148.md) [`008c1b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1b84.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) [`0096d6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d6b8.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) · 呼出先 45件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00558fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558fd0.md)
- 新版 呼出元 6件 [`0066e148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e148.md) [`008c1b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1b84.md) [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) [`0096d6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096d6b8.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) · 呼出先 45件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00558fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.10% / 新版 92.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 43件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006a938c",
      "incomplete_value": true,
      "site": "006a938c",
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
      "definition_site": "006a938c",
      "incomplete_value": true,
      "site": "006a938c",
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
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006a93b4",
      "incomplete_value": true,
      "site": "006a93b8",
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
      "definition_site": "006a93b4",
      "incomplete_value": true,
      "site": "006a93b8",
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
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006a93f8",
      "incomplete_value": true,
      "site": "006a93f8",
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
      "definition_site": "006a93f8",
      "incomplete_value": true,
      "site": "006a93f8",
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
      "006a8ea4",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "006a8f18",
      "DATA",
      [
        "storage",
        "00bf8f20",
        null,
        "undefined *"
      ]
    ],
    [
      "006a8f18",
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
      "006a8ea4",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "006a8f18",
      "DATA",
      [
        "storage",
        "00bf8f70",
        null,
        "undefined *"
      ]
    ],
    [
      "006a8f18",
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

- 旧版 [`006a8ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md#insn-006a8ea4) · [`006a8ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md#insn-006a8ecc) · [`006a8f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md#insn-006a8f08)
- 新版 `006a8ea4`（命令位置の公開資料なし） · `006a8ecc`（命令位置の公開資料なし） · `006a8f08`（命令位置の公開資料なし）

~~~diff
- 006a8ea4 ["COPY", "tmp:0:8", ["const:866:8"]]
- 006a8ea4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006a8ea4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006a8ea4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006a8ea4 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 006a8ea4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006a8ea4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006a8ea4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006a8ea4 bytes 21982191
+ 006a8ea4 bytes 21641f91
- 006a8ecc ["COPY", "tmp:0:8", ["const:f20:8"]]
- 006a8ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006a8ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006a8ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006a8ecc ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 006a8ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006a8ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006a8ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006a8ecc bytes 08813c91
+ 006a8ecc bytes 08c13d91
- 006a8f08 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 006a8f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006a8f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006a8f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006a8f08 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 006a8f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006a8f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006a8f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006a8f08 bytes 08813e91
+ 006a8f08 bytes 08c13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-149cf940a950ab321ddc712c8bcaa52b"></a>

### [`006aad48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006aa/006aad48.md) → [`006aad48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006aa/006aad48.md) FUN_006aad48

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008c2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) · 呼出先 44件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 3件 [`008c2a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2a7c.md) [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) · 呼出先 44件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.18% / 新版 99.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ab7d8",
      "incomplete_value": true,
      "site": "006ab7d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b0c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ab7d8",
      "incomplete_value": true,
      "site": "006ab7d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a72:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "006ab7dc",
      "incomplete_value": true,
      "site": "006ab7dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006ab7dc",
      "incomplete_value": true,
      "site": "006ab7dc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006ab95c",
      "incomplete_value": false,
      "site": "006ab964",
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
            "const:4f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ab95c",
      "incomplete_value": false,
      "site": "006ab964",
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
            "const:457:8"
          ]
        ]
      ]
    },
    "ordinal": 149,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ab7c8",
      "READ",
      [
        "storage",
        "002a6a72",
        null,
        "string"
      ]
    ],
    [
      "006ab7cc",
      "READ",
      [
        "storage",
        "002a6a77",
        null,
        "string"
      ]
    ],
    [
      "006ab95c",
      "PARAM",
      [
        "storage",
        "002a8457",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006ab7c8",
      "READ",
      [
        "storage",
        "002a6b0c",
        null,
        "string"
      ]
    ],
    [
      "006ab7cc",
      "READ",
      [
        "storage",
        "002a6b11",
        null,
        "string"
      ]
    ],
    [
      "006ab95c",
      "PARAM",
      [
        "storage",
        "002a84f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ab7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006aa/006aad48.md#insn-006ab7c0) · [`006ab95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006aa/006aad48.md#insn-006ab95c) · [`006ab9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006aa/006aad48.md#insn-006ab9b8)
- 新版 `006ab7c0`（命令位置の公開資料なし） · `006ab95c`（命令位置の公開資料なし） · `006ab9b8`（命令位置の公開資料なし）

~~~diff
- 006ab7c0 ["COPY", "tmp:0:8", ["const:a72:8"]]
- 006ab7c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ab7c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ab7c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ab7c0 ["COPY", "tmp:0:8", ["const:b0c:8"]]
+ 006ab7c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ab7c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ab7c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ab7c0 bytes 29c92991
+ 006ab7c0 bytes 29312c91
- 006ab95c ["COPY", "tmp:0:8", ["const:457:8"]]
- 006ab95c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006ab95c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006ab95c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006ab95c ["COPY", "tmp:0:8", ["const:4f1:8"]]
+ 006ab95c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006ab95c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006ab95c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006ab95c bytes 215c1191
+ 006ab95c bytes 21c41391
- 006ab9b8 ["COPY", "tmp:0:8", ["const:bc5:8"]]
- 006ab9b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006ab9b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006ab9b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006ab9b8 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 006ab9b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006ab9b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006ab9b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006ab9b8 bytes 21142f91
+ 006ab9b8 bytes 21e02c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe695a6be840a3290f01ce4644a667d4"></a>

### [`006ad28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad28c.md) → [`006ad28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md) FUN_006ad28c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a6/006a6d68.md) · 呼出先 10件 [`006ad590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad590.md) [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`006ad8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8e8.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a6/006a6d68.md) · 呼出先 10件 [`006ad590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad590.md) [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

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
      "definition_site": "006ad54c",
      "incomplete_value": false,
      "site": "006ad550",
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
      "definition_site": "006ad54c",
      "incomplete_value": false,
      "site": "006ad550",
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
      "006ad54c",
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
      "006ad54c",
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

- 旧版 [`006ad54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad28c.md#insn-006ad54c)
- 新版 `006ad54c`（命令位置の公開資料なし）

~~~diff
- 006ad54c ["COPY", "tmp:0:8", ["const:23:8"]]
- 006ad54c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006ad54c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006ad54c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006ad54c ["COPY", "tmp:0:8", ["const:21:8"]]
+ 006ad54c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006ad54c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006ad54c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006ad54c bytes 008c0091
+ 006ad54c bytes 00840091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

