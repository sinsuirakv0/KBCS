# v15.7.3 → v15.7.4 · 最優先の変更候補 (36)

[一覧の目次](README.md)

<a id="compare-af5149ccd3a5b02f548f83bd5bd79f32"></a>

### [`007c28f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c28f0.md) → [`007c28f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c28f0.md) FUN_007c28f0

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
      "definition_site": "007c28f4",
      "incomplete_value": false,
      "site": "007c28f8",
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
      "definition_site": "007c28f4",
      "incomplete_value": false,
      "site": "007c28f8",
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
      "007c28f8",
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
      "007c28f8",
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

- 旧版 [`007c28f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c28f0.md#insn-007c28f4)
- 新版 [`007c28f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c28f0.md#insn-007c28f4)

~~~diff
- 007c28f4 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 007c28f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c28f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c28f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c28f4 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 007c28f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c28f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c28f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c28f4 bytes 08a12291
+ 007c28f4 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-603fd7e94c09de1901697a2e7bdc384b"></a>

### [`007c2918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2918.md) → [`007c2918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c2918.md) FUN_007c2918

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.94% / 新版 95.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c2a1c",
      "incomplete_value": true,
      "site": "007c2a2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8bc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c2a1c",
      "incomplete_value": true,
      "site": "007c2a2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8be:8"
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
      "definition_site": "007c2a20",
      "incomplete_value": true,
      "site": "007c2a30",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007c2a20",
      "incomplete_value": true,
      "site": "007c2a30",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007c2c28",
      "incomplete_value": true,
      "site": "007c2c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a84:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c2c28",
      "incomplete_value": true,
      "site": "007c2c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b11:8"
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
      "007c2a1c",
      "READ",
      [
        "storage",
        "0029b8be",
        null,
        "string"
      ]
    ],
    [
      "007c2a20",
      "READ",
      [
        "storage",
        "0029b8ce",
        null,
        "string"
      ]
    ],
    [
      "007c2c14",
      "READ",
      [
        "storage",
        "00293b11",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007c2a1c",
      "READ",
      [
        "storage",
        "0029b8bc",
        null,
        "string"
      ]
    ],
    [
      "007c2a20",
      "READ",
      [
        "storage",
        "0029b8cc",
        null,
        "string"
      ]
    ],
    [
      "007c2c14",
      "READ",
      [
        "storage",
        "00293a84",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c2a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2918.md#insn-007c2a14) · [`007c2a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2918.md#insn-007c2a18)
- 新版 [`007c2a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c2918.md#insn-007c2a14) · [`007c2a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c2918.md#insn-007c2a18)

~~~diff
- 007c2a14 ["COPY", "tmp:0:8", ["const:8be:8"]]
- 007c2a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c2a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c2a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c2a14 ["COPY", "tmp:0:8", ["const:8bc:8"]]
+ 007c2a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c2a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c2a14 bytes 08f92291
+ 007c2a14 bytes 08f12291
- 007c2a18 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 007c2a18 bytes 69d7ffd0
+ 007c2a18 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 007c2a18 bytes 69d7ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d061f9a04df53dff3e4e70a2f9e1b77"></a>

### [`007c2ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2ff8.md) → [`007c2ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c2ff8.md) FUN_007c2ff8

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
      "definition_site": "007c3018",
      "incomplete_value": false,
      "site": "007c301c",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3018",
      "incomplete_value": false,
      "site": "007c301c",
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
            "const:918:8"
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
      "007c301c",
      "DATA",
      [
        "storage",
        "00bfd918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c301c",
      "DATA",
      [
        "storage",
        "00bfd968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2ff8.md#insn-007c3018)
- 新版 [`007c3018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c2ff8.md#insn-007c3018)

~~~diff
- 007c3018 ["COPY", "tmp:0:8", ["const:918:8"]]
- 007c3018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3018 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 007c3018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3018 bytes 08612491
+ 007c3018 bytes 08a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59f69c834564e99bc0d236afb6dea897"></a>

### [`007c3030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3030.md) → [`007c3030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3030.md) FUN_007c3030

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
      "definition_site": "007c3034",
      "incomplete_value": false,
      "site": "007c3038",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3034",
      "incomplete_value": false,
      "site": "007c3038",
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
      "007c3038",
      "DATA",
      [
        "storage",
        "00bfd918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3038",
      "DATA",
      [
        "storage",
        "00bfd968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3030.md#insn-007c3034)
- 新版 [`007c3034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3030.md#insn-007c3034)

~~~diff
- 007c3034 ["COPY", "tmp:0:8", ["const:918:8"]]
- 007c3034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3034 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 007c3034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3034 bytes 08612491
+ 007c3034 bytes 08a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0d09a5af2be9711a9209e3fec718940"></a>

### [`007c3480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3480.md) → [`007c3480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3480.md) FUN_007c3480

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
      "definition_site": "007c3494",
      "incomplete_value": false,
      "site": "007c3498",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3494",
      "incomplete_value": false,
      "site": "007c3498",
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
      "007c3498",
      "DATA",
      [
        "storage",
        "00bfd9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3498",
      "DATA",
      [
        "storage",
        "00bfd9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3480.md#insn-007c3494)
- 新版 [`007c3494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3480.md#insn-007c3494)

~~~diff
- 007c3494 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 007c3494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3494 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 007c3494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3494 bytes 08a12691
+ 007c3494 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6a233355a17be342a3080cc34aaa37d"></a>

### [`007c34bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c34bc.md) → [`007c34bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c34bc.md) FUN_007c34bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c350c",
      "incomplete_value": false,
      "site": "007c351c",
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
      "definition_site": "007c350c",
      "incomplete_value": false,
      "site": "007c351c",
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
      "definition_site": "007c3514",
      "incomplete_value": false,
      "site": "007c351c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3514",
      "incomplete_value": false,
      "site": "007c351c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "007c3500",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c350c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3514",
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
      "007c3500",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c350c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3514",
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

- 旧版 [`007c3500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c34bc.md#insn-007c3500) · [`007c350c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c34bc.md#insn-007c350c) · [`007c3514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c34bc.md#insn-007c3514)
- 新版 [`007c3500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c34bc.md#insn-007c3500) · [`007c350c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c34bc.md#insn-007c350c) · [`007c3514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c34bc.md#insn-007c3514)

~~~diff
- 007c3500 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007c3500 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c3500 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007c3500 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c3500 bytes 003d45f9
+ 007c3500 bytes 005d45f9
- 007c350c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007c350c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c350c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c350c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c350c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007c350c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c350c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c350c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c350c bytes 21203991
+ 007c350c bytes 21603a91
- 007c3514 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007c3514 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c3514 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c3514 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c3514 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007c3514 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3514 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3514 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c3514 bytes 42601491
+ 007c3514 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9431027cb3599fe26b5a7e43bebe0be"></a>

### [`007c36c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c36c0.md) → [`007c36c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c36c0.md) FUN_007c36c0

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
      "definition_site": "007c36e4",
      "incomplete_value": false,
      "site": "007c36e4",
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c36e4",
      "incomplete_value": false,
      "site": "007c36e4",
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
            "const:a28:8"
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
      "007c36e4",
      "DATA",
      [
        "storage",
        "00bfda28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c36e4",
      "DATA",
      [
        "storage",
        "00bfda78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c36e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c36c0.md#insn-007c36e0)
- 新版 [`007c36e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c36c0.md#insn-007c36e0)

~~~diff
- 007c36e0 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 007c36e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c36e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c36e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c36e0 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 007c36e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c36e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c36e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c36e0 bytes 08a12891
+ 007c36e0 bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e408aaede5378f99b1674ea03a4404b"></a>

### [`007c36f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c36f4.md) → [`007c36f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c36f4.md) FUN_007c36f4

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
      "definition_site": "007c3700",
      "incomplete_value": false,
      "site": "007c3700",
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3700",
      "incomplete_value": false,
      "site": "007c3700",
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
      "007c3700",
      "DATA",
      [
        "storage",
        "00bfda28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3700",
      "DATA",
      [
        "storage",
        "00bfda78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c36fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c36f4.md#insn-007c36fc)
- 新版 [`007c36fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c36f4.md#insn-007c36fc)

~~~diff
- 007c36fc ["COPY", "tmp:0:8", ["const:a28:8"]]
- 007c36fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c36fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c36fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c36fc ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 007c36fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c36fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c36fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c36fc bytes 29a12891
+ 007c36fc bytes 29e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d92ebe47e57b4ac952b49b12e3cb53a5"></a>

### [`007c37c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c37c4.md) → [`007c37c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c37c4.md) FUN_007c37c4

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
      "definition_site": "007c37d8",
      "incomplete_value": false,
      "site": "007c37dc",
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
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c37d8",
      "incomplete_value": false,
      "site": "007c37dc",
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
            "const:aa8:8"
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
      "007c37dc",
      "DATA",
      [
        "storage",
        "00bfdaa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c37dc",
      "DATA",
      [
        "storage",
        "00bfdaf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c37d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c37c4.md#insn-007c37d8)
- 新版 [`007c37d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c37c4.md#insn-007c37d8)

~~~diff
- 007c37d8 ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 007c37d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c37d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c37d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c37d8 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 007c37d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c37d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c37d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c37d8 bytes 08a12a91
+ 007c37d8 bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e947f223575f65fa8466b2c48e9d7ec7"></a>

### [`007c37e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c37e8.md) → [`007c37e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c37e8.md) FUN_007c37e8

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
      "definition_site": "007c37ec",
      "incomplete_value": false,
      "site": "007c37f0",
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
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c37ec",
      "incomplete_value": false,
      "site": "007c37f0",
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
      "007c37f0",
      "DATA",
      [
        "storage",
        "00bfdaa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c37f0",
      "DATA",
      [
        "storage",
        "00bfdaf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c37ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c37e8.md#insn-007c37ec)
- 新版 [`007c37ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c37e8.md#insn-007c37ec)

~~~diff
- 007c37ec ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 007c37ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c37ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c37ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c37ec ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 007c37ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c37ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c37ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c37ec bytes 08a12a91
+ 007c37ec bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8866eef02b3133c11d732ad988f5f663"></a>

### [`007c3874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3874.md) → [`007c3874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3874.md) FUN_007c3874

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
      "definition_site": "007c3898",
      "incomplete_value": false,
      "site": "007c3898",
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
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3898",
      "incomplete_value": false,
      "site": "007c3898",
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
      "007c3898",
      "DATA",
      [
        "storage",
        "00bfdb28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3898",
      "DATA",
      [
        "storage",
        "00bfdb78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3874.md#insn-007c3894)
- 新版 [`007c3894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3874.md#insn-007c3894)

~~~diff
- 007c3894 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 007c3894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3894 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 007c3894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3894 bytes 08a12c91
+ 007c3894 bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a6f4331aa1b6942455a47ef91271182"></a>

### [`007c38a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c38a8.md) → [`007c38a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c38a8.md) FUN_007c38a8

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
      "definition_site": "007c38b4",
      "incomplete_value": false,
      "site": "007c38b4",
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
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c38b4",
      "incomplete_value": false,
      "site": "007c38b4",
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
      "007c38b4",
      "DATA",
      [
        "storage",
        "00bfdb28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c38b4",
      "DATA",
      [
        "storage",
        "00bfdb78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c38b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c38a8.md#insn-007c38b0)
- 新版 [`007c38b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c38a8.md#insn-007c38b0)

~~~diff
- 007c38b0 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 007c38b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c38b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c38b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c38b0 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 007c38b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c38b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c38b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c38b0 bytes 29a12c91
+ 007c38b0 bytes 29e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d907556aa39c541c9d511112768332f5"></a>

### [`007c38c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c38c4.md) → [`007c38c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c38c4.md) FUN_007c38c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.20% / 新版 97.20%

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
      "definition_site": "007c3908",
      "incomplete_value": true,
      "site": "007c3908",
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
      "definition_site": "007c3908",
      "incomplete_value": true,
      "site": "007c3908",
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
      "definition_site": "007c3918",
      "incomplete_value": false,
      "site": "007c3920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3918",
      "incomplete_value": false,
      "site": "007c3920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "007c38fc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c3910",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3918",
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
      "007c38fc",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c3910",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3918",
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

- 旧版 [`007c38fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c38c4.md#insn-007c38fc) · [`007c3910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c38c4.md#insn-007c3910) · [`007c3918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c38c4.md#insn-007c3918)
- 新版 [`007c38fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c38c4.md#insn-007c38fc) · [`007c3910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c38c4.md#insn-007c3910) · [`007c3918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c38c4.md#insn-007c3918)

~~~diff
- 007c38fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 007c38fc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c38fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 007c38fc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c38fc bytes 203d45f9
+ 007c38fc bytes 205d45f9
- 007c3910 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007c3910 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c3910 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c3910 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c3910 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007c3910 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c3910 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c3910 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c3910 bytes 21203991
+ 007c3910 bytes 21603a91
- 007c3918 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007c3918 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c3918 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c3918 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c3918 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007c3918 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3918 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3918 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c3918 bytes 42601491
+ 007c3918 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ade83a106928704845bd2ef6d565b55c"></a>

### [`007c3c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3c48.md) → [`007c3c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3c48.md) FUN_007c3c48

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
      "definition_site": "007c3c6c",
      "incomplete_value": false,
      "site": "007c3c6c",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3c6c",
      "incomplete_value": false,
      "site": "007c3c6c",
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
      "007c3c6c",
      "DATA",
      [
        "storage",
        "00bfdba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3c6c",
      "DATA",
      [
        "storage",
        "00bfdbf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3c48.md#insn-007c3c68)
- 新版 [`007c3c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3c48.md#insn-007c3c68)

~~~diff
- 007c3c68 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 007c3c68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3c68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3c68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3c68 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 007c3c68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3c68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3c68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3c68 bytes 08a12e91
+ 007c3c68 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcad04a527e15fe53a11c272b4ec4e6d"></a>

### [`007c3c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3c7c.md) → [`007c3c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3c7c.md) FUN_007c3c7c

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
      "definition_site": "007c3c88",
      "incomplete_value": false,
      "site": "007c3c88",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3c88",
      "incomplete_value": false,
      "site": "007c3c88",
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
      "007c3c88",
      "DATA",
      [
        "storage",
        "00bfdba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3c88",
      "DATA",
      [
        "storage",
        "00bfdbf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3c7c.md#insn-007c3c84)
- 新版 [`007c3c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3c7c.md#insn-007c3c84)

~~~diff
- 007c3c84 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 007c3c84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c3c84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c3c84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c3c84 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 007c3c84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c3c84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c3c84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c3c84 bytes 29a12e91
+ 007c3c84 bytes 29e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c9b2155254408dd77601615deed8c71"></a>

### [`007c3d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d2c.md) → [`007c3d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3d2c.md) FUN_007c3d2c

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
      "definition_site": "007c3d50",
      "incomplete_value": false,
      "site": "007c3d50",
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
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3d50",
      "incomplete_value": false,
      "site": "007c3d50",
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
      "007c3d50",
      "DATA",
      [
        "storage",
        "00bfdc28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3d50",
      "DATA",
      [
        "storage",
        "00bfdc78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d2c.md#insn-007c3d4c)
- 新版 [`007c3d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3d2c.md#insn-007c3d4c)

~~~diff
- 007c3d4c ["COPY", "tmp:0:8", ["const:c28:8"]]
- 007c3d4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3d4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3d4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3d4c ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 007c3d4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3d4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3d4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3d4c bytes 08a13091
+ 007c3d4c bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb80f6caa30c8fbfc746ceacd1e21ab"></a>

### [`007c3d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d60.md) → [`007c3d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3d60.md) FUN_007c3d60

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
      "definition_site": "007c3d6c",
      "incomplete_value": false,
      "site": "007c3d6c",
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
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3d6c",
      "incomplete_value": false,
      "site": "007c3d6c",
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
      "007c3d6c",
      "DATA",
      [
        "storage",
        "00bfdc28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3d6c",
      "DATA",
      [
        "storage",
        "00bfdc78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d60.md#insn-007c3d68)
- 新版 [`007c3d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3d60.md#insn-007c3d68)

~~~diff
- 007c3d68 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 007c3d68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c3d68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c3d68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c3d68 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 007c3d68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c3d68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c3d68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c3d68 bytes 29a13091
+ 007c3d68 bytes 29e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8e5a7bd7ce380455b9bbea7b54acc78"></a>

### [`007c3d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d7c.md) → [`007c3d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3d7c.md) FUN_007c3d7c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.15% / 新版 93.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007c3da0",
      "incomplete_value": true,
      "site": "007c3da0",
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
      "definition_site": "007c3da0",
      "incomplete_value": true,
      "site": "007c3da0",
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
      "007c3d98",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c3da8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3db0",
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
      "007c3d98",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c3da8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3db0",
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

- 旧版 [`007c3d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d7c.md#insn-007c3d98) · [`007c3da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d7c.md#insn-007c3da8) · [`007c3db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d7c.md#insn-007c3db0)
- 新版 [`007c3d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3d7c.md#insn-007c3d98) · [`007c3da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3d7c.md#insn-007c3da8) · [`007c3db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3d7c.md#insn-007c3db0)

~~~diff
- 007c3d98 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 007c3d98 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c3d98 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 007c3d98 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c3d98 bytes 203d45f9
+ 007c3d98 bytes 205d45f9
- 007c3da8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007c3da8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c3da8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c3da8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c3da8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007c3da8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c3da8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c3da8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c3da8 bytes 21203991
+ 007c3da8 bytes 21603a91
- 007c3db0 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007c3db0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c3db0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c3db0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c3db0 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007c3db0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3db0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3db0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c3db0 bytes 42601491
+ 007c3db0 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31b6c00940f0a0c0bb846cc3a2db9e62"></a>

### [`007c3ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3ecc.md) → [`007c3ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3ecc.md) FUN_007c3ecc

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
      "definition_site": "007c3ee0",
      "incomplete_value": false,
      "site": "007c3ee4",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3ee0",
      "incomplete_value": false,
      "site": "007c3ee4",
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
      "007c3ee4",
      "DATA",
      [
        "storage",
        "00bfdca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3ee4",
      "DATA",
      [
        "storage",
        "00bfdcf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3ecc.md#insn-007c3ee0)
- 新版 [`007c3ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3ecc.md#insn-007c3ee0)

~~~diff
- 007c3ee0 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 007c3ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3ee0 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 007c3ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3ee0 bytes 08a13291
+ 007c3ee0 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7751069ff31e8d7c591459123284522b"></a>

### [`007c3ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3ef0.md) → [`007c3ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3ef0.md) FUN_007c3ef0

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
      "definition_site": "007c3ef4",
      "incomplete_value": true,
      "site": "007c3ef8",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3ef4",
      "incomplete_value": true,
      "site": "007c3ef8",
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
      "007c3ef8",
      "DATA",
      [
        "storage",
        "00bfdca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3ef8",
      "DATA",
      [
        "storage",
        "00bfdcf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3ef0.md#insn-007c3ef4)
- 新版 [`007c3ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3ef0.md#insn-007c3ef4)

~~~diff
- 007c3ef4 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 007c3ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3ef4 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 007c3ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3ef4 bytes 08a13291
+ 007c3ef4 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b3cf7e5b0041923cd1057dcb4938a26"></a>

### [`007c3f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3f74.md) → [`007c3f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3f74.md) FUN_007c3f74

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
      "definition_site": "007c3f98",
      "incomplete_value": false,
      "site": "007c3f98",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3f98",
      "incomplete_value": false,
      "site": "007c3f98",
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
            "const:d28:8"
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
      "007c3f98",
      "DATA",
      [
        "storage",
        "00bfdd28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3f98",
      "DATA",
      [
        "storage",
        "00bfdd78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3f74.md#insn-007c3f94)
- 新版 [`007c3f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3f74.md#insn-007c3f94)

~~~diff
- 007c3f94 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007c3f94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3f94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3f94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3f94 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007c3f94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3f94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3f94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3f94 bytes 08a13491
+ 007c3f94 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99f6a8f2a64822a24239d7a772c75344"></a>

### [`007c3fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3fa8.md) → [`007c3fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3fa8.md) FUN_007c3fa8

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
      "definition_site": "007c3fb4",
      "incomplete_value": false,
      "site": "007c3fb4",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3fb4",
      "incomplete_value": false,
      "site": "007c3fb4",
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
      "007c3fb4",
      "DATA",
      [
        "storage",
        "00bfdd28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3fb4",
      "DATA",
      [
        "storage",
        "00bfdd78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3fa8.md#insn-007c3fb0)
- 新版 [`007c3fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3fa8.md#insn-007c3fb0)

~~~diff
- 007c3fb0 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007c3fb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c3fb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c3fb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c3fb0 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 007c3fb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c3fb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c3fb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c3fb0 bytes 29a13491
+ 007c3fb0 bytes 29e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d248af24162c2e1c64aecb10a9184fb8"></a>

### [`007c3fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3fc4.md) → [`007c3fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3fc4.md) FUN_007c3fc4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c42e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42e0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007c42e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c42e0.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c40d8",
      "incomplete_value": true,
      "site": "007c40ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c40d8",
      "incomplete_value": true,
      "site": "007c40ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9fd:8"
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
      "definition_site": "007c410c",
      "incomplete_value": false,
      "site": "007c410c",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c410c",
      "incomplete_value": false,
      "site": "007c410c",
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
            "const:d98:8"
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
      "007c4020",
      "READ",
      [
        "storage",
        "00c1b688",
        null,
        "pointer"
      ]
    ],
    [
      "007c4038",
      "READ",
      [
        "storage",
        "00c24254",
        null,
        "undefined4"
      ]
    ],
    [
      "007c4038",
      "READ",
      [
        "storage",
        "00c24258",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "007c4020",
      "READ",
      [
        "storage",
        "00c1b6d8",
        null,
        "pointer"
      ]
    ],
    [
      "007c4038",
      "READ",
      [
        "storage",
        "00c242a4",
        null,
        "undefined4"
      ]
    ],
    [
      "007c4038",
      "READ",
      [
        "storage",
        "00c242a8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3fc4.md#insn-007c4020) · [`007c40d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3fc4.md#insn-007c40d0) · [`007c40d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3fc4.md#insn-007c40d4)
- 新版 [`007c4020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3fc4.md#insn-007c4020) · [`007c40d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3fc4.md#insn-007c40d0)

~~~diff
- 007c4020 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:688:8"]]
- 007c4020 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c4020 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d8:8"]]
+ 007c4020 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 007c4020 bytes 294543f9
+ 007c4020 bytes 296d43f9
- 007c40d0 ["COPY", "tmp:0:8", ["const:9fd:8"]]
- 007c40d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c40d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c40d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c40d0 ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 007c40d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c40d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c40d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c40d0 bytes 29f52791
+ 007c40d0 bytes 29212a91
- 007c40d4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 007c40d4 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fc805c70962755e2431d2b2449dfdfd"></a>

### [`007c4298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4298.md) → [`007c4298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4298.md) FUN_007c4298

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
      "definition_site": "007c42bc",
      "incomplete_value": false,
      "site": "007c42bc",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c42bc",
      "incomplete_value": false,
      "site": "007c42bc",
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
            "const:d98:8"
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
      "007c42bc",
      "DATA",
      [
        "storage",
        "00bfdd98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c42bc",
      "DATA",
      [
        "storage",
        "00bfdde8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c42b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4298.md#insn-007c42b8)
- 新版 [`007c42b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4298.md#insn-007c42b8)

~~~diff
- 007c42b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007c42b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c42b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c42b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c42b8 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 007c42b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c42b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c42b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c42b8 bytes 08613691
+ 007c42b8 bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e32b1e23622af0739126f3d59e8ea8b4"></a>

### [`007c42cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42cc.md) → [`007c42cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c42cc.md) FUN_007c42cc

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
      "definition_site": "007c42d8",
      "incomplete_value": false,
      "site": "007c42d8",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c42d8",
      "incomplete_value": false,
      "site": "007c42d8",
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
            "const:d98:8"
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
      "007c42d8",
      "DATA",
      [
        "storage",
        "00bfdd98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c42d8",
      "DATA",
      [
        "storage",
        "00bfdde8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c42d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42cc.md#insn-007c42d4)
- 新版 [`007c42d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c42cc.md#insn-007c42d4)

~~~diff
- 007c42d4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007c42d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c42d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c42d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c42d4 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 007c42d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c42d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c42d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c42d4 bytes 29613691
+ 007c42d4 bytes 29a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c402876ec5fece03a3f6c73c30e75c38"></a>

### [`007c42e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42e8.md) → [`007c42e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c42e8.md) FUN_007c42e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c457c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c457c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007c457c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c457c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c4374",
      "incomplete_value": true,
      "site": "007c4388",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4374",
      "incomplete_value": true,
      "site": "007c4388",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a59:8"
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
      "definition_site": "007c43a4",
      "incomplete_value": false,
      "site": "007c43a4",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c43a4",
      "incomplete_value": false,
      "site": "007c43a4",
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
            "const:e08:8"
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
      "007c4374",
      "READ",
      [
        "storage",
        "002a9a59",
        null,
        "string"
      ]
    ],
    [
      "007c43a4",
      "DATA",
      [
        "storage",
        "00bfde08",
        null,
        "undefined *"
      ]
    ],
    [
      "007c4428",
      "READ",
      [
        "storage",
        "00bfde28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c4374",
      "READ",
      [
        "storage",
        "002a9a68",
        null,
        "string"
      ]
    ],
    [
      "007c43a4",
      "DATA",
      [
        "storage",
        "00bfde58",
        null,
        "undefined *"
      ]
    ],
    [
      "007c4428",
      "READ",
      [
        "storage",
        "00bfde78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c436c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42e8.md#insn-007c436c) · [`007c4370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42e8.md#insn-007c4370)
- 新版 [`007c436c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c42e8.md#insn-007c436c) · [`007c4370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c42e8.md#insn-007c4370)

~~~diff
- 007c436c ["COPY", "tmp:0:8", ["const:a59:8"]]
- 007c436c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c436c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c436c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c436c ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 007c436c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c436c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c436c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c436c bytes 29652991
+ 007c436c bytes 29a12991
- 007c4370 ["COPY", "register:4098:8", ["register:4000:8"]]
- 007c4370 bytes f30300aa
+ 007c4370 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 007c4370 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-932d65f303a1565888a8cd87990dc7ca"></a>

### [`007c4534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4534.md) → [`007c4534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4534.md) FUN_007c4534

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
      "definition_site": "007c4558",
      "incomplete_value": false,
      "site": "007c4558",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4558",
      "incomplete_value": false,
      "site": "007c4558",
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
            "const:e08:8"
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
      "007c4558",
      "DATA",
      [
        "storage",
        "00bfde08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4558",
      "DATA",
      [
        "storage",
        "00bfde58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4534.md#insn-007c4554)
- 新版 [`007c4554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4534.md#insn-007c4554)

~~~diff
- 007c4554 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 007c4554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4554 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 007c4554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4554 bytes 08213891
+ 007c4554 bytes 08613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d0c46170f3daeed6bb75c0875319045"></a>

### [`007c4568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4568.md) → [`007c4568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4568.md) FUN_007c4568

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
      "definition_site": "007c4574",
      "incomplete_value": false,
      "site": "007c4574",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4574",
      "incomplete_value": false,
      "site": "007c4574",
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
            "const:e08:8"
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
      "007c4574",
      "DATA",
      [
        "storage",
        "00bfde08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4574",
      "DATA",
      [
        "storage",
        "00bfde58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4568.md#insn-007c4570)
- 新版 [`007c4570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4568.md#insn-007c4570)

~~~diff
- 007c4570 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 007c4570 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c4570 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c4570 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c4570 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 007c4570 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4570 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4570 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c4570 bytes 29213891
+ 007c4570 bytes 29613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3754aaa3562a1407a24b2e0cc0c98d4d"></a>

### [`007c4614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4614.md) → [`007c4614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4614.md) FUN_007c4614

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
      "definition_site": "007c4638",
      "incomplete_value": false,
      "site": "007c4638",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4638",
      "incomplete_value": false,
      "site": "007c4638",
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
            "const:ea8:8"
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
      "007c4638",
      "DATA",
      [
        "storage",
        "00bfdea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4638",
      "DATA",
      [
        "storage",
        "00bfdef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4614.md#insn-007c4634)
- 新版 [`007c4634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4614.md#insn-007c4634)

~~~diff
- 007c4634 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 007c4634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4634 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 007c4634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4634 bytes 08a13a91
+ 007c4634 bytes 08e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0424b36db1b05576ba3e938603f1177"></a>

### [`007c4648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4648.md) → [`007c4648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4648.md) FUN_007c4648

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
      "definition_site": "007c4654",
      "incomplete_value": false,
      "site": "007c4654",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4654",
      "incomplete_value": false,
      "site": "007c4654",
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
            "const:ea8:8"
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
      "007c4654",
      "DATA",
      [
        "storage",
        "00bfdea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4654",
      "DATA",
      [
        "storage",
        "00bfdef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4648.md#insn-007c4650)
- 新版 [`007c4650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4648.md#insn-007c4650)

~~~diff
- 007c4650 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 007c4650 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c4650 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c4650 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c4650 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 007c4650 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4650 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4650 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c4650 bytes 29a13a91
+ 007c4650 bytes 29e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39b3f99d102d152075f253bf7c104711"></a>

### [`007c4664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4664.md) → [`007c4664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4664.md) FUN_007c4664

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c48f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48f8.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007c48f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c48f8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c46f0",
      "incomplete_value": true,
      "site": "007c4704",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c46f0",
      "incomplete_value": true,
      "site": "007c4704",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a59:8"
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
      "definition_site": "007c4720",
      "incomplete_value": false,
      "site": "007c4720",
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
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4720",
      "incomplete_value": false,
      "site": "007c4720",
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
            "const:f18:8"
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
      "007c46f0",
      "READ",
      [
        "storage",
        "002a9a59",
        null,
        "string"
      ]
    ],
    [
      "007c4720",
      "DATA",
      [
        "storage",
        "00bfdf18",
        null,
        "undefined *"
      ]
    ],
    [
      "007c47a4",
      "READ",
      [
        "storage",
        "00bfdf38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c46f0",
      "READ",
      [
        "storage",
        "002a9a68",
        null,
        "string"
      ]
    ],
    [
      "007c4720",
      "DATA",
      [
        "storage",
        "00bfdf68",
        null,
        "undefined *"
      ]
    ],
    [
      "007c47a4",
      "READ",
      [
        "storage",
        "00bfdf88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c46e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4664.md#insn-007c46e8) · [`007c46ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4664.md#insn-007c46ec)
- 新版 [`007c46e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4664.md#insn-007c46e8) · [`007c46ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4664.md#insn-007c46ec)

~~~diff
- 007c46e8 ["COPY", "tmp:0:8", ["const:a59:8"]]
- 007c46e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c46e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c46e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c46e8 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 007c46e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c46e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c46e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c46e8 bytes 29652991
+ 007c46e8 bytes 29a12991
- 007c46ec ["COPY", "register:4098:8", ["register:4000:8"]]
- 007c46ec bytes f30300aa
+ 007c46ec ["COPY", "register:4098:8", ["register:4000:8"]]
+ 007c46ec bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bb446c2a26646e2709f99da1a7872b9"></a>

### [`007c48b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48b0.md) → [`007c48b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c48b0.md) FUN_007c48b0

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
      "definition_site": "007c48d4",
      "incomplete_value": false,
      "site": "007c48d4",
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
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c48d4",
      "incomplete_value": false,
      "site": "007c48d4",
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
            "const:f18:8"
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
      "007c48d4",
      "DATA",
      [
        "storage",
        "00bfdf18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c48d4",
      "DATA",
      [
        "storage",
        "00bfdf68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c48d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48b0.md#insn-007c48d0)
- 新版 [`007c48d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c48b0.md#insn-007c48d0)

~~~diff
- 007c48d0 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 007c48d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c48d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c48d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c48d0 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 007c48d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c48d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c48d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c48d0 bytes 08613c91
+ 007c48d0 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddae70531c58a9eeb88fc68ace977f2d"></a>

### [`007c48e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48e4.md) → [`007c48e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c48e4.md) FUN_007c48e4

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
      "definition_site": "007c48f0",
      "incomplete_value": false,
      "site": "007c48f0",
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
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c48f0",
      "incomplete_value": false,
      "site": "007c48f0",
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
            "const:f18:8"
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
      "007c48f0",
      "DATA",
      [
        "storage",
        "00bfdf18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c48f0",
      "DATA",
      [
        "storage",
        "00bfdf68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c48ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48e4.md#insn-007c48ec)
- 新版 [`007c48ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c48e4.md#insn-007c48ec)

~~~diff
- 007c48ec ["COPY", "tmp:0:8", ["const:f18:8"]]
- 007c48ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c48ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c48ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c48ec ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 007c48ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c48ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c48ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c48ec bytes 29613c91
+ 007c48ec bytes 29a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-794486d642f3b42aa0faab17563421c9"></a>

### [`007c4990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4990.md) → [`007c4990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4990.md) FUN_007c4990

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
      "definition_site": "007c49b4",
      "incomplete_value": false,
      "site": "007c49b4",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c49b4",
      "incomplete_value": false,
      "site": "007c49b4",
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
            "const:fa8:8"
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
      "007c49b4",
      "DATA",
      [
        "storage",
        "00bfdfa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c49b4",
      "DATA",
      [
        "storage",
        "00bfdff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c49b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4990.md#insn-007c49b0)
- 新版 [`007c49b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4990.md#insn-007c49b0)

~~~diff
- 007c49b0 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007c49b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c49b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c49b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c49b0 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 007c49b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c49b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c49b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c49b0 bytes 08a13e91
+ 007c49b0 bytes 08e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f6767782cdf66f67a645c91166ff9a1"></a>

### [`007c49c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c49c4.md) → [`007c49c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c49c4.md) FUN_007c49c4

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
      "definition_site": "007c49d0",
      "incomplete_value": false,
      "site": "007c49d0",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c49d0",
      "incomplete_value": false,
      "site": "007c49d0",
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
      "007c49d0",
      "DATA",
      [
        "storage",
        "00bfdfa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c49d0",
      "DATA",
      [
        "storage",
        "00bfdff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c49cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c49c4.md#insn-007c49cc)
- 新版 [`007c49cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c49c4.md#insn-007c49cc)

~~~diff
- 007c49cc ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007c49cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c49cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c49cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c49cc ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 007c49cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c49cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c49cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c49cc bytes 29a13e91
+ 007c49cc bytes 29e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e631fe6c55f28908ad77c2b473fbed21"></a>

### [`007c49e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c49e0.md) → [`007c49e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c49e0.md) FUN_007c49e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 17件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c4d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d50.md) [`007c4d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d54.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007c4d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4d50.md) [`007c4d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4d54.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.55% / 新版 90.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c4a70",
      "incomplete_value": true,
      "site": "007c4a80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4a70",
      "incomplete_value": true,
      "site": "007c4a80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da5:8"
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
      "definition_site": "007c4a74",
      "incomplete_value": true,
      "site": "007c4a84",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007c4a74",
      "incomplete_value": true,
      "site": "007c4a84",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c4aa8",
      "incomplete_value": false,
      "site": "007c4aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4aa8",
      "incomplete_value": false,
      "site": "007c4aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "007c4a70",
      "READ",
      [
        "storage",
        "00294da5",
        null,
        "string"
      ]
    ],
    [
      "007c4a74",
      "READ",
      [
        "storage",
        "00294db5",
        null,
        "string"
      ]
    ],
    [
      "007c4aa8",
      "DATA",
      [
        "storage",
        "00bfe018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4a70",
      "READ",
      [
        "storage",
        "00294d18",
        null,
        "string"
      ]
    ],
    [
      "007c4a74",
      "READ",
      [
        "storage",
        "00294d28",
        null,
        "string"
      ]
    ],
    [
      "007c4aa8",
      "DATA",
      [
        "storage",
        "00bfe068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c49e0.md#insn-007c4a68) · [`007c4a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c49e0.md#insn-007c4a6c)
- 新版 [`007c4a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c49e0.md#insn-007c4a68) · [`007c4a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c49e0.md#insn-007c4a6c)

~~~diff
- 007c4a68 ["COPY", "tmp:0:8", ["const:da5:8"]]
- 007c4a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4a68 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 007c4a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4a68 bytes 08953691
+ 007c4a68 bytes 08613491
- 007c4a6c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 007c4a6c bytes 69d7ff90
+ 007c4a6c ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 007c4a6c bytes 69d7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8473cebdf1a6a3d010e737b15041d4c2"></a>

### [`007c4d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d08.md) → [`007c4d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4d08.md) FUN_007c4d08

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
      "definition_site": "007c4d2c",
      "incomplete_value": false,
      "site": "007c4d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4d2c",
      "incomplete_value": false,
      "site": "007c4d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "007c4d2c",
      "DATA",
      [
        "storage",
        "00bfe018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4d2c",
      "DATA",
      [
        "storage",
        "00bfe068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d08.md#insn-007c4d28)
- 新版 [`007c4d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4d08.md#insn-007c4d28)

~~~diff
- 007c4d28 ["COPY", "tmp:0:8", ["const:18:8"]]
- 007c4d28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4d28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4d28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4d28 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 007c4d28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4d28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4d28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4d28 bytes 08610091
+ 007c4d28 bytes 08a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27fcf3d59eb5bbf3963333df52523318"></a>

### [`007c4d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d3c.md) → [`007c4d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4d3c.md) FUN_007c4d3c

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
      "definition_site": "007c4d48",
      "incomplete_value": false,
      "site": "007c4d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4d48",
      "incomplete_value": false,
      "site": "007c4d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "007c4d48",
      "DATA",
      [
        "storage",
        "00bfe018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4d48",
      "DATA",
      [
        "storage",
        "00bfe068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d3c.md#insn-007c4d44)
- 新版 [`007c4d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4d3c.md#insn-007c4d44)

~~~diff
- 007c4d44 ["COPY", "tmp:0:8", ["const:18:8"]]
- 007c4d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c4d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c4d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c4d44 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 007c4d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c4d44 bytes 29610091
+ 007c4d44 bytes 29a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-415e3286757780a415f25e7c7dbd9714"></a>

### [`007c4d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d88.md) → [`007c4d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4d88.md) FUN_007c4d88

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
      "definition_site": "007c4dac",
      "incomplete_value": false,
      "site": "007c4dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4dac",
      "incomplete_value": false,
      "site": "007c4dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c4dac",
      "DATA",
      [
        "storage",
        "00bfe098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4dac",
      "DATA",
      [
        "storage",
        "00bfe0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d88.md#insn-007c4da8)
- 新版 [`007c4da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4d88.md#insn-007c4da8)

~~~diff
- 007c4da8 ["COPY", "tmp:0:8", ["const:98:8"]]
- 007c4da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4da8 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 007c4da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4da8 bytes 08610291
+ 007c4da8 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c1ad52447d7ec489b7c43260d9d3be3"></a>

### [`007c4dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4dbc.md) → [`007c4dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4dbc.md) FUN_007c4dbc

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
      "definition_site": "007c4dc8",
      "incomplete_value": false,
      "site": "007c4dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4dc8",
      "incomplete_value": false,
      "site": "007c4dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "007c4dc8",
      "DATA",
      [
        "storage",
        "00bfe098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4dc8",
      "DATA",
      [
        "storage",
        "00bfe0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4dbc.md#insn-007c4dc4)
- 新版 [`007c4dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4dbc.md#insn-007c4dc4)

~~~diff
- 007c4dc4 ["COPY", "tmp:0:8", ["const:98:8"]]
- 007c4dc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c4dc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c4dc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c4dc4 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 007c4dc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4dc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4dc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c4dc4 bytes 29610291
+ 007c4dc4 bytes 29a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d88ddaa7363afac5e5a0505628a51bd3"></a>

### [`007c4f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f38.md) → [`007c4f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4f38.md) FUN_007c4f38

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
      "definition_site": "007c4f5c",
      "incomplete_value": false,
      "site": "007c4f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4f5c",
      "incomplete_value": false,
      "site": "007c4f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c4f5c",
      "DATA",
      [
        "storage",
        "00bfe118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4f5c",
      "DATA",
      [
        "storage",
        "00bfe168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f38.md#insn-007c4f58)
- 新版 [`007c4f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4f38.md#insn-007c4f58)

~~~diff
- 007c4f58 ["COPY", "tmp:0:8", ["const:118:8"]]
- 007c4f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4f58 ["COPY", "tmp:0:8", ["const:168:8"]]
+ 007c4f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4f58 bytes 08610491
+ 007c4f58 bytes 08a10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec70f30ea614899f1c693f5acd9eedb1"></a>

### [`007c4f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f6c.md) → [`007c4f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4f6c.md) FUN_007c4f6c

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
      "definition_site": "007c4f78",
      "incomplete_value": false,
      "site": "007c4f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4f78",
      "incomplete_value": false,
      "site": "007c4f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c4f78",
      "DATA",
      [
        "storage",
        "00bfe118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4f78",
      "DATA",
      [
        "storage",
        "00bfe168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f6c.md#insn-007c4f74)
- 新版 [`007c4f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4f6c.md#insn-007c4f74)

~~~diff
- 007c4f74 ["COPY", "tmp:0:8", ["const:118:8"]]
- 007c4f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c4f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c4f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c4f74 ["COPY", "tmp:0:8", ["const:168:8"]]
+ 007c4f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c4f74 bytes 29610491
+ 007c4f74 bytes 29a10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5af3a0276b83ea45d83858009f86c49b"></a>

### [`007c4f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f88.md) → [`007c4f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4f88.md) FUN_007c4f88

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`004489a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/004489a8.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`00883bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md) [`00883c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883c74.md) [`00883c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883c7c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004489a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/004489a8.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md) [`00883bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883bb8.md) [`00883c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883c74.md) [`00883c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883c7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c4fd8",
      "incomplete_value": true,
      "site": "007c4fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "007c4fd8",
      "incomplete_value": true,
      "site": "007c4fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c4fd4",
      "incomplete_value": false,
      "site": "007c4fe8",
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
      "definition_site": "007c4fd4",
      "incomplete_value": false,
      "site": "007c4fe8",
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
      "definition_site": "007c4fe0",
      "incomplete_value": false,
      "site": "007c4fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4fe0",
      "incomplete_value": false,
      "site": "007c4fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "007c4fd4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c4fd8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c4fe0",
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
      "007c4fd4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c4fd8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c4fe0",
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

- 旧版 [`007c4fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f88.md#insn-007c4fd4) · [`007c4fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f88.md#insn-007c4fd8) · [`007c4fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f88.md#insn-007c4fe0)
- 新版 [`007c4fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4f88.md#insn-007c4fd4) · [`007c4fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4f88.md#insn-007c4fd8) · [`007c4fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4f88.md#insn-007c4fe0)

~~~diff
- 007c4fd4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007c4fd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c4fd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c4fd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c4fd4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007c4fd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c4fd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c4fd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c4fd4 bytes 21203991
+ 007c4fd4 bytes 21603a91
- 007c4fd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007c4fd8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c4fd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007c4fd8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c4fd8 bytes 003d45f9
+ 007c4fd8 bytes 005d45f9
- 007c4fe0 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007c4fe0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c4fe0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c4fe0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c4fe0 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007c4fe0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c4fe0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c4fe0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c4fe0 bytes 42601491
+ 007c4fe0 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64418aa4192b377e59115a9d8c48ced9"></a>

### [`007c50cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c50cc.md) → [`007c50cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c50cc.md) FUN_007c50cc

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
      "definition_site": "007c50f0",
      "incomplete_value": false,
      "site": "007c50f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c50f0",
      "incomplete_value": false,
      "site": "007c50f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "007c50f0",
      "DATA",
      [
        "storage",
        "00bfe1a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c50f0",
      "DATA",
      [
        "storage",
        "00bfe1f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c50ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c50cc.md#insn-007c50ec)
- 新版 [`007c50ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c50cc.md#insn-007c50ec)

~~~diff
- 007c50ec ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 007c50ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c50ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c50ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c50ec ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 007c50ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c50ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c50ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c50ec bytes 08a10691
+ 007c50ec bytes 08e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76fe300dbda64687cd6694a87e0a1a1d"></a>

### [`007c5100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5100.md) → [`007c5100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5100.md) FUN_007c5100

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
      "definition_site": "007c510c",
      "incomplete_value": false,
      "site": "007c510c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c510c",
      "incomplete_value": false,
      "site": "007c510c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "007c510c",
      "DATA",
      [
        "storage",
        "00bfe1a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c510c",
      "DATA",
      [
        "storage",
        "00bfe1f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5100.md#insn-007c5108)
- 新版 [`007c5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5100.md#insn-007c5108)

~~~diff
- 007c5108 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 007c5108 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5108 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5108 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5108 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 007c5108 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5108 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5108 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5108 bytes 29a10691
+ 007c5108 bytes 29e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-084ff0d85af2bb9de47e1798da44a7a3"></a>

### [`007c5174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5174.md) → [`007c5174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5174.md) FUN_007c5174

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
      "definition_site": "007c5188",
      "incomplete_value": false,
      "site": "007c518c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5188",
      "incomplete_value": false,
      "site": "007c518c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "007c518c",
      "DATA",
      [
        "storage",
        "00bfe228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c518c",
      "DATA",
      [
        "storage",
        "00bfe278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5174.md#insn-007c5188)
- 新版 [`007c5188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5174.md#insn-007c5188)

~~~diff
- 007c5188 ["COPY", "tmp:0:8", ["const:228:8"]]
- 007c5188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5188 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 007c5188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5188 bytes 08a10891
+ 007c5188 bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4741c921058d4a784af285ff2e18ad8"></a>

### [`007c5198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5198.md) → [`007c5198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5198.md) FUN_007c5198

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
      "definition_site": "007c519c",
      "incomplete_value": false,
      "site": "007c51a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c519c",
      "incomplete_value": false,
      "site": "007c51a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "007c51a0",
      "DATA",
      [
        "storage",
        "00bfe228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c51a0",
      "DATA",
      [
        "storage",
        "00bfe278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c519c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5198.md#insn-007c519c)
- 新版 [`007c519c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5198.md#insn-007c519c)

~~~diff
- 007c519c ["COPY", "tmp:0:8", ["const:228:8"]]
- 007c519c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c519c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c519c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c519c ["COPY", "tmp:0:8", ["const:278:8"]]
+ 007c519c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c519c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c519c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c519c bytes 08a10891
+ 007c519c bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bca8b59a2951efb9f56227de444c4418"></a>

### [`007c5224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5224.md) → [`007c5224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5224.md) FUN_007c5224

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
      "definition_site": "007c5238",
      "incomplete_value": false,
      "site": "007c523c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5238",
      "incomplete_value": false,
      "site": "007c523c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "007c523c",
      "DATA",
      [
        "storage",
        "00bfe2a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c523c",
      "DATA",
      [
        "storage",
        "00bfe2f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5224.md#insn-007c5238)
- 新版 [`007c5238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5224.md#insn-007c5238)

~~~diff
- 007c5238 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 007c5238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5238 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007c5238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5238 bytes 08a10a91
+ 007c5238 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86b057fa55a73800dab517046997379f"></a>

### [`007c5248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5248.md) → [`007c5248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5248.md) FUN_007c5248

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
      "definition_site": "007c524c",
      "incomplete_value": false,
      "site": "007c5250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c524c",
      "incomplete_value": false,
      "site": "007c5250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "007c5250",
      "DATA",
      [
        "storage",
        "00bfe2a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5250",
      "DATA",
      [
        "storage",
        "00bfe2f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c524c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5248.md#insn-007c524c)
- 新版 [`007c524c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5248.md#insn-007c524c)

~~~diff
- 007c524c ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 007c524c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c524c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c524c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c524c ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007c524c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c524c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c524c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c524c bytes 08a10a91
+ 007c524c bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a19d6f860b13784037cc6a30efb8484f"></a>

### [`007c52d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c52d4.md) → [`007c52d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c52d4.md) FUN_007c52d4

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
      "definition_site": "007c52e8",
      "incomplete_value": false,
      "site": "007c52ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c52e8",
      "incomplete_value": false,
      "site": "007c52ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "007c52ec",
      "DATA",
      [
        "storage",
        "00bfe328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c52ec",
      "DATA",
      [
        "storage",
        "00bfe378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c52e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c52d4.md#insn-007c52e8)
- 新版 [`007c52e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c52d4.md#insn-007c52e8)

~~~diff
- 007c52e8 ["COPY", "tmp:0:8", ["const:328:8"]]
- 007c52e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c52e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c52e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c52e8 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 007c52e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c52e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c52e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c52e8 bytes 08a10c91
+ 007c52e8 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a52c0facc9e6aee715acc359e7d1fa54"></a>

### [`007c52f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c52f8.md) → [`007c52f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c52f8.md) FUN_007c52f8

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
      "definition_site": "007c52fc",
      "incomplete_value": false,
      "site": "007c5300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c52fc",
      "incomplete_value": false,
      "site": "007c5300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "007c5300",
      "DATA",
      [
        "storage",
        "00bfe328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5300",
      "DATA",
      [
        "storage",
        "00bfe378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c52fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c52f8.md#insn-007c52fc)
- 新版 [`007c52fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c52f8.md#insn-007c52fc)

~~~diff
- 007c52fc ["COPY", "tmp:0:8", ["const:328:8"]]
- 007c52fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c52fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c52fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c52fc ["COPY", "tmp:0:8", ["const:378:8"]]
+ 007c52fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c52fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c52fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c52fc bytes 08a10c91
+ 007c52fc bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcbd722b912b12feb35a06cdf6d68b3b"></a>

### [`007c5384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5384.md) → [`007c5384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5384.md) FUN_007c5384

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
      "definition_site": "007c5398",
      "incomplete_value": false,
      "site": "007c539c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5398",
      "incomplete_value": false,
      "site": "007c539c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "007c539c",
      "DATA",
      [
        "storage",
        "00bfe3a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c539c",
      "DATA",
      [
        "storage",
        "00bfe3f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5384.md#insn-007c5398)
- 新版 [`007c5398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5384.md#insn-007c5398)

~~~diff
- 007c5398 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 007c5398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5398 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 007c5398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5398 bytes 08a10e91
+ 007c5398 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bda52de50f9e580cebf221ef431fd67"></a>

### [`007c53a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c53a8.md) → [`007c53a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c53a8.md) FUN_007c53a8

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
      "definition_site": "007c53ac",
      "incomplete_value": false,
      "site": "007c53b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c53ac",
      "incomplete_value": false,
      "site": "007c53b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "007c53b0",
      "DATA",
      [
        "storage",
        "00bfe3a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c53b0",
      "DATA",
      [
        "storage",
        "00bfe3f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c53ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c53a8.md#insn-007c53ac)
- 新版 [`007c53ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c53a8.md#insn-007c53ac)

~~~diff
- 007c53ac ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 007c53ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c53ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c53ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c53ac ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 007c53ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c53ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c53ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c53ac bytes 08a10e91
+ 007c53ac bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89f7e191bae19bd51595678e3f4e093b"></a>

### [`007c5434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5434.md) → [`007c5434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5434.md) FUN_007c5434

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
      "definition_site": "007c5458",
      "incomplete_value": false,
      "site": "007c5458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5458",
      "incomplete_value": false,
      "site": "007c5458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "007c5458",
      "DATA",
      [
        "storage",
        "00bfe428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5458",
      "DATA",
      [
        "storage",
        "00bfe478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5434.md#insn-007c5454)
- 新版 [`007c5454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5434.md#insn-007c5454)

~~~diff
- 007c5454 ["COPY", "tmp:0:8", ["const:428:8"]]
- 007c5454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5454 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 007c5454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5454 bytes 08a11091
+ 007c5454 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d521ba830c829b5d7d8ed467ada9281b"></a>

### [`007c5468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5468.md) → [`007c5468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5468.md) FUN_007c5468

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
      "definition_site": "007c5474",
      "incomplete_value": false,
      "site": "007c5474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5474",
      "incomplete_value": false,
      "site": "007c5474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "007c5474",
      "DATA",
      [
        "storage",
        "00bfe428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5474",
      "DATA",
      [
        "storage",
        "00bfe478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5468.md#insn-007c5470)
- 新版 [`007c5470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5468.md#insn-007c5470)

~~~diff
- 007c5470 ["COPY", "tmp:0:8", ["const:428:8"]]
- 007c5470 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5470 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5470 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5470 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 007c5470 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5470 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5470 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5470 bytes 29a11091
+ 007c5470 bytes 29e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a4bbdf2fe5a8b39336eee105ad06400"></a>

### [`007c5484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5484.md) → [`007c5484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5484.md) FUN_007c5484

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c5768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5768.md) [`007c576c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c576c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007c5768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5768.md) [`007c576c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c576c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c5578",
      "incomplete_value": false,
      "site": "007c5578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5578",
      "incomplete_value": false,
      "site": "007c5578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007c5508",
      "READ",
      [
        "storage",
        "0029c949",
        null,
        "string"
      ]
    ],
    [
      "007c5510",
      "READ",
      [
        "storage",
        "0029c94f",
        null,
        "string"
      ]
    ],
    [
      "007c553c",
      "DATA",
      [
        "storage",
        "00bfe498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5508",
      "READ",
      [
        "storage",
        "0029c9d4",
        null,
        "string"
      ]
    ],
    [
      "007c5510",
      "READ",
      [
        "storage",
        "0029c9da",
        null,
        "string"
      ]
    ],
    [
      "007c553c",
      "DATA",
      [
        "storage",
        "00bfe4e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5484.md#insn-007c5504) · [`007c5534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5484.md#insn-007c5534) · [`007c5570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5484.md#insn-007c5570)
- 新版 [`007c5504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5484.md#insn-007c5504) · [`007c5534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5484.md#insn-007c5534) · [`007c5570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5484.md#insn-007c5570)

~~~diff
- 007c5504 ["COPY", "tmp:0:8", ["const:949:8"]]
- 007c5504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5504 ["COPY", "tmp:0:8", ["const:9d4:8"]]
+ 007c5504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5504 bytes 29252591
+ 007c5504 bytes 29512791
- 007c5534 ["COPY", "tmp:0:8", ["const:498:8"]]
- 007c5534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5534 ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 007c5534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5534 bytes 08611291
+ 007c5534 bytes 08a11391
- 007c5570 ["COPY", "tmp:0:8", ["const:798:8"]]
- 007c5570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5570 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 007c5570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5570 bytes 08611e91
+ 007c5570 bytes 08a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59dfee3fd7ee7095787b2ed54eaec7c2"></a>

### [`007c5720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5720.md) → [`007c5720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5720.md) FUN_007c5720

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
      "definition_site": "007c5744",
      "incomplete_value": false,
      "site": "007c5744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5744",
      "incomplete_value": false,
      "site": "007c5744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "007c5744",
      "DATA",
      [
        "storage",
        "00bfe498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5744",
      "DATA",
      [
        "storage",
        "00bfe4e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5720.md#insn-007c5740)
- 新版 [`007c5740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5720.md#insn-007c5740)

~~~diff
- 007c5740 ["COPY", "tmp:0:8", ["const:498:8"]]
- 007c5740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5740 ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 007c5740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5740 bytes 08611291
+ 007c5740 bytes 08a11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c097e890009293ad34764fd992d1743a"></a>

### [`007c5754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5754.md) → [`007c5754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5754.md) FUN_007c5754

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
      "definition_site": "007c5760",
      "incomplete_value": false,
      "site": "007c5760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5760",
      "incomplete_value": false,
      "site": "007c5760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c5760",
      "DATA",
      [
        "storage",
        "00bfe498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5760",
      "DATA",
      [
        "storage",
        "00bfe4e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c575c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5754.md#insn-007c575c)
- 新版 [`007c575c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5754.md#insn-007c575c)

~~~diff
- 007c575c ["COPY", "tmp:0:8", ["const:498:8"]]
- 007c575c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c575c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c575c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c575c ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 007c575c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c575c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c575c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c575c bytes 29611291
+ 007c575c bytes 29a11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a926ab8e612c406bb0cee76736aed6d9"></a>

### [`007c5770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5770.md) → [`007c5770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5770.md) FUN_007c5770

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c5ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ac8.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007c5ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ac8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c5810",
      "incomplete_value": false,
      "site": "007c5810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5810",
      "incomplete_value": false,
      "site": "007c5810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "definition_site": "007c5840",
      "incomplete_value": false,
      "site": "007c5840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5840",
      "incomplete_value": false,
      "site": "007c5840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:688:8"
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
      "definition_site": "007c5860",
      "incomplete_value": false,
      "site": "007c5860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5860",
      "incomplete_value": false,
      "site": "007c5860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:708:8"
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
      "007c5810",
      "DATA",
      [
        "storage",
        "00bfe508",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5840",
      "DATA",
      [
        "storage",
        "00bfe688",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5860",
      "DATA",
      [
        "storage",
        "00bfe708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5810",
      "DATA",
      [
        "storage",
        "00bfe558",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5840",
      "DATA",
      [
        "storage",
        "00bfe6d8",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5860",
      "DATA",
      [
        "storage",
        "00bfe758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5770.md#insn-007c5808) · [`007c583c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5770.md#insn-007c583c) · [`007c5858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5770.md#insn-007c5858)
- 新版 [`007c5808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5770.md#insn-007c5808) · [`007c583c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5770.md#insn-007c583c) · [`007c5858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5770.md#insn-007c5858)

~~~diff
- 007c5808 ["COPY", "tmp:0:8", ["const:508:8"]]
- 007c5808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5808 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 007c5808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5808 bytes 08211491
+ 007c5808 bytes 08611591
- 007c583c ["COPY", "tmp:0:8", ["const:688:8"]]
- 007c583c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c583c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c583c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c583c ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 007c583c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c583c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c583c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c583c bytes 08211a91
+ 007c583c bytes 08611b91
- 007c5858 ["COPY", "tmp:0:8", ["const:708:8"]]
- 007c5858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5858 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 007c5858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5858 bytes 08211c91
+ 007c5858 bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cfdaf1132e03d58ab444990ba4e94cc"></a>

### [`007c5a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5a80.md) → [`007c5a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5a80.md) FUN_007c5a80

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
      "definition_site": "007c5aa4",
      "incomplete_value": false,
      "site": "007c5aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5aa4",
      "incomplete_value": false,
      "site": "007c5aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "007c5aa4",
      "DATA",
      [
        "storage",
        "00bfe508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5aa4",
      "DATA",
      [
        "storage",
        "00bfe558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5a80.md#insn-007c5aa0)
- 新版 [`007c5aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5a80.md#insn-007c5aa0)

~~~diff
- 007c5aa0 ["COPY", "tmp:0:8", ["const:508:8"]]
- 007c5aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5aa0 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 007c5aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5aa0 bytes 08211491
+ 007c5aa0 bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c10623d64cb33b26175fc3282b35fd62"></a>

### [`007c5ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ab4.md) → [`007c5ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ab4.md) FUN_007c5ab4

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
      "definition_site": "007c5ac0",
      "incomplete_value": false,
      "site": "007c5ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5ac0",
      "incomplete_value": false,
      "site": "007c5ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "007c5ac0",
      "DATA",
      [
        "storage",
        "00bfe508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5ac0",
      "DATA",
      [
        "storage",
        "00bfe558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ab4.md#insn-007c5abc)
- 新版 [`007c5abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ab4.md#insn-007c5abc)

~~~diff
- 007c5abc ["COPY", "tmp:0:8", ["const:508:8"]]
- 007c5abc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5abc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5abc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5abc ["COPY", "tmp:0:8", ["const:558:8"]]
+ 007c5abc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5abc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5abc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5abc bytes 29211491
+ 007c5abc bytes 29611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-833586b7f4864b433a1f65633c813717"></a>

### [`007c5ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ad0.md) → [`007c5ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ad0.md) FUN_007c5ad0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c5d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d70.md) [`007c5d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d74.md) [`007c5e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5e2c.md) [`007c5e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5e30.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007c5d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d70.md) [`007c5d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d74.md) [`007c5e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5e2c.md) [`007c5e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5e30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c5b44",
      "incomplete_value": false,
      "site": "007c5b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5b44",
      "incomplete_value": false,
      "site": "007c5b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "007c5b10",
      "READ",
      [
        "storage",
        "002aef0f",
        null,
        "string"
      ]
    ],
    [
      "007c5b18",
      "READ",
      [
        "storage",
        "002aef15",
        null,
        "string"
      ]
    ],
    [
      "007c5b44",
      "DATA",
      [
        "storage",
        "00bfe578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5b10",
      "READ",
      [
        "storage",
        "002aee7b",
        null,
        "string"
      ]
    ],
    [
      "007c5b18",
      "READ",
      [
        "storage",
        "002aee81",
        null,
        "string"
      ]
    ],
    [
      "007c5b44",
      "DATA",
      [
        "storage",
        "00bfe5c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ad0.md#insn-007c5b0c) · [`007c5b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ad0.md#insn-007c5b3c) · [`007c5b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ad0.md#insn-007c5b78)
- 新版 [`007c5b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ad0.md#insn-007c5b0c) · [`007c5b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ad0.md#insn-007c5b3c) · [`007c5b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ad0.md#insn-007c5b78)

~~~diff
- 007c5b0c ["COPY", "tmp:0:8", ["const:f0f:8"]]
- 007c5b0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5b0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5b0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5b0c ["COPY", "tmp:0:8", ["const:e7b:8"]]
+ 007c5b0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5b0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5b0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5b0c bytes 293d3c91
+ 007c5b0c bytes 29ed3991
- 007c5b3c ["COPY", "tmp:0:8", ["const:578:8"]]
- 007c5b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5b3c ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 007c5b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5b3c bytes 08e11591
+ 007c5b3c bytes 08211791
- 007c5b78 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 007c5b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5b78 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 007c5b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5b78 bytes 08e11791
+ 007c5b78 bytes 08211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf2e206a07a070b291b30441e2a1efd9"></a>

### [`007c5d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d28.md) → [`007c5d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d28.md) FUN_007c5d28

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
      "definition_site": "007c5d4c",
      "incomplete_value": false,
      "site": "007c5d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5d4c",
      "incomplete_value": false,
      "site": "007c5d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "007c5d4c",
      "DATA",
      [
        "storage",
        "00bfe578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5d4c",
      "DATA",
      [
        "storage",
        "00bfe5c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d28.md#insn-007c5d48)
- 新版 [`007c5d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d28.md#insn-007c5d48)

~~~diff
- 007c5d48 ["COPY", "tmp:0:8", ["const:578:8"]]
- 007c5d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5d48 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 007c5d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5d48 bytes 08e11591
+ 007c5d48 bytes 08211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0e67aaf62bcb59a18ad112a54eeb1da"></a>

### [`007c5d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d5c.md) → [`007c5d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d5c.md) FUN_007c5d5c

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
      "definition_site": "007c5d68",
      "incomplete_value": false,
      "site": "007c5d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5d68",
      "incomplete_value": false,
      "site": "007c5d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "007c5d68",
      "DATA",
      [
        "storage",
        "00bfe578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5d68",
      "DATA",
      [
        "storage",
        "00bfe5c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d5c.md#insn-007c5d64)
- 新版 [`007c5d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d5c.md#insn-007c5d64)

~~~diff
- 007c5d64 ["COPY", "tmp:0:8", ["const:578:8"]]
- 007c5d64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5d64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5d64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5d64 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 007c5d64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5d64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5d64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5d64 bytes 29e11591
+ 007c5d64 bytes 29211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7078298b06109b413aca4ab10a1a3bf2"></a>

### [`007c5de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5de4.md) → [`007c5de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5de4.md) FUN_007c5de4

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
      "definition_site": "007c5e08",
      "incomplete_value": false,
      "site": "007c5e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5e08",
      "incomplete_value": false,
      "site": "007c5e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c5e08",
      "DATA",
      [
        "storage",
        "00bfe5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5e08",
      "DATA",
      [
        "storage",
        "00bfe648",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5de4.md#insn-007c5e04)
- 新版 [`007c5e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5de4.md#insn-007c5e04)

~~~diff
- 007c5e04 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 007c5e04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5e04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5e04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5e04 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 007c5e04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5e04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5e04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5e04 bytes 08e11791
+ 007c5e04 bytes 08211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0161d6ab39a519d1a35043efaa6011d8"></a>

### [`007c5e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5e18.md) → [`007c5e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5e18.md) FUN_007c5e18

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
      "definition_site": "007c5e24",
      "incomplete_value": false,
      "site": "007c5e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5e24",
      "incomplete_value": false,
      "site": "007c5e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c5e24",
      "DATA",
      [
        "storage",
        "00bfe5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5e24",
      "DATA",
      [
        "storage",
        "00bfe648",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5e18.md#insn-007c5e20)
- 新版 [`007c5e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5e18.md#insn-007c5e20)

~~~diff
- 007c5e20 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 007c5e20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5e20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5e20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5e20 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 007c5e20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5e20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5e20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5e20 bytes 29e11791
+ 007c5e20 bytes 29211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3681cabeb203b6d6ffeb5548e04cc02"></a>

### [`007c616c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c616c.md) → [`007c616c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c616c.md) FUN_007c616c

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
      "definition_site": "007c6190",
      "incomplete_value": false,
      "site": "007c6190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6190",
      "incomplete_value": false,
      "site": "007c6190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6190",
      "DATA",
      [
        "storage",
        "00bfe688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6190",
      "DATA",
      [
        "storage",
        "00bfe6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c618c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c616c.md#insn-007c618c)
- 新版 [`007c618c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c616c.md#insn-007c618c)

~~~diff
- 007c618c ["COPY", "tmp:0:8", ["const:688:8"]]
- 007c618c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c618c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c618c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c618c ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 007c618c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c618c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c618c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c618c bytes 08211a91
+ 007c618c bytes 08611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1713dffecf8dde671b36bb2d2719fb50"></a>

### [`007c61a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c61a0.md) → [`007c61a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c61a0.md) FUN_007c61a0

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
      "definition_site": "007c61ac",
      "incomplete_value": false,
      "site": "007c61ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c61ac",
      "incomplete_value": false,
      "site": "007c61ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c61ac",
      "DATA",
      [
        "storage",
        "00bfe688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c61ac",
      "DATA",
      [
        "storage",
        "00bfe6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c61a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c61a0.md#insn-007c61a8)
- 新版 [`007c61a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c61a0.md#insn-007c61a8)

~~~diff
- 007c61a8 ["COPY", "tmp:0:8", ["const:688:8"]]
- 007c61a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c61a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c61a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c61a8 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 007c61a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c61a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c61a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c61a8 bytes 29211a91
+ 007c61a8 bytes 29611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eba3ed0604a65f30264759eda2b9551d"></a>

### [`007c6294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6294.md) → [`007c6294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6294.md) FUN_007c6294

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
      "definition_site": "007c62a0",
      "incomplete_value": false,
      "site": "007c62a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c62a0",
      "incomplete_value": false,
      "site": "007c62a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c62a0",
      "DATA",
      [
        "storage",
        "00bfe708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c62a0",
      "DATA",
      [
        "storage",
        "00bfe758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c629c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6294.md#insn-007c629c)
- 新版 [`007c629c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6294.md#insn-007c629c)

~~~diff
- 007c629c ["COPY", "tmp:0:8", ["const:708:8"]]
- 007c629c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c629c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c629c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c629c ["COPY", "tmp:0:8", ["const:758:8"]]
+ 007c629c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c629c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c629c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c629c bytes 29211c91
+ 007c629c bytes 29611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e839eb7cb9b8a035561e7f800f940b6"></a>

### [`007c62b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c62b0.md) → [`007c62b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c62b0.md) FUN_007c62b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004489a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004489a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007c62fc",
      "incomplete_value": true,
      "site": "007c62fc",
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
      "definition_site": "007c62fc",
      "incomplete_value": true,
      "site": "007c62fc",
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
      "definition_site": "007c6304",
      "incomplete_value": false,
      "site": "007c6314",
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
      "definition_site": "007c6304",
      "incomplete_value": false,
      "site": "007c6314",
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
      "definition_site": "007c630c",
      "incomplete_value": false,
      "site": "007c6314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c630c",
      "incomplete_value": false,
      "site": "007c6314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "007c62e0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c6304",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c630c",
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
      "007c62e0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c6304",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c630c",
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

- 旧版 [`007c62e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c62b0.md#insn-007c62e0) · [`007c6304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c62b0.md#insn-007c6304) · [`007c630c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c62b0.md#insn-007c630c)
- 新版 [`007c62e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c62b0.md#insn-007c62e0) · [`007c6304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c62b0.md#insn-007c6304) · [`007c630c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c62b0.md#insn-007c630c)

~~~diff
- 007c62e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007c62e0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c62e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007c62e0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c62e0 bytes 003d45f9
+ 007c62e0 bytes 005d45f9
- 007c6304 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007c6304 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c6304 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c6304 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c6304 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007c6304 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c6304 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c6304 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c6304 bytes 21203991
+ 007c6304 bytes 21603a91
- 007c630c ["COPY", "tmp:0:8", ["const:518:8"]]
- 007c630c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c630c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c630c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c630c ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007c630c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c630c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c630c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c630c bytes 42601491
+ 007c630c bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a84b35391379a976d46e3438342b69a2"></a>

### [`007c6448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6448.md) → [`007c6448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6448.md) FUN_007c6448

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
      "definition_site": "007c646c",
      "incomplete_value": false,
      "site": "007c646c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c646c",
      "incomplete_value": false,
      "site": "007c646c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "007c646c",
      "DATA",
      [
        "storage",
        "00bfe798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c646c",
      "DATA",
      [
        "storage",
        "00bfe7e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6448.md#insn-007c6468)
- 新版 [`007c6468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6448.md#insn-007c6468)

~~~diff
- 007c6468 ["COPY", "tmp:0:8", ["const:798:8"]]
- 007c6468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6468 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 007c6468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6468 bytes 08611e91
+ 007c6468 bytes 08a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a761d029613b46fca779ac0394a6749"></a>

### [`007c647c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c647c.md) → [`007c647c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c647c.md) FUN_007c647c

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
      "definition_site": "007c6488",
      "incomplete_value": false,
      "site": "007c6488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6488",
      "incomplete_value": false,
      "site": "007c6488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6488",
      "DATA",
      [
        "storage",
        "00bfe798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6488",
      "DATA",
      [
        "storage",
        "00bfe7e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c647c.md#insn-007c6484)
- 新版 [`007c6484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c647c.md#insn-007c6484)

~~~diff
- 007c6484 ["COPY", "tmp:0:8", ["const:798:8"]]
- 007c6484 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c6484 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c6484 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c6484 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 007c6484 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c6484 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c6484 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c6484 bytes 29611e91
+ 007c6484 bytes 29a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-450fd67e9a81c6b956140c4c170245f1"></a>

### [`007c6498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6498.md) → [`007c6498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6498.md) FUN_007c6498

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md) [`004489a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00447378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447378.md) [`004489a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 97.99% / 新版 97.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007c64f0",
      "incomplete_value": true,
      "site": "007c64f0",
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
      "definition_site": "007c64f0",
      "incomplete_value": true,
      "site": "007c64f0",
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
      "007c64d4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c64f8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c6500",
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
      "007c64d4",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c64f8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c6500",
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

- 旧版 [`007c64d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6498.md#insn-007c64d4) · [`007c64f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6498.md#insn-007c64f8) · [`007c6500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6498.md#insn-007c6500)
- 新版 [`007c64d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6498.md#insn-007c64d4) · [`007c64f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6498.md#insn-007c64f8) · [`007c6500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6498.md#insn-007c6500)

~~~diff
- 007c64d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 007c64d4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c64d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 007c64d4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c64d4 bytes 003d45f9
+ 007c64d4 bytes 005d45f9
- 007c64f8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007c64f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c64f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c64f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c64f8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007c64f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c64f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c64f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c64f8 bytes 21203991
+ 007c64f8 bytes 21603a91
- 007c6500 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007c6500 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c6500 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c6500 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c6500 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007c6500 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c6500 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c6500 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c6500 bytes 42601491
+ 007c6500 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e53e91d08e9fd04b8ffb253ba46ab89b"></a>

### [`007c67e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c67e0.md) → [`007c67e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c67e0.md) FUN_007c67e0

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
      "definition_site": "007c6804",
      "incomplete_value": false,
      "site": "007c6804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6804",
      "incomplete_value": false,
      "site": "007c6804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6804",
      "DATA",
      [
        "storage",
        "00bfe828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6804",
      "DATA",
      [
        "storage",
        "00bfe878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c67e0.md#insn-007c6800)
- 新版 [`007c6800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c67e0.md#insn-007c6800)

~~~diff
- 007c6800 ["COPY", "tmp:0:8", ["const:828:8"]]
- 007c6800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6800 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 007c6800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6800 bytes 08a12091
+ 007c6800 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-624223aa3efee5efda6e215e3d7637e9"></a>

### [`007c6814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6814.md) → [`007c6814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6814.md) FUN_007c6814

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
      "definition_site": "007c6820",
      "incomplete_value": false,
      "site": "007c6820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6820",
      "incomplete_value": false,
      "site": "007c6820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6820",
      "DATA",
      [
        "storage",
        "00bfe828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6820",
      "DATA",
      [
        "storage",
        "00bfe878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6814.md#insn-007c681c)
- 新版 [`007c681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6814.md#insn-007c681c)

~~~diff
- 007c681c ["COPY", "tmp:0:8", ["const:828:8"]]
- 007c681c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c681c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c681c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c681c ["COPY", "tmp:0:8", ["const:878:8"]]
+ 007c681c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c681c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c681c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c681c bytes 29a12091
+ 007c681c bytes 29e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e5fb215a4906181418b45710d0f2205"></a>

### [`007c6830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6830.md) → [`007c6830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6830.md) FUN_007c6830

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`004489a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`004489a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.33% / 新版 96.33%

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
      "definition_site": "007c6870",
      "incomplete_value": true,
      "site": "007c6870",
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
      "definition_site": "007c6870",
      "incomplete_value": true,
      "site": "007c6870",
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
      "definition_site": "007c6878",
      "incomplete_value": false,
      "site": "007c6888",
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
      "definition_site": "007c6878",
      "incomplete_value": false,
      "site": "007c6888",
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
      "definition_site": "007c6880",
      "incomplete_value": false,
      "site": "007c6888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6880",
      "incomplete_value": false,
      "site": "007c6888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "007c6860",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c6878",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c6880",
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
      "007c6860",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c6878",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c6880",
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

- 旧版 [`007c6860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6830.md#insn-007c6860) · [`007c6878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6830.md#insn-007c6878) · [`007c6880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6830.md#insn-007c6880)
- 新版 [`007c6860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6830.md#insn-007c6860) · [`007c6878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6830.md#insn-007c6878) · [`007c6880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6830.md#insn-007c6880)

~~~diff
- 007c6860 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 007c6860 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c6860 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 007c6860 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c6860 bytes 203d45f9
+ 007c6860 bytes 205d45f9
- 007c6878 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007c6878 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c6878 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c6878 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c6878 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 007c6878 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c6878 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c6878 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c6878 bytes 21203991
+ 007c6878 bytes 21603a91
- 007c6880 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007c6880 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c6880 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c6880 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c6880 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007c6880 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c6880 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c6880 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c6880 bytes 42601491
+ 007c6880 bytes 42a01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a654ee639cab566b2299de3da0828240"></a>

### [`007c6a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6a3c.md) → [`007c6a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a3c.md) FUN_007c6a3c

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
      "definition_site": "007c6a50",
      "incomplete_value": false,
      "site": "007c6a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6a50",
      "incomplete_value": false,
      "site": "007c6a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6a54",
      "DATA",
      [
        "storage",
        "00bfe8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6a54",
      "DATA",
      [
        "storage",
        "00bfe8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6a3c.md#insn-007c6a50)
- 新版 [`007c6a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a3c.md#insn-007c6a50)

~~~diff
- 007c6a50 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 007c6a50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6a50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6a50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6a50 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 007c6a50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6a50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6a50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6a50 bytes 08a12291
+ 007c6a50 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ff515ce08a451bdb591f62776a5a242"></a>

### [`007c6a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6a60.md) → [`007c6a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a60.md) FUN_007c6a60

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
      "definition_site": "007c6a64",
      "incomplete_value": false,
      "site": "007c6a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6a64",
      "incomplete_value": false,
      "site": "007c6a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6a68",
      "DATA",
      [
        "storage",
        "00bfe8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6a68",
      "DATA",
      [
        "storage",
        "00bfe8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6a60.md#insn-007c6a64)
- 新版 [`007c6a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a60.md#insn-007c6a64)

~~~diff
- 007c6a64 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 007c6a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6a64 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 007c6a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6a64 bytes 08a12291
+ 007c6a64 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4e82e8b9843771f5b2d4ab0616cf899"></a>

### [`007c6b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6b10.md) → [`007c6b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b10.md) FUN_007c6b10

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
      "definition_site": "007c6b14",
      "incomplete_value": false,
      "site": "007c6b18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6b14",
      "incomplete_value": false,
      "site": "007c6b18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "007c6b18",
      "DATA",
      [
        "storage",
        "00bfe928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6b18",
      "DATA",
      [
        "storage",
        "00bfe978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6b10.md#insn-007c6b14)
- 新版 [`007c6b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b10.md#insn-007c6b14)

~~~diff
- 007c6b14 ["COPY", "tmp:0:8", ["const:928:8"]]
- 007c6b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6b14 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 007c6b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6b14 bytes 08a12491
+ 007c6b14 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54be527d5b3096790e2040db0d605c88"></a>

### [`007c6b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6b9c.md) → [`007c6b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b9c.md) FUN_007c6b9c

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
      "definition_site": "007c6bb0",
      "incomplete_value": false,
      "site": "007c6bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6bb0",
      "incomplete_value": false,
      "site": "007c6bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6bb4",
      "DATA",
      [
        "storage",
        "00bfe9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6bb4",
      "DATA",
      [
        "storage",
        "00bfe9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6b9c.md#insn-007c6bb0)
- 新版 [`007c6bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b9c.md#insn-007c6bb0)

~~~diff
- 007c6bb0 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 007c6bb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6bb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6bb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6bb0 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 007c6bb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6bb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6bb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6bb0 bytes 08a12691
+ 007c6bb0 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ae00dfb507154873b6a3437fbae89b"></a>

### [`007c6bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6bc0.md) → [`007c6bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6bc0.md) FUN_007c6bc0

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
      "definition_site": "007c6bc4",
      "incomplete_value": false,
      "site": "007c6bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6bc4",
      "incomplete_value": false,
      "site": "007c6bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6bc8",
      "DATA",
      [
        "storage",
        "00bfe9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6bc8",
      "DATA",
      [
        "storage",
        "00bfe9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6bc0.md#insn-007c6bc4)
- 新版 [`007c6bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6bc0.md#insn-007c6bc4)

~~~diff
- 007c6bc4 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 007c6bc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6bc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6bc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6bc4 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 007c6bc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6bc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6bc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6bc4 bytes 08a12691
+ 007c6bc4 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bec9adbc2ae0c376c586569fe8df413"></a>

### [`007c6c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6c4c.md) → [`007c6c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c4c.md) FUN_007c6c4c

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
      "definition_site": "007c6c60",
      "incomplete_value": false,
      "site": "007c6c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6c60",
      "incomplete_value": false,
      "site": "007c6c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6c64",
      "DATA",
      [
        "storage",
        "00bfea28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6c64",
      "DATA",
      [
        "storage",
        "00bfea78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6c4c.md#insn-007c6c60)
- 新版 [`007c6c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c4c.md#insn-007c6c60)

~~~diff
- 007c6c60 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 007c6c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6c60 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 007c6c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6c60 bytes 08a12891
+ 007c6c60 bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb4b9f65c2c96e93ae89873bb06f7b78"></a>

### [`007c6c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6c70.md) → [`007c6c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c70.md) FUN_007c6c70

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
      "definition_site": "007c6c74",
      "incomplete_value": false,
      "site": "007c6c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6c74",
      "incomplete_value": false,
      "site": "007c6c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6c78",
      "DATA",
      [
        "storage",
        "00bfea28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6c78",
      "DATA",
      [
        "storage",
        "00bfea78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6c70.md#insn-007c6c74)
- 新版 [`007c6c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c70.md#insn-007c6c74)

~~~diff
- 007c6c74 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 007c6c74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6c74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6c74 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 007c6c74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6c74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6c74 bytes 08a12891
+ 007c6c74 bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4b253bd5c879f940e5ea1738bfcc57c"></a>

### [`007c6cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6cfc.md) → [`007c6cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6cfc.md) FUN_007c6cfc

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
      "definition_site": "007c6d10",
      "incomplete_value": false,
      "site": "007c6d14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6d10",
      "incomplete_value": false,
      "site": "007c6d14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "007c6d14",
      "DATA",
      [
        "storage",
        "00bfeaa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6d14",
      "DATA",
      [
        "storage",
        "00bfeaf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6cfc.md#insn-007c6d10)
- 新版 [`007c6d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6cfc.md#insn-007c6d10)

~~~diff
- 007c6d10 ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 007c6d10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6d10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6d10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6d10 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 007c6d10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6d10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6d10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6d10 bytes 08a12a91
+ 007c6d10 bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd06fd8fdc295bfd4f4b7628f6457acf"></a>

### [`007c6d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6d20.md) → [`007c6d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6d20.md) FUN_007c6d20

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
      "definition_site": "007c6d24",
      "incomplete_value": false,
      "site": "007c6d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6d24",
      "incomplete_value": false,
      "site": "007c6d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6d28",
      "DATA",
      [
        "storage",
        "00bfeaa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6d28",
      "DATA",
      [
        "storage",
        "00bfeaf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6d20.md#insn-007c6d24)
- 新版 [`007c6d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6d20.md#insn-007c6d24)

~~~diff
- 007c6d24 ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 007c6d24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6d24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6d24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6d24 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 007c6d24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6d24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6d24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6d24 bytes 08a12a91
+ 007c6d24 bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd54036f9a7489674d2a4c3703f2a071"></a>

### [`007c6dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6dac.md) → [`007c6dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6dac.md) FUN_007c6dac

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
      "definition_site": "007c6dcc",
      "incomplete_value": false,
      "site": "007c6dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6dcc",
      "incomplete_value": false,
      "site": "007c6dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6dd0",
      "DATA",
      [
        "storage",
        "00bfeb28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6dd0",
      "DATA",
      [
        "storage",
        "00bfeb78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6dac.md#insn-007c6dcc)
- 新版 [`007c6dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6dac.md#insn-007c6dcc)

~~~diff
- 007c6dcc ["COPY", "tmp:0:8", ["const:b28:8"]]
- 007c6dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6dcc ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 007c6dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6dcc bytes 08a12c91
+ 007c6dcc bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea27d671c8cc45c61134fb11ac5f949"></a>

### [`007c6de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6de4.md) → [`007c6de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6de4.md) FUN_007c6de4

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
      "definition_site": "007c6de8",
      "incomplete_value": false,
      "site": "007c6dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6de8",
      "incomplete_value": false,
      "site": "007c6dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6dec",
      "DATA",
      [
        "storage",
        "00bfeb28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6dec",
      "DATA",
      [
        "storage",
        "00bfeb78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6de4.md#insn-007c6de8)
- 新版 [`007c6de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6de4.md#insn-007c6de8)

~~~diff
- 007c6de8 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 007c6de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6de8 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 007c6de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6de8 bytes 08a12c91
+ 007c6de8 bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-303cf911313b06a0950e070a94679acb"></a>

### [`007c6e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6e78.md) → [`007c6e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6e78.md) FUN_007c6e78

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
      "definition_site": "007c6e8c",
      "incomplete_value": true,
      "site": "007c6e90",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6e8c",
      "incomplete_value": true,
      "site": "007c6e90",
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
      "007c6e90",
      "DATA",
      [
        "storage",
        "00bfeba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6e90",
      "DATA",
      [
        "storage",
        "00bfebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6e78.md#insn-007c6e8c)
- 新版 [`007c6e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6e78.md#insn-007c6e8c)

~~~diff
- 007c6e8c ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 007c6e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6e8c ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 007c6e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6e8c bytes 08a12e91
+ 007c6e8c bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7b22260c0b27e2ed1320e850fdf40b9"></a>

### [`007c6e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6e9c.md) → [`007c6e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6e9c.md) FUN_007c6e9c

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
      "definition_site": "007c6ea0",
      "incomplete_value": false,
      "site": "007c6ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6ea0",
      "incomplete_value": false,
      "site": "007c6ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6ea4",
      "DATA",
      [
        "storage",
        "00bfeba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6ea4",
      "DATA",
      [
        "storage",
        "00bfebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6e9c.md#insn-007c6ea0)
- 新版 [`007c6ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6e9c.md#insn-007c6ea0)

~~~diff
- 007c6ea0 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 007c6ea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6ea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6ea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6ea0 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 007c6ea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6ea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6ea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6ea0 bytes 08a12e91
+ 007c6ea0 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89c606b17cdac9f7326f4cb705470d59"></a>

### [`007c6f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f28.md) → [`007c6f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6f28.md) FUN_007c6f28

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
      "definition_site": "007c6f48",
      "incomplete_value": false,
      "site": "007c6f4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6f48",
      "incomplete_value": false,
      "site": "007c6f4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6f4c",
      "DATA",
      [
        "storage",
        "00bfec28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6f4c",
      "DATA",
      [
        "storage",
        "00bfec78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f28.md#insn-007c6f48)
- 新版 [`007c6f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6f28.md#insn-007c6f48)

~~~diff
- 007c6f48 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 007c6f48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6f48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6f48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6f48 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 007c6f48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6f48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6f48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6f48 bytes 08a13091
+ 007c6f48 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-469541a6b688d48a5fcc7cab91000849"></a>

### [`007c6f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f60.md) → [`007c6f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6f60.md) FUN_007c6f60

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
      "definition_site": "007c6f64",
      "incomplete_value": false,
      "site": "007c6f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6f64",
      "incomplete_value": false,
      "site": "007c6f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6f68",
      "DATA",
      [
        "storage",
        "00bfec28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6f68",
      "DATA",
      [
        "storage",
        "00bfec78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f60.md#insn-007c6f64)
- 新版 [`007c6f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6f60.md#insn-007c6f64)

~~~diff
- 007c6f64 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 007c6f64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6f64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6f64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6f64 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 007c6f64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6f64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6f64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6f64 bytes 08a13091
+ 007c6f64 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7abdca6c514574059df1ab11c613ec8d"></a>

### [`007c6f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f80.md) → [`007c6f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6f80.md) FUN_007c6f80

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.89% / 新版 96.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c71a0",
      "incomplete_value": true,
      "site": "007c71a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c71a0",
      "incomplete_value": true,
      "site": "007c71a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a5:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c7330",
      "incomplete_value": false,
      "site": "007c7330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c7330",
      "incomplete_value": false,
      "site": "007c7330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "007c7094",
      "READ",
      [
        "storage",
        "002a3916",
        null,
        "string"
      ]
    ],
    [
      "007c7184",
      "READ",
      [
        "storage",
        "002a27a5",
        null,
        "string"
      ]
    ],
    [
      "007c71e0",
      "DATA",
      [
        "storage",
        "00bfed18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c7094",
      "READ",
      [
        "storage",
        "002a39a1",
        null,
        "string"
      ]
    ],
    [
      "007c7184",
      "READ",
      [
        "storage",
        "002a2830",
        null,
        "string"
      ]
    ],
    [
      "007c71e0",
      "DATA",
      [
        "storage",
        "00bfed68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c708c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f80.md#insn-007c708c) · [`007c7180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f80.md#insn-007c7180) · [`007c71d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f80.md#insn-007c71d8)
- 新版 [`007c708c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6f80.md#insn-007c708c) · [`007c7180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6f80.md#insn-007c7180) · [`007c71d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6f80.md#insn-007c71d8)

~~~diff
- 007c708c ["COPY", "tmp:0:8", ["const:916:8"]]
- 007c708c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c708c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c708c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c708c ["COPY", "tmp:0:8", ["const:9a1:8"]]
+ 007c708c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c708c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c708c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c708c bytes 29592491
+ 007c708c bytes 29852691
- 007c7180 ["COPY", "tmp:0:8", ["const:7a5:8"]]
- 007c7180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c7180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c7180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c7180 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 007c7180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c7180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c7180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c7180 bytes 29951e91
+ 007c7180 bytes 29c12091
- 007c71d8 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 007c71d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c71d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c71d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c71d8 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 007c71d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c71d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c71d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c71d8 bytes 08613491
+ 007c71d8 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1df65bbaef557fee716769ac6258e553"></a>

### [`007c7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7590.md) → [`007c7590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7590.md) FUN_007c7590

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
      "definition_site": "007c75b0",
      "incomplete_value": false,
      "site": "007c75b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c75b0",
      "incomplete_value": false,
      "site": "007c75b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "007c75b4",
      "DATA",
      [
        "storage",
        "00bfec98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c75b4",
      "DATA",
      [
        "storage",
        "00bfece8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c75b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7590.md#insn-007c75b0)
- 新版 [`007c75b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7590.md#insn-007c75b0)

~~~diff
- 007c75b0 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 007c75b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c75b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c75b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c75b0 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 007c75b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c75b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c75b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c75b0 bytes 08613291
+ 007c75b0 bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-477719568f9afa83ce4eedd526e7cacc"></a>

### [`007c76a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c76a0.md) → [`007c76a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c76a0.md) FUN_007c76a0

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
      "definition_site": "007c76b4",
      "incomplete_value": false,
      "site": "007c76b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c76b4",
      "incomplete_value": false,
      "site": "007c76b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:d18:8"
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
      "007c76b8",
      "DATA",
      [
        "storage",
        "00bfed18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c76b8",
      "DATA",
      [
        "storage",
        "00bfed68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c76b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c76a0.md#insn-007c76b4)
- 新版 [`007c76b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c76a0.md#insn-007c76b4)

~~~diff
- 007c76b4 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 007c76b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c76b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c76b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c76b4 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 007c76b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c76b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c76b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c76b4 bytes 08613491
+ 007c76b4 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee32ed09b4be874e49e244f1912686bb"></a>

### [`007c76c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c76c4.md) → [`007c76c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c76c4.md) FUN_007c76c4

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
      "definition_site": "007c76c8",
      "incomplete_value": false,
      "site": "007c76cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c76c8",
      "incomplete_value": false,
      "site": "007c76cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:d18:8"
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
      "007c76cc",
      "DATA",
      [
        "storage",
        "00bfed18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c76cc",
      "DATA",
      [
        "storage",
        "00bfed68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c76c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c76c4.md#insn-007c76c8)
- 新版 [`007c76c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c76c4.md#insn-007c76c8)

~~~diff
- 007c76c8 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 007c76c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c76c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c76c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c76c8 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 007c76c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c76c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c76c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c76c8 bytes 08613491
+ 007c76c8 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c99675d1427a975b7596a3c594c8bd54"></a>

### [`007c7750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7750.md) → [`007c7750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7750.md) FUN_007c7750

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c776c",
      "incomplete_value": false,
      "site": "007c7778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c776c",
      "incomplete_value": false,
      "site": "007c7778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "007c7778",
      "DATA",
      [
        "storage",
        "00bfeda8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c7778",
      "DATA",
      [
        "storage",
        "00bfedf8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c776c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7750.md#insn-007c776c)
- 新版 [`007c776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7750.md#insn-007c776c)

~~~diff
- 007c776c ["COPY", "tmp:0:8", ["const:da8:8"]]
- 007c776c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c776c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c776c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c776c ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 007c776c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c776c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c776c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c776c bytes 08a13691
+ 007c776c bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df97e075321ff57b0088b3727c8d882b"></a>

### [`007c7798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7798.md) → [`007c7798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7798.md) FUN_007c7798

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c779c",
      "incomplete_value": false,
      "site": "007c77a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c779c",
      "incomplete_value": false,
      "site": "007c77a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "007c77a0",
      "DATA",
      [
        "storage",
        "00bfeda8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c77a0",
      "DATA",
      [
        "storage",
        "00bfedf8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c779c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7798.md#insn-007c779c)
- 新版 [`007c779c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7798.md#insn-007c779c)

~~~diff
- 007c779c ["COPY", "tmp:0:8", ["const:da8:8"]]
- 007c779c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c779c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c779c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c779c ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 007c779c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c779c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c779c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c779c bytes 08a13691
+ 007c779c bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e382dd5a1142543caa8d92ef7daf4e8"></a>

### [`007c77c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c77c8.md) → [`007c77c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c77c8.md) FUN_007c77c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 26件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 26件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c7c68",
      "incomplete_value": false,
      "site": "007c7c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c7c68",
      "incomplete_value": false,
      "site": "007c7c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:e18:8"
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
      "007c7c68",
      "DATA",
      [
        "storage",
        "00bfee18",
        null,
        "undefined *"
      ]
    ],
    [
      "007c7cc0",
      "READ",
      [
        "storage",
        "00bfee38",
        null,
        "pointer"
      ]
    ],
    [
      "007c7cc0",
      "READ",
      [
        "storage",
        "00bfee40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c7c68",
      "DATA",
      [
        "storage",
        "00bfee68",
        null,
        "undefined *"
      ]
    ],
    [
      "007c7cc0",
      "READ",
      [
        "storage",
        "00bfee88",
        null,
        "pointer"
      ]
    ],
    [
      "007c7cc0",
      "READ",
      [
        "storage",
        "00bfee90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c7c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c77c8.md#insn-007c7c60) · [`007c7c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c77c8.md#insn-007c7c64)
- 新版 [`007c7c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c77c8.md#insn-007c7c60) · [`007c7c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c77c8.md#insn-007c7c64)

~~~diff
- 007c7c60 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 007c7c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c7c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c7c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c7c60 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 007c7c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c7c60 bytes 08613891
+ 007c7c60 bytes 08a13991
- 007c7c64 ["INT_SUB", "register:4098:8", ["register:40e8:8", "const:40:8"]]
- 007c7c64 bytes b30301d1
+ 007c7c64 ["INT_SUB", "register:4098:8", ["register:40e8:8", "const:40:8"]]
+ 007c7c64 bytes b30301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54de815667c7a6db928fa4302b96bdd0"></a>

### [`007c7dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7dac.md) → [`007c7dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7dac.md) FUN_007c7dac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007c77c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c77c8.md) [`007c8c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8c78.md) · 呼出先 11件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0063e588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e588.md) [`0071a054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a054.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 2件 [`007c77c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c77c8.md) [`007c8c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8c78.md) · 呼出先 11件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0063e588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e588.md) [`0071a054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a054.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.18% / 新版 83.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007c7f24",
      "incomplete_value": false,
      "site": "007c7f24",
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
      "definition_site": "007c7f24",
      "incomplete_value": false,
      "site": "007c7f24",
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
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007c7f28",
      "incomplete_value": false,
      "site": "007c7f28",
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
      "definition_site": "007c7f28",
      "incomplete_value": false,
      "site": "007c7f28",
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
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c7f24",
      "incomplete_value": false,
      "site": "007c7f28",
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
      "definition_site": "007c7f24",
      "incomplete_value": false,
      "site": "007c7f28",
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
      "007c7df8",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "007c7e10",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "007c7e14",
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
      "007c7df8",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "007c7e10",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "007c7e14",
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

- 旧版 [`007c7df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7dac.md#insn-007c7df4) · [`007c7e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7dac.md#insn-007c7e10) · [`007c7e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7dac.md#insn-007c7e14)
- 新版 [`007c7df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7dac.md#insn-007c7df4) · [`007c7e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7dac.md#insn-007c7e10) · [`007c7e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7dac.md#insn-007c7e14)

~~~diff
- 007c7df4 ["COPY", "tmp:0:8", ["const:38:8"]]
- 007c7df4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c7df4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c7df4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c7df4 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007c7df4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7df4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7df4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c7df4 bytes 08e10091
+ 007c7df4 bytes 08e10191
- 007c7e10 ["COPY", "tmp:0:8", ["const:0:8"]]
- 007c7e10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007c7e10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007c7e10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007c7e10 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 007c7e10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007c7e10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007c7e10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007c7e10 bytes 00000091
+ 007c7e10 bytes 00000191
- 007c7e14 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 007c7e14 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c7e14 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 007c7e14 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 007c7e14 bytes 423047f9
+ 007c7e14 bytes 425847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f3e3e341daa4c1d34e8e27a2691b2e8"></a>

### [`007c7f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7f88.md) → [`007c7f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7f88.md) FUN_007c7f88

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
      "definition_site": "007c7f9c",
      "incomplete_value": false,
      "site": "007c7fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c7f9c",
      "incomplete_value": false,
      "site": "007c7fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c7fa0",
      "DATA",
      [
        "storage",
        "00bfee18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c7fa0",
      "DATA",
      [
        "storage",
        "00bfee68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c7f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7f88.md#insn-007c7f9c)
- 新版 [`007c7f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7f88.md#insn-007c7f9c)

~~~diff
- 007c7f9c ["COPY", "tmp:0:8", ["const:e18:8"]]
- 007c7f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c7f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c7f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c7f9c ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 007c7f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c7f9c bytes 08613891
+ 007c7f9c bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

