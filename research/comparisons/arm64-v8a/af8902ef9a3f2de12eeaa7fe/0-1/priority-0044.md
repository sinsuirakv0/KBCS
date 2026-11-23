# v15.7.3 → v15.7.4 · 最優先の変更候補 (44)

[一覧の目次](README.md)

<a id="compare-996d822ff37715790df74f3b3305e866"></a>

### [`008779f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/008779f4.md) → [`008779f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/008779f4.md) FUN_008779f4

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
      "definition_site": "00877a18",
      "incomplete_value": false,
      "site": "00877a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877a18",
      "incomplete_value": false,
      "site": "00877a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00877a18",
      "DATA",
      [
        "storage",
        "00c05208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00877a18",
      "DATA",
      [
        "storage",
        "00c05258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/008779f4.md#insn-00877a14)
- 新版 [`00877a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/008779f4.md#insn-00877a14)

~~~diff
- 00877a14 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00877a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00877a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00877a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00877a14 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00877a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00877a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00877a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00877a14 bytes 08210891
+ 00877a14 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bb70785ad7fa893833b2dfdd91c3e0b"></a>

### [`00877a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md) → [`00877a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md) FUN_00877a44

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449b7c.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449b7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00877aa8",
      "incomplete_value": true,
      "site": "00877aa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a7d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877aa8",
      "incomplete_value": true,
      "site": "00877aa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b0a:8"
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
      "definition_site": "00877aac",
      "incomplete_value": true,
      "site": "00877aac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00877aac",
      "incomplete_value": true,
      "site": "00877aac",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00877b04",
      "incomplete_value": false,
      "site": "00877b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877b04",
      "incomplete_value": false,
      "site": "00877b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "00877a74",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00877a80",
      "READ",
      [
        "storage",
        "00c24d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00877a80",
      "READ",
      [
        "storage",
        "00c24d7c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00877a74",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00877a80",
      "READ",
      [
        "storage",
        "00c24db8",
        null,
        "undefined4"
      ]
    ],
    [
      "00877a80",
      "READ",
      [
        "storage",
        "00c24dbc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md#insn-00877a74) · [`00877a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md#insn-00877a90) · [`00877afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md#insn-00877afc)
- 新版 [`00877a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md#insn-00877a74) · [`00877a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md#insn-00877a90) · [`00877afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md#insn-00877afc)

~~~diff
- 00877a74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d28:8"]]
- 00877a74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00877a74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d78:8"]]
+ 00877a74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00877a74 bytes 299546f9
+ 00877a74 bytes 29bd46f9
- 00877a90 ["COPY", "tmp:0:8", ["const:b0a:8"]]
- 00877a90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00877a90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00877a90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00877a90 ["COPY", "tmp:0:8", ["const:a7d:8"]]
+ 00877a90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00877a90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00877a90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00877a90 bytes 29292c91
+ 00877a90 bytes 29f52991
- 00877afc ["COPY", "tmp:0:8", ["const:278:8"]]
- 00877afc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00877afc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00877afc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00877afc ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00877afc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00877afc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00877afc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00877afc bytes 29e10991
+ 00877afc bytes 29210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c6f48660bd68a7b7f55b820e6029abc"></a>

### [`008786ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008786ac.md) → [`008786ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/008786ac.md) FUN_008786ac

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
      "definition_site": "008786cc",
      "incomplete_value": false,
      "site": "008786d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008786cc",
      "incomplete_value": false,
      "site": "008786d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "008786d0",
      "DATA",
      [
        "storage",
        "00c05278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008786d0",
      "DATA",
      [
        "storage",
        "00c052c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008786cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008786ac.md#insn-008786cc)
- 新版 [`008786cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/008786ac.md#insn-008786cc)

~~~diff
- 008786cc ["COPY", "tmp:0:8", ["const:278:8"]]
- 008786cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008786cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008786cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008786cc ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 008786cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008786cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008786cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008786cc bytes 08e10991
+ 008786cc bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e8c75ee3c88ef3d8e9e2feec457ff07"></a>

### [`008786e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008786e4.md) → [`008786e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/008786e4.md) FUN_008786e4

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
      "definition_site": "008786e8",
      "incomplete_value": false,
      "site": "008786ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008786e8",
      "incomplete_value": false,
      "site": "008786ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "008786ec",
      "DATA",
      [
        "storage",
        "00c05278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008786ec",
      "DATA",
      [
        "storage",
        "00c052c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008786e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008786e4.md#insn-008786e8)
- 新版 [`008786e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/008786e4.md#insn-008786e8)

~~~diff
- 008786e8 ["COPY", "tmp:0:8", ["const:278:8"]]
- 008786e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008786e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008786e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008786e8 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 008786e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008786e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008786e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008786e8 bytes 08e10991
+ 008786e8 bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5f7448fe04c07c4debffd99a8c0bcd9"></a>

### [`0087898c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/0087898c.md) → [`0087898c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/0087898c.md) FUN_0087898c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008780d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008780d4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`008780d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/008780d4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00878998",
      "incomplete_value": false,
      "site": "0087899c",
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
      "definition_site": "00878998",
      "incomplete_value": false,
      "site": "0087899c",
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
      "00878998",
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
      "00878998",
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

- 旧版 [`00878998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/0087898c.md#insn-00878998)
- 新版 [`00878998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/0087898c.md#insn-00878998)

~~~diff
- 00878998 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00878998 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00878998 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00878998 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00878998 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00878998 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00878998 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00878998 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00878998 bytes 000c0c91
+ 00878998 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ae598f4ecb2c6c9dac1a2e89ffb0508"></a>

### [`008789a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008789a4.md) → [`008789a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/008789a4.md) FUN_008789a4

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
      "definition_site": "008789b8",
      "incomplete_value": false,
      "site": "008789bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008789b8",
      "incomplete_value": false,
      "site": "008789bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:308:8"
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
      "008789bc",
      "DATA",
      [
        "storage",
        "00c05308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008789bc",
      "DATA",
      [
        "storage",
        "00c05358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008789b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008789a4.md#insn-008789b8)
- 新版 [`008789b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/008789a4.md#insn-008789b8)

~~~diff
- 008789b8 ["COPY", "tmp:0:8", ["const:308:8"]]
- 008789b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008789b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008789b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008789b8 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 008789b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008789b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008789b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008789b8 bytes 08210c91
+ 008789b8 bytes 08610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a65f20ddc70e64bcc6ebc45dfe1062a1"></a>

### [`008789c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008789c8.md) → [`008789c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/008789c8.md) FUN_008789c8

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
      "definition_site": "008789cc",
      "incomplete_value": false,
      "site": "008789d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008789cc",
      "incomplete_value": false,
      "site": "008789d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "008789d0",
      "DATA",
      [
        "storage",
        "00c05308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008789d0",
      "DATA",
      [
        "storage",
        "00c05358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008789cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008789c8.md#insn-008789cc)
- 新版 [`008789cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/008789c8.md#insn-008789cc)

~~~diff
- 008789cc ["COPY", "tmp:0:8", ["const:308:8"]]
- 008789cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008789cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008789cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008789cc ["COPY", "tmp:0:8", ["const:358:8"]]
+ 008789cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008789cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008789cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008789cc bytes 08210c91
+ 008789cc bytes 08610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c32dc556124db6dd4cf8fc1aae4d8ba"></a>

### [`00878a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878a6c.md) → [`00878a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878a6c.md) FUN_00878a6c

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
      "definition_site": "00878a70",
      "incomplete_value": false,
      "site": "00878a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878a70",
      "incomplete_value": false,
      "site": "00878a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00878a74",
      "DATA",
      [
        "storage",
        "00c05388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00878a74",
      "DATA",
      [
        "storage",
        "00c053d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878a6c.md#insn-00878a70)
- 新版 [`00878a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878a6c.md#insn-00878a70)

~~~diff
- 00878a70 ["COPY", "tmp:0:8", ["const:388:8"]]
- 00878a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00878a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00878a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00878a70 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 00878a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00878a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00878a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00878a70 bytes 08210e91
+ 00878a70 bytes 08610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26bc569f54c399c7f82f2ebd840c3977"></a>

### [`00878ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878ac4.md) → [`00878ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878ac4.md) FUN_00878ac4

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
      "definition_site": "00878ae8",
      "incomplete_value": false,
      "site": "00878ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878ae8",
      "incomplete_value": false,
      "site": "00878ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00878ae8",
      "DATA",
      [
        "storage",
        "00c05408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00878ae8",
      "DATA",
      [
        "storage",
        "00c05458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878ac4.md#insn-00878ae4)
- 新版 [`00878ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878ac4.md#insn-00878ae4)

~~~diff
- 00878ae4 ["COPY", "tmp:0:8", ["const:408:8"]]
- 00878ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00878ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00878ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00878ae4 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 00878ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00878ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00878ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00878ae4 bytes 08211091
+ 00878ae4 bytes 08611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c22c514c47da1a1b74f41c45957b089"></a>

### [`00878b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md) → [`00878b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md) FUN_00878b14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449b7c.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449b7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.41% / 新版 95.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00878b78",
      "incomplete_value": true,
      "site": "00878b78",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a7d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878b78",
      "incomplete_value": true,
      "site": "00878b78",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:b0a:8"
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
      "definition_site": "00878b7c",
      "incomplete_value": true,
      "site": "00878b7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00878b7c",
      "incomplete_value": true,
      "site": "00878b7c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878bd4",
      "incomplete_value": false,
      "site": "00878bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878bd4",
      "incomplete_value": false,
      "site": "00878bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "00878b44",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00878b50",
      "READ",
      [
        "storage",
        "00c24d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00878b50",
      "READ",
      [
        "storage",
        "00c24d7c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00878b44",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00878b50",
      "READ",
      [
        "storage",
        "00c24db8",
        null,
        "undefined4"
      ]
    ],
    [
      "00878b50",
      "READ",
      [
        "storage",
        "00c24dbc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md#insn-00878b44) · [`00878b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md#insn-00878b60) · [`00878bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md#insn-00878bcc)
- 新版 [`00878b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md#insn-00878b44) · [`00878b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md#insn-00878b60) · [`00878bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md#insn-00878bcc)

~~~diff
- 00878b44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d28:8"]]
- 00878b44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00878b44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d78:8"]]
+ 00878b44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00878b44 bytes 299546f9
+ 00878b44 bytes 29bd46f9
- 00878b60 ["COPY", "tmp:0:8", ["const:b0a:8"]]
- 00878b60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00878b60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00878b60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00878b60 ["COPY", "tmp:0:8", ["const:a7d:8"]]
+ 00878b60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00878b60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00878b60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00878b60 bytes 29292c91
+ 00878b60 bytes 29f52991
- 00878bcc ["COPY", "tmp:0:8", ["const:478:8"]]
- 00878bcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00878bcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00878bcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00878bcc ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 00878bcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00878bcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00878bcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00878bcc bytes 29e11191
+ 00878bcc bytes 29211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41b1eb9c2014384b13a83f33801248c7"></a>

### [`00879758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879758.md) → [`00879758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879758.md) FUN_00879758

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
      "definition_site": "0087975c",
      "incomplete_value": false,
      "site": "00879760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087975c",
      "incomplete_value": false,
      "site": "00879760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "00879760",
      "DATA",
      [
        "storage",
        "00c05478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879760",
      "DATA",
      [
        "storage",
        "00c054c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087975c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879758.md#insn-0087975c)
- 新版 [`0087975c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879758.md#insn-0087975c)

~~~diff
- 0087975c ["COPY", "tmp:0:8", ["const:478:8"]]
- 0087975c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087975c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087975c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087975c ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0087975c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087975c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087975c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087975c bytes 08e11191
+ 0087975c bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-823f376037c70320d4b181e5d70d4f22"></a>

### [`00879a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879a00.md) → [`00879a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a00.md) FUN_00879a00

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0087919c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/0087919c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0087919c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/0087919c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00879a0c",
      "incomplete_value": false,
      "site": "00879a10",
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
      "definition_site": "00879a0c",
      "incomplete_value": false,
      "site": "00879a10",
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
      "00879a0c",
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
      "00879a0c",
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

- 旧版 [`00879a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879a00.md#insn-00879a0c)
- 新版 [`00879a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a00.md#insn-00879a0c)

~~~diff
- 00879a0c ["COPY", "tmp:0:8", ["const:303:8"]]
- 00879a0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00879a0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00879a0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00879a0c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00879a0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00879a0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00879a0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00879a0c bytes 000c0c91
+ 00879a0c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f65a5978e3647d30f3bcb20196d2cd9"></a>

### [`00879a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879a18.md) → [`00879a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a18.md) FUN_00879a18

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
      "definition_site": "00879a2c",
      "incomplete_value": false,
      "site": "00879a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879a2c",
      "incomplete_value": false,
      "site": "00879a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "00879a30",
      "DATA",
      [
        "storage",
        "00c05508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879a30",
      "DATA",
      [
        "storage",
        "00c05558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879a18.md#insn-00879a2c)
- 新版 [`00879a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a18.md#insn-00879a2c)

~~~diff
- 00879a2c ["COPY", "tmp:0:8", ["const:508:8"]]
- 00879a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879a2c ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00879a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879a2c bytes 08211491
+ 00879a2c bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c46c8bf71162be0a8dfd778fca39745f"></a>

### [`00879a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879a3c.md) → [`00879a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a3c.md) FUN_00879a3c

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
      "definition_site": "00879a40",
      "incomplete_value": false,
      "site": "00879a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879a40",
      "incomplete_value": false,
      "site": "00879a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00879a44",
      "DATA",
      [
        "storage",
        "00c05508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879a44",
      "DATA",
      [
        "storage",
        "00c05558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879a3c.md#insn-00879a40)
- 新版 [`00879a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a3c.md#insn-00879a40)

~~~diff
- 00879a40 ["COPY", "tmp:0:8", ["const:508:8"]]
- 00879a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879a40 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00879a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879a40 bytes 08211491
+ 00879a40 bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34954246c3f4d7262fb8fa29c2ceffa1"></a>

### [`00879ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879ac8.md) → [`00879ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879ac8.md) FUN_00879ac8

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
      "definition_site": "00879adc",
      "incomplete_value": true,
      "site": "00879ae0",
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
      "definition_site": "00879adc",
      "incomplete_value": true,
      "site": "00879ae0",
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
      "00879ae0",
      "DATA",
      [
        "storage",
        "00c05588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879ae0",
      "DATA",
      [
        "storage",
        "00c055d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879ac8.md#insn-00879adc)
- 新版 [`00879adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879ac8.md#insn-00879adc)

~~~diff
- 00879adc ["COPY", "tmp:0:8", ["const:588:8"]]
- 00879adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879adc ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00879adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879adc bytes 08211691
+ 00879adc bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ba7d40ffc692703efac47d494737870"></a>

### [`00879aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879aec.md) → [`00879aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879aec.md) FUN_00879aec

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
      "definition_site": "00879af0",
      "incomplete_value": true,
      "site": "00879af4",
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
      "definition_site": "00879af0",
      "incomplete_value": true,
      "site": "00879af4",
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
      "00879af4",
      "DATA",
      [
        "storage",
        "00c05588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879af4",
      "DATA",
      [
        "storage",
        "00c055d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879aec.md#insn-00879af0)
- 新版 [`00879af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879aec.md#insn-00879af0)

~~~diff
- 00879af0 ["COPY", "tmp:0:8", ["const:588:8"]]
- 00879af0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879af0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879af0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879af0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00879af0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879af0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879af0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879af0 bytes 08211691
+ 00879af0 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01c82d0f8668a5788754a8b0baf03096"></a>

### [`00879b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879b58.md) → [`00879b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b58.md) FUN_00879b58

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
      "definition_site": "00879b5c",
      "incomplete_value": false,
      "site": "00879b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879b5c",
      "incomplete_value": false,
      "site": "00879b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "00879b60",
      "DATA",
      [
        "storage",
        "00c05608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879b60",
      "DATA",
      [
        "storage",
        "00c05658",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879b58.md#insn-00879b5c)
- 新版 [`00879b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b58.md#insn-00879b5c)

~~~diff
- 00879b5c ["COPY", "tmp:0:8", ["const:608:8"]]
- 00879b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879b5c ["COPY", "tmp:0:8", ["const:658:8"]]
+ 00879b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879b5c bytes 08211891
+ 00879b5c bytes 08611991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71eb325fc135fd3e2fbb8fe494e000a0"></a>

### [`00879b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879b70.md) → [`00879b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b70.md) FUN_00879b70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`008309c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008309c8.md) [`00879df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879df0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`008309c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00830/008309c8.md) [`00879df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879df0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00879c5c",
      "incomplete_value": false,
      "site": "00879c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879c5c",
      "incomplete_value": false,
      "site": "00879c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00879c38",
      "READ",
      [
        "storage",
        "002a885a",
        null,
        "string"
      ]
    ],
    [
      "00879c38",
      "READ",
      [
        "storage",
        "002a7a6b",
        null,
        "string"
      ]
    ],
    [
      "00879c3c",
      "READ",
      [
        "storage",
        "002a8867",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00879c38",
      "READ",
      [
        "storage",
        "002a88f4",
        null,
        "string"
      ]
    ],
    [
      "00879c38",
      "READ",
      [
        "storage",
        "002a7b05",
        null,
        "string"
      ]
    ],
    [
      "00879c3c",
      "READ",
      [
        "storage",
        "002a8901",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879b70.md#insn-00879c18) · [`00879c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879b70.md#insn-00879c24) · [`00879c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879b70.md#insn-00879c5c)
- 新版 [`00879c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b70.md#insn-00879c18) · [`00879c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b70.md#insn-00879c24) · [`00879c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b70.md#insn-00879c5c)

~~~diff
- 00879c18 ["COPY", "tmp:0:8", ["const:85a:8"]]
- 00879c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879c18 ["COPY", "tmp:0:8", ["const:8f4:8"]]
+ 00879c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879c18 bytes 08692191
+ 00879c18 bytes 08d12391
- 00879c24 ["COPY", "tmp:0:8", ["const:a6b:8"]]
- 00879c24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00879c24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00879c24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00879c24 ["COPY", "tmp:0:8", ["const:b05:8"]]
+ 00879c24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00879c24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00879c24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00879c24 bytes 29ad2991
+ 00879c24 bytes 29152c91
- 00879c5c ["COPY", "tmp:0:8", ["const:678:8"]]
- 00879c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879c5c ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00879c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879c5c bytes 08e11991
+ 00879c5c bytes 08211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f59baead15eb829d7682d616f0335dc"></a>

### [`00879dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879dbc.md) → [`00879dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879dbc.md) FUN_00879dbc

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
      "definition_site": "00879dd0",
      "incomplete_value": false,
      "site": "00879dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879dd0",
      "incomplete_value": false,
      "site": "00879dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00879dd4",
      "DATA",
      [
        "storage",
        "00c05678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879dd4",
      "DATA",
      [
        "storage",
        "00c056c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879dbc.md#insn-00879dd0)
- 新版 [`00879dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879dbc.md#insn-00879dd0)

~~~diff
- 00879dd0 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00879dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879dd0 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00879dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879dd0 bytes 08e11991
+ 00879dd0 bytes 08211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-923ef972f287336c86cc3d7b8a8a8f52"></a>

### [`00879de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879de0.md) → [`00879de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879de0.md) FUN_00879de0

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
      "definition_site": "00879de4",
      "incomplete_value": false,
      "site": "00879de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879de4",
      "incomplete_value": false,
      "site": "00879de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00879de8",
      "DATA",
      [
        "storage",
        "00c05678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879de8",
      "DATA",
      [
        "storage",
        "00c056c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879de0.md#insn-00879de4)
- 新版 [`00879de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879de0.md#insn-00879de4)

~~~diff
- 00879de4 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00879de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879de4 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00879de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879de4 bytes 08e11991
+ 00879de4 bytes 08211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-250ac56a139809581dfce55df4bf26f6"></a>

### [`00879e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879e6c.md) → [`00879e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879e6c.md) FUN_00879e6c

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
      "definition_site": "00879e80",
      "incomplete_value": false,
      "site": "00879e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879e80",
      "incomplete_value": false,
      "site": "00879e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:708:8"
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
      "00879e84",
      "DATA",
      [
        "storage",
        "00c05708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879e84",
      "DATA",
      [
        "storage",
        "00c05758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879e6c.md#insn-00879e80)
- 新版 [`00879e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879e6c.md#insn-00879e80)

~~~diff
- 00879e80 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00879e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879e80 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00879e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879e80 bytes 08211c91
+ 00879e80 bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32a53125f3b4a743ac4075d28b4e24a7"></a>

### [`00879fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879fa8.md) → [`00879fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879fa8.md) FUN_00879fa8

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
      "definition_site": "00879fbc",
      "incomplete_value": false,
      "site": "00879fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879fbc",
      "incomplete_value": false,
      "site": "00879fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "00879fc0",
      "DATA",
      [
        "storage",
        "00c05778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879fc0",
      "DATA",
      [
        "storage",
        "00c057c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879fa8.md#insn-00879fbc)
- 新版 [`00879fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879fa8.md#insn-00879fbc)

~~~diff
- 00879fbc ["COPY", "tmp:0:8", ["const:778:8"]]
- 00879fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879fbc ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00879fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879fbc bytes 08e11d91
+ 00879fbc bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dba9860533ec47d00a300aa9028395af"></a>

### [`00879fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879fcc.md) → [`00879fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879fcc.md) FUN_00879fcc

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
      "definition_site": "00879fd0",
      "incomplete_value": false,
      "site": "00879fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879fd0",
      "incomplete_value": false,
      "site": "00879fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "00879fd4",
      "DATA",
      [
        "storage",
        "00c05778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879fd4",
      "DATA",
      [
        "storage",
        "00c057c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879fcc.md#insn-00879fd0)
- 新版 [`00879fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879fcc.md#insn-00879fd0)

~~~diff
- 00879fd0 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00879fd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879fd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879fd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879fd0 ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00879fd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879fd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879fd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879fd0 bytes 08e11d91
+ 00879fd0 bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c6a0bec2d171c98b3e157829793b839"></a>

### [`00879fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879fe4.md) → [`00879fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879fe4.md) FUN_00879fe4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0087a124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a124.md) [`0087a128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a128.md) [`00ada774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada774.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0087a124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a124.md) [`0087a128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a128.md) [`00ada7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0087a010",
      "incomplete_value": false,
      "site": "0087a018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a010",
      "incomplete_value": false,
      "site": "0087a018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "0087a018",
      "DATA",
      [
        "storage",
        "00c057e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0087a04c",
      "READ",
      [
        "storage",
        "00c05808",
        null,
        "pointer"
      ]
    ],
    [
      "0087a04c",
      "READ",
      [
        "storage",
        "00c05810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a018",
      "DATA",
      [
        "storage",
        "00c05838",
        null,
        "undefined *"
      ]
    ],
    [
      "0087a04c",
      "READ",
      [
        "storage",
        "00c05858",
        null,
        "pointer"
      ]
    ],
    [
      "0087a04c",
      "READ",
      [
        "storage",
        "00c05860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879fe4.md#insn-0087a010)
- 新版 [`0087a010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879fe4.md#insn-0087a010)

~~~diff
- 0087a010 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 0087a010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a010 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 0087a010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a010 bytes 08a11f91
+ 0087a010 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-107a7228df80d5fea9719fff11a75cd6"></a>

### [`0087a0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a0f0.md) → [`0087a0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a0f0.md) FUN_0087a0f0

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
      "definition_site": "0087a104",
      "incomplete_value": true,
      "site": "0087a108",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a104",
      "incomplete_value": true,
      "site": "0087a108",
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
            "const:7e8:8"
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
      "0087a108",
      "DATA",
      [
        "storage",
        "00c057e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a108",
      "DATA",
      [
        "storage",
        "00c05838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a0f0.md#insn-0087a104)
- 新版 [`0087a104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a0f0.md#insn-0087a104)

~~~diff
- 0087a104 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 0087a104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a104 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 0087a104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a104 bytes 08a11f91
+ 0087a104 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c2e394faec8e6ca9b827ec7ae71459a"></a>

### [`0087a114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a114.md) → [`0087a114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a114.md) FUN_0087a114

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
      "definition_site": "0087a118",
      "incomplete_value": false,
      "site": "0087a11c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a118",
      "incomplete_value": false,
      "site": "0087a11c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "0087a11c",
      "DATA",
      [
        "storage",
        "00c057e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a11c",
      "DATA",
      [
        "storage",
        "00c05838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a114.md#insn-0087a118)
- 新版 [`0087a118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a114.md#insn-0087a118)

~~~diff
- 0087a118 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 0087a118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a118 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 0087a118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a118 bytes 08a11f91
+ 0087a118 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90394d329e677490a4eecb85849735ae"></a>

### [`0087a12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a12c.md) → [`0087a12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a12c.md) FUN_0087a12c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087a274",
      "incomplete_value": false,
      "site": "0087a274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a274",
      "incomplete_value": false,
      "site": "0087a274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "0087a19c",
      "READ",
      [
        "storage",
        "00293c23",
        null,
        "string"
      ]
    ],
    [
      "0087a274",
      "DATA",
      [
        "storage",
        "00c05858",
        null,
        "undefined *"
      ]
    ],
    [
      "0087a2cc",
      "READ",
      [
        "storage",
        "00c05878",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0087a19c",
      "READ",
      [
        "storage",
        "00293b96",
        null,
        "string"
      ]
    ],
    [
      "0087a274",
      "DATA",
      [
        "storage",
        "00c058a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0087a2cc",
      "READ",
      [
        "storage",
        "00c058c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a12c.md#insn-0087a194) · [`0087a26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a12c.md#insn-0087a26c) · [`0087a270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a12c.md#insn-0087a270)
- 新版 [`0087a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a12c.md#insn-0087a194) · [`0087a26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a12c.md#insn-0087a26c)

~~~diff
- 0087a194 ["COPY", "tmp:0:8", ["const:c23:8"]]
- 0087a194 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087a194 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087a194 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087a194 ["COPY", "tmp:0:8", ["const:b96:8"]]
+ 0087a194 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087a194 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087a194 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087a194 bytes 298d3091
+ 0087a194 bytes 29592e91
- 0087a26c ["COPY", "tmp:0:8", ["const:858:8"]]
- 0087a26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a26c ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0087a26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a26c bytes 08612191
+ 0087a26c bytes 08a12291
- 0087a270 ["INT_SUB", "register:4098:8", ["register:40e8:8", "const:40:8"]]
- 0087a270 bytes b30301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c53348ad1891c3cbb6944686363dcc58"></a>

### [`0087a4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a4d4.md) → [`0087a4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a4d4.md) FUN_0087a4d4

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
      "definition_site": "0087a4e8",
      "incomplete_value": true,
      "site": "0087a4ec",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a4e8",
      "incomplete_value": true,
      "site": "0087a4ec",
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
            "const:858:8"
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
      "0087a4ec",
      "DATA",
      [
        "storage",
        "00c05858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a4ec",
      "DATA",
      [
        "storage",
        "00c058a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a4d4.md#insn-0087a4e8)
- 新版 [`0087a4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a4d4.md#insn-0087a4e8)

~~~diff
- 0087a4e8 ["COPY", "tmp:0:8", ["const:858:8"]]
- 0087a4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a4e8 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0087a4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a4e8 bytes 08612191
+ 0087a4e8 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ae575c0951df78b055ed607e08c9537"></a>

### [`0087a4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a4f8.md) → [`0087a4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a4f8.md) FUN_0087a4f8

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
      "definition_site": "0087a4fc",
      "incomplete_value": false,
      "site": "0087a500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a4fc",
      "incomplete_value": false,
      "site": "0087a500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "0087a500",
      "DATA",
      [
        "storage",
        "00c05858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a500",
      "DATA",
      [
        "storage",
        "00c058a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a4fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a4f8.md#insn-0087a4fc)
- 新版 [`0087a4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a4f8.md#insn-0087a4fc)

~~~diff
- 0087a4fc ["COPY", "tmp:0:8", ["const:858:8"]]
- 0087a4fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a4fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a4fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a4fc ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0087a4fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a4fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a4fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a4fc bytes 08612191
+ 0087a4fc bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13c786f7ab7358389d7e93eff04609d6"></a>

### [`0087a584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a584.md) → [`0087a584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a584.md) FUN_0087a584

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
      "definition_site": "0087a598",
      "incomplete_value": false,
      "site": "0087a59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a598",
      "incomplete_value": false,
      "site": "0087a59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "0087a59c",
      "DATA",
      [
        "storage",
        "00c05908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a59c",
      "DATA",
      [
        "storage",
        "00c05958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a584.md#insn-0087a598)
- 新版 [`0087a598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a584.md#insn-0087a598)

~~~diff
- 0087a598 ["COPY", "tmp:0:8", ["const:908:8"]]
- 0087a598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a598 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 0087a598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a598 bytes 08212491
+ 0087a598 bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9319a3b2e20c8a90c5595cc664e4ef3a"></a>

### [`0087a5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a5c0.md) → [`0087a5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a5c0.md) FUN_0087a5c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md)
- 新版 呼出元 0件  · 呼出先 20件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.91% / 新版 93.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087a658",
      "incomplete_value": true,
      "site": "0087a668",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:152:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a658",
      "incomplete_value": true,
      "site": "0087a668",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1df:8"
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
      "definition_site": "0087a658",
      "incomplete_value": true,
      "site": "0087a668",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0087a658",
      "incomplete_value": true,
      "site": "0087a668",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087a6e4",
      "incomplete_value": true,
      "site": "0087a6f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:369:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a6e4",
      "incomplete_value": true,
      "site": "0087a6f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:36b:8"
              ]
            ]
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
      "0087a658",
      "READ",
      [
        "storage",
        "002971df",
        null,
        "string"
      ]
    ],
    [
      "0087a658",
      "READ",
      [
        "storage",
        "002971ef",
        null,
        "string"
      ]
    ],
    [
      "0087a6e4",
      "READ",
      [
        "storage",
        "0029a36b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087a658",
      "READ",
      [
        "storage",
        "00297152",
        null,
        "string"
      ]
    ],
    [
      "0087a658",
      "READ",
      [
        "storage",
        "00297162",
        null,
        "string"
      ]
    ],
    [
      "0087a6e4",
      "READ",
      [
        "storage",
        "0029a369",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a5c0.md#insn-0087a650) · [`0087a654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a5c0.md#insn-0087a654)
- 新版 [`0087a650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a5c0.md#insn-0087a650) · [`0087a654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a5c0.md#insn-0087a654)

~~~diff
- 0087a650 ["COPY", "tmp:0:8", ["const:1df:8"]]
- 0087a650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a650 ["COPY", "tmp:0:8", ["const:152:8"]]
+ 0087a650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a650 bytes 087d0791
+ 0087a650 bytes 08490591
- 0087a654 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0087a654 bytes a9d1fff0
+ 0087a654 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0087a654 bytes a9d1fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48d0bc59309e9e066963bdac6639e009"></a>

### [`0087aa04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aa04.md) → [`0087aa04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aa04.md) FUN_0087aa04

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
      "definition_site": "0087aa18",
      "incomplete_value": false,
      "site": "0087aa1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087aa18",
      "incomplete_value": false,
      "site": "0087aa1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "0087aa1c",
      "DATA",
      [
        "storage",
        "00c05978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087aa1c",
      "DATA",
      [
        "storage",
        "00c059c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aa04.md#insn-0087aa18)
- 新版 [`0087aa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aa04.md#insn-0087aa18)

~~~diff
- 0087aa18 ["COPY", "tmp:0:8", ["const:978:8"]]
- 0087aa18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087aa18 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 0087aa18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087aa18 bytes 08e12591
+ 0087aa18 bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23a5e5d8b08db897b01fde1b1360f693"></a>

### [`0087aa28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aa28.md) → [`0087aa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aa28.md) FUN_0087aa28

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
      "definition_site": "0087aa2c",
      "incomplete_value": false,
      "site": "0087aa30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087aa2c",
      "incomplete_value": false,
      "site": "0087aa30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "0087aa30",
      "DATA",
      [
        "storage",
        "00c05978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087aa30",
      "DATA",
      [
        "storage",
        "00c059c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aa28.md#insn-0087aa2c)
- 新版 [`0087aa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aa28.md#insn-0087aa2c)

~~~diff
- 0087aa2c ["COPY", "tmp:0:8", ["const:978:8"]]
- 0087aa2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087aa2c ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 0087aa2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087aa2c bytes 08e12591
+ 0087aa2c bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-323d8483a0d24a0c358cedad7a834706"></a>

### [`0087aa84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aa84.md) → [`0087aa84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aa84.md) FUN_0087aa84

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
      "definition_site": "0087aa98",
      "incomplete_value": false,
      "site": "0087aa9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087aa98",
      "incomplete_value": false,
      "site": "0087aa9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "0087aa9c",
      "DATA",
      [
        "storage",
        "00c059f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087aa9c",
      "DATA",
      [
        "storage",
        "00c05a48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aa98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aa84.md#insn-0087aa98)
- 新版 [`0087aa98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aa84.md#insn-0087aa98)

~~~diff
- 0087aa98 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 0087aa98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087aa98 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 0087aa98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087aa98 bytes 08e12791
+ 0087aa98 bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ae02f337a915a70ae47f4316c414ad9"></a>

### [`0087aaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aaa8.md) → [`0087aaa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aaa8.md) FUN_0087aaa8

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
      "definition_site": "0087aaac",
      "incomplete_value": false,
      "site": "0087aab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087aaac",
      "incomplete_value": false,
      "site": "0087aab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "0087aab0",
      "DATA",
      [
        "storage",
        "00c059f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087aab0",
      "DATA",
      [
        "storage",
        "00c05a48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aaac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aaa8.md#insn-0087aaac)
- 新版 [`0087aaac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aaa8.md#insn-0087aaac)

~~~diff
- 0087aaac ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 0087aaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087aaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087aaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087aaac ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 0087aaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087aaac bytes 08e12791
+ 0087aaac bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-049dda51bca3a9c7cb4bba208eb4eb29"></a>

### [`0087ab04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab04.md) → [`0087ab04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ab04.md) FUN_0087ab04

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
      "definition_site": "0087ab28",
      "incomplete_value": false,
      "site": "0087ab28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ab28",
      "incomplete_value": false,
      "site": "0087ab28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "0087ab28",
      "DATA",
      [
        "storage",
        "00c05a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087ab28",
      "DATA",
      [
        "storage",
        "00c05ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ab24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab04.md#insn-0087ab24)
- 新版 [`0087ab24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ab04.md#insn-0087ab24)

~~~diff
- 0087ab24 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 0087ab24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087ab24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087ab24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087ab24 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 0087ab24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087ab24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087ab24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087ab24 bytes 08212a91
+ 0087ab24 bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93dcd851f91aab6e80a8bc52c665ccb7"></a>

### [`0087ab38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab38.md) → [`0087ab38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ab38.md) FUN_0087ab38

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
      "definition_site": "0087ab44",
      "incomplete_value": true,
      "site": "0087ab44",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ab44",
      "incomplete_value": true,
      "site": "0087ab44",
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
            "const:a88:8"
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
      "0087ab44",
      "DATA",
      [
        "storage",
        "00c05a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087ab44",
      "DATA",
      [
        "storage",
        "00c05ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ab40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab38.md#insn-0087ab40)
- 新版 [`0087ab40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ab38.md#insn-0087ab40)

~~~diff
- 0087ab40 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 0087ab40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087ab40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087ab40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087ab40 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 0087ab40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087ab40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087ab40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087ab40 bytes 29212a91
+ 0087ab40 bytes 29612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f2e1169c5d9c82e456e0f3d588fa7c7"></a>

### [`0087ab54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab54.md) → [`0087ab54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ab54.md) FUN_0087ab54

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00708fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/00708fe4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a4ec40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4ec40.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00708fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00708/00708fe4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a4ec84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4ec84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0087ab8c",
      "incomplete_value": true,
      "site": "0087ab8c",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ab8c",
      "incomplete_value": true,
      "site": "0087ab8c",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087ab7c",
      "READ",
      [
        "storage",
        "0109e6b0",
        null,
        "undefined1"
      ]
    ],
    [
      "0087ab8c",
      "WRITE",
      [
        "storage",
        "0109e6b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0087ab7c",
      "READ",
      [
        "storage",
        "0109e6f0",
        null,
        "undefined1"
      ]
    ],
    [
      "0087ab8c",
      "WRITE",
      [
        "storage",
        "0109e6f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ab8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab54.md#insn-0087ab8c) · [`0087ab7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab54.md#insn-0087ab7c)
- 新版 [`0087ab8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ab54.md#insn-0087ab8c) · [`0087ab7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ab54.md#insn-0087ab7c)

~~~diff
- 0087ab8c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0087ab8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0087ab8c ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:6b0:8"]]
- 0087ab8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0087ab8c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0087ab8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0087ab8c ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:6f0:8"]]
+ 0087ab8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0087ab8c bytes 1fc11a39
+ 0087ab8c bytes 1fc11b39
- 0087ab7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6b0:8"]]
- 0087ab7c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0087ab7c ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
+ 0087ab7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6f0:8"]]
+ 0087ab7c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0087ab7c ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 0087ab7c bytes 09c15a39
+ 0087ab7c bytes 09c15b39
~~~


<a id="compare-ce349a528ce90614862482ac3cdb6906"></a>

### [`0087acb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087acb4.md) → [`0087acb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087acb4.md) FUN_0087acb4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00870980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00870/00870980.md) [`0087acb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087acb4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00870980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870980.md) [`0087acb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087acb4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087ae10",
      "incomplete_value": false,
      "site": "0087ae18",
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
      "definition_site": "0087ae10",
      "incomplete_value": false,
      "site": "0087ae18",
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
      "definition_site": "0087ae34",
      "incomplete_value": false,
      "site": "0087ae40",
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
      "definition_site": "0087ae34",
      "incomplete_value": false,
      "site": "0087ae40",
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
      "definition_site": "0087af68",
      "incomplete_value": false,
      "site": "0087af70",
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
      "definition_site": "0087af68",
      "incomplete_value": false,
      "site": "0087af70",
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
      "0087ae10",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087ae34",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0087af68",
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
      "0087ae10",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0087ae34",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0087af68",
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

- 旧版 [`0087ae10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087acb4.md#insn-0087ae10) · [`0087ae34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087acb4.md#insn-0087ae34) · [`0087af68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087acb4.md#insn-0087af68)
- 新版 [`0087ae10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087acb4.md#insn-0087ae10) · [`0087ae34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087acb4.md#insn-0087ae34) · [`0087af68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087acb4.md#insn-0087af68)

~~~diff
- 0087ae10 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0087ae10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087ae10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087ae10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087ae10 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0087ae10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ae10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ae10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087ae10 bytes 21280c91
+ 0087ae10 bytes 21900e91
- 0087ae34 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0087ae34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087ae34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087ae34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087ae34 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0087ae34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ae34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ae34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087ae34 bytes 21642491
+ 0087ae34 bytes 21142291
- 0087af68 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0087af68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087af68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087af68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087af68 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0087af68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087af68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087af68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087af68 bytes 21b80b91
+ 0087af68 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba8ac8950a2c0a99709b809c8ec92d2"></a>

### [`0087b620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087b620.md) → [`0087b620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087b620.md) FUN_0087b620

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) [`0087b620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087b620.md) [`0097a22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a22c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) [`0087b620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087b620.md) [`0097a22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a22c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087b7a4",
      "incomplete_value": false,
      "site": "0087b7ac",
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
      "definition_site": "0087b7a4",
      "incomplete_value": false,
      "site": "0087b7ac",
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
      "definition_site": "0087b914",
      "incomplete_value": false,
      "site": "0087b920",
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
      "definition_site": "0087b914",
      "incomplete_value": false,
      "site": "0087b920",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087bc00",
      "incomplete_value": false,
      "site": "0087bc10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5e5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087bc00",
      "incomplete_value": false,
      "site": "0087bc10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:672:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087b7a4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087b7c8",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0087b8fc",
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
      "0087b7a4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0087b7c8",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0087b8fc",
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

- 旧版 [`0087b7a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087b620.md#insn-0087b7a4) · [`0087b7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087b620.md#insn-0087b7c8) · [`0087b8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087b620.md#insn-0087b8fc)
- 新版 [`0087b7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087b620.md#insn-0087b7a4) · [`0087b7c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087b620.md#insn-0087b7c8) · [`0087b8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087b620.md#insn-0087b8fc)

~~~diff
- 0087b7a4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0087b7a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087b7a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087b7a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087b7a4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0087b7a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b7a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b7a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087b7a4 bytes 21280c91
+ 0087b7a4 bytes 21900e91
- 0087b7c8 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0087b7c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087b7c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087b7c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087b7c8 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0087b7c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b7c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b7c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087b7c8 bytes 21642491
+ 0087b7c8 bytes 21142291
- 0087b8fc ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0087b8fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087b8fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087b8fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087b8fc ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0087b8fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b8fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b8fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087b8fc bytes 21b80b91
+ 0087b8fc bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-601263f39817d2b80c2425f59a77856d"></a>

### [`0087bed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087bed0.md) → [`0087bed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087bed0.md) FUN_0087bed0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087b620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087b620.md) [`0087bed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087bed0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087b620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087b620.md) [`0087bed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087bed0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087c048",
      "incomplete_value": false,
      "site": "0087c050",
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
      "definition_site": "0087c048",
      "incomplete_value": false,
      "site": "0087c050",
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
      "definition_site": "0087c06c",
      "incomplete_value": false,
      "site": "0087c078",
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
      "definition_site": "0087c06c",
      "incomplete_value": false,
      "site": "0087c078",
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
      "definition_site": "0087c1a0",
      "incomplete_value": false,
      "site": "0087c1a8",
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
      "definition_site": "0087c1a0",
      "incomplete_value": false,
      "site": "0087c1a8",
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
      "0087c048",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087c06c",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0087c1a0",
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
      "0087c048",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0087c06c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0087c1a0",
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

- 旧版 [`0087c048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087bed0.md#insn-0087c048) · [`0087c06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087bed0.md#insn-0087c06c) · [`0087c1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087bed0.md#insn-0087c1a0)
- 新版 [`0087c048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087bed0.md#insn-0087c048) · [`0087c06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087bed0.md#insn-0087c06c) · [`0087c1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087bed0.md#insn-0087c1a0)

~~~diff
- 0087c048 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0087c048 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087c048 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087c048 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087c048 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0087c048 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c048 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c048 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087c048 bytes 21280c91
+ 0087c048 bytes 21900e91
- 0087c06c ["COPY", "tmp:0:8", ["const:919:8"]]
- 0087c06c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087c06c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087c06c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087c06c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0087c06c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c06c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c06c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087c06c bytes 21642491
+ 0087c06c bytes 21142291
- 0087c1a0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0087c1a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087c1a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087c1a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087c1a0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0087c1a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c1a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c1a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087c1a0 bytes 21b80b91
+ 0087c1a0 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-749d9ec041a9e69c60ac1dce440c2452"></a>

### [`0087c758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087c758.md) → [`0087c758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087c758.md) FUN_0087c758

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087bed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087bed0.md) [`0087c758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087c758.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087bed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087b/0087bed0.md) [`0087c758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087c758.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.56% / 新版 98.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087c8cc",
      "incomplete_value": false,
      "site": "0087c8d4",
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
      "definition_site": "0087c8cc",
      "incomplete_value": false,
      "site": "0087c8d4",
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
      "definition_site": "0087c8f0",
      "incomplete_value": false,
      "site": "0087c8fc",
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
      "definition_site": "0087c8f0",
      "incomplete_value": false,
      "site": "0087c8fc",
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
      "definition_site": "0087ca24",
      "incomplete_value": true,
      "site": "0087ca2c",
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
      "definition_site": "0087ca24",
      "incomplete_value": true,
      "site": "0087ca2c",
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
      "0087c8cc",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087c8f0",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0087ca24",
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
      "0087c8cc",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0087c8f0",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0087ca24",
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

- 旧版 [`0087c8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087c758.md#insn-0087c8cc) · [`0087c8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087c758.md#insn-0087c8f0) · [`0087ca24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087c758.md#insn-0087ca24)
- 新版 [`0087c8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087c758.md#insn-0087c8cc) · [`0087c8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087c758.md#insn-0087c8f0) · [`0087ca24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087c758.md#insn-0087ca24)

~~~diff
- 0087c8cc ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0087c8cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087c8cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087c8cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087c8cc ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0087c8cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c8cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c8cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087c8cc bytes 21280c91
+ 0087c8cc bytes 21900e91
- 0087c8f0 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0087c8f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087c8f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087c8f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087c8f0 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0087c8f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c8f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c8f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087c8f0 bytes 21642491
+ 0087c8f0 bytes 21142291
- 0087ca24 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0087ca24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087ca24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087ca24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087ca24 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0087ca24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ca24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ca24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087ca24 bytes 21b80b91
+ 0087ca24 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f543709218a7a44709320cd88a8780f2"></a>

### [`0087cfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087cfbc.md) → [`0087cfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087cfbc.md) FUN_0087cfbc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0087c758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087c758.md) [`0087cfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087cfbc.md) [`00979584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979584.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`0087c758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087c758.md) [`0087cfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087cfbc.md) [`00979584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979584.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.53% / 新版 98.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087d124",
      "incomplete_value": false,
      "site": "0087d12c",
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
      "definition_site": "0087d124",
      "incomplete_value": false,
      "site": "0087d12c",
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
      "definition_site": "0087d148",
      "incomplete_value": false,
      "site": "0087d154",
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
      "definition_site": "0087d148",
      "incomplete_value": false,
      "site": "0087d154",
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
      "definition_site": "0087d27c",
      "incomplete_value": false,
      "site": "0087d284",
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
      "definition_site": "0087d27c",
      "incomplete_value": false,
      "site": "0087d284",
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
      "0087d124",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087d148",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0087d27c",
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
      "0087d124",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0087d148",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0087d27c",
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

- 旧版 [`0087d124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087cfbc.md#insn-0087d124) · [`0087d148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087cfbc.md#insn-0087d148) · [`0087d27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087cfbc.md#insn-0087d27c)
- 新版 [`0087d124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087cfbc.md#insn-0087d124) · [`0087d148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087cfbc.md#insn-0087d148) · [`0087d27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087cfbc.md#insn-0087d27c)

~~~diff
- 0087d124 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0087d124 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087d124 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087d124 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087d124 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0087d124 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d124 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d124 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087d124 bytes 21280c91
+ 0087d124 bytes 21900e91
- 0087d148 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0087d148 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087d148 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087d148 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087d148 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0087d148 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d148 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d148 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087d148 bytes 21642491
+ 0087d148 bytes 21142291
- 0087d27c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0087d27c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087d27c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087d27c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087d27c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0087d27c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d27c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d27c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087d27c bytes 21b80b91
+ 0087d27c bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e51e94a6a94be2a64e07c53678d5089"></a>

### [`0087d9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087d/0087d9b4.md) → [`0087d9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d9b4.md) FUN_0087d9b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00870c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00870/00870c7c.md) [`0087d9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087d/0087d9b4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00870c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870c7c.md) [`0087d9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d9b4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087db60",
      "incomplete_value": false,
      "site": "0087db6c",
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
      "definition_site": "0087db60",
      "incomplete_value": false,
      "site": "0087db6c",
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
      "definition_site": "0087dc94",
      "incomplete_value": false,
      "site": "0087dc9c",
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
      "definition_site": "0087dc94",
      "incomplete_value": false,
      "site": "0087dc9c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087dcac",
      "incomplete_value": false,
      "site": "0087dcb8",
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
      "definition_site": "0087dcac",
      "incomplete_value": false,
      "site": "0087dcb8",
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
      "0087db3c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087db60",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0087dc94",
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
      "0087db3c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0087db60",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0087dc94",
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

- 旧版 [`0087db3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087d/0087d9b4.md#insn-0087db3c) · [`0087db60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087d/0087d9b4.md#insn-0087db60) · [`0087dc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087d/0087d9b4.md#insn-0087dc94)
- 新版 [`0087db3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d9b4.md#insn-0087db3c) · [`0087db60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d9b4.md#insn-0087db60) · [`0087dc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d9b4.md#insn-0087dc94)

~~~diff
- 0087db3c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0087db3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087db3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087db3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087db3c ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0087db3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087db3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087db3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087db3c bytes 21280c91
+ 0087db3c bytes 21900e91
- 0087db60 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0087db60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087db60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087db60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087db60 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0087db60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087db60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087db60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087db60 bytes 21642491
+ 0087db60 bytes 21142291
- 0087dc94 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0087dc94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087dc94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087dc94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087dc94 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0087dc94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087dc94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087dc94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087dc94 bytes 21b80b91
+ 0087dc94 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7f76354399164e60d1f3c840856dd5c"></a>

### [`0087e398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087e398.md) → [`0087e398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087e398.md) FUN_0087e398

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087d9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087d/0087d9b4.md) [`0087e398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087e398.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087d9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d9b4.md) [`0087e398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087e398.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.76% / 新版 98.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087e518",
      "incomplete_value": false,
      "site": "0087e520",
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
      "definition_site": "0087e518",
      "incomplete_value": false,
      "site": "0087e520",
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
      "definition_site": "0087e670",
      "incomplete_value": false,
      "site": "0087e678",
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
      "definition_site": "0087e670",
      "incomplete_value": false,
      "site": "0087e678",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087e688",
      "incomplete_value": false,
      "site": "0087e694",
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
      "definition_site": "0087e688",
      "incomplete_value": false,
      "site": "0087e694",
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
      "0087e518",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087e53c",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0087e670",
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
      "0087e518",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0087e53c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0087e670",
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

- 旧版 [`0087e518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087e398.md#insn-0087e518) · [`0087e53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087e398.md#insn-0087e53c) · [`0087e670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087e398.md#insn-0087e670)
- 新版 [`0087e518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087e398.md#insn-0087e518) · [`0087e53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087e398.md#insn-0087e53c) · [`0087e670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087e398.md#insn-0087e670)

~~~diff
- 0087e518 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0087e518 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087e518 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087e518 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087e518 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0087e518 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e518 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e518 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087e518 bytes 21280c91
+ 0087e518 bytes 21900e91
- 0087e53c ["COPY", "tmp:0:8", ["const:919:8"]]
- 0087e53c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087e53c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087e53c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087e53c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0087e53c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e53c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e53c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087e53c bytes 21642491
+ 0087e53c bytes 21142291
- 0087e670 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0087e670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087e670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087e670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087e670 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0087e670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087e670 bytes 21b80b91
+ 0087e670 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b248bee6135c0e3728833195e4d7963"></a>

### [`0087ed74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087ed74.md) → [`0087ed74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087ed74.md) FUN_0087ed74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087e398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087e398.md) [`0087ed74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087ed74.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087e398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087e398.md) [`0087ed74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087ed74.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.74% / 新版 98.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087eeec",
      "incomplete_value": false,
      "site": "0087eef4",
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
      "definition_site": "0087eeec",
      "incomplete_value": false,
      "site": "0087eef4",
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
      "definition_site": "0087ef10",
      "incomplete_value": false,
      "site": "0087ef1c",
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
      "definition_site": "0087ef10",
      "incomplete_value": false,
      "site": "0087ef1c",
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
      "definition_site": "0087f044",
      "incomplete_value": false,
      "site": "0087f04c",
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
      "definition_site": "0087f044",
      "incomplete_value": false,
      "site": "0087f04c",
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
      "0087eeec",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087ef10",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0087f044",
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
      "0087eeec",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0087ef10",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0087f044",
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

- 旧版 [`0087eeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087ed74.md#insn-0087eeec) · [`0087ef10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087ed74.md#insn-0087ef10) · [`0087f044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087ed74.md#insn-0087f044)
- 新版 [`0087eeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087ed74.md#insn-0087eeec) · [`0087ef10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087ed74.md#insn-0087ef10) · [`0087f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087ed74.md#insn-0087f044)

~~~diff
- 0087eeec ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0087eeec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087eeec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087eeec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087eeec ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0087eeec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087eeec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087eeec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087eeec bytes 21280c91
+ 0087eeec bytes 21900e91
- 0087ef10 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0087ef10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087ef10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087ef10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087ef10 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0087ef10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ef10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ef10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087ef10 bytes 21642491
+ 0087ef10 bytes 21142291
- 0087f044 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0087f044 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087f044 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087f044 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087f044 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0087f044 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f044 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f044 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087f044 bytes 21b80b91
+ 0087f044 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-376bf7a79278afc5cff886a3d3f8f7e6"></a>

### [`0087f724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087f/0087f724.md) → [`0087f724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087f/0087f724.md) FUN_0087f724

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087ed74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087ed74.md) [`0087f724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087f/0087f724.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087ed74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087e/0087ed74.md) [`0087f724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087f/0087f724.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087f8a4",
      "incomplete_value": false,
      "site": "0087f8ac",
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
      "definition_site": "0087f8a4",
      "incomplete_value": false,
      "site": "0087f8ac",
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
      "definition_site": "0087f95c",
      "incomplete_value": false,
      "site": "0087f964",
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
      "definition_site": "0087f95c",
      "incomplete_value": false,
      "site": "0087f964",
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
      "definition_site": "0087f978",
      "incomplete_value": false,
      "site": "0087f984",
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
      "definition_site": "0087f978",
      "incomplete_value": false,
      "site": "0087f984",
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
      "0087f8a4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087f95c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087f978",
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
      "0087f8a4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0087f95c",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "0087f978",
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

- 旧版 [`0087f8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087f/0087f724.md#insn-0087f8a4) · [`0087f95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087f/0087f724.md#insn-0087f95c) · [`0087f978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087f/0087f724.md#insn-0087f978)
- 新版 [`0087f8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087f/0087f724.md#insn-0087f8a4) · [`0087f95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087f/0087f724.md#insn-0087f95c) · [`0087f978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087f/0087f724.md#insn-0087f978)

~~~diff
- 0087f8a4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0087f8a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087f8a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087f8a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087f8a4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0087f8a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f8a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f8a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087f8a4 bytes 21280c91
+ 0087f8a4 bytes 21900e91
- 0087f95c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0087f95c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087f95c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087f95c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087f95c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0087f95c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f95c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f95c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087f95c bytes 21b80b91
+ 0087f95c bytes 21e40d91
- 0087f978 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0087f978 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087f978 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087f978 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087f978 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0087f978 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f978 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f978 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087f978 bytes 21642491
+ 0087f978 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88ea6b7d3a6c78e97df17b346fcf3e00"></a>

### [`0088004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/0088004c.md) → [`0088004c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/0088004c.md) FUN_0088004c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087f724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087f/0087f724.md) [`0088004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/0088004c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087f724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087f/0087f724.md) [`0088004c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/0088004c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008801ac",
      "incomplete_value": false,
      "site": "008801b4",
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
      "definition_site": "008801ac",
      "incomplete_value": false,
      "site": "008801b4",
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
      "definition_site": "008801d0",
      "incomplete_value": false,
      "site": "008801dc",
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
      "definition_site": "008801d0",
      "incomplete_value": false,
      "site": "008801dc",
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
      "definition_site": "00880304",
      "incomplete_value": false,
      "site": "0088030c",
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
      "definition_site": "00880304",
      "incomplete_value": false,
      "site": "0088030c",
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
      "008801ac",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "008801d0",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00880304",
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
      "008801ac",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "008801d0",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00880304",
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

- 旧版 [`008801ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/0088004c.md#insn-008801ac) · [`008801d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/0088004c.md#insn-008801d0) · [`00880304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/0088004c.md#insn-00880304)
- 新版 [`008801ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/0088004c.md#insn-008801ac) · [`008801d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/0088004c.md#insn-008801d0) · [`00880304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/0088004c.md#insn-00880304)

~~~diff
- 008801ac ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008801ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008801ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008801ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008801ac ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 008801ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008801ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008801ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008801ac bytes 21280c91
+ 008801ac bytes 21900e91
- 008801d0 ["COPY", "tmp:0:8", ["const:919:8"]]
- 008801d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008801d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008801d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008801d0 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 008801d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008801d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008801d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008801d0 bytes 21642491
+ 008801d0 bytes 21142291
- 00880304 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00880304 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00880304 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00880304 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00880304 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00880304 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00880304 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00880304 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00880304 bytes 21b80b91
+ 00880304 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8419cf790a3305a86f487e17e0a9f2ed"></a>

### [`00880878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/00880878.md) → [`00880878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/00880878.md) FUN_00880878

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0088004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/0088004c.md) [`00880878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/00880878.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0088004c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/0088004c.md) [`00880878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/00880878.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008809d4",
      "incomplete_value": false,
      "site": "008809dc",
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
      "definition_site": "008809d4",
      "incomplete_value": false,
      "site": "008809dc",
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
      "definition_site": "008809f8",
      "incomplete_value": false,
      "site": "00880a04",
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
      "definition_site": "008809f8",
      "incomplete_value": false,
      "site": "00880a04",
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
      "definition_site": "00880b2c",
      "incomplete_value": false,
      "site": "00880b34",
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
      "definition_site": "00880b2c",
      "incomplete_value": false,
      "site": "00880b34",
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
      "008809d4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "008809f8",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00880b2c",
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
      "008809d4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "008809f8",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00880b2c",
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

- 旧版 [`008809d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/00880878.md#insn-008809d4) · [`008809f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/00880878.md#insn-008809f8) · [`00880b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/00880878.md#insn-00880b2c)
- 新版 [`008809d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/00880878.md#insn-008809d4) · [`008809f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/00880878.md#insn-008809f8) · [`00880b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/00880878.md#insn-00880b2c)

~~~diff
- 008809d4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008809d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008809d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008809d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008809d4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 008809d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008809d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008809d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008809d4 bytes 21280c91
+ 008809d4 bytes 21900e91
- 008809f8 ["COPY", "tmp:0:8", ["const:919:8"]]
- 008809f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008809f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008809f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008809f8 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 008809f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008809f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008809f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008809f8 bytes 21642491
+ 008809f8 bytes 21142291
- 00880b2c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00880b2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00880b2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00880b2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00880b2c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00880b2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00880b2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00880b2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00880b2c bytes 21b80b91
+ 00880b2c bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-686a275180133b78b1fe34e88abd8602"></a>

### [`00881090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/00881090.md) → [`00881090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/00881090.md) FUN_00881090

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00880878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/00880878.md) [`00881090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/00881090.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00880878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00880/00880878.md) [`00881090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/00881090.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008811ec",
      "incomplete_value": false,
      "site": "008811f4",
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
      "definition_site": "008811ec",
      "incomplete_value": false,
      "site": "008811f4",
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
      "definition_site": "00881210",
      "incomplete_value": false,
      "site": "0088121c",
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
      "definition_site": "00881210",
      "incomplete_value": false,
      "site": "0088121c",
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
      "definition_site": "00881344",
      "incomplete_value": false,
      "site": "0088134c",
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
      "definition_site": "00881344",
      "incomplete_value": false,
      "site": "0088134c",
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
      "008811ec",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00881210",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00881344",
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
      "008811ec",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00881210",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00881344",
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

- 旧版 [`008811ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/00881090.md#insn-008811ec) · [`00881210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/00881090.md#insn-00881210) · [`00881344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/00881090.md#insn-00881344)
- 新版 [`008811ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/00881090.md#insn-008811ec) · [`00881210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/00881090.md#insn-00881210) · [`00881344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/00881090.md#insn-00881344)

~~~diff
- 008811ec ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008811ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008811ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008811ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008811ec ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 008811ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008811ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008811ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008811ec bytes 21280c91
+ 008811ec bytes 21900e91
- 00881210 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00881210 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00881210 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00881210 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00881210 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00881210 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00881210 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00881210 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00881210 bytes 21642491
+ 00881210 bytes 21142291
- 00881344 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00881344 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00881344 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00881344 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00881344 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00881344 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00881344 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00881344 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00881344 bytes 21b80b91
+ 00881344 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-320fbaef526f887b4bab4a591f59c12e"></a>

### [`008818a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/008818a8.md) → [`008818a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/008818a8.md) FUN_008818a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00881090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/00881090.md) [`008818a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/008818a8.md) [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`00881090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/00881090.md) [`008818a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/008818a8.md) [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

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
      "definition_site": "00881a00",
      "incomplete_value": false,
      "site": "00881a08",
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
      "definition_site": "00881a00",
      "incomplete_value": false,
      "site": "00881a08",
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
      "definition_site": "00881a24",
      "incomplete_value": false,
      "site": "00881a30",
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
      "definition_site": "00881a24",
      "incomplete_value": false,
      "site": "00881a30",
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
      "definition_site": "00881b70",
      "incomplete_value": false,
      "site": "00881b7c",
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
      "definition_site": "00881b70",
      "incomplete_value": false,
      "site": "00881b7c",
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
      "00881a00",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00881a24",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00881b58",
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
      "00881a00",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00881a24",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00881b58",
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

- 旧版 [`00881a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/008818a8.md#insn-00881a00) · [`00881a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/008818a8.md#insn-00881a24) · [`00881b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/008818a8.md#insn-00881b58)
- 新版 [`00881a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/008818a8.md#insn-00881a00) · [`00881a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/008818a8.md#insn-00881a24) · [`00881b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/008818a8.md#insn-00881b58)

~~~diff
- 00881a00 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00881a00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00881a00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00881a00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00881a00 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00881a00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00881a00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00881a00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00881a00 bytes 21280c91
+ 00881a00 bytes 21900e91
- 00881a24 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00881a24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00881a24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00881a24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00881a24 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00881a24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00881a24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00881a24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00881a24 bytes 21642491
+ 00881a24 bytes 21142291
- 00881b58 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00881b58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00881b58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00881b58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00881b58 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00881b58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00881b58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00881b58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00881b58 bytes 21b80b91
+ 00881b58 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc3f5400a4cc7d8583dc347171823fb1"></a>

### [`008820ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/008820ac.md) → [`008820ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/008820ac.md) FUN_008820ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00870df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00870/00870df0.md) [`008820ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/008820ac.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00870df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870df0.md) [`008820ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/008820ac.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00882208",
      "incomplete_value": false,
      "site": "00882210",
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
      "definition_site": "00882208",
      "incomplete_value": false,
      "site": "00882210",
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
      "definition_site": "0088222c",
      "incomplete_value": false,
      "site": "00882238",
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
      "definition_site": "0088222c",
      "incomplete_value": false,
      "site": "00882238",
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
      "definition_site": "00882378",
      "incomplete_value": false,
      "site": "00882384",
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
      "definition_site": "00882378",
      "incomplete_value": false,
      "site": "00882384",
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
      "00882208",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0088222c",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00882360",
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
      "00882208",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0088222c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00882360",
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

- 旧版 [`00882208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/008820ac.md#insn-00882208) · [`0088222c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/008820ac.md#insn-0088222c) · [`00882360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/008820ac.md#insn-00882360)
- 新版 [`00882208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/008820ac.md#insn-00882208) · [`0088222c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/008820ac.md#insn-0088222c) · [`00882360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/008820ac.md#insn-00882360)

~~~diff
- 00882208 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00882208 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00882208 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00882208 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00882208 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00882208 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00882208 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00882208 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00882208 bytes 21280c91
+ 00882208 bytes 21900e91
- 0088222c ["COPY", "tmp:0:8", ["const:919:8"]]
- 0088222c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0088222c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0088222c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0088222c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0088222c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0088222c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0088222c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0088222c bytes 21642491
+ 0088222c bytes 21142291
- 00882360 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00882360 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00882360 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00882360 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00882360 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00882360 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00882360 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00882360 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00882360 bytes 21b80b91
+ 00882360 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fe3f6937c3010b028c1d5b5edc3328f"></a>

### [`00882a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/00882a18.md) → [`00882a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/00882a18.md) FUN_00882a18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008820ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/008820ac.md) [`00882a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/00882a18.md) [`00a39ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a39/00a39ff4.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`008820ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/008820ac.md) [`00882a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/00882a18.md) [`00a3a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a038.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.62% / 新版 98.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00882b84",
      "incomplete_value": false,
      "site": "00882b8c",
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
      "definition_site": "00882b84",
      "incomplete_value": false,
      "site": "00882b8c",
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
      "definition_site": "00882c3c",
      "incomplete_value": false,
      "site": "00882c44",
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
      "definition_site": "00882c3c",
      "incomplete_value": false,
      "site": "00882c44",
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
      "definition_site": "00882c58",
      "incomplete_value": false,
      "site": "00882c64",
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
      "definition_site": "00882c58",
      "incomplete_value": false,
      "site": "00882c64",
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
      "00882b84",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00882c3c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00882c58",
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
      "00882b84",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00882c3c",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00882c58",
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

- 旧版 [`00882b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/00882a18.md#insn-00882b84) · [`00882c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/00882a18.md#insn-00882c3c) · [`00882c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/00882a18.md#insn-00882c58)
- 新版 [`00882b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/00882a18.md#insn-00882b84) · [`00882c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/00882a18.md#insn-00882c3c) · [`00882c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/00882a18.md#insn-00882c58)

~~~diff
- 00882b84 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00882b84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00882b84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00882b84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00882b84 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00882b84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00882b84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00882b84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00882b84 bytes 21280c91
+ 00882b84 bytes 21900e91
- 00882c3c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00882c3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00882c3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00882c3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00882c3c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00882c3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00882c3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00882c3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00882c3c bytes 21b80b91
+ 00882c3c bytes 21e40d91
- 00882c58 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00882c58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00882c58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00882c58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00882c58 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00882c58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00882c58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00882c58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00882c58 bytes 21642491
+ 00882c58 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c08b8165e859fadaa77f934639008a61"></a>

### [`008832e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/008832e8.md) → [`008832e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/008832e8.md) _INIT_163

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 79.33% / 新版 79.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 7件, `store_value` 7件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883324",
      "incomplete_value": true,
      "site": "00883340",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00883324",
      "incomplete_value": true,
      "site": "00883340",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00883348",
      "incomplete_value": true,
      "site": "00883364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00883348",
      "incomplete_value": true,
      "site": "00883364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00883368",
      "incomplete_value": true,
      "site": "00883384",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00883368",
      "incomplete_value": true,
      "site": "00883384",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00883324",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00883348",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00883368",
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
      "00883324",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00883348",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00883368",
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

- 旧版 [`00883520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/008832e8.md#insn-00883520) · [`00883560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/008832e8.md#insn-00883560)
- 新版 [`00883520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/008832e8.md#insn-00883520)

~~~diff
- 00883520 ["INT_ADD", "register:40f0:8", ["const:883520:8", "const:4:8"]]
- 00883520 ["CALL", null, ["callee:00bdafe0:8"]]
- 00883520 bytes 9c5e0d94
+ 00883520 ["INT_ADD", "register:40f0:8", ["const:883520:8", "const:4:8"]]
+ 00883520 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00883520 bytes b05e0d94
- 00883560 ["INT_ADD", "register:40f0:8", ["const:883560:8", "const:4:8"]]
- 00883560 ["CALL", null, ["callee:00bdafe0:8"]]
- 00883560 bytes 8c5e0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b46368f0845beeb239dcb84eab082bb0"></a>

### [`008836f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/008836f4.md) → [`008836f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/008836f4.md) FUN_008836f4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md) · 呼出先 5件 [`00884834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884834.md) [`00884900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884900.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md) · 呼出先 5件 [`00884834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884834.md) [`00884900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884900.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883758",
      "incomplete_value": true,
      "site": "00883758",
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
      "definition_site": "00883758",
      "incomplete_value": true,
      "site": "00883758",
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
      "00883750",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "00883758",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "00883820",
      "READ",
      [
        "storage",
        "00c246b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00883750",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "00883758",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "00883820",
      "READ",
      [
        "storage",
        "00c24708",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/008836f4.md#insn-00883750) · [`00883818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/008836f4.md#insn-00883818)
- 新版 [`00883750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/008836f4.md#insn-00883750) · [`00883818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/008836f4.md#insn-00883818)

~~~diff
- 00883750 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
- 00883750 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00883750 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 00883750 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00883750 bytes 089142f9
+ 00883750 bytes 08b942f9
- 00883818 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00883818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00883818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00883818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883818 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00883818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00883818 bytes 08e11a91
+ 00883818 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9efbc3be4ae99ad9d19482a771f856bf"></a>

### [`00883bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md) → [`00883bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883bb8.md) FUN_00883bb8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 56件 [`005a33f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a33f8.md) [`005e97d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e9/005e97d8.md) [`005ecde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ecde0.md) [`005ee758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ee/005ee758.md) [`005efbac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ef/005efbac.md) · 呼出先 3件 [`009e9760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9760.md) [`009e9afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9afc.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 56件 [`005a33f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a33f8.md) [`005e97d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e9/005e97d8.md) [`005ecde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ecde0.md) [`005ee758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ee/005ee758.md) [`005efbac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ef/005efbac.md) · 呼出先 3件 [`009e97a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e97a4.md) [`009e9b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9b40.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00883bfc",
      "incomplete_value": true,
      "site": "00883c00",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883bfc",
      "incomplete_value": true,
      "site": "00883c00",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
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
      "00883bf8",
      "READ",
      [
        "storage",
        "00c1b720",
        null,
        "pointer"
      ]
    ],
    [
      "00883bf8",
      "PARAM",
      [
        "storage",
        "00c0bd08",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00883bfc",
      "READ",
      [
        "storage",
        "00c1b728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00883bf8",
      "READ",
      [
        "storage",
        "00c1b770",
        null,
        "pointer"
      ]
    ],
    [
      "00883bf8",
      "PARAM",
      [
        "storage",
        "00c0bd58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00883bfc",
      "READ",
      [
        "storage",
        "00c1b778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md#insn-00883bf8) · [`00883bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md#insn-00883bfc)
- 新版 [`00883bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883bb8.md#insn-00883bf8) · [`00883bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883bb8.md#insn-00883bfc)

~~~diff
- 00883bf8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:720:8"]]
- 00883bf8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00883bf8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:770:8"]]
+ 00883bf8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00883bf8 bytes 219043f9
+ 00883bf8 bytes 21b843f9
- 00883bfc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:728:8"]]
- 00883bfc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00883bfc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:778:8"]]
+ 00883bfc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00883bfc bytes 429443f9
+ 00883bfc bytes 42bc43f9
~~~


<a id="compare-7b7e2814c9fe25e4b69de5d01e268974"></a>

### [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md) → [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md) FUN_00883e08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 70件 [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e144c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e144c.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`008836f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/008836f4.md) [`00884834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884834.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 70件 [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e144c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e144c.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005eb/005eb040.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`008836f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/008836f4.md) [`00884834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884834.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883f7c",
      "incomplete_value": true,
      "site": "00883f7c",
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
      "definition_site": "00883f7c",
      "incomplete_value": true,
      "site": "00883f7c",
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
      "00883f74",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "00883f7c",
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
      "00883f74",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "00883f7c",
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

- 旧版 [`00883f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md#insn-00883f74)
- 新版 [`00883f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md#insn-00883f74)

~~~diff
- 00883f74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
- 00883f74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00883f74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 00883f74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00883f74 bytes 089142f9
+ 00883f74 bytes 08b942f9
~~~


<a id="compare-409f36e6222787203825fefd39dccfb9"></a>

### [`008841e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008841e8.md) → [`008841e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008841e8.md) FUN_008841e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00884a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884a68.md) · 呼出先 3件 [`00884834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884834.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00884a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884a68.md) · 呼出先 3件 [`00884834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884834.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "00884274",
      "incomplete_value": true,
      "site": "00884274",
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
      "definition_site": "00884274",
      "incomplete_value": true,
      "site": "00884274",
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
      "0088426c",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "00884274",
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
      "0088426c",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "00884274",
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

- 旧版 [`0088426c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008841e8.md#insn-0088426c)
- 新版 [`0088426c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008841e8.md#insn-0088426c)

~~~diff
- 0088426c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
- 0088426c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0088426c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 0088426c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0088426c bytes 089142f9
+ 0088426c bytes 08b942f9
~~~


<a id="compare-9cd4d233e682050e362d99a6ac531b32"></a>

### [`00884b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884b3c.md) → [`00884b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884b3c.md) _INIT_164

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00884bbc",
      "incomplete_value": true,
      "site": "00884bd8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00884bbc",
      "incomplete_value": true,
      "site": "00884bd8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00884bdc",
      "incomplete_value": true,
      "site": "00884bf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00884bdc",
      "incomplete_value": true,
      "site": "00884bf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00884d64",
      "incomplete_value": false,
      "site": "00884d70",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00884d64",
      "incomplete_value": false,
      "site": "00884d70",
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
            "const:6b8:8"
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
      "00884b78",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00884b9c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00884bbc",
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
      "00884b78",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00884b9c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00884bbc",
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

- 旧版 [`00884b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884b3c.md#insn-00884b68) · [`00884b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884b3c.md#insn-00884b74) · [`00884b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884b3c.md#insn-00884b90)
- 新版 [`00884b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884b3c.md#insn-00884b68) · [`00884b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884b3c.md#insn-00884b74) · [`00884b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884b3c.md#insn-00884b90)

~~~diff
- 00884b68 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00884b68 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00884b68 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00884b68 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00884b68 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00884b68 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00884b68 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00884b68 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00884b68 bytes 73e21a91
+ 00884b68 bytes 73e21b91
- 00884b74 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00884b74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00884b74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00884b74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00884b74 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00884b74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00884b74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00884b74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00884b74 bytes 29750b91
+ 00884b74 bytes 29dd0d91
- 00884b90 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 00884b90 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00884b90 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00884b90 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00884b90 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 00884b90 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00884b90 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00884b90 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00884b90 bytes 4ac10b91
+ 00884b90 bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ddf5ca1f7dc1b93f172aeda09942d49"></a>

### [`00884ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884ecc.md) → [`00884ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884ecc.md) FUN_00884ecc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00885170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885170.md) · 呼出先 10件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c68.md) [`008887f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/008887f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00885170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885170.md) · 呼出先 10件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00467c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c68.md) [`008887f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/008887f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008850cc",
      "incomplete_value": false,
      "site": "008850cc",
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
      "definition_site": "008850cc",
      "incomplete_value": false,
      "site": "008850cc",
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
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008850d0",
      "incomplete_value": false,
      "site": "008850d0",
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
      "definition_site": "008850d0",
      "incomplete_value": false,
      "site": "008850d0",
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
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008850cc",
      "incomplete_value": false,
      "site": "008850d0",
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
      "definition_site": "008850cc",
      "incomplete_value": false,
      "site": "008850d0",
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
      "00884f8c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00884f9c",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "00884fa0",
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
      "00884f8c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00884f9c",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "00884fa0",
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

- 旧版 [`00884f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884ecc.md#insn-00884f88) · [`00884f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884ecc.md#insn-00884f9c) · [`00884fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884ecc.md#insn-00884fa0)
- 新版 [`00884f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884ecc.md#insn-00884f88) · [`00884f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884ecc.md#insn-00884f9c) · [`00884fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884ecc.md#insn-00884fa0)

~~~diff
- 00884f88 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00884f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00884f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00884f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00884f88 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00884f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00884f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00884f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00884f88 bytes 08e10091
+ 00884f88 bytes 08e10191
- 00884f9c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00884f9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00884f9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00884f9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00884f9c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00884f9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00884f9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00884f9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00884f9c bytes 00000091
+ 00884f9c bytes 00000191
- 00884fa0 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 00884fa0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00884fa0 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 00884fa0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00884fa0 bytes 423047f9
+ 00884fa0 bytes 425847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80f9aa7848a4ee5a663e8f3f1c8c65b7"></a>

### [`00886564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/00886564.md) → [`00886564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886564.md) FUN_00886564

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 9件 [`0066f184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f184.md) [`00670388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670388.md) [`00671c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671c4c.md) [`00672ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672ef4.md) [`006893c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/006893c0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 9件 [`0066f184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f184.md) [`00670388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670388.md) [`00671c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c4c.md) [`00672ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ef4.md) [`006893c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006893c0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00886590",
      "incomplete_value": true,
      "site": "0088659c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00886590",
      "incomplete_value": true,
      "site": "0088659c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "0088658c",
      "READ",
      [
        "storage",
        "00c1b660",
        null,
        "pointer"
      ]
    ],
    [
      "00886590",
      "DATA",
      [
        "storage",
        "00c2454c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088658c",
      "READ",
      [
        "storage",
        "00c1b6b0",
        null,
        "pointer"
      ]
    ],
    [
      "00886590",
      "DATA",
      [
        "storage",
        "00c2459c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088658c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/00886564.md#insn-0088658c)
- 新版 [`0088658c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886564.md#insn-0088658c)

~~~diff
- 0088658c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:660:8"]]
- 0088658c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0088658c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6b0:8"]]
+ 0088658c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0088658c bytes 293143f9
+ 0088658c bytes 295943f9
~~~


<a id="compare-4bb92485a5bbd267bc3d9c9ef694c6aa"></a>

### [`00888984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/00888984.md) → [`00888984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888984.md) FUN_00888984

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008887f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/008887f0.md) [`00a24a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24a34.md) [`00a26320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26320.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`008887f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/008887f0.md) [`00a24a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a24/00a24a78.md) [`00a26364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26364.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00888990",
      "incomplete_value": false,
      "site": "00888994",
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
      "definition_site": "00888990",
      "incomplete_value": false,
      "site": "00888994",
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
      "00888990",
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
      "00888990",
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

- 旧版 [`00888990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/00888984.md#insn-00888990)
- 新版 [`00888990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888984.md#insn-00888990)

~~~diff
- 00888990 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00888990 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00888990 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00888990 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00888990 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00888990 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00888990 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00888990 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00888990 bytes 000c0c91
+ 00888990 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed5019675eaf4fa3a8b5be90b386f829"></a>

### [`00888f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/00888f58.md) → [`00888f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888f58.md) FUN_00888f58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00888b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/00888b00.md) [`00a25060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25060.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00888b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888b00.md) [`00a250a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a250a4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00888f64",
      "incomplete_value": false,
      "site": "00888f68",
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
      "definition_site": "00888f64",
      "incomplete_value": false,
      "site": "00888f68",
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
      "00888f64",
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
      "00888f64",
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

- 旧版 [`00888f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/00888f58.md#insn-00888f64)
- 新版 [`00888f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888f58.md#insn-00888f64)

~~~diff
- 00888f64 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00888f64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00888f64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00888f64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00888f64 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00888f64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00888f64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00888f64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00888f64 bytes 000c0c91
+ 00888f64 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91572337d38d421f30ac9a5941ec753e"></a>

### [`0088923c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/0088923c.md) → [`0088923c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/0088923c.md) FUN_0088923c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00887594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/00887594.md) [`008879f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/008879f4.md) [`00887e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/00887e18.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`00887594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/00887594.md) [`008879f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879f4.md) [`00887e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/00887e18.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00889248",
      "incomplete_value": false,
      "site": "0088924c",
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
      "definition_site": "00889248",
      "incomplete_value": false,
      "site": "0088924c",
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
      "00889248",
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
      "00889248",
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

- 旧版 [`00889248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/0088923c.md#insn-00889248)
- 新版 [`00889248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/0088923c.md#insn-00889248)

~~~diff
- 00889248 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00889248 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00889248 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00889248 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00889248 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00889248 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00889248 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00889248 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00889248 bytes 000c0c91
+ 00889248 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c5a5319f9f1da145ca765f765071e6c"></a>

### [`00889250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/00889250.md) → [`00889250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/00889250.md) FUN_00889250

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00888268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/00888268.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00888268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888268.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0088925c",
      "incomplete_value": false,
      "site": "00889260",
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
      "definition_site": "0088925c",
      "incomplete_value": false,
      "site": "00889260",
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
      "0088925c",
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
      "0088925c",
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

- 旧版 [`0088925c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/00889250.md#insn-0088925c)
- 新版 [`0088925c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/00889250.md#insn-0088925c)

~~~diff
- 0088925c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0088925c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0088925c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0088925c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0088925c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0088925c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0088925c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0088925c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0088925c bytes 000c0c91
+ 0088925c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9da50b5d07a1f542fe94c049da8f7118"></a>

### [`00889264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/00889264.md) → [`00889264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/00889264.md) _INIT_165

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
      "definition_site": "008892a0",
      "incomplete_value": true,
      "site": "008892bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008892a0",
      "incomplete_value": true,
      "site": "008892bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008892c4",
      "incomplete_value": true,
      "site": "008892e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008892c4",
      "incomplete_value": true,
      "site": "008892e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008892e4",
      "incomplete_value": true,
      "site": "00889300",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008892e4",
      "incomplete_value": true,
      "site": "00889300",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "008892a0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008892c4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008892e4",
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
      "008892a0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "008892c4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "008892e4",
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

- 旧版 [`00889290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/00889264.md#insn-00889290) · [`00889298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/00889264.md#insn-00889298)
- 新版 [`00889290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/00889264.md#insn-00889290) · [`00889298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/00889264.md#insn-00889298)

~~~diff
- 00889290 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 00889290 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00889290 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00889290 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00889290 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00889290 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00889290 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00889290 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00889290 bytes 73421b91
+ 00889290 bytes 73421c91
- 00889298 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00889298 bytes e9d0ffd0
+ 00889298 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00889298 bytes e9d0ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f1973bb15b16727a9d24e4723e124b3"></a>

### [`008895f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/008895f4.md) → [`008895f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008895f4.md) FUN_008895f4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) · 呼出先 14件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00640008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640008.md) [`0072dfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072d/0072dfbc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) · 呼出先 14件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00640008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640008.md) [`0072dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 1件, `store_value` 17件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00889638",
      "incomplete_value": false,
      "site": "0088963c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889638",
      "incomplete_value": false,
      "site": "0088963c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "definition_site": "008896d8",
      "incomplete_value": true,
      "site": "008896d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "008896d8",
      "incomplete_value": true,
      "site": "008896d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 53,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008896f0",
      "incomplete_value": true,
      "site": "008896f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "008896f0",
      "incomplete_value": true,
      "site": "008896f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0088963c",
      "DATA",
      [
        "storage",
        "00c05b08",
        null,
        "pointer"
      ]
    ],
    [
      "008896a8",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008896c8",
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
      "0088963c",
      "DATA",
      [
        "storage",
        "00c05b58",
        null,
        "pointer"
      ]
    ],
    [
      "008896a8",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008896c8",
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

- 旧版 [`00889638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/008895f4.md#insn-00889638) · [`00889640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/008895f4.md#insn-00889640)
- 新版 [`00889638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008895f4.md#insn-00889638) · [`00889640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008895f4.md#insn-00889640)

~~~diff
- 00889638 ["COPY", "tmp:0:8", ["const:b08:8"]]
- 00889638 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00889638 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00889638 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00889638 ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 00889638 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00889638 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00889638 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00889638 bytes 08212c91
+ 00889638 bytes 08612d91
- 00889640 ["COPY", "register:40c0:8", ["const:c25000:8"]]
- 00889640 bytes f81c0090
+ 00889640 ["COPY", "register:40c0:8", ["const:c25000:8"]]
+ 00889640 bytes f81c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b732c747aa6e9994a91fee60788ba6b2"></a>

### [`0088a82c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088a/0088a82c.md) → [`0088a82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088a/0088a82c.md) FUN_0088a82c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008895f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/008895f4.md) · 呼出先 47件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`008895f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008895f4.md) · 呼出先 47件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 11件, `store_value` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088a89c",
      "incomplete_value": true,
      "site": "0088a89c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:52d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a89c",
      "incomplete_value": true,
      "site": "0088a89c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:493:8"
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
      "definition_site": "0088a954",
      "incomplete_value": true,
      "site": "0088a95c",
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
      "definition_site": "0088a954",
      "incomplete_value": true,
      "site": "0088a95c",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088b2b8",
      "incomplete_value": true,
      "site": "0088b2b8",
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
      "definition_site": "0088b2b8",
      "incomplete_value": true,
      "site": "0088b2b8",
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
    "ordinal": 134,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0088a86c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0088a88c",
      "READ",
      [
        "storage",
        "002a8493",
        null,
        "string"
      ]
    ],
    [
      "0088a8c0",
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
      "0088a86c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0088a88c",
      "READ",
      [
        "storage",
        "002a852d",
        null,
        "string"
      ]
    ],
    [
      "0088a8c0",
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

- 旧版 [`0088a868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088a/0088a82c.md#insn-0088a868) · [`0088a888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088a/0088a82c.md#insn-0088a888) · [`0088a8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088a/0088a82c.md#insn-0088a8c0)
- 新版 [`0088a868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088a/0088a82c.md#insn-0088a868) · [`0088a888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088a/0088a82c.md#insn-0088a888) · [`0088a8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088a/0088a82c.md#insn-0088a8c0)

~~~diff
- 0088a868 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0088a868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a868 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0088a868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a868 bytes 08e10091
+ 0088a868 bytes 08e10191
- 0088a888 ["COPY", "tmp:0:8", ["const:493:8"]]
- 0088a888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a888 ["COPY", "tmp:0:8", ["const:52d:8"]]
+ 0088a888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a888 bytes 084d1291
+ 0088a888 bytes 08b51491
- 0088a8c0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0088a8c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0088a8c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0088a8c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0088a8c0 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0088a8c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0088a8c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0088a8c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0088a8c0 bytes 00000091
+ 0088a8c0 bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-216d1efeb453540eecf0c6bf9e8aa88f"></a>

### [`0088e208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088e/0088e208.md) → [`0088e208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088e208.md) FUN_0088e208

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008920f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00892/008920f8.md) · 呼出先 13件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) · 呼出先 13件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.34% / 新版 95.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088e2f4",
      "incomplete_value": true,
      "site": "0088e308",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088e2f4",
      "incomplete_value": true,
      "site": "0088e308",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:267:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088e374",
      "incomplete_value": true,
      "site": "0088e38c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088e374",
      "incomplete_value": true,
      "site": "0088e38c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b23:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088e384",
      "incomplete_value": true,
      "site": "0088e390",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0088e384",
      "incomplete_value": true,
      "site": "0088e390",
      "value": [
        "LOAD",
        "16",
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
      "0088e2f4",
      "READ",
      [
        "storage",
        "00298267",
        null,
        "string"
      ]
    ],
    [
      "0088e374",
      "READ",
      [
        "storage",
        "0029eb23",
        null,
        "string"
      ]
    ],
    [
      "0088e384",
      "READ",
      [
        "storage",
        "0029eb2e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0088e2f4",
      "READ",
      [
        "storage",
        "002981da",
        null,
        "string"
      ]
    ],
    [
      "0088e374",
      "READ",
      [
        "storage",
        "0029ebae",
        null,
        "string"
      ]
    ],
    [
      "0088e384",
      "READ",
      [
        "storage",
        "0029ebb9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088e2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088e/0088e208.md#insn-0088e2f0) · [`0088e370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088e/0088e208.md#insn-0088e370) · [`0088e480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088e/0088e208.md#insn-0088e480)
- 新版 [`0088e2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088e208.md#insn-0088e2f0) · [`0088e370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088e208.md#insn-0088e370) · [`0088e480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088e208.md#insn-0088e480)

~~~diff
- 0088e2f0 ["COPY", "tmp:0:8", ["const:267:8"]]
- 0088e2f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088e2f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088e2f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088e2f0 ["COPY", "tmp:0:8", ["const:1da:8"]]
+ 0088e2f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088e2f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088e2f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088e2f0 bytes 089d0991
+ 0088e2f0 bytes 08690791
- 0088e370 ["COPY", "tmp:0:8", ["const:b23:8"]]
- 0088e370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088e370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088e370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088e370 ["COPY", "tmp:0:8", ["const:bae:8"]]
+ 0088e370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088e370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088e370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088e370 bytes 088d2c91
+ 0088e370 bytes 08b92e91
- 0088e480 ["COPY", "tmp:0:8", ["const:8e:8"]]
- 0088e480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088e480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088e480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088e480 ["COPY", "tmp:0:8", ["const:1:8"]]
+ 0088e480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088e480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088e480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088e480 bytes 08390291
+ 0088e480 bytes 08050091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a1a5e0d427875fd40843097b629d53a"></a>

### [`0088ee54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088e/0088ee54.md) → [`0088ee54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088ee54.md) FUN_0088ee54

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008920f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00892/008920f8.md) [`00894d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00894/00894d08.md) [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`00894d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00894/00894d08.md) [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.13% / 新版 91.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088ef14",
      "incomplete_value": true,
      "site": "0088ef14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ef14",
      "incomplete_value": true,
      "site": "0088ef14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d4c:8"
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
      "definition_site": "0088ef94",
      "incomplete_value": true,
      "site": "0088ef94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:994:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ef94",
      "incomplete_value": true,
      "site": "0088ef94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:909:8"
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
      "definition_site": "0088ef98",
      "incomplete_value": true,
      "site": "0088ef98",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0088ef98",
      "incomplete_value": true,
      "site": "0088ef98",
      "value": [
        "LOAD",
        "8",
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
      "0088ef04",
      "READ",
      [
        "storage",
        "002a5d4c",
        null,
        "string"
      ]
    ],
    [
      "0088ef08",
      "READ",
      [
        "storage",
        "002a5d52",
        null,
        "string"
      ]
    ],
    [
      "0088ef84",
      "READ",
      [
        "storage",
        "002a2909",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0088ef04",
      "READ",
      [
        "storage",
        "002a5dd7",
        null,
        "string"
      ]
    ],
    [
      "0088ef08",
      "READ",
      [
        "storage",
        "002a5ddd",
        null,
        "string"
      ]
    ],
    [
      "0088ef84",
      "READ",
      [
        "storage",
        "002a2994",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088eefc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088e/0088ee54.md#insn-0088eefc) · [`0088ef7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088e/0088ee54.md#insn-0088ef7c) · [`0088efb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088e/0088ee54.md#insn-0088efb0)
- 新版 [`0088eefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088ee54.md#insn-0088eefc) · [`0088ef7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088ee54.md#insn-0088ef7c) · [`0088efb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088ee54.md#insn-0088efb0)

~~~diff
- 0088eefc ["COPY", "tmp:0:8", ["const:d4c:8"]]
- 0088eefc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088eefc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088eefc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088eefc ["COPY", "tmp:0:8", ["const:dd7:8"]]
+ 0088eefc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088eefc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088eefc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088eefc bytes 29313591
+ 0088eefc bytes 295d3791
- 0088ef7c ["COPY", "tmp:0:8", ["const:909:8"]]
- 0088ef7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088ef7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088ef7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088ef7c ["COPY", "tmp:0:8", ["const:994:8"]]
+ 0088ef7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088ef7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088ef7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088ef7c bytes 29252491
+ 0088ef7c bytes 29512691
- 0088efb0 ["COPY", "tmp:0:8", ["const:38f:8"]]
- 0088efb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088efb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088efb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088efb0 ["COPY", "tmp:0:8", ["const:38d:8"]]
+ 0088efb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088efb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088efb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088efb0 bytes 293d0e91
+ 0088efb0 bytes 29350e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dfa62c45a60f078d05181f2d6971004"></a>

### [`00890a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890a30.md) → [`00890a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890a30.md) FUN_00890a30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) [`00897400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897400.md) [`00897c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897c24.md) [`0089b4ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b4ec.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449290.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`004752f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004752f8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 4件 [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) [`00897c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897c24.md) [`0089b4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b4ec.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449290.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`004752f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004752f8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00890bc0",
      "incomplete_value": false,
      "site": "00890bc0",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00890bc0",
      "incomplete_value": false,
      "site": "00890bc0",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00890c44",
      "incomplete_value": false,
      "site": "00890c44",
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
      "definition_site": "00890c44",
      "incomplete_value": false,
      "site": "00890c44",
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
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00890c48",
      "incomplete_value": false,
      "site": "00890c48",
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
      "definition_site": "00890c48",
      "incomplete_value": false,
      "site": "00890c48",
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
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00890a5c",
      "READ",
      [
        "storage",
        "00c246d0",
        null,
        "undefined4"
      ]
    ],
    [
      "00890bc0",
      "WRITE",
      [
        "storage",
        "00c246d0",
        null,
        "undefined4"
      ]
    ],
    [
      "00890bcc",
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
      "00890a5c",
      "READ",
      [
        "storage",
        "00c24720",
        null,
        "undefined4"
      ]
    ],
    [
      "00890bc0",
      "WRITE",
      [
        "storage",
        "00c24720",
        null,
        "undefined4"
      ]
    ],
    [
      "00890bcc",
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

- 旧版 [`00890bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890a30.md#insn-00890bc0) · [`00890a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890a30.md#insn-00890a5c) · [`00890bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890a30.md#insn-00890bc8)
- 新版 [`00890bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890a30.md#insn-00890bc0) · [`00890a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890a30.md#insn-00890a5c) · [`00890bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890a30.md#insn-00890bc8)

~~~diff
- 00890bc0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d0:8"]]
- 00890bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00890bc0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:720:8"]]
+ 00890bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00890bc0 bytes 28d106b9
+ 00890bc0 bytes 282107b9
- 00890a5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d0:8"]]
- 00890a5c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00890a5c ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 00890a5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:720:8"]]
+ 00890a5c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00890a5c ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 00890a5c bytes 29d146b9
+ 00890a5c bytes 292147b9
- 00890bc8 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00890bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00890bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00890bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00890bc8 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00890bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00890bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00890bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00890bc8 bytes 08e10091
+ 00890bc8 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-365752efe1ec2180a24e5254d03f5559"></a>

### [`00890c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890c70.md) → [`00890c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890c70.md) FUN_00890c70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00890a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890a30.md) [`008b7948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7948.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0060dcac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060dcac.md)
- 新版 呼出元 2件 [`00890a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890a30.md) [`008b7948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7948.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0060dcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.28% / 新版 92.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00890e90",
      "incomplete_value": true,
      "site": "00890e90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00890e90",
      "incomplete_value": true,
      "site": "00890e90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b8:8"
              ]
            ]
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
      "definition_site": "00890e94",
      "incomplete_value": true,
      "site": "00890e94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00890e94",
      "incomplete_value": true,
      "site": "00890e94",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008912f4",
      "incomplete_value": false,
      "site": "008912f4",
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
      "definition_site": "008912f4",
      "incomplete_value": false,
      "site": "008912f4",
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
      "00890da0",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00890db4",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00890db4",
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
      "00890da0",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00890db4",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "00890db4",
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

- 旧版 [`00890d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890c70.md#insn-00890d9c) · [`00890db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890c70.md#insn-00890db0) · [`00890db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890c70.md#insn-00890db4)
- 新版 [`00890d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890c70.md#insn-00890d9c) · [`00890db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890c70.md#insn-00890db0) · [`00890db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890c70.md#insn-00890db4)

~~~diff
- 00890d9c ["COPY", "tmp:0:8", ["const:38:8"]]
- 00890d9c ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00890d9c ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00890d9c ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00890d9c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00890d9c ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00890d9c ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00890d9c ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00890d9c bytes 39e30091
+ 00890d9c bytes 39e30191
- 00890db0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00890db0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00890db0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00890db0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00890db0 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00890db0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00890db0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00890db0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00890db0 bytes 94020091
+ 00890db0 bytes 94020191
- 00890db4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 00890db4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00890db4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 00890db4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00890db4 bytes 423047f9
+ 00890db4 bytes 425847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f368b2cf3dee5ffe2656beac6bacdc55"></a>

### [`00891558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00891/00891558.md) → [`00891558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md) FUN_00891558

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0081c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081c/0081c6a0.md) [`00891554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00891/00891554.md) [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 30件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`006ae0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae0f8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 4件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`00891554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891554.md) [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 30件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`006ae0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae0f8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.09% / 新版 98.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00891748",
      "incomplete_value": false,
      "site": "00891750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00891748",
      "incomplete_value": false,
      "site": "00891750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:d40:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00891b78",
      "incomplete_value": false,
      "site": "00891b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00891b78",
      "incomplete_value": false,
      "site": "00891b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00891da4",
      "incomplete_value": false,
      "site": "00891da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00891da4",
      "incomplete_value": false,
      "site": "00891da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "ordinal": 80,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00891590",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0089159c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008915a4",
      "PARAM",
      [
        "storage",
        "00c05b18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00891590",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0089159c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008915a4",
      "PARAM",
      [
        "storage",
        "00c05b68",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00891590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00891/00891558.md#insn-00891590) · [`0089159c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00891/00891558.md#insn-0089159c) · [`008915a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00891/00891558.md#insn-008915a4)
- 新版 [`00891590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md#insn-00891590) · [`0089159c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md#insn-0089159c) · [`008915a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md#insn-008915a4)

~~~diff
- 00891590 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00891590 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00891590 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00891590 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00891590 bytes 083d45f9
+ 00891590 bytes 085d45f9
- 0089159c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0089159c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0089159c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0089159c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0089159c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0089159c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0089159c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0089159c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0089159c bytes 21203991
+ 0089159c bytes 21603a91
- 008915a4 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 008915a4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008915a4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008915a4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008915a4 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 008915a4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008915a4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008915a4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008915a4 bytes 42602c91
+ 008915a4 bytes 42a02d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b066d80280c2ac01fe54f396512384e6"></a>

### [`008920f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00892/008920f8.md) → [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) FUN_008920f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00897400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897400.md) · 呼出先 64件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)
- 新版 呼出元 1件 [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) · 呼出先 64件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.60% / 新版 97.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 14件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00892220",
      "incomplete_value": true,
      "site": "00892238",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e5f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892220",
      "incomplete_value": true,
      "site": "00892238",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dc5:8"
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
      "definition_site": "0089223c",
      "incomplete_value": true,
      "site": "0089223c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0089223c",
      "incomplete_value": true,
      "site": "0089223c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892258",
      "incomplete_value": false,
      "site": "00892258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892258",
      "incomplete_value": false,
      "site": "00892258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "00892220",
      "READ",
      [
        "storage",
        "002a6dc5",
        null,
        "string"
      ]
    ],
    [
      "00892228",
      "READ",
      [
        "storage",
        "002a6dd2",
        null,
        "string"
      ]
    ],
    [
      "00892258",
      "DATA",
      [
        "storage",
        "00c05f10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892220",
      "READ",
      [
        "storage",
        "002a6e5f",
        null,
        "string"
      ]
    ],
    [
      "00892228",
      "READ",
      [
        "storage",
        "002a6e6c",
        null,
        "string"
      ]
    ],
    [
      "00892258",
      "DATA",
      [
        "storage",
        "00c05f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089221c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00892/008920f8.md#insn-0089221c) · [`00892250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00892/008920f8.md#insn-00892250) · [`00892520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00892/008920f8.md#insn-00892520)
- 新版 [`0089221c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md#insn-0089221c) · [`00892250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md#insn-00892250) · [`00892520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md#insn-00892520)

~~~diff
- 0089221c ["COPY", "tmp:0:8", ["const:dc5:8"]]
- 0089221c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0089221c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0089221c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0089221c ["COPY", "tmp:0:8", ["const:e5f:8"]]
+ 0089221c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0089221c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0089221c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0089221c bytes 29153791
+ 0089221c bytes 297d3991
- 00892250 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 00892250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00892250 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00892250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00892250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00892250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892250 bytes 08413c91
+ 00892250 bytes 08813d91
- 00892520 ["COPY", "tmp:0:8", ["const:21d:8"]]
- 00892520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00892520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00892520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00892520 ["COPY", "tmp:0:8", ["const:190:8"]]
+ 00892520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00892520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00892520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00892520 bytes 29750891
+ 00892520 bytes 29410691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5627987e83efdca242095d2fdc5ebf3"></a>

### [`008959c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/008959c8.md) → [`008959c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md) FUN_008959c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00897610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897610.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00446784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446784.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00897610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897610.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`00446784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446784.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008959f0",
      "incomplete_value": true,
      "site": "008959f0",
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
      "definition_site": "008959f0",
      "incomplete_value": true,
      "site": "008959f0",
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
      "008959ec",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008959f8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00895a00",
      "PARAM",
      [
        "storage",
        "00c05b18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008959ec",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008959f8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00895a00",
      "PARAM",
      [
        "storage",
        "00c05b68",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008959ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/008959c8.md#insn-008959ec) · [`008959f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/008959c8.md#insn-008959f8) · [`00895a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/008959c8.md#insn-00895a00)
- 新版 [`008959ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md#insn-008959ec) · [`008959f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md#insn-008959f8) · [`00895a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md#insn-00895a00)

~~~diff
- 008959ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008959ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008959ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008959ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008959ec bytes 083d45f9
+ 008959ec bytes 085d45f9
- 008959f8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008959f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008959f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008959f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008959f8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008959f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008959f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008959f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008959f8 bytes 21203991
+ 008959f8 bytes 21603a91
- 00895a00 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 00895a00 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00895a00 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00895a00 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00895a00 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00895a00 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00895a00 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00895a00 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00895a00 bytes 42602c91
+ 00895a00 bytes 42a02d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41e11074e15023961333e2d1a820920b"></a>

### [`00895e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/00895e64.md) → [`00895e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895e64.md) FUN_00895e64

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008959c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/008959c8.md) [`008b89f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b89f8.md) · 呼出先 14件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d90.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446784.md)
- 新版 呼出元 2件 [`008959c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md) [`008b89f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b89f8.md) · 呼出先 14件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d90.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446784.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.88% / 新版 98.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00895e9c",
      "incomplete_value": true,
      "site": "00895e9c",
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
      "definition_site": "00895e9c",
      "incomplete_value": true,
      "site": "00895e9c",
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
      "definition_site": "00895ea4",
      "incomplete_value": false,
      "site": "00895eb8",
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
      "definition_site": "00895ea4",
      "incomplete_value": false,
      "site": "00895eb8",
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
      "definition_site": "00895eac",
      "incomplete_value": false,
      "site": "00895eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00895eac",
      "incomplete_value": false,
      "site": "00895eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "00895e90",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00895ea4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00895eac",
      "PARAM",
      [
        "storage",
        "00c05b18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00895e90",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00895ea4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00895eac",
      "PARAM",
      [
        "storage",
        "00c05b68",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00895e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/00895e64.md#insn-00895e90) · [`00895ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/00895e64.md#insn-00895ea4) · [`00895eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/00895e64.md#insn-00895eac)
- 新版 [`00895e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895e64.md#insn-00895e90) · [`00895ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895e64.md#insn-00895ea4) · [`00895eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895e64.md#insn-00895eac)

~~~diff
- 00895e90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00895e90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00895e90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00895e90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00895e90 bytes 083d45f9
+ 00895e90 bytes 085d45f9
- 00895ea4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00895ea4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00895ea4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00895ea4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00895ea4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00895ea4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00895ea4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00895ea4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00895ea4 bytes 21203991
+ 00895ea4 bytes 21603a91
- 00895eac ["COPY", "tmp:0:8", ["const:b18:8"]]
- 00895eac ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00895eac ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00895eac ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00895eac ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00895eac ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00895eac ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00895eac ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00895eac bytes 42602c91
+ 00895eac bytes 42a02d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dbe705185a5b9b1e33f55bbab4f86a6"></a>

### [`008963f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/008963f8.md) → [`008963f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/008963f8.md) FUN_008963f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00abe18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abe/00abe18c.md) · 呼出先 17件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md)
- 新版 呼出元 1件 [`00abe1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abe/00abe1d0.md) · 呼出先 17件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.86% / 新版 93.86%

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
      "definition_site": "00896438",
      "incomplete_value": false,
      "site": "0089643c",
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
      "definition_site": "00896438",
      "incomplete_value": false,
      "site": "0089643c",
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
      "definition_site": "00896494",
      "incomplete_value": true,
      "site": "008964a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00896494",
      "incomplete_value": true,
      "site": "008964a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9dd:8"
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
      "definition_site": "0089668c",
      "incomplete_value": true,
      "site": "00896690",
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
      "definition_site": "0089668c",
      "incomplete_value": true,
      "site": "00896690",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0089643c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00896494",
      "READ",
      [
        "storage",
        "0029d9dd",
        null,
        "string"
      ]
    ],
    [
      "0089667c",
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
      "0089643c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00896494",
      "READ",
      [
        "storage",
        "0029da68",
        null,
        "string"
      ]
    ],
    [
      "0089667c",
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

- 旧版 [`00896438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/008963f8.md#insn-00896438) · [`0089648c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/008963f8.md#insn-0089648c) · [`0089667c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/008963f8.md#insn-0089667c)
- 新版 [`00896438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/008963f8.md#insn-00896438) · [`0089648c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/008963f8.md#insn-0089648c) · [`0089667c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/008963f8.md#insn-0089667c)

~~~diff
- 00896438 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00896438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00896438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00896438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00896438 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00896438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00896438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00896438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00896438 bytes 08a13491
+ 00896438 bytes 08e13591
- 0089648c ["COPY", "tmp:0:8", ["const:9dd:8"]]
- 0089648c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0089648c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0089648c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0089648c ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 0089648c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0089648c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0089648c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0089648c bytes 29752791
+ 0089648c bytes 29a12991
- 0089667c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0089667c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0089667c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0089667c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0089667c bytes 08b946f9
+ 0089667c bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5180216423a4897e6b9781301bef2b36"></a>

### [`00896810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896810.md) → [`00896810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896810.md) FUN_00896810

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00abe18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abe/00abe18c.md) · 呼出先 16件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00abe1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abe/00abe1d0.md) · 呼出先 16件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.58% / 新版 93.58%

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
      "definition_site": "00896850",
      "incomplete_value": false,
      "site": "00896854",
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
      "definition_site": "00896850",
      "incomplete_value": false,
      "site": "00896854",
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
      "definition_site": "008968ac",
      "incomplete_value": true,
      "site": "008968c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008968ac",
      "incomplete_value": true,
      "site": "008968c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ac:8"
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
      "definition_site": "00896a7c",
      "incomplete_value": true,
      "site": "00896a80",
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
      "definition_site": "00896a7c",
      "incomplete_value": true,
      "site": "00896a80",
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
      "00896854",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008968ac",
      "READ",
      [
        "storage",
        "002950ac",
        null,
        "string"
      ]
    ],
    [
      "00896a6c",
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
      "00896854",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "008968ac",
      "READ",
      [
        "storage",
        "0029501f",
        null,
        "string"
      ]
    ],
    [
      "00896a6c",
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

- 旧版 [`00896850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896810.md#insn-00896850) · [`008968a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896810.md#insn-008968a4) · [`00896a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896810.md#insn-00896a6c)
- 新版 [`00896850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896810.md#insn-00896850) · [`008968a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896810.md#insn-008968a4) · [`00896a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896810.md#insn-00896a6c)

~~~diff
- 00896850 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00896850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00896850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00896850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00896850 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00896850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00896850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00896850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00896850 bytes 08a13491
+ 00896850 bytes 08e13591
- 008968a4 ["COPY", "tmp:0:8", ["const:ac:8"]]
- 008968a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008968a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008968a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008968a4 ["COPY", "tmp:0:8", ["const:1f:8"]]
+ 008968a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008968a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008968a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008968a4 bytes 29b10291
+ 008968a4 bytes 297d0091
- 00896a6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 00896a6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00896a6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00896a6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00896a6c bytes 08b946f9
+ 00896a6c bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-061f357c3377b96a1aa51d5c0edab1b1"></a>

### [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) → [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) FUN_00896c7c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 37件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 37件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00646dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646dc4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.12% / 新版 88.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 13件, `store_destination` 10件, `store_value` 10件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00896cc0",
      "incomplete_value": false,
      "site": "00896cc0",
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
      "definition_site": "00896cc0",
      "incomplete_value": false,
      "site": "00896cc0",
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
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00896cb8",
      "incomplete_value": true,
      "site": "00896cc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00896cb8",
      "incomplete_value": true,
      "site": "00896cc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00896cc4",
      "incomplete_value": false,
      "site": "00896cc4",
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
      "definition_site": "00896cc4",
      "incomplete_value": false,
      "site": "00896cc4",
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
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00896cb8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00896cbc",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00896cc0",
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
      "00896cb8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00896cbc",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00896cc0",
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

- 旧版 [`00896cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md#insn-00896cc0) · [`00896cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md#insn-00896cc4) · [`00896ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md#insn-00896ce0)
- 新版 [`00896cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md#insn-00896cc0) · [`00896cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md#insn-00896cc4) · [`00896ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md#insn-00896ce0)

~~~diff
- 00896cc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00896cc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00896cc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 00896cc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00896cc0 bytes 093505f9
+ 00896cc0 bytes 095505f9
- 00896cc4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 00896cc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00896cc4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 00896cc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00896cc4 bytes ca3e05f9
+ 00896cc4 bytes ca5e05f9
- 00896ce0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 00896ce0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00896ce0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 00896ce0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00896ce0 bytes d53e05f9
+ 00896ce0 bytes d55e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c51afa51703b78e6d2062b00f99bfbc1"></a>

### [`00897610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897610.md) → [`00897610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897610.md) FUN_00897610

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 18件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 18件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0089763c",
      "incomplete_value": true,
      "site": "0089763c",
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
      "definition_site": "0089763c",
      "incomplete_value": true,
      "site": "0089763c",
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
      "definition_site": "00897644",
      "incomplete_value": false,
      "site": "00897654",
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
      "definition_site": "00897644",
      "incomplete_value": false,
      "site": "00897654",
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
      "definition_site": "0089764c",
      "incomplete_value": false,
      "site": "00897654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089764c",
      "incomplete_value": false,
      "site": "00897654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "00897630",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00897644",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0089764c",
      "PARAM",
      [
        "storage",
        "00c05b18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00897630",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00897644",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0089764c",
      "PARAM",
      [
        "storage",
        "00c05b68",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00897630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897610.md#insn-00897630) · [`00897644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897610.md#insn-00897644) · [`0089764c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897610.md#insn-0089764c)
- 新版 [`00897630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897610.md#insn-00897630) · [`00897644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897610.md#insn-00897644) · [`0089764c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897610.md#insn-0089764c)

~~~diff
- 00897630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00897630 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00897630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00897630 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00897630 bytes 003d45f9
+ 00897630 bytes 005d45f9
- 00897644 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00897644 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00897644 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00897644 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00897644 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00897644 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00897644 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00897644 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00897644 bytes 21203991
+ 00897644 bytes 21603a91
- 0089764c ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0089764c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0089764c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0089764c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0089764c ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0089764c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0089764c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0089764c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0089764c bytes 42602c91
+ 0089764c bytes 42a02d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05cb5385b2a35929e9f75b542114d36e"></a>

### [`008977b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/008977b8.md) → [`008977b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/008977b8.md) FUN_008977b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0089787c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/0089787c.md) · 呼出先 5件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`0068be5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068b/0068be5c.md) [`00763798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763798.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0089787c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/0089787c.md) · 呼出先 5件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`0068be5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068b/0068be5c.md) [`00763798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763798.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.80% / 新版 89.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008977fc",
      "incomplete_value": false,
      "site": "00897800",
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
      "definition_site": "008977fc",
      "incomplete_value": false,
      "site": "00897800",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00897838",
      "incomplete_value": false,
      "site": "0089783c",
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
      "definition_site": "00897838",
      "incomplete_value": false,
      "site": "0089783c",
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
      "008977d0",
      "DATA",
      [
        "storage",
        "00c05b08",
        null,
        "pointer"
      ]
    ],
    [
      "00897800",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "0089783c",
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
      "008977d0",
      "DATA",
      [
        "storage",
        "00c05b58",
        null,
        "pointer"
      ]
    ],
    [
      "00897800",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "0089783c",
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

- 旧版 [`008977c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/008977b8.md#insn-008977c8) · [`008977fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/008977b8.md#insn-008977fc) · [`00897838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/008977b8.md#insn-00897838)
- 新版 [`008977c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/008977b8.md#insn-008977c8) · [`008977fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/008977b8.md#insn-008977fc) · [`00897838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/008977b8.md#insn-00897838)

~~~diff
- 008977c8 ["COPY", "tmp:0:8", ["const:b08:8"]]
- 008977c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008977c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008977c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008977c8 ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 008977c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008977c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008977c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008977c8 bytes 08212c91
+ 008977c8 bytes 08612d91
- 008977fc ["COPY", "tmp:0:8", ["const:db8:8"]]
- 008977fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008977fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008977fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008977fc ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 008977fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008977fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008977fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008977fc bytes 08e13691
+ 008977fc bytes 08213891
- 00897838 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00897838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00897838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00897838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00897838 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00897838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00897838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00897838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00897838 bytes 08610a91
+ 00897838 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1d5aa87dead65132e2457546b0b1faa"></a>

### [`008978a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/008978a4.md) → [`008978a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/008978a4.md) FUN_008978a4

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
      "definition_site": "008978c4",
      "incomplete_value": false,
      "site": "008978c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008978c4",
      "incomplete_value": false,
      "site": "008978c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "008978c8",
      "DATA",
      [
        "storage",
        "00c05b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008978c8",
      "DATA",
      [
        "storage",
        "00c05b90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008978c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/008978a4.md#insn-008978c4)
- 新版 [`008978c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/008978a4.md#insn-008978c4)

~~~diff
- 008978c4 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 008978c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008978c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008978c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008978c4 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 008978c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008978c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008978c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008978c4 bytes 08012d91
+ 008978c4 bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e586db74d6ba47a7f42315c98827cc8d"></a>

### [`008978dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/008978dc.md) → [`008978dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/008978dc.md) FUN_008978dc

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
      "definition_site": "008978e0",
      "incomplete_value": false,
      "site": "008978e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008978e0",
      "incomplete_value": false,
      "site": "008978e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "008978e4",
      "DATA",
      [
        "storage",
        "00c05b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008978e4",
      "DATA",
      [
        "storage",
        "00c05b90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008978e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/008978dc.md#insn-008978e0)
- 新版 [`008978e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/008978dc.md#insn-008978e0)

~~~diff
- 008978e0 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 008978e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008978e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008978e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008978e0 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 008978e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008978e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008978e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008978e0 bytes 08012d91
+ 008978e0 bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be4e172d139730caf5903b5fbda5ce49"></a>

### [`00897bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897bbc.md) → [`00897bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897bbc.md) FUN_00897bbc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0088a82c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088a/0088a82c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0088a82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088a/0088a82c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00897bc8",
      "incomplete_value": false,
      "site": "00897bcc",
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
      "definition_site": "00897bc8",
      "incomplete_value": false,
      "site": "00897bcc",
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
      "00897bc8",
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
      "00897bc8",
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

- 旧版 [`00897bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897bbc.md#insn-00897bc8)
- 新版 [`00897bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897bbc.md#insn-00897bc8)

~~~diff
- 00897bc8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00897bc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00897bc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00897bc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00897bc8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00897bc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00897bc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00897bc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00897bc8 bytes 000c0c91
+ 00897bc8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22514a0f37a9500fc6e8ccf058f37ba5"></a>

### [`00897bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897bd4.md) → [`00897bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897bd4.md) FUN_00897bd4

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
      "definition_site": "00897bf8",
      "incomplete_value": false,
      "site": "00897bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00897bf8",
      "incomplete_value": false,
      "site": "00897bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00897bf8",
      "DATA",
      [
        "storage",
        "00c05bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00897bf8",
      "DATA",
      [
        "storage",
        "00c05c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00897bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897bd4.md#insn-00897bf4)
- 新版 [`00897bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897bd4.md#insn-00897bf4)

~~~diff
- 00897bf4 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00897bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00897bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00897bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00897bf4 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00897bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00897bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00897bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00897bf4 bytes 08012f91
+ 00897bf4 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6be040699587c6a59a4da9356f495338"></a>

### [`00897c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897c08.md) → [`00897c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897c08.md) FUN_00897c08

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
      "definition_site": "00897c14",
      "incomplete_value": false,
      "site": "00897c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00897c14",
      "incomplete_value": false,
      "site": "00897c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00897c14",
      "DATA",
      [
        "storage",
        "00c05bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00897c14",
      "DATA",
      [
        "storage",
        "00c05c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00897c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897c08.md#insn-00897c10)
- 新版 [`00897c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897c08.md#insn-00897c10)

~~~diff
- 00897c10 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00897c10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00897c10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00897c10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00897c10 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00897c10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00897c10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00897c10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00897c10 bytes 29012f91
+ 00897c10 bytes 29413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253025991592ac687ae0f67665108dfd"></a>

### [`00897f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897f00.md) → [`00897f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897f00.md) FUN_00897f00

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
      "definition_site": "00897f24",
      "incomplete_value": false,
      "site": "00897f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00897f24",
      "incomplete_value": false,
      "site": "00897f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00897f24",
      "DATA",
      [
        "storage",
        "00c05c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00897f24",
      "DATA",
      [
        "storage",
        "00c05c90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00897f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897f00.md#insn-00897f20)
- 新版 [`00897f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897f00.md#insn-00897f20)

~~~diff
- 00897f20 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00897f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00897f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00897f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00897f20 ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 00897f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00897f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00897f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00897f20 bytes 08013191
+ 00897f20 bytes 08413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb832310abfed90e4913fa1065069d51"></a>

### [`00897f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897f34.md) → [`00897f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897f34.md) FUN_00897f34

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
      "definition_site": "00897f40",
      "incomplete_value": false,
      "site": "00897f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00897f40",
      "incomplete_value": false,
      "site": "00897f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00897f40",
      "DATA",
      [
        "storage",
        "00c05c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00897f40",
      "DATA",
      [
        "storage",
        "00c05c90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00897f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897f34.md#insn-00897f3c)
- 新版 [`00897f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897f34.md#insn-00897f3c)

~~~diff
- 00897f3c ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00897f3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00897f3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00897f3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00897f3c ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 00897f3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00897f3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00897f3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00897f3c bytes 29013191
+ 00897f3c bytes 29413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45aa04107f370ec841ffc7e220c31786"></a>

### [`00898378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/00898378.md) → [`00898378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898378.md) FUN_00898378

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
      "definition_site": "0089839c",
      "incomplete_value": false,
      "site": "0089839c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089839c",
      "incomplete_value": false,
      "site": "0089839c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "0089839c",
      "DATA",
      [
        "storage",
        "00c05cc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089839c",
      "DATA",
      [
        "storage",
        "00c05d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00898398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/00898378.md#insn-00898398)
- 新版 [`00898398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898378.md#insn-00898398)

~~~diff
- 00898398 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 00898398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00898398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00898398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00898398 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00898398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00898398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00898398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00898398 bytes 08013391
+ 00898398 bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2009810176bb33cc466484c9237e37d6"></a>

### [`008983ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/008983ac.md) → [`008983ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/008983ac.md) FUN_008983ac

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
      "definition_site": "008983b8",
      "incomplete_value": false,
      "site": "008983b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008983b8",
      "incomplete_value": false,
      "site": "008983b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "008983b8",
      "DATA",
      [
        "storage",
        "00c05cc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008983b8",
      "DATA",
      [
        "storage",
        "00c05d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008983b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/008983ac.md#insn-008983b4)
- 新版 [`008983b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/008983ac.md#insn-008983b4)

~~~diff
- 008983b4 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 008983b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008983b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008983b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008983b4 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 008983b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008983b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008983b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008983b4 bytes 29013391
+ 008983b4 bytes 29413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ddd34dc42611ad20a432719b3443f7b"></a>

### [`00898444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/00898444.md) → [`00898444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898444.md) FUN_00898444

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
      "definition_site": "00898448",
      "incomplete_value": false,
      "site": "0089844c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00898448",
      "incomplete_value": false,
      "site": "0089844c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "0089844c",
      "DATA",
      [
        "storage",
        "00c05d40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0089844c",
      "DATA",
      [
        "storage",
        "00c05d90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00898448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/00898444.md#insn-00898448)
- 新版 [`00898448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898444.md#insn-00898448)

~~~diff
- 00898448 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 00898448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00898448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00898448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00898448 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00898448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00898448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00898448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00898448 bytes 08013591
+ 00898448 bytes 08413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67030debbf6d1f26b3a1b6d4a9961d88"></a>

### [`00898454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/00898454.md) → [`00898454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898454.md) FUN_00898454

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
      "definition_site": "00898464",
      "incomplete_value": false,
      "site": "0089846c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00898464",
      "incomplete_value": false,
      "site": "0089846c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "0089846c",
      "DATA",
      [
        "storage",
        "00c05d40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0089846c",
      "DATA",
      [
        "storage",
        "00c05d90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00898464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/00898454.md#insn-00898464)
- 新版 [`00898464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898454.md#insn-00898464)

~~~diff
- 00898464 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 00898464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00898464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00898464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00898464 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00898464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00898464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00898464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00898464 bytes 08013591
+ 00898464 bytes 08413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50e734245b346bbdbd55beabacd0aa17"></a>

### [`008985cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/008985cc.md) → [`008985cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/008985cc.md) FUN_008985cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0089848c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/0089848c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0089848c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/0089848c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "008985d8",
      "incomplete_value": false,
      "site": "008985dc",
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
      "definition_site": "008985d8",
      "incomplete_value": false,
      "site": "008985dc",
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
      "008985d8",
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
      "008985d8",
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

- 旧版 [`008985d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00898/008985cc.md#insn-008985d8)
- 新版 [`008985d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/008985cc.md#insn-008985d8)

~~~diff
- 008985d8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 008985d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008985d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008985d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008985d8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 008985d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008985d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008985d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008985d8 bytes 000c0c91
+ 008985d8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1ae320e58bb20715372a51d669a9494"></a>

### [`0089b3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b3c0.md) → [`0089b3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b3c0.md) FUN_0089b3c0

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
      "definition_site": "0089b3e4",
      "incomplete_value": false,
      "site": "0089b3e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089b3e4",
      "incomplete_value": false,
      "site": "0089b3e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "0089b3e4",
      "DATA",
      [
        "storage",
        "00c05d90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089b3e4",
      "DATA",
      [
        "storage",
        "00c05de0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089b3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b3c0.md#insn-0089b3e0)
- 新版 [`0089b3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b3c0.md#insn-0089b3e0)

~~~diff
- 0089b3e0 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 0089b3e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0089b3e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0089b3e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0089b3e0 ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 0089b3e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0089b3e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0089b3e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0089b3e0 bytes 08413691
+ 0089b3e0 bytes 08813791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3629b239672a85d56f977f0d7a1159aa"></a>

### [`0089b3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b3f4.md) → [`0089b3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b3f4.md) FUN_0089b3f4

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
      "definition_site": "0089b400",
      "incomplete_value": false,
      "site": "0089b400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089b400",
      "incomplete_value": false,
      "site": "0089b400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "0089b400",
      "DATA",
      [
        "storage",
        "00c05d90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089b400",
      "DATA",
      [
        "storage",
        "00c05de0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089b3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b3f4.md#insn-0089b3fc)
- 新版 [`0089b3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b3f4.md#insn-0089b3fc)

~~~diff
- 0089b3fc ["COPY", "tmp:0:8", ["const:d90:8"]]
- 0089b3fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0089b3fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0089b3fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0089b3fc ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 0089b3fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0089b3fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0089b3fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0089b3fc bytes 29413691
+ 0089b3fc bytes 29813791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbfa4e6d8b1ec102c8c96435d382bd9a"></a>

### [`0089b49c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b49c.md) → [`0089b49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b49c.md) FUN_0089b49c

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
      "definition_site": "0089b4c0",
      "incomplete_value": false,
      "site": "0089b4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089b4c0",
      "incomplete_value": false,
      "site": "0089b4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "0089b4c0",
      "DATA",
      [
        "storage",
        "00c05e10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089b4c0",
      "DATA",
      [
        "storage",
        "00c05e60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089b4bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b49c.md#insn-0089b4bc)
- 新版 [`0089b4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b49c.md#insn-0089b4bc)

~~~diff
- 0089b4bc ["COPY", "tmp:0:8", ["const:e10:8"]]
- 0089b4bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0089b4bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0089b4bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0089b4bc ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0089b4bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0089b4bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0089b4bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0089b4bc bytes 08413891
+ 0089b4bc bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21635f249b84bf52bff42749c2fce3c9"></a>

### [`0089b4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b4d0.md) → [`0089b4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b4d0.md) FUN_0089b4d0

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
      "definition_site": "0089b4dc",
      "incomplete_value": false,
      "site": "0089b4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089b4dc",
      "incomplete_value": false,
      "site": "0089b4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "0089b4dc",
      "DATA",
      [
        "storage",
        "00c05e10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089b4dc",
      "DATA",
      [
        "storage",
        "00c05e60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089b4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b4d0.md#insn-0089b4d8)
- 新版 [`0089b4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b4d0.md#insn-0089b4d8)

~~~diff
- 0089b4d8 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 0089b4d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0089b4d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0089b4d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0089b4d8 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0089b4d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0089b4d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0089b4d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0089b4d8 bytes 29413891
+ 0089b4d8 bytes 29813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5ac5ea24923f9f95cb1ee5889bc960c"></a>

### [`0089b68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b68c.md) → [`0089b68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b68c.md) FUN_0089b68c

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
      "definition_site": "0089b6a0",
      "incomplete_value": false,
      "site": "0089b6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089b6a0",
      "incomplete_value": false,
      "site": "0089b6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "0089b6a4",
      "DATA",
      [
        "storage",
        "00c05e90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089b6a4",
      "DATA",
      [
        "storage",
        "00c05ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089b6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b68c.md#insn-0089b6a0)
- 新版 [`0089b6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b68c.md#insn-0089b6a0)

~~~diff
- 0089b6a0 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 0089b6a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0089b6a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0089b6a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0089b6a0 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 0089b6a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0089b6a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0089b6a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0089b6a0 bytes 08413a91
+ 0089b6a0 bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fa133c5d6c9c61d1ce4fbd00196b8c9"></a>

### [`0089b6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b6b0.md) → [`0089b6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b6b0.md) FUN_0089b6b0

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
      "definition_site": "0089b6b4",
      "incomplete_value": false,
      "site": "0089b6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089b6b4",
      "incomplete_value": false,
      "site": "0089b6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "0089b6b8",
      "DATA",
      [
        "storage",
        "00c05e90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089b6b8",
      "DATA",
      [
        "storage",
        "00c05ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089b6b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b6b0.md#insn-0089b6b4)
- 新版 [`0089b6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b6b0.md#insn-0089b6b4)

~~~diff
- 0089b6b4 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 0089b6b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0089b6b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0089b6b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0089b6b4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 0089b6b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0089b6b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0089b6b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0089b6b4 bytes 08413a91
+ 0089b6b4 bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ddc12c22713c330b8371354f5b5144b"></a>

### [`0089b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b75c.md) → [`0089b75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b75c.md) FUN_0089b75c

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
      "definition_site": "0089b770",
      "incomplete_value": true,
      "site": "0089b774",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089b770",
      "incomplete_value": true,
      "site": "0089b774",
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
            "const:f10:8"
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
      "0089b774",
      "DATA",
      [
        "storage",
        "00c05f10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089b774",
      "DATA",
      [
        "storage",
        "00c05f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089b770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089b/0089b75c.md#insn-0089b770)
- 新版 [`0089b770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b75c.md#insn-0089b770)

~~~diff
- 0089b770 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 0089b770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0089b770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0089b770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0089b770 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 0089b770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0089b770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0089b770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0089b770 bytes 08413c91
+ 0089b770 bytes 08813d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

