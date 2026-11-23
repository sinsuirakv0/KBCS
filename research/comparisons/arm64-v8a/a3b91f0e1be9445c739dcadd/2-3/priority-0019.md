# v15.7.4 → v16.0.0 · 最優先の変更候補 (19)

[一覧の目次](README.md)

<a id="compare-8a9fb93e2aaa8b70fe0660975f88ef5a"></a>

### [`005698ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005698ec.md) → [`0058c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c784.md) FUN_0058c784

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574770.md) · 呼出先 6件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00558fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md)
- 新版 呼出元 1件 [`00597608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597608.md) · 呼出先 6件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.16% / 新版 94.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058c8dc",
      "incomplete_value": true,
      "site": "0058c8dc",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569a44",
      "incomplete_value": true,
      "site": "00569a44",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0058c7c8",
      "incomplete_value": true,
      "site": "0058c7c8",
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
      "definition_site": "00569930",
      "incomplete_value": true,
      "site": "00569930",
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
      "definition_site": "0058c8d8",
      "incomplete_value": true,
      "site": "0058c8d8",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "00569a40",
      "incomplete_value": true,
      "site": "00569a40",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058c7b4",
      "PARAM",
      [
        "storage",
        "00c264f0",
        null,
        null
      ]
    ],
    [
      "0058c7c4",
      "READ",
      [
        "storage",
        "00c264e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c81c",
      "READ",
      [
        "storage",
        "00c26530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c7b4",
      "PARAM",
      [
        "storage",
        "00ca5fb0",
        null,
        null
      ]
    ],
    [
      "0058c7c4",
      "READ",
      [
        "storage",
        "00ca5fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c81c",
      "READ",
      [
        "storage",
        "00ca5ff0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005698ec.md#insn-00569920) · [`00569a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005698ec.md#insn-00569a44) · [`00569a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005698ec.md#insn-00569a9c)
- 新版 `0058c7b8`（命令位置の公開資料なし） · `0058c8dc`（命令位置の公開資料なし） · `0058c934`（命令位置の公開資料なし）

~~~diff
- 00569920 ["INT_ADD", "register:40f0:8", ["const:569920:8", "const:4:8"]]
- 00569920 ["CALL", null, ["callee:00c57ce0:8"]]
+ 0058c7b8 ["INT_ADD", "register:40f0:8", ["const:58c7b8:8", "const:4:8"]]
+ 0058c7b8 ["CALL", null, ["callee:00c57ce0:8"]]
- 00569920 bytes 5cc61994
+ 0058c7b8 bytes 4a2d1b94
- 00569a44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4d8:8"]]
- 00569a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0058c8dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f98:8"]]
+ 0058c8dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00569a44 bytes 286d02f9
+ 0058c8dc bytes 28cd07f9
- 00569a9c ["INT_ADD", "register:40f0:8", ["const:569a9c:8", "const:4:8"]]
- 00569a9c ["CALL", null, ["callee:00c57cf0:8"]]
+ 0058c934 ["INT_ADD", "register:40f0:8", ["const:58c934:8", "const:4:8"]]
+ 0058c934 ["CALL", null, ["callee:00c57cf0:8"]]
- 00569a9c bytes 01c61994
+ 0058c934 bytes ef2c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d0600e3fd1a0330cc507e5b35d8b0be"></a>

### [`00569b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569b74.md) → [`0058ca0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058ca0c.md) FUN_0058ca0c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574774.md) · 呼出先 13件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0059760c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059760c.md) · 呼出先 13件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ca60",
      "incomplete_value": true,
      "site": "0058ca60",
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
                "const:71c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569bc8",
      "incomplete_value": true,
      "site": "00569bc8",
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
                "const:296000:8"
              ],
              [
                "leaf",
                "const:be7:8"
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
      "definition_site": "0058ca74",
      "incomplete_value": true,
      "site": "0058ca84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569bdc",
      "incomplete_value": true,
      "site": "00569bec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8cc:8"
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
      "0058ca54",
      "READ",
      [
        "storage",
        "00296be7",
        null,
        "string"
      ]
    ],
    [
      "0058ca74",
      "READ",
      [
        "storage",
        "002918cc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058ca54",
      "READ",
      [
        "storage",
        "002a671c",
        null,
        "string"
      ]
    ],
    [
      "0058ca74",
      "READ",
      [
        "storage",
        "002a0ee5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569b74.md#insn-00569b98) · [`00569ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569b74.md#insn-00569ba0) · [`00569bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569b74.md#insn-00569bb4)
- 新版 `0058ca30`（命令位置の公開資料なし） · `0058ca38`（命令位置の公開資料なし） · `0058ca4c`（命令位置の公開資料なし）

~~~diff
- 00569b98 ["INT_ADD", "register:40f0:8", ["const:569b98:8", "const:4:8"]]
- 00569b98 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058ca30 ["INT_ADD", "register:40f0:8", ["const:58ca30:8", "const:4:8"]]
+ 0058ca30 ["CALL", null, ["callee:00588e2c:8"]]
- 00569b98 bytes fff0ff97
+ 0058ca30 bytes fff0ff97
- 00569ba0 ["INT_ADD", "register:40f0:8", ["const:569ba0:8", "const:4:8"]]
- 00569ba0 ["CALL", null, ["callee:0058911c:8"]]
+ 0058ca38 ["INT_ADD", "register:40f0:8", ["const:58ca38:8", "const:4:8"]]
+ 0058ca38 ["CALL", null, ["callee:0058911c:8"]]
- 00569ba0 bytes b9f1ff97
+ 0058ca38 bytes b9f1ff97
- 00569bb4 ["COPY", "register:4040:8", ["const:296000:8"]]
+ 0058ca4c ["COPY", "register:4040:8", ["const:2a6000:8"]]
- 00569bb4 bytes 68e9ffb0
+ 0058ca4c bytes c8e8ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-318105c3bfc4404594b68a1f61a35a9e"></a>

### [`00569dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569dd8.md) → [`0058cc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc70.md) FUN_0058cc70

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0057477c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057477c.md) · 呼出先 13件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00597614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597614.md) · 呼出先 13件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.79% / 新版 93.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ccfc",
      "incomplete_value": true,
      "site": "0058cd04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569e64",
      "incomplete_value": true,
      "site": "00569e6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8b0:8"
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
      "definition_site": "0058ccf8",
      "incomplete_value": true,
      "site": "0058cd08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5de:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569e60",
      "incomplete_value": true,
      "site": "00569e70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:570:8"
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
      "definition_site": "0058ccf8",
      "incomplete_value": true,
      "site": "0058cd08",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00569e60",
      "incomplete_value": true,
      "site": "00569e70",
      "value": [
        "LOAD",
        "16",
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
      "0058ccf8",
      "READ",
      [
        "storage",
        "0029b570",
        null,
        "string"
      ]
    ],
    [
      "0058ccf8",
      "READ",
      [
        "storage",
        "0029b580",
        null,
        "string"
      ]
    ],
    [
      "0058ccfc",
      "READ",
      [
        "storage",
        "002b18b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058ccf8",
      "READ",
      [
        "storage",
        "002ab5de",
        null,
        "string"
      ]
    ],
    [
      "0058ccf8",
      "READ",
      [
        "storage",
        "002ab5ee",
        null,
        "string"
      ]
    ],
    [
      "0058ccfc",
      "READ",
      [
        "storage",
        "002c2f40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569dd8.md#insn-00569f3c) · [`00569e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569dd8.md#insn-00569e20) · [`00569e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569dd8.md#insn-00569e28)
- 新版 `0058cdd4`（命令位置の公開資料なし） · `0058ccb8`（命令位置の公開資料なし） · `0058ccc0`（命令位置の公開資料なし）

~~~diff
- 00569f3c ["INT_ADD", "register:40f0:8", ["const:569f3c:8", "const:4:8"]]
- 00569f3c ["CALL", null, ["callee:0058f3f4:8"]]
+ 0058cdd4 ["INT_ADD", "register:40f0:8", ["const:58cdd4:8", "const:4:8"]]
+ 0058cdd4 ["CALL", null, ["callee:0058f3f4:8"]]
- 00569f3c bytes 88090094
+ 0058cdd4 bytes 88090094
- 00569e20 ["INT_ADD", "register:40f0:8", ["const:569e20:8", "const:4:8"]]
- 00569e20 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058ccb8 ["INT_ADD", "register:40f0:8", ["const:58ccb8:8", "const:4:8"]]
+ 0058ccb8 ["CALL", null, ["callee:00588e2c:8"]]
- 00569e20 bytes 5df0ff97
+ 0058ccb8 bytes 5df0ff97
- 00569e28 ["INT_ADD", "register:40f0:8", ["const:569e28:8", "const:4:8"]]
- 00569e28 ["CALL", null, ["callee:0058911c:8"]]
+ 0058ccc0 ["INT_ADD", "register:40f0:8", ["const:58ccc0:8", "const:4:8"]]
+ 0058ccc0 ["CALL", null, ["callee:0058911c:8"]]
- 00569e28 bytes 17f1ff97
+ 0058ccc0 bytes 17f1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22a36a2ef5e9cadacce54a71732f5b91"></a>

### [`0056a080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a080.md) → [`0058cf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cf18.md) FUN_0058cf18

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00574780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574780.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00597618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597618.md) · 呼出先 12件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058cf6c",
      "incomplete_value": true,
      "site": "0058cf6c",
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
                "const:20c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a0d4",
      "incomplete_value": true,
      "site": "0056a0d4",
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
                "const:bf3:8"
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
      "definition_site": "0058cf78",
      "incomplete_value": true,
      "site": "0058cf88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a0e0",
      "incomplete_value": true,
      "site": "0056a0f0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:725:8"
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
      "definition_site": "0058cf8c",
      "incomplete_value": true,
      "site": "0058cf8c",
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
      "definition_site": "0056a0f4",
      "incomplete_value": true,
      "site": "0056a0f4",
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
      "0058cf58",
      "READ",
      [
        "storage",
        "00291bf3",
        null,
        "string"
      ]
    ],
    [
      "0058cf78",
      "READ",
      [
        "storage",
        "002aa725",
        null,
        "string"
      ]
    ],
    [
      "0058cf80",
      "READ",
      [
        "storage",
        "002aa732",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058cf58",
      "READ",
      [
        "storage",
        "002a120c",
        null,
        "string"
      ]
    ],
    [
      "0058cf78",
      "READ",
      [
        "storage",
        "002bb4a1",
        null,
        "string"
      ]
    ],
    [
      "0058cf80",
      "READ",
      [
        "storage",
        "002bb4ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056a1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a080.md#insn-0056a1b0) · [`0056a0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a080.md#insn-0056a0a8) · [`0056a0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a080.md#insn-0056a0b0)
- 新版 `0058d048`（命令位置の公開資料なし） · `0058cf40`（命令位置の公開資料なし） · `0058cf48`（命令位置の公開資料なし）

~~~diff
- 0056a1b0 ["INT_ADD", "register:40f0:8", ["const:56a1b0:8", "const:4:8"]]
- 0056a1b0 ["CALL", null, ["callee:0058f3f4:8"]]
+ 0058d048 ["INT_ADD", "register:40f0:8", ["const:58d048:8", "const:4:8"]]
+ 0058d048 ["CALL", null, ["callee:0058f3f4:8"]]
- 0056a1b0 bytes eb080094
+ 0058d048 bytes eb080094
- 0056a0a8 ["INT_ADD", "register:40f0:8", ["const:56a0a8:8", "const:4:8"]]
- 0056a0a8 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058cf40 ["INT_ADD", "register:40f0:8", ["const:58cf40:8", "const:4:8"]]
+ 0058cf40 ["CALL", null, ["callee:00588e2c:8"]]
- 0056a0a8 bytes bbefff97
+ 0058cf40 bytes bbefff97
- 0056a0b0 ["INT_ADD", "register:40f0:8", ["const:56a0b0:8", "const:4:8"]]
- 0056a0b0 ["CALL", null, ["callee:0058911c:8"]]
+ 0058cf48 ["INT_ADD", "register:40f0:8", ["const:58cf48:8", "const:4:8"]]
+ 0058cf48 ["CALL", null, ["callee:0058911c:8"]]
- 0056a0b0 bytes 75f0ff97
+ 0058cf48 bytes 75f0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4a99aef1c0761465145ce43866c03ca"></a>

### [`0056a298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a298.md) → [`0058d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md) FUN_0058d130

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056bde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bde8.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566290.md)
- 新版 呼出元 1件 [`0058ec80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ec80.md) · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589128.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.97% / 新版 92.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d1ac",
      "incomplete_value": true,
      "site": "0058d1c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8ee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a314",
      "incomplete_value": true,
      "site": "0056a32c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c95:8"
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
      "definition_site": "0058d1e4",
      "incomplete_value": true,
      "site": "0058d1ec",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a34c",
      "incomplete_value": true,
      "site": "0056a354",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:510:8"
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
      "definition_site": "0058d2ec",
      "incomplete_value": true,
      "site": "0058d2ec",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:10d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a454",
      "incomplete_value": true,
      "site": "0056a454",
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
                "const:28f000:8"
              ],
              [
                "leaf",
                "const:ccd:8"
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
      "0058d16c",
      "DATA",
      [
        "storage",
        "00beff78",
        null,
        "undefined *"
      ]
    ],
    [
      "0058d1ac",
      "READ",
      [
        "storage",
        "00297c95",
        null,
        "string"
      ]
    ],
    [
      "0058d1e0",
      "READ",
      [
        "storage",
        "00291bfd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058d16c",
      "DATA",
      [
        "storage",
        "00c6cb38",
        null,
        "undefined *"
      ]
    ],
    [
      "0058d1ac",
      "READ",
      [
        "storage",
        "002a78ee",
        null,
        "string"
      ]
    ],
    [
      "0058d1e0",
      "READ",
      [
        "storage",
        "002a1216",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056a2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a298.md#insn-0056a2b8) · [`0056a2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a298.md#insn-0056a2bc) · [`0056a2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a298.md#insn-0056a2d8)
- 新版 `0058d150`（命令位置の公開資料なし） · `0058d154`（命令位置の公開資料なし） · `0058d170`（命令位置の公開資料なし）

~~~diff
- 0056a2b8 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 0058d150 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0056a2b8 bytes 293400b0
+ 0058d150 bytes e93600f0
- 0056a2bc ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0056a2bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056a2bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056a2bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058d154 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 0058d154 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058d154 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058d154 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056a2bc bytes 29e13d91
+ 0058d154 bytes 29e12c91
- 0056a2d8 ["INT_ADD", "register:40f0:8", ["const:56a2d8:8", "const:4:8"]]
- 0056a2d8 ["CALL", null, ["callee:00589128:8"]]
+ 0058d170 ["INT_ADD", "register:40f0:8", ["const:58d170:8", "const:4:8"]]
+ 0058d170 ["CALL", null, ["callee:00589128:8"]]
- 0056a2d8 bytes eeefff97
+ 0058d170 bytes eeefff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-067bec2719335e01ed081ca949300ad9"></a>

### [`0056a72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a72c.md) → [`0058d5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d5c4.md) FUN_0058d5c4

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d638",
      "incomplete_value": true,
      "site": "0058d640",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a7a0",
      "incomplete_value": true,
      "site": "0056a7a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a0:8"
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
      "definition_site": "0058d634",
      "incomplete_value": true,
      "site": "0058d644",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a79c",
      "incomplete_value": true,
      "site": "0056a7ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a64:8"
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
      "definition_site": "0058d634",
      "incomplete_value": true,
      "site": "0058d644",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056a79c",
      "incomplete_value": true,
      "site": "0056a7ac",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058d634",
      "READ",
      [
        "storage",
        "002aea64",
        null,
        "string"
      ]
    ],
    [
      "0058d634",
      "READ",
      [
        "storage",
        "002aea74",
        null,
        "string"
      ]
    ],
    [
      "0058d638",
      "READ",
      [
        "storage",
        "002b12a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058d634",
      "READ",
      [
        "storage",
        "002bff48",
        null,
        "string"
      ]
    ],
    [
      "0058d634",
      "READ",
      [
        "storage",
        "002bff58",
        null,
        "string"
      ]
    ],
    [
      "0058d638",
      "READ",
      [
        "storage",
        "002c28e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056a758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a72c.md#insn-0056a758) · [`0056a760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a72c.md#insn-0056a760) · [`0056a78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a72c.md#insn-0056a78c)
- 新版 `0058d5f0`（命令位置の公開資料なし） · `0058d5f8`（命令位置の公開資料なし） · `0058d624`（命令位置の公開資料なし）

~~~diff
- 0056a758 ["INT_ADD", "register:40f0:8", ["const:56a758:8", "const:4:8"]]
- 0056a758 ["CALL", null, ["callee:00589800:8"]]
+ 0058d5f0 ["INT_ADD", "register:40f0:8", ["const:58d5f0:8", "const:4:8"]]
+ 0058d5f0 ["CALL", null, ["callee:00589800:8"]]
- 0056a758 bytes 84f0ff97
+ 0058d5f0 bytes 84f0ff97
- 0056a760 ["INT_ADD", "register:40f0:8", ["const:56a760:8", "const:4:8"]]
- 0056a760 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058d5f8 ["INT_ADD", "register:40f0:8", ["const:58d5f8:8", "const:4:8"]]
+ 0058d5f8 ["CALL", null, ["callee:00588e2c:8"]]
- 0056a760 bytes 0deeff97
+ 0058d5f8 bytes 0deeff97
- 0056a78c ["INT_ADD", "register:40f0:8", ["const:56a78c:8", "const:4:8"]]
- 0056a78c ["CALL", null, ["callee:00c57a90:8"]]
+ 0058d624 ["INT_ADD", "register:40f0:8", ["const:58d624:8", "const:4:8"]]
+ 0058d624 ["CALL", null, ["callee:00c57a90:8"]]
- 0056a78c bytes 2dc21994
+ 0058d624 bytes 1b291b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad029445e553144a903357d062da960"></a>

### [`0056a900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a900.md) → [`0058d798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d798.md) FUN_0058d798

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d7f4",
      "incomplete_value": true,
      "site": "0058d7f4",
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
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:8de:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a95c",
      "incomplete_value": true,
      "site": "0056a95c",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:654:8"
              ]
            ]
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
      "0058d7e8",
      "READ",
      [
        "storage",
        "0029d654",
        null,
        "string"
      ]
    ],
    [
      "0058d808",
      "READ",
      [
        "storage",
        "0029f6f5",
        null,
        "string"
      ]
    ],
    [
      "0058d80c",
      "READ",
      [
        "storage",
        "0029f703",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058d7e8",
      "READ",
      [
        "storage",
        "002ad8de",
        null,
        "string"
      ]
    ],
    [
      "0058d808",
      "READ",
      [
        "storage",
        "002afb08",
        null,
        "string"
      ]
    ],
    [
      "0058d80c",
      "READ",
      [
        "storage",
        "002afb16",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056a92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a900.md#insn-0056a92c) · [`0056a934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a900.md#insn-0056a934) · [`0056a948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a900.md#insn-0056a948)
- 新版 `0058d7c4`（命令位置の公開資料なし） · `0058d7cc`（命令位置の公開資料なし） · `0058d7e0`（命令位置の公開資料なし）

~~~diff
- 0056a92c ["INT_ADD", "register:40f0:8", ["const:56a92c:8", "const:4:8"]]
- 0056a92c ["CALL", null, ["callee:00589800:8"]]
+ 0058d7c4 ["INT_ADD", "register:40f0:8", ["const:58d7c4:8", "const:4:8"]]
+ 0058d7c4 ["CALL", null, ["callee:00589800:8"]]
- 0056a92c bytes 0ff0ff97
+ 0058d7c4 bytes 0ff0ff97
- 0056a934 ["INT_ADD", "register:40f0:8", ["const:56a934:8", "const:4:8"]]
- 0056a934 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058d7cc ["INT_ADD", "register:40f0:8", ["const:58d7cc:8", "const:4:8"]]
+ 0058d7cc ["CALL", null, ["callee:00588e2c:8"]]
- 0056a934 bytes 98edff97
+ 0058d7cc bytes 98edff97
- 0056a948 ["COPY", "register:4040:8", ["const:29d000:8"]]
+ 0058d7e0 ["COPY", "register:4040:8", ["const:2ad000:8"]]
- 0056a948 bytes 88e9fff0
+ 0058d7e0 bytes 08e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3a38031e25aba001292b9c08507d109"></a>

### [`0056aad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056aad8.md) → [`0058d970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d970.md) FUN_0058d970

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d9e4",
      "incomplete_value": true,
      "site": "0058d9f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:507:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ab4c",
      "incomplete_value": true,
      "site": "0056ab58",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:78b:8"
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
      "definition_site": "0058d9f4",
      "incomplete_value": true,
      "site": "0058d9f4",
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
      "definition_site": "0056ab5c",
      "incomplete_value": true,
      "site": "0056ab5c",
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
      "0058d9e4",
      "READ",
      [
        "storage",
        "002aa78b",
        null,
        "string"
      ]
    ],
    [
      "0058d9e8",
      "READ",
      [
        "storage",
        "002aa799",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058d9e4",
      "READ",
      [
        "storage",
        "002bb507",
        null,
        "string"
      ]
    ],
    [
      "0058d9e8",
      "READ",
      [
        "storage",
        "002bb515",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ab08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056aad8.md#insn-0056ab08) · [`0056ab14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056aad8.md#insn-0056ab14) · [`0056ab44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056aad8.md#insn-0056ab44)
- 新版 `0058d9a0`（命令位置の公開資料なし） · `0058d9ac`（命令位置の公開資料なし） · `0058d9dc`（命令位置の公開資料なし）

~~~diff
- 0056ab08 ["INT_ADD", "register:40f0:8", ["const:56ab08:8", "const:4:8"]]
- 0056ab08 ["CALL", null, ["callee:00589800:8"]]
+ 0058d9a0 ["INT_ADD", "register:40f0:8", ["const:58d9a0:8", "const:4:8"]]
+ 0058d9a0 ["CALL", null, ["callee:00589800:8"]]
- 0056ab08 bytes 98efff97
+ 0058d9a0 bytes 98efff97
- 0056ab14 ["INT_ADD", "register:40f0:8", ["const:56ab14:8", "const:4:8"]]
- 0056ab14 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058d9ac ["INT_ADD", "register:40f0:8", ["const:58d9ac:8", "const:4:8"]]
+ 0058d9ac ["CALL", null, ["callee:00588e2c:8"]]
- 0056ab14 bytes 20edff97
+ 0058d9ac bytes 20edff97
- 0056ab44 ["COPY", "register:4048:8", ["const:2aa000:8"]]
+ 0058d9dc ["COPY", "register:4048:8", ["const:2bb000:8"]]
- 0056ab44 bytes 09eaff90
+ 0058d9dc bytes 69e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-557c5caefc8b9caecb9505b1a445258f"></a>

### [`0056acb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056acb4.md) → [`0058db4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058db4c.md) FUN_0058db4c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.90% / 新版 94.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058dbc0",
      "incomplete_value": true,
      "site": "0058dbc8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:340:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ad28",
      "incomplete_value": true,
      "site": "0056ad30",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:a2a:8"
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
      "definition_site": "0058dbcc",
      "incomplete_value": true,
      "site": "0058dbcc",
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
      "definition_site": "0056ad34",
      "incomplete_value": true,
      "site": "0056ad34",
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
      "0058dbc0",
      "READ",
      [
        "storage",
        "00294a2a",
        null,
        "string"
      ]
    ],
    [
      "0058dbc4",
      "READ",
      [
        "storage",
        "00294a38",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058dbc0",
      "READ",
      [
        "storage",
        "002a4340",
        null,
        "string"
      ]
    ],
    [
      "0058dbc4",
      "READ",
      [
        "storage",
        "002a434e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ace0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056acb4.md#insn-0056ace0) · [`0056ace8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056acb4.md#insn-0056ace8) · [`0056ad20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056acb4.md#insn-0056ad20)
- 新版 `0058db78`（命令位置の公開資料なし） · `0058db80`（命令位置の公開資料なし） · `0058dbb8`（命令位置の公開資料なし）

~~~diff
- 0056ace0 ["INT_ADD", "register:40f0:8", ["const:56ace0:8", "const:4:8"]]
- 0056ace0 ["CALL", null, ["callee:00589800:8"]]
+ 0058db78 ["INT_ADD", "register:40f0:8", ["const:58db78:8", "const:4:8"]]
+ 0058db78 ["CALL", null, ["callee:00589800:8"]]
- 0056ace0 bytes 22efff97
+ 0058db78 bytes 22efff97
- 0056ace8 ["INT_ADD", "register:40f0:8", ["const:56ace8:8", "const:4:8"]]
- 0056ace8 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058db80 ["INT_ADD", "register:40f0:8", ["const:58db80:8", "const:4:8"]]
+ 0058db80 ["CALL", null, ["callee:00588e2c:8"]]
- 0056ace8 bytes abecff97
+ 0058db80 bytes abecff97
- 0056ad20 ["COPY", "register:4040:8", ["const:294000:8"]]
+ 0058dbb8 ["COPY", "register:4040:8", ["const:2a4000:8"]]
- 0056ad20 bytes 48e9ffd0
+ 0058dbb8 bytes a8e8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0036266599e3988ccd7c98338252c534"></a>

### [`0056ae88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056ae88.md) → [`0058dd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058dd20.md) FUN_0058dd20

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.85% / 新版 94.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058dd90",
      "incomplete_value": true,
      "site": "0058dd98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:903:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056aef8",
      "incomplete_value": true,
      "site": "0056af00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:caa:8"
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
      "definition_site": "0058dd9c",
      "incomplete_value": true,
      "site": "0058dd9c",
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
      "definition_site": "0056af04",
      "incomplete_value": true,
      "site": "0056af04",
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
      "0058dd90",
      "READ",
      [
        "storage",
        "00297caa",
        null,
        "string"
      ]
    ],
    [
      "0058dd94",
      "READ",
      [
        "storage",
        "00297cb8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058dd90",
      "READ",
      [
        "storage",
        "002a7903",
        null,
        "string"
      ]
    ],
    [
      "0058dd94",
      "READ",
      [
        "storage",
        "002a7911",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056aeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056ae88.md#insn-0056aeb4) · [`0056aebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056ae88.md#insn-0056aebc) · [`0056aef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056ae88.md#insn-0056aef0)
- 新版 `0058dd4c`（命令位置の公開資料なし） · `0058dd54`（命令位置の公開資料なし） · `0058dd88`（命令位置の公開資料なし）

~~~diff
- 0056aeb4 ["INT_ADD", "register:40f0:8", ["const:56aeb4:8", "const:4:8"]]
- 0056aeb4 ["CALL", null, ["callee:00589800:8"]]
+ 0058dd4c ["INT_ADD", "register:40f0:8", ["const:58dd4c:8", "const:4:8"]]
+ 0058dd4c ["CALL", null, ["callee:00589800:8"]]
- 0056aeb4 bytes adeeff97
+ 0058dd4c bytes adeeff97
- 0056aebc ["INT_ADD", "register:40f0:8", ["const:56aebc:8", "const:4:8"]]
- 0056aebc ["CALL", null, ["callee:00588e2c:8"]]
+ 0058dd54 ["INT_ADD", "register:40f0:8", ["const:58dd54:8", "const:4:8"]]
+ 0058dd54 ["CALL", null, ["callee:00588e2c:8"]]
- 0056aebc bytes 36ecff97
+ 0058dd54 bytes 36ecff97
- 0056aef0 ["COPY", "register:4040:8", ["const:297000:8"]]
+ 0058dd88 ["COPY", "register:4040:8", ["const:2a7000:8"]]
- 0056aef0 bytes 68e9ffb0
+ 0058dd88 bytes c8e8ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bce566c621ba85ccbdd2ace75aea6e8"></a>

### [`0056b058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b058.md) → [`0058def0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058def0.md) FUN_0058def0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.43% / 新版 89.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058df4c",
      "incomplete_value": true,
      "site": "0058df4c",
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
                "const:91a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b0b4",
      "incomplete_value": true,
      "site": "0056b0b4",
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
                "const:cc1:8"
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
      "definition_site": "0058df6c",
      "incomplete_value": true,
      "site": "0058df74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b0d4",
      "incomplete_value": true,
      "site": "0056b0dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:510:8"
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
      "definition_site": "0058df68",
      "incomplete_value": true,
      "site": "0058df78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:903:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b0d0",
      "incomplete_value": true,
      "site": "0056b0e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:76a:8"
              ]
            ]
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
      "0058df3c",
      "READ",
      [
        "storage",
        "00297cc1",
        null,
        "string"
      ]
    ],
    [
      "0058df68",
      "READ",
      [
        "storage",
        "0029c76a",
        null,
        "string"
      ]
    ],
    [
      "0058df68",
      "READ",
      [
        "storage",
        "0029c77a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058df3c",
      "READ",
      [
        "storage",
        "002a791a",
        null,
        "string"
      ]
    ],
    [
      "0058df68",
      "READ",
      [
        "storage",
        "002ac903",
        null,
        "string"
      ]
    ],
    [
      "0058df68",
      "READ",
      [
        "storage",
        "002ac913",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b058.md#insn-0056b08c) · [`0056b094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b058.md#insn-0056b094) · [`0056b098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b058.md#insn-0056b098)
- 新版 `0058df24`（命令位置の公開資料なし） · `0058df2c`（命令位置の公開資料なし） · `0058df30`（命令位置の公開資料なし）

~~~diff
- 0056b08c ["INT_ADD", "register:40f0:8", ["const:56b08c:8", "const:4:8"]]
- 0056b08c ["CALL", null, ["callee:00589800:8"]]
+ 0058df24 ["INT_ADD", "register:40f0:8", ["const:58df24:8", "const:4:8"]]
+ 0058df24 ["CALL", null, ["callee:00589800:8"]]
- 0056b08c bytes 37eeff97
+ 0058df24 bytes 37eeff97
- 0056b094 ["INT_ADD", "register:40f0:8", ["const:56b094:8", "const:4:8"]]
- 0056b094 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058df2c ["INT_ADD", "register:40f0:8", ["const:58df2c:8", "const:4:8"]]
+ 0058df2c ["CALL", null, ["callee:00588e2c:8"]]
- 0056b094 bytes c0ebff97
+ 0058df2c bytes c0ebff97
- 0056b098 ["COPY", "register:4048:8", ["const:297000:8"]]
+ 0058df30 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0056b098 bytes 69e9ff90
+ 0058df30 bytes c9e8ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84db2a485c05fcbb6b0e8fe11b5314cc"></a>

### [`0056b2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b2b8.md) → [`0058e150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e150.md) FUN_0058e150

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.13% / 新版 87.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e1b4",
      "incomplete_value": true,
      "site": "0058e1b4",
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
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:8e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b31c",
      "incomplete_value": true,
      "site": "0056b31c",
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
                "const:29d000:8"
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e1d0",
      "incomplete_value": true,
      "site": "0058e1d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b338",
      "incomplete_value": true,
      "site": "0056b340",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e1cc",
      "incomplete_value": true,
      "site": "0058e1dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:f22:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b334",
      "incomplete_value": true,
      "site": "0056b344",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6b5:8"
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
      "0058e1a0",
      "READ",
      [
        "storage",
        "0029d65f",
        null,
        "string"
      ]
    ],
    [
      "0058e1cc",
      "READ",
      [
        "storage",
        "002a46b5",
        null,
        "string"
      ]
    ],
    [
      "0058e1cc",
      "READ",
      [
        "storage",
        "002a46c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058e1a0",
      "READ",
      [
        "storage",
        "002ad8e9",
        null,
        "string"
      ]
    ],
    [
      "0058e1cc",
      "READ",
      [
        "storage",
        "002b4f22",
        null,
        "string"
      ]
    ],
    [
      "0058e1cc",
      "READ",
      [
        "storage",
        "002b4f32",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b2b8.md#insn-0056b2ec) · [`0056b2f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b2b8.md#insn-0056b2f4) · [`0056b2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b2b8.md#insn-0056b2fc)
- 新版 `0058e184`（命令位置の公開資料なし） · `0058e18c`（命令位置の公開資料なし） · `0058e194`（命令位置の公開資料なし）

~~~diff
- 0056b2ec ["INT_ADD", "register:40f0:8", ["const:56b2ec:8", "const:4:8"]]
- 0056b2ec ["CALL", null, ["callee:00589800:8"]]
+ 0058e184 ["INT_ADD", "register:40f0:8", ["const:58e184:8", "const:4:8"]]
+ 0058e184 ["CALL", null, ["callee:00589800:8"]]
- 0056b2ec bytes 9fedff97
+ 0058e184 bytes 9fedff97
- 0056b2f4 ["INT_ADD", "register:40f0:8", ["const:56b2f4:8", "const:4:8"]]
- 0056b2f4 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058e18c ["INT_ADD", "register:40f0:8", ["const:58e18c:8", "const:4:8"]]
+ 0058e18c ["CALL", null, ["callee:00588e2c:8"]]
- 0056b2f4 bytes 28ebff97
+ 0058e18c bytes 28ebff97
- 0056b2fc ["COPY", "register:4048:8", ["const:29d000:8"]]
+ 0058e194 ["COPY", "register:4048:8", ["const:2ad000:8"]]
- 0056b2fc bytes 89e9ffd0
+ 0058e194 bytes e9e8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e3dbe5ea9a55626439a9575c1b6398a"></a>

### [`0056b4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b4a0.md) → [`0058e338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e338.md) FUN_0058e338

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.10% / 新版 90.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e3b4",
      "incomplete_value": true,
      "site": "0058e3bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b51c",
      "incomplete_value": true,
      "site": "0056b524",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e3b0",
      "incomplete_value": true,
      "site": "0058e3c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:60a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b518",
      "incomplete_value": true,
      "site": "0056b528",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:59c:8"
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
      "definition_site": "0058e3b0",
      "incomplete_value": true,
      "site": "0058e3c0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056b518",
      "incomplete_value": true,
      "site": "0056b528",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058e3b0",
      "READ",
      [
        "storage",
        "0029b59c",
        null,
        "string"
      ]
    ],
    [
      "0058e3b0",
      "READ",
      [
        "storage",
        "0029b5ac",
        null,
        "string"
      ]
    ],
    [
      "0058e3b4",
      "READ",
      [
        "storage",
        "002b0d60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058e3b0",
      "READ",
      [
        "storage",
        "002ab60a",
        null,
        "string"
      ]
    ],
    [
      "0058e3b0",
      "READ",
      [
        "storage",
        "002ab61a",
        null,
        "string"
      ]
    ],
    [
      "0058e3b4",
      "READ",
      [
        "storage",
        "002c2360",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b4a0.md#insn-0056b4d4) · [`0056b4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b4a0.md#insn-0056b4dc) · [`0056b508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b4a0.md#insn-0056b508)
- 新版 `0058e36c`（命令位置の公開資料なし） · `0058e374`（命令位置の公開資料なし） · `0058e3a0`（命令位置の公開資料なし）

~~~diff
- 0056b4d4 ["INT_ADD", "register:40f0:8", ["const:56b4d4:8", "const:4:8"]]
- 0056b4d4 ["CALL", null, ["callee:00589800:8"]]
+ 0058e36c ["INT_ADD", "register:40f0:8", ["const:58e36c:8", "const:4:8"]]
+ 0058e36c ["CALL", null, ["callee:00589800:8"]]
- 0056b4d4 bytes 25edff97
+ 0058e36c bytes 25edff97
- 0056b4dc ["INT_ADD", "register:40f0:8", ["const:56b4dc:8", "const:4:8"]]
- 0056b4dc ["CALL", null, ["callee:00588e2c:8"]]
+ 0058e374 ["INT_ADD", "register:40f0:8", ["const:58e374:8", "const:4:8"]]
+ 0058e374 ["CALL", null, ["callee:00588e2c:8"]]
- 0056b4dc bytes aeeaff97
+ 0058e374 bytes aeeaff97
- 0056b508 ["INT_ADD", "register:40f0:8", ["const:56b508:8", "const:4:8"]]
- 0056b508 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058e3a0 ["INT_ADD", "register:40f0:8", ["const:58e3a0:8", "const:4:8"]]
+ 0058e3a0 ["CALL", null, ["callee:00c57a90:8"]]
- 0056b508 bytes cebe1994
+ 0058e3a0 bytes bc251b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70d98121066f6c9cb66a8ef019c30977"></a>

### [`0056b870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b870.md) → [`0058e708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e708.md) FUN_0058e708

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e784",
      "incomplete_value": true,
      "site": "0058e78c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b8ec",
      "incomplete_value": true,
      "site": "0056b8f4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e780",
      "incomplete_value": true,
      "site": "0058e790",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b4000:8"
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
      "definition_site": "0056b8e8",
      "incomplete_value": true,
      "site": "0056b8f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6f5:8"
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
      "definition_site": "0058e780",
      "incomplete_value": true,
      "site": "0058e790",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056b8e8",
      "incomplete_value": true,
      "site": "0056b8f8",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058e780",
      "READ",
      [
        "storage",
        "002a46f5",
        null,
        "string"
      ]
    ],
    [
      "0058e780",
      "READ",
      [
        "storage",
        "002a4705",
        null,
        "string"
      ]
    ],
    [
      "0058e784",
      "READ",
      [
        "storage",
        "002b0d60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058e780",
      "READ",
      [
        "storage",
        "002b4f62",
        null,
        "string"
      ]
    ],
    [
      "0058e780",
      "READ",
      [
        "storage",
        "002b4f72",
        null,
        "string"
      ]
    ],
    [
      "0058e784",
      "READ",
      [
        "storage",
        "002c2360",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b870.md#insn-0056b8a4) · [`0056b8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b870.md#insn-0056b8ac) · [`0056b8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b870.md#insn-0056b8d8)
- 新版 `0058e73c`（命令位置の公開資料なし） · `0058e744`（命令位置の公開資料なし） · `0058e770`（命令位置の公開資料なし）

~~~diff
- 0056b8a4 ["INT_ADD", "register:40f0:8", ["const:56b8a4:8", "const:4:8"]]
- 0056b8a4 ["CALL", null, ["callee:00589800:8"]]
+ 0058e73c ["INT_ADD", "register:40f0:8", ["const:58e73c:8", "const:4:8"]]
+ 0058e73c ["CALL", null, ["callee:00589800:8"]]
- 0056b8a4 bytes 31ecff97
+ 0058e73c bytes 31ecff97
- 0056b8ac ["INT_ADD", "register:40f0:8", ["const:56b8ac:8", "const:4:8"]]
- 0056b8ac ["CALL", null, ["callee:00588e2c:8"]]
+ 0058e744 ["INT_ADD", "register:40f0:8", ["const:58e744:8", "const:4:8"]]
+ 0058e744 ["CALL", null, ["callee:00588e2c:8"]]
- 0056b8ac bytes bae9ff97
+ 0058e744 bytes bae9ff97
- 0056b8d8 ["INT_ADD", "register:40f0:8", ["const:56b8d8:8", "const:4:8"]]
- 0056b8d8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058e770 ["INT_ADD", "register:40f0:8", ["const:58e770:8", "const:4:8"]]
+ 0058e770 ["CALL", null, ["callee:00c57a90:8"]]
- 0056b8d8 bytes dabd1994
+ 0058e770 bytes c8241b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf19370973d78f4236af1492fcfb4669"></a>

### [`0056ba54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056ba54.md) → [`0058e8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e8ec.md) FUN_0058e8ec

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.07% / 新版 88.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e948",
      "incomplete_value": true,
      "site": "0058e948",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:297:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056bab0",
      "incomplete_value": true,
      "site": "0056bab0",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:d07:8"
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
      "definition_site": "0058e968",
      "incomplete_value": true,
      "site": "0058e970",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056bad0",
      "incomplete_value": true,
      "site": "0056bad8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:770:8"
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
      "definition_site": "0058e964",
      "incomplete_value": true,
      "site": "0058e974",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056bacc",
      "incomplete_value": true,
      "site": "0056badc",
      "value": [
        "LOAD",
        "16",
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
      "0058e938",
      "READ",
      [
        "storage",
        "002afd07",
        null,
        "string"
      ]
    ],
    [
      "0058e964",
      "READ",
      [
        "storage",
        "00294a61",
        null,
        "string"
      ]
    ],
    [
      "0058e964",
      "READ",
      [
        "storage",
        "00294a71",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058e938",
      "READ",
      [
        "storage",
        "002c1297",
        null,
        "string"
      ]
    ],
    [
      "0058e964",
      "READ",
      [
        "storage",
        "002a4377",
        null,
        "string"
      ]
    ],
    [
      "0058e964",
      "READ",
      [
        "storage",
        "002a4387",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ba88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056ba54.md#insn-0056ba88) · [`0056ba90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056ba54.md#insn-0056ba90) · [`0056ba94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056ba54.md#insn-0056ba94)
- 新版 `0058e920`（命令位置の公開資料なし） · `0058e928`（命令位置の公開資料なし） · `0058e92c`（命令位置の公開資料なし）

~~~diff
- 0056ba88 ["INT_ADD", "register:40f0:8", ["const:56ba88:8", "const:4:8"]]
- 0056ba88 ["CALL", null, ["callee:00589800:8"]]
+ 0058e920 ["INT_ADD", "register:40f0:8", ["const:58e920:8", "const:4:8"]]
+ 0058e920 ["CALL", null, ["callee:00589800:8"]]
- 0056ba88 bytes b8ebff97
+ 0058e920 bytes b8ebff97
- 0056ba90 ["INT_ADD", "register:40f0:8", ["const:56ba90:8", "const:4:8"]]
- 0056ba90 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058e928 ["INT_ADD", "register:40f0:8", ["const:58e928:8", "const:4:8"]]
+ 0058e928 ["CALL", null, ["callee:00588e2c:8"]]
- 0056ba90 bytes 41e9ff97
+ 0058e928 bytes 41e9ff97
- 0056ba94 ["COPY", "register:4048:8", ["const:2af000:8"]]
+ 0058e92c ["COPY", "register:4048:8", ["const:2c1000:8"]]
- 0056ba94 bytes 29eaff90
+ 0058e92c bytes 89e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f45e4d39899f070b8e161eab883100c7"></a>

### [`0056bde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bde8.md) → [`0058ec80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ec80.md) FUN_0058ec80

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) · 呼出先 2件 [`0056a298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a298.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) · 呼出先 2件 [`0058d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0058eca8",
      "incomplete_value": false,
      "site": "0058ecb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056be10",
      "incomplete_value": false,
      "site": "0056be1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "0058ecb4",
      "DATA",
      [
        "storage",
        "00bf0000",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058ecb4",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056be04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bde8.md#insn-0056be04) · [`0056be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bde8.md#insn-0056be0c) · [`0056be10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bde8.md#insn-0056be10)
- 新版 `0058ec9c`（命令位置の公開資料なし） · `0058eca4`（命令位置の公開資料なし） · `0058eca8`（命令位置の公開資料なし）

~~~diff
- 0056be04 ["INT_ADD", "register:40f0:8", ["const:56be04:8", "const:4:8"]]
- 0056be04 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058ec9c ["INT_ADD", "register:40f0:8", ["const:58ec9c:8", "const:4:8"]]
+ 0058ec9c ["CALL", null, ["callee:00c57a90:8"]]
- 0056be04 bytes 8fbc1994
+ 0058ec9c bytes 7d231b94
- 0056be0c ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0058eca4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056be0c bytes 283400b0
+ 0058eca4 bytes e83600d0
- 0056be10 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0056be10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056be10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056be10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058eca8 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 0058eca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058eca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058eca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056be10 bytes 08010091
+ 0058eca8 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-347e597120bdf36d8530d6ae75e7ed58"></a>

### [`0056bfc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bfc8.md) → [`0058ee60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ee60.md) FUN_0058ee60

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fec.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00597e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e84.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.57% / 新版 94.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058eecc",
      "incomplete_value": true,
      "site": "0058eedc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c034",
      "incomplete_value": true,
      "site": "0056c044",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8cc:8"
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
      "0058eea8",
      "READ",
      [
        "storage",
        "002a699a",
        null,
        "string"
      ]
    ],
    [
      "0058eecc",
      "READ",
      [
        "storage",
        "002918cc",
        null,
        "string"
      ]
    ],
    [
      "0058ef8c",
      "DATA",
      [
        "storage",
        "00302e31",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "0058eea8",
      "READ",
      [
        "storage",
        "002b748b",
        null,
        "string"
      ]
    ],
    [
      "0058eecc",
      "READ",
      [
        "storage",
        "002a0ee5",
        null,
        "string"
      ]
    ],
    [
      "0058ef8c",
      "DATA",
      [
        "storage",
        "00302e31",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056bfec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bfc8.md#insn-0056bfec) · [`0056bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bfc8.md#insn-0056bff4) · [`0056c008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056bfc8.md#insn-0056c008)
- 新版 `0058ee84`（命令位置の公開資料なし） · `0058ee8c`（命令位置の公開資料なし） · `0058eea0`（命令位置の公開資料なし）

~~~diff
- 0056bfec ["INT_ADD", "register:40f0:8", ["const:56bfec:8", "const:4:8"]]
- 0056bfec ["CALL", null, ["callee:00588e2c:8"]]
+ 0058ee84 ["INT_ADD", "register:40f0:8", ["const:58ee84:8", "const:4:8"]]
+ 0058ee84 ["CALL", null, ["callee:00588e2c:8"]]
- 0056bfec bytes eae7ff97
+ 0058ee84 bytes eae7ff97
- 0056bff4 ["INT_ADD", "register:40f0:8", ["const:56bff4:8", "const:4:8"]]
- 0056bff4 ["CALL", null, ["callee:0058911c:8"]]
+ 0058ee8c ["INT_ADD", "register:40f0:8", ["const:58ee8c:8", "const:4:8"]]
+ 0058ee8c ["CALL", null, ["callee:0058911c:8"]]
- 0056bff4 bytes a4e8ff97
+ 0058ee8c bytes a4e8ff97
- 0056c008 ["COPY", "register:4040:8", ["const:2a6000:8"]]
+ 0058eea0 ["COPY", "register:4040:8", ["const:2b7000:8"]]
- 0056c008 bytes c8e9ffd0
+ 0058eea0 bytes 48e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fc70773ea9cd0c64ac37c5219638f83"></a>

### [`0056c174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c174.md) → [`0058f00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f00c.md) FUN_0058f00c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f080",
      "incomplete_value": true,
      "site": "0058f08c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c1e8",
      "incomplete_value": true,
      "site": "0056c1f4",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:300:8"
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
      "0058f07c",
      "READ",
      [
        "storage",
        "00292981",
        null,
        "string"
      ]
    ],
    [
      "0058f07c",
      "READ",
      [
        "storage",
        "00292991",
        null,
        "string"
      ]
    ],
    [
      "0058f080",
      "READ",
      [
        "storage",
        "002b1300",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058f07c",
      "READ",
      [
        "storage",
        "002a2091",
        null,
        "string"
      ]
    ],
    [
      "0058f07c",
      "READ",
      [
        "storage",
        "002a20a1",
        null,
        "string"
      ]
    ],
    [
      "0058f080",
      "READ",
      [
        "storage",
        "002c2940",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c174.md#insn-0056c1a0) · [`0056c1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c174.md#insn-0056c1a8) · [`0056c1d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c174.md#insn-0056c1d4)
- 新版 `0058f038`（命令位置の公開資料なし） · `0058f040`（命令位置の公開資料なし） · `0058f06c`（命令位置の公開資料なし）

~~~diff
- 0056c1a0 ["INT_ADD", "register:40f0:8", ["const:56c1a0:8", "const:4:8"]]
- 0056c1a0 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058f038 ["INT_ADD", "register:40f0:8", ["const:58f038:8", "const:4:8"]]
+ 0058f038 ["CALL", null, ["callee:00588e2c:8"]]
- 0056c1a0 bytes 7de7ff97
+ 0058f038 bytes 7de7ff97
- 0056c1a8 ["INT_ADD", "register:40f0:8", ["const:56c1a8:8", "const:4:8"]]
- 0056c1a8 ["CALL", null, ["callee:0058911c:8"]]
+ 0058f040 ["INT_ADD", "register:40f0:8", ["const:58f040:8", "const:4:8"]]
+ 0058f040 ["CALL", null, ["callee:0058911c:8"]]
- 0056c1a8 bytes 37e8ff97
+ 0058f040 bytes 37e8ff97
- 0056c1d4 ["INT_ADD", "register:40f0:8", ["const:56c1d4:8", "const:4:8"]]
- 0056c1d4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058f06c ["INT_ADD", "register:40f0:8", ["const:58f06c:8", "const:4:8"]]
+ 0058f06c ["CALL", null, ["callee:00c57a90:8"]]
- 0056c1d4 bytes 9bbb1994
+ 0058f06c bytes 89221b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfb3cdc1d60fb90b563e80e3b1099b19"></a>

### [`0056c3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c3d0.md) → [`0058f268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f268.md) Java_jp_co_ponos_battlecats_MyActivity_shareComplete

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0058f28c",
      "incomplete_value": true,
      "site": "0058f28c",
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
              [
                "leaf",
                "const:ca6000:8"
              ]
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
      "definition_site": "0056c3f4",
      "incomplete_value": true,
      "site": "0056c3f4",
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
    "guard": [
      [
        "FALL_THROUGH",
        "0056c3f4"
      ],
      [
        "FALL_THROUGH",
        "0058f28c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0058f28c",
      "incomplete_value": true,
      "site": "0058f2a4",
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
              [
                "leaf",
                "const:ca6000:8"
              ]
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
      "definition_site": "0056c3f4",
      "incomplete_value": true,
      "site": "0056c40c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058f288",
      "READ",
      [
        "storage",
        "00c26540",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058f288",
      "READ",
      [
        "storage",
        "00ca6000",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c3d0.md#insn-0056c3ec) · [`0056c3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c3d0.md#insn-0056c3f0) · [`0056c410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c3d0.md#insn-0056c410)
- 新版 `0058f284`（命令位置の公開資料なし） · `0058f288`（命令位置の公開資料なし） · `0058f2a8`（命令位置の公開資料なし）

~~~diff
- 0056c3ec ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 0058f284 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0056c3ec bytes c83500d0
+ 0058f284 bytes a83800f0
- 0056c3f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:540:8"]]
- 0056c3f0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0058f288 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0058f288 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0056c3f0 bytes 00a142f9
+ 0058f288 bytes 000140f9
- 0056c410 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c410 ["INT_ADD", "register:40f0:8", ["const:56c410:8", "const:4:8"]]
- 0056c410 ["CALLIND", null, ["register:0:8"]]
+ 0058f2a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f2a8 ["INT_ADD", "register:40f0:8", ["const:58f2a8:8", "const:4:8"]]
+ 0058f2a8 ["CALLIND", null, ["register:0:8"]]
- 0056c410 bytes 00013fd6
+ 0058f2a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce50739086bb8cc4299dde16c60ce198"></a>

### [`0056c7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c7a0.md) → [`0058f638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f638.md) FUN_0058f638

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`005679e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md)

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
      "definition_site": "0058f648",
      "incomplete_value": false,
      "site": "0058f650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c7b0",
      "incomplete_value": false,
      "site": "0056c7b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "0058f650",
      "DATA",
      [
        "storage",
        "00beff78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f650",
      "DATA",
      [
        "storage",
        "00c6cb38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c7a0.md#insn-0056c7ac) · [`0056c7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c7a0.md#insn-0056c7b0) · [`0056c7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c7a0.md#insn-0056c7c0)
- 新版 `0058f644`（命令位置の公開資料なし） · `0058f648`（命令位置の公開資料なし） · `0058f658`（命令位置の公開資料なし）

~~~diff
- 0056c7ac ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058f644 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056c7ac bytes 083400f0
+ 0058f644 bytes e83600b0
- 0056c7b0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0056c7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056c7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056c7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f648 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 0058f648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056c7b0 bytes 08e13d91
+ 0058f648 bytes 08e12c91
- 0056c7c0 ["INT_ADD", "register:40f0:8", ["const:56c7c0:8", "const:4:8"]]
- 0056c7c0 ["CALL", null, ["callee:0058a87c:8"]]
+ 0058f658 ["INT_ADD", "register:40f0:8", ["const:58f658:8", "const:4:8"]]
+ 0058f658 ["CALL", null, ["callee:0058a87c:8"]]
- 0056c7c0 bytes 89ecff97
+ 0058f658 bytes 89ecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-280ebe4881d82a47aaa2dfafb49673ba"></a>

### [`0056c7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c7d8.md) → [`0058f670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f670.md) _INIT_34

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00557a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a80.md) [`00569da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569da8.md) [`00b7d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2a0.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0057a918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a918.md) [`0058cc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc40.md) [`00bf9ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ce8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f69c",
      "incomplete_value": false,
      "site": "0058f69c",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:f98:8"
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
      "definition_site": "0056c804",
      "incomplete_value": false,
      "site": "0056c804",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:4d8:8"
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
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f6a0",
      "incomplete_value": false,
      "site": "0058f6a0",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:f98:8"
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
      "definition_site": "0056c808",
      "incomplete_value": false,
      "site": "0056c808",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:4d8:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f6a4",
      "incomplete_value": false,
      "site": "0058f6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c80c",
      "incomplete_value": false,
      "site": "0056c80c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "0058f680",
      "PARAM",
      [
        "storage",
        "00c264d8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f694",
      "PARAM",
      [
        "storage",
        "00557a80",
        null,
        null
      ]
    ],
    [
      "0058f698",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058f680",
      "PARAM",
      [
        "storage",
        "00ca5f98",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f694",
      "PARAM",
      [
        "storage",
        "0057a918",
        null,
        null
      ]
    ],
    [
      "0058f698",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c7d8.md#insn-0056c810) · [`0056c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c7d8.md#insn-0056c828) · [`0056c7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c7d8.md#insn-0056c7e4)
- 新版 `0058f6a8`（命令位置の公開資料なし） · `0058f6c0`（命令位置の公開資料なし） · `0058f67c`（命令位置の公開資料なし）

~~~diff
- 0056c810 ["INT_ADD", "register:40f0:8", ["const:56c810:8", "const:4:8"]]
- 0056c810 ["CALL", null, ["callee:00c57a30:8"]]
+ 0058f6a8 ["INT_ADD", "register:40f0:8", ["const:58f6a8:8", "const:4:8"]]
+ 0058f6a8 ["CALL", null, ["callee:00c57a30:8"]]
- 0056c810 bytes f4b91994
+ 0058f6a8 bytes e2201b94
- 0056c828 ["INT_ADD", "register:40f0:8", ["const:56c828:8", "const:4:8"]]
- 0056c828 ["CALL", null, ["callee:00c57a30:8"]]
+ 0058f6c0 ["INT_ADD", "register:40f0:8", ["const:58f6c0:8", "const:4:8"]]
+ 0058f6c0 ["CALL", null, ["callee:00c57a30:8"]]
- 0056c828 bytes eeb91994
+ 0058f6c0 bytes dc201b94
- 0056c7e4 ["COPY", "register:4008:8", ["const:c26000:8"]]
+ 0058f67c ["COPY", "register:4008:8", ["const:ca5000:8"]]
- 0056c7e4 bytes c13500d0
+ 0058f67c bytes a13800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-120d4a0aa7251d933bfb055851a9f4bc"></a>

### [`0056c8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c8b0.md) → [`0058f748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f748.md) FUN_0058f748

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056cb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0058fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f7a0",
      "incomplete_value": false,
      "site": "0058f7a0",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:74:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c908",
      "incomplete_value": false,
      "site": "0056c908",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:5b4:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f7a8",
      "incomplete_value": false,
      "site": "0058f7a8",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:74:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c910",
      "incomplete_value": false,
      "site": "0056c910",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:5b4:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0058f858",
      "incomplete_value": true,
      "site": "0058f858",
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
      "definition_site": "0056c9c0",
      "incomplete_value": true,
      "site": "0056c9c0",
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
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058f794",
      "READ",
      [
        "storage",
        "00c26650",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f7a0",
      "WRITE",
      [
        "storage",
        "00c265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f7a8",
      "WRITE",
      [
        "storage",
        "00c265b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058f794",
      "READ",
      [
        "storage",
        "00ca6110",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f7a0",
      "WRITE",
      [
        "storage",
        "00ca6080",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f7a8",
      "WRITE",
      [
        "storage",
        "00ca6078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c8b0.md#insn-0056c9c0) · [`0056c9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c8b0.md#insn-0056c9d8) · [`0056c8e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c8b0.md#insn-0056c8e4)
- 新版 `0058f858`（命令位置の公開資料なし） · `0058f870`（命令位置の公開資料なし） · `0058f77c`（命令位置の公開資料なし）

~~~diff
- 0056c9c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c9c0 ["INT_ADD", "register:40f0:8", ["const:56c9c0:8", "const:4:8"]]
- 0056c9c0 ["CALLIND", null, ["register:0:8"]]
+ 0058f858 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f858 ["INT_ADD", "register:40f0:8", ["const:58f858:8", "const:4:8"]]
+ 0058f858 ["CALLIND", null, ["register:0:8"]]
- 0056c9c0 bytes 00013fd6
+ 0058f858 bytes 00013fd6
- 0056c9d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056c9d8 ["INT_ADD", "register:40f0:8", ["const:56c9d8:8", "const:4:8"]]
- 0056c9d8 ["CALLIND", null, ["register:0:8"]]
+ 0058f870 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f870 ["INT_ADD", "register:40f0:8", ["const:58f870:8", "const:4:8"]]
+ 0058f870 ["CALLIND", null, ["register:0:8"]]
- 0056c9d8 bytes 00013fd6
+ 0058f870 bytes 00013fd6
- 0056c8e4 ["COPY", "register:40a8:8", ["const:c26000:8"]]
+ 0058f77c ["COPY", "register:40a8:8", ["const:ca6000:8"]]
- 0056c8e4 bytes d53500d0
+ 0058f77c bytes b53800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c11abbe414b1940828aaf05f5c19267c"></a>

### [`0056cb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md) → [`0058fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md) FUN_0058fa08

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004184bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004184bc.md) [`0041876c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041876c.md) [`00444e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444e6c.md) · 呼出先 5件 [`0056c8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c8b0.md) [`0056ca28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056ca28.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`0043afbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043afbc.md) [`0043b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b26c.md) [`00467d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d04.md) · 呼出先 5件 [`0058f748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f748.md) [`0058f8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f8c0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 79.71% / 新版 79.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件, `store_destination` 2件

アドレスに依存する影響 `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa48",
      "incomplete_value": false,
      "site": "0058fa48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:5c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cbb0",
      "incomplete_value": false,
      "site": "0056cbb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:59c:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa50",
      "incomplete_value": false,
      "site": "0058fa50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cbb8",
      "incomplete_value": false,
      "site": "0056cbb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa58",
      "incomplete_value": false,
      "site": "0058fa58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cbc0",
      "incomplete_value": false,
      "site": "0056cbc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:5a4:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058fa48",
      "WRITE",
      [
        "storage",
        "00c2659c",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fa50",
      "WRITE",
      [
        "storage",
        "00c265a0",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fa58",
      "WRITE",
      [
        "storage",
        "00c265a4",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0058fa48",
      "WRITE",
      [
        "storage",
        "00ca605c",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fa50",
      "WRITE",
      [
        "storage",
        "00ca6060",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fa58",
      "WRITE",
      [
        "storage",
        "00ca6064",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056cbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md#insn-0056cbb0) · [`0056cbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md#insn-0056cbb8) · [`0056cbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md#insn-0056cbc0)
- 新版 `0058fa48`（命令位置の公開資料なし） · `0058fa50`（命令位置の公開資料なし） · `0058fa58`（命令位置の公開資料なし）

~~~diff
- 0056cbb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:59c:8"]]
- 0056cbb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
+ 0058fa48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c:8"]]
+ 0058fa48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
- 0056cbb0 bytes 049d05b9
+ 0058fa48 bytes 045d00b9
- 0056cbb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5a0:8"]]
- 0056cbb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
+ 0058fa50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:60:8"]]
+ 0058fa50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
- 0056cbb8 bytes 05a105b9
+ 0058fa50 bytes 056100b9
- 0056cbc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5a4:8"]]
- 0056cbc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 0058fa58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:64:8"]]
+ 0058fa58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 0056cbc0 bytes 00a505b9
+ 0058fa58 bytes 006500b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6092acbf2bc822826ad8a500a85452c2"></a>

### [`0056cca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cca8.md) → [`0058fb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb40.md) FUN_0058fb40

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`005f483c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f483c.md) [`00878704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878704.md) [`00879778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879778.md) [`008a5430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5430.md) · 呼出先 0件 
- 新版 呼出元 4件 [`0061a08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a08c.md) [`008ab8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab8a4.md) [`008ac918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac918.md) [`008d92c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d92c8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fb5c",
      "incomplete_value": false,
      "site": "0058fb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ccc4",
      "incomplete_value": false,
      "site": "0056ccc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:5a4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fb64",
      "incomplete_value": false,
      "site": "0058fb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cccc",
      "incomplete_value": false,
      "site": "0056cccc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fb70",
      "incomplete_value": false,
      "site": "0058fb70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ccd8",
      "incomplete_value": false,
      "site": "0056ccd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:5ac:8"
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
      "0058fb50",
      "READ",
      [
        "storage",
        "00c26650",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fb5c",
      "WRITE",
      [
        "storage",
        "00c265a4",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fb64",
      "WRITE",
      [
        "storage",
        "00c265a8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0058fb50",
      "READ",
      [
        "storage",
        "00ca6110",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fb5c",
      "WRITE",
      [
        "storage",
        "00ca6064",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fb64",
      "WRITE",
      [
        "storage",
        "00ca6068",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ccc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cca8.md#insn-0056ccc4) · [`0056cccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cca8.md#insn-0056cccc) · [`0056ccd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cca8.md#insn-0056ccd8)
- 新版 `0058fb5c`（命令位置の公開資料なし） · `0058fb64`（命令位置の公開資料なし） · `0058fb70`（命令位置の公開資料なし）

~~~diff
- 0056ccc4 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:5a4:8"]]
- 0056ccc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 0058fb5c ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:64:8"]]
+ 0058fb5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 0056ccc4 bytes 88a505b9
+ 0058fb5c bytes 886500b9
- 0056cccc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5a8:8"]]
- 0056cccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 0058fb64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:68:8"]]
+ 0058fb64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0056cccc bytes 09a905b9
+ 0058fb64 bytes 096900b9
- 0056ccd8 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:5ac:8"]]
- 0056ccd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
+ 0058fb70 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:6c:8"]]
+ 0058fb70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 0056ccd8 bytes 4bad05b9
+ 0058fb70 bytes 4b6d00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a53db83fb70e1d463bfcd0af657f881c"></a>

### [`0056cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cdfc.md) → [`0058fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md) FUN_0058fc94

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0053a710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a710.md) [`0053a8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a8e8.md) [`0053aac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aac4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_value, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 44.00% / 新版 44.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0056ce80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0056ce84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0056ce88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058fc98",
      "READ",
      [
        "storage",
        "00c26640",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fcac",
      "READ",
      [
        "storage",
        "00c26638",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0056ce34",
      "READ",
      [
        "storage",
        "00c26620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fc98",
      "READ",
      [
        "storage",
        "00ca6100",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fcac",
      "READ",
      [
        "storage",
        "00ca60f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fccc",
      "READ",
      [
        "storage",
        "00ca60e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ce68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cdfc.md#insn-0056ce68) · [`0056ce80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cdfc.md#insn-0056ce80) · [`0056ce84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cdfc.md#insn-0056ce84)

~~~diff
- 0056ce68 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0056ce68 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0056ce68 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0056ce68 ["COPY", "tmp:1:8", ["register:4080:8"]]
- 0056ce68 bytes eb03909a
- 0056ce80 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:20:8"]]
- 0056ce80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:8"]]
- 0056ce80 bytes 4c1100f9
- 0056ce84 ["INT_ADD", "tmp:0:8", ["register:4070:8", "const:10:8"]]
- 0056ce84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4078:8"]]
- 0056ce84 bytes cf0900f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b55b7d509d36cce4a8b20ebda88fee15"></a>

### [`0056dee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dee0.md) → [`00590d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md) FUN_00590d78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0056f4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f4d8.md) · 呼出先 17件 [`0052dd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd2c.md) [`0053239c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053239c.md) [`0056e384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e384.md) [`0056f6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f6a0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 1件 [`00592370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592370.md) · 呼出先 17件 [`00550bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bc4.md) [`00555234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555234.md) [`0059121c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059121c.md) [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00590da4",
      "incomplete_value": false,
      "site": "00590db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056df0c",
      "incomplete_value": false,
      "site": "0056df18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:50:8"
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
      "definition_site": "00590de4",
      "incomplete_value": true,
      "site": "00590de4",
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
                "const:162:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056df4c",
      "incomplete_value": true,
      "site": "0056df4c",
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
                "const:290000:8"
              ],
              [
                "leaf",
                "const:c20:8"
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
      "definition_site": "00590e24",
      "incomplete_value": true,
      "site": "00590e24",
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
                "const:cba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056df8c",
      "incomplete_value": true,
      "site": "0056df8c",
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
                "const:5e0:8"
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
      "00590db0",
      "DATA",
      [
        "storage",
        "00bf0050",
        null,
        "undefined *"
      ]
    ],
    [
      "00590dd4",
      "READ",
      [
        "storage",
        "00290c20",
        null,
        "string"
      ]
    ],
    [
      "00590e14",
      "READ",
      [
        "storage",
        "002a35e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00590db0",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ],
    [
      "00590dd4",
      "READ",
      [
        "storage",
        "002a0162",
        null,
        "string"
      ]
    ],
    [
      "00590e14",
      "READ",
      [
        "storage",
        "002b3cba",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dee0.md#insn-0056e010) · [`0056e0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dee0.md#insn-0056e0a4) · [`0056e0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dee0.md#insn-0056e0d4)
- 新版 `00590ea8`（命令位置の公開資料なし） · `00590f3c`（命令位置の公開資料なし） · `00590f6c`（命令位置の公開資料なし）

~~~diff
- 0056e010 ["INT_ADD", "register:40f0:8", ["const:56e010:8", "const:4:8"]]
- 0056e010 ["CALL", null, ["callee:00c58210:8"]]
+ 00590ea8 ["INT_ADD", "register:40f0:8", ["const:590ea8:8", "const:4:8"]]
+ 00590ea8 ["CALL", null, ["callee:00c58210:8"]]
- 0056e010 bytes ecb51994
+ 00590ea8 bytes da1c1b94
- 0056e0a4 ["INT_ADD", "register:40f0:8", ["const:56e0a4:8", "const:4:8"]]
- 0056e0a4 ["CALL", null, ["callee:00592538:8"]]
+ 00590f3c ["INT_ADD", "register:40f0:8", ["const:590f3c:8", "const:4:8"]]
+ 00590f3c ["CALL", null, ["callee:00592538:8"]]
- 0056e0a4 bytes 7f050094
+ 00590f3c bytes 7f050094
- 0056e0d4 ["INT_ADD", "register:40f0:8", ["const:56e0d4:8", "const:4:8"]]
- 0056e0d4 ["CALL", null, ["callee:00592538:8"]]
+ 00590f6c ["INT_ADD", "register:40f0:8", ["const:590f6c:8", "const:4:8"]]
+ 00590f6c ["CALL", null, ["callee:00592538:8"]]
- 0056e0d4 bytes 73050094
+ 00590f6c bytes 73050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-734d6b0702f8b7a432ac27046cc18496"></a>

### [`0056e3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e3e0.md) → [`00591278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591278.md) FUN_00591278

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd510.md) [`00bdd520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd520.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f60.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00591344",
      "incomplete_value": false,
      "site": "00591344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e4ac",
      "incomplete_value": false,
      "site": "0056e4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "definition_site": "0059135c",
      "incomplete_value": true,
      "site": "00591364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e4c4",
      "incomplete_value": true,
      "site": "0056e4cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005912d4",
      "incomplete_value": true,
      "site": "005912d8",
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
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e43c",
      "incomplete_value": true,
      "site": "0056e440",
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
              "LOAD"
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
      "005912d0",
      "READ",
      [
        "storage",
        "00c1b490",
        null,
        "pointer"
      ]
    ],
    [
      "005912d4",
      "READ",
      [
        "storage",
        "00c23f5c",
        null,
        "undefined4"
      ]
    ],
    [
      "005912dc",
      "READ",
      [
        "storage",
        "00c23f60",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005912d0",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "005912d4",
      "READ",
      [
        "storage",
        "00ca3a44",
        null,
        "undefined4"
      ]
    ],
    [
      "005912dc",
      "READ",
      [
        "storage",
        "00ca3a48",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e3e0.md#insn-0056e440) · [`0056e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e3e0.md#insn-0056e41c) · [`0056e428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e3e0.md#insn-0056e428)
- 新版 `005912d8`（命令位置の公開資料なし） · `005912b4`（命令位置の公開資料なし） · `005912c0`（命令位置の公開資料なし）

~~~diff
- 0056e440 ["INT_ADD", "register:40f0:8", ["const:56e440:8", "const:4:8"]]
- 0056e440 ["CALL", null, ["callee:00c59f80:8"]]
+ 005912d8 ["INT_ADD", "register:40f0:8", ["const:5912d8:8", "const:4:8"]]
+ 005912d8 ["CALL", null, ["callee:00c59f80:8"]]
- 0056e440 bytes 3cbc1994
+ 005912d8 bytes 2a231b94
- 0056e41c ["INT_ADD", "register:40f0:8", ["const:56e41c:8", "const:4:8"]]
- 0056e41c ["CALL", null, ["callee:00c59f60:8"]]
+ 005912b4 ["INT_ADD", "register:40f0:8", ["const:5912b4:8", "const:4:8"]]
+ 005912b4 ["CALL", null, ["callee:00c59f60:8"]]
- 0056e41c bytes 3dbc1994
+ 005912b4 bytes 2b231b94
- 0056e428 ["INT_ADD", "register:40f0:8", ["const:56e428:8", "const:4:8"]]
- 0056e428 ["CALL", null, ["callee:00c59f70:8"]]
+ 005912c0 ["INT_ADD", "register:40f0:8", ["const:5912c0:8", "const:4:8"]]
+ 005912c0 ["CALL", null, ["callee:00c59f70:8"]]
- 0056e428 bytes 3ebc1994
+ 005912c0 bytes 2c231b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba05929b5a79d6ce1ba0d520d91f33b"></a>

### [`0056e528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e528.md) → [`005913c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005913c0.md) FUN_005913c0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd510.md) [`00bdd520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd520.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f60.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.35% / 新版 84.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059149c",
      "incomplete_value": false,
      "site": "005914a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e604",
      "incomplete_value": false,
      "site": "0056e60c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:220:8"
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
      "definition_site": "005914bc",
      "incomplete_value": false,
      "site": "005914bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e624",
      "incomplete_value": false,
      "site": "0056e624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "definition_site": "005914d4",
      "incomplete_value": true,
      "site": "005914d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e63c",
      "incomplete_value": true,
      "site": "0056e640",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d0:8"
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
      "00591420",
      "READ",
      [
        "storage",
        "00c1b490",
        null,
        "pointer"
      ]
    ],
    [
      "00591424",
      "READ",
      [
        "storage",
        "00c23f5c",
        null,
        "undefined4"
      ]
    ],
    [
      "0059142c",
      "READ",
      [
        "storage",
        "00c23f60",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00591420",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "00591424",
      "READ",
      [
        "storage",
        "00ca3a44",
        null,
        "undefined4"
      ]
    ],
    [
      "0059142c",
      "READ",
      [
        "storage",
        "00ca3a48",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e528.md#insn-0056e590) · [`0056e56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e528.md#insn-0056e56c) · [`0056e578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e528.md#insn-0056e578)
- 新版 `00591428`（命令位置の公開資料なし） · `00591404`（命令位置の公開資料なし） · `00591410`（命令位置の公開資料なし）

~~~diff
- 0056e590 ["INT_ADD", "register:40f0:8", ["const:56e590:8", "const:4:8"]]
- 0056e590 ["CALL", null, ["callee:00c59f80:8"]]
+ 00591428 ["INT_ADD", "register:40f0:8", ["const:591428:8", "const:4:8"]]
+ 00591428 ["CALL", null, ["callee:00c59f80:8"]]
- 0056e590 bytes e8bb1994
+ 00591428 bytes d6221b94
- 0056e56c ["INT_ADD", "register:40f0:8", ["const:56e56c:8", "const:4:8"]]
- 0056e56c ["CALL", null, ["callee:00c59f60:8"]]
+ 00591404 ["INT_ADD", "register:40f0:8", ["const:591404:8", "const:4:8"]]
+ 00591404 ["CALL", null, ["callee:00c59f60:8"]]
- 0056e56c bytes e9bb1994
+ 00591404 bytes d7221b94
- 0056e578 ["INT_ADD", "register:40f0:8", ["const:56e578:8", "const:4:8"]]
- 0056e578 ["CALL", null, ["callee:00c59f70:8"]]
+ 00591410 ["INT_ADD", "register:40f0:8", ["const:591410:8", "const:4:8"]]
+ 00591410 ["CALL", null, ["callee:00c59f70:8"]]
- 0056e578 bytes eabb1994
+ 00591410 bytes d8221b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf5a9a73ad57dc17fb1a2e94e2b4b8b6"></a>

### [`0056e724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e724.md) → [`005915bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005915bc.md) FUN_005915bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd5b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00591600",
      "incomplete_value": false,
      "site": "00591608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e768",
      "incomplete_value": false,
      "site": "0056e770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "definition_site": "00591620",
      "incomplete_value": false,
      "site": "00591620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e788",
      "incomplete_value": false,
      "site": "0056e788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "00591608",
      "DATA",
      [
        "storage",
        "00bf0390",
        null,
        "undefined *"
      ]
    ],
    [
      "00591620",
      "DATA",
      [
        "storage",
        "00bf03e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591608",
      "DATA",
      [
        "storage",
        "00c6cf50",
        null,
        "undefined *"
      ]
    ],
    [
      "00591620",
      "DATA",
      [
        "storage",
        "00c6cfa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e724.md#insn-0056e758) · [`0056e760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e724.md#insn-0056e760) · [`0056e764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e724.md#insn-0056e764)
- 新版 `005915f0`（命令位置の公開資料なし） · `005915f8`（命令位置の公開資料なし） · `005915fc`（命令位置の公開資料なし）

~~~diff
- 0056e758 ["INT_ADD", "register:40f0:8", ["const:56e758:8", "const:4:8"]]
- 0056e758 ["CALL", null, ["callee:00c5a000:8"]]
+ 005915f0 ["INT_ADD", "register:40f0:8", ["const:5915f0:8", "const:4:8"]]
+ 005915f0 ["CALL", null, ["callee:00c5a000:8"]]
- 0056e758 bytes 96bb1994
+ 005915f0 bytes 84221b94
- 0056e760 ["INT_ADD", "register:40f0:8", ["const:56e760:8", "const:4:8"]]
- 0056e760 ["CALL", null, ["callee:00c57a90:8"]]
+ 005915f8 ["INT_ADD", "register:40f0:8", ["const:5915f8:8", "const:4:8"]]
+ 005915f8 ["CALL", null, ["callee:00c57a90:8"]]
- 0056e760 bytes 38b21994
+ 005915f8 bytes 26191b94
- 0056e764 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 005915fc ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056e764 bytes 083400d0
+ 005915fc bytes c83600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8370899288ece9120cbc8acf3000d0be"></a>

### [`0056e8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e8b0.md) → [`00591748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591748.md) FUN_00591748

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0056f6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f6a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591760",
      "incomplete_value": false,
      "site": "0059176c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:e67:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e8c8",
      "incomplete_value": false,
      "site": "0056e8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:b41:8"
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
      "00591760",
      "PARAM",
      [
        "storage",
        "002adb41",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00591760",
      "PARAM",
      [
        "storage",
        "002bee67",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e8b0.md#insn-0056e8d4) · [`0056e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e8b0.md#insn-0056e8c4) · [`0056e8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e8b0.md#insn-0056e8c8)
- 新版 `0059176c`（命令位置の公開資料なし） · `0059175c`（命令位置の公開資料なし） · `00591760`（命令位置の公開資料なし）

~~~diff
- 0056e8d4 ["INT_ADD", "register:40f0:8", ["const:56e8d4:8", "const:4:8"]]
- 0056e8d4 ["CALL", null, ["callee:00592538:8"]]
+ 0059176c ["INT_ADD", "register:40f0:8", ["const:59176c:8", "const:4:8"]]
+ 0059176c ["CALL", null, ["callee:00592538:8"]]
- 0056e8d4 bytes 73030094
+ 0059176c bytes 73030094
- 0056e8c4 ["COPY", "register:4008:8", ["const:2ad000:8"]]
+ 0059175c ["COPY", "register:4008:8", ["const:2be000:8"]]
- 0056e8c4 bytes e1e9fff0
+ 0059175c bytes 61e9ffb0
- 0056e8c8 ["COPY", "tmp:0:8", ["const:b41:8"]]
- 0056e8c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056e8c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056e8c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591760 ["COPY", "tmp:0:8", ["const:e67:8"]]
+ 00591760 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591760 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591760 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056e8c8 bytes 21042d91
+ 00591760 bytes 219c3991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04a061366ac152f9d56dfab906c4c617"></a>

### [`0056e968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e968.md) → [`00591800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591800.md) FUN_00591800

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0056f6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f6a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591818",
      "incomplete_value": false,
      "site": "00591824",
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
            "const:20a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e980",
      "incomplete_value": false,
      "site": "0056e98c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:a11:8"
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
      "00591818",
      "PARAM",
      [
        "storage",
        "00293a11",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00591818",
      "PARAM",
      [
        "storage",
        "002a320a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e968.md#insn-0056e98c) · [`0056e97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e968.md#insn-0056e97c) · [`0056e980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e968.md#insn-0056e980)
- 新版 `00591824`（命令位置の公開資料なし） · `00591814`（命令位置の公開資料なし） · `00591818`（命令位置の公開資料なし）

~~~diff
- 0056e98c ["INT_ADD", "register:40f0:8", ["const:56e98c:8", "const:4:8"]]
- 0056e98c ["CALL", null, ["callee:00592538:8"]]
+ 00591824 ["INT_ADD", "register:40f0:8", ["const:591824:8", "const:4:8"]]
+ 00591824 ["CALL", null, ["callee:00592538:8"]]
- 0056e98c bytes 45030094
+ 00591824 bytes 45030094
- 0056e97c ["COPY", "register:4008:8", ["const:293000:8"]]
+ 00591814 ["COPY", "register:4008:8", ["const:2a3000:8"]]
- 0056e97c bytes 21e9ffb0
+ 00591814 bytes 81e8ffd0
- 0056e980 ["COPY", "tmp:0:8", ["const:a11:8"]]
- 0056e980 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056e980 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056e980 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591818 ["COPY", "tmp:0:8", ["const:20a:8"]]
+ 00591818 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591818 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591818 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056e980 bytes 21442891
+ 00591818 bytes 21280891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63bb58b58accc4ab2b4e7656302bab5e"></a>

### [`0056e9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e9b0.md) → [`00591848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591848.md) FUN_00591848

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0056f6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f6a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591860",
      "incomplete_value": false,
      "site": "00591870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:8f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e9c8",
      "incomplete_value": false,
      "site": "0056e9d8",
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
            "const:66a:8"
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
      "00591860",
      "PARAM",
      [
        "storage",
        "0029d66a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00591860",
      "PARAM",
      [
        "storage",
        "002ad8f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e9b0.md#insn-0056e9d8) · [`0056e9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e9b0.md#insn-0056e9c4) · [`0056e9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e9b0.md#insn-0056e9c8)
- 新版 `00591870`（命令位置の公開資料なし） · `0059185c`（命令位置の公開資料なし） · `00591860`（命令位置の公開資料なし）

~~~diff
- 0056e9d8 ["INT_ADD", "register:40f0:8", ["const:56e9d8:8", "const:4:8"]]
- 0056e9d8 ["CALL", null, ["callee:00592538:8"]]
+ 00591870 ["INT_ADD", "register:40f0:8", ["const:591870:8", "const:4:8"]]
+ 00591870 ["CALL", null, ["callee:00592538:8"]]
- 0056e9d8 bytes 32030094
+ 00591870 bytes 32030094
- 0056e9c4 ["COPY", "register:4008:8", ["const:29d000:8"]]
+ 0059185c ["COPY", "register:4008:8", ["const:2ad000:8"]]
- 0056e9c4 bytes 61e9fff0
+ 0059185c bytes e1e8ff90
- 0056e9c8 ["COPY", "tmp:0:8", ["const:66a:8"]]
- 0056e9c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056e9c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056e9c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591860 ["COPY", "tmp:0:8", ["const:8f4:8"]]
+ 00591860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056e9c8 bytes 21a81991
+ 00591860 bytes 21d02391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9bbfd89e3ed9f8c97d10dc15169aaac"></a>

### [`0056eae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eae0.md) → [`00591978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591978.md) FUN_00591978

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) [`00bdd620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd620.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005919a0",
      "incomplete_value": false,
      "site": "005919b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056eb08",
      "incomplete_value": false,
      "site": "0056eb18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:200:8"
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
      "definition_site": "005919a4",
      "incomplete_value": true,
      "site": "005919b0",
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056eb0c",
      "incomplete_value": true,
      "site": "0056eb18",
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
                "const:4f0:8"
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
      "005919a0",
      "PARAM",
      [
        "storage",
        "00bf0200",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005919a4",
      "READ",
      [
        "storage",
        "00c1b4f0",
        null,
        "pointer"
      ]
    ],
    [
      "005919a4",
      "PARAM",
      [
        "storage",
        "00bf0520",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005919a0",
      "PARAM",
      [
        "storage",
        "00c6cdc0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005919a4",
      "READ",
      [
        "storage",
        "00c9aee0",
        null,
        "pointer"
      ]
    ],
    [
      "005919a4",
      "PARAM",
      [
        "storage",
        "00c6d0e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056eb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eae0.md#insn-0056eb18) · [`0056eafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eae0.md#insn-0056eafc) · [`0056eb04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eae0.md#insn-0056eb04)
- 新版 `005919b0`（命令位置の公開資料なし） · `00591994`（命令位置の公開資料なし） · `0059199c`（命令位置の公開資料なし）

~~~diff
- 0056eb18 ["INT_ADD", "register:40f0:8", ["const:56eb18:8", "const:4:8"]]
- 0056eb18 ["CALL", null, ["callee:00c58210:8"]]
+ 005919b0 ["INT_ADD", "register:40f0:8", ["const:5919b0:8", "const:4:8"]]
+ 005919b0 ["CALL", null, ["callee:00c58210:8"]]
- 0056eb18 bytes 2ab31994
+ 005919b0 bytes 181a1b94
- 0056eafc ["COPY", "register:4010:8", ["const:c1b000:8"]]
+ 00591994 ["COPY", "register:4010:8", ["const:c9a000:8"]]
- 0056eafc bytes 623500b0
+ 00591994 bytes 423800b0
- 0056eb04 ["COPY", "register:4008:8", ["const:bf0000:8"]]
+ 0059199c ["COPY", "register:4008:8", ["const:c6c000:8"]]
- 0056eb04 bytes 013400d0
+ 0059199c bytes c13600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eff668745369488ffb62baa8ab33a46"></a>

### [`0056ec5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ec5c.md) → [`00591af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591af4.md) FUN_00591af4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0056ccec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056ccec.md) [`00bdd520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd520.md) [`00bdd680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd680.md) [`00bdd690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd690.md) [`00bdd6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd6a0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0058fb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb84.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c5a0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0d0.md) [`00c5a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0e0.md) [`00c5a0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0f0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

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
      "site": "00591b20",
      "value": [
        "leaf",
        "ram:58fb84:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0056ec88",
      "value": [
        "leaf",
        "ram:56ccec:8"
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
      "00591b20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056ccec"
      ]
    ]
  ],
  "added": [
    [
      "00591b20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058fb84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ec88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ec5c.md#insn-0056ec88) · [`0056ec84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ec5c.md#insn-0056ec84) · [`0056eca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ec5c.md#insn-0056eca4)
- 新版 `00591b20`（命令位置の公開資料なし） · `00591b1c`（命令位置の公開資料なし） · `00591b3c`（命令位置の公開資料なし）

~~~diff
- 0056ec88 ["INT_ADD", "register:40f0:8", ["const:56ec88:8", "const:4:8"]]
- 0056ec88 ["CALL", null, ["ram:56ccec:8"]]
+ 00591b20 ["INT_ADD", "register:40f0:8", ["const:591b20:8", "const:4:8"]]
+ 00591b20 ["CALL", null, ["ram:58fb84:8"]]
- 0056ec88 bytes 19f8ff97
+ 00591b20 bytes 19f8ff97
- 0056ec84 ["INT_ADD", "register:40f0:8", ["const:56ec84:8", "const:4:8"]]
- 0056ec84 ["CALL", null, ["callee:00c59f70:8"]]
+ 00591b1c ["INT_ADD", "register:40f0:8", ["const:591b1c:8", "const:4:8"]]
+ 00591b1c ["CALL", null, ["callee:00c59f70:8"]]
- 0056ec84 bytes 27ba1994
+ 00591b1c bytes 15211b94
- 0056eca4 ["INT_ADD", "register:40f0:8", ["const:56eca4:8", "const:4:8"]]
- 0056eca4 ["CALL", null, ["callee:00c5a0d0:8"]]
+ 00591b3c ["INT_ADD", "register:40f0:8", ["const:591b3c:8", "const:4:8"]]
+ 00591b3c ["CALL", null, ["callee:00c5a0d0:8"]]
- 0056eca4 bytes 77ba1994
+ 00591b3c bytes 65211b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3e2d0589d5dc5485af867c03cd12952"></a>

### [`0056ece8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ece8.md) → [`00591b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591b80.md) FUN_00591b80

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0056ccec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056ccec.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) [`00bdd520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd520.md) [`00bdd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd550.md) [`00bdd680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd680.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0058fb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb84.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c59fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fa0.md) [`00c5a0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.62% / 新版 93.62%

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
      "site": "00591bc4",
      "value": [
        "leaf",
        "ram:58fb84:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0056ed2c",
      "value": [
        "leaf",
        "ram:56ccec:8"
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
      "00591b98",
      "PARAM",
      [
        "storage",
        "00bf0160",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591ba0",
      "PARAM",
      [
        "storage",
        "00bf0170",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591bc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056ccec"
      ]
    ]
  ],
  "added": [
    [
      "00591b98",
      "PARAM",
      [
        "storage",
        "00c6cd20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591ba0",
      "PARAM",
      [
        "storage",
        "00c6cd30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591bc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058fb84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ed2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ece8.md#insn-0056ed2c) · [`0056ecfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ece8.md#insn-0056ecfc) · [`0056ed00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ece8.md#insn-0056ed00)
- 新版 `00591bc4`（命令位置の公開資料なし） · `00591b94`（命令位置の公開資料なし） · `00591b98`（命令位置の公開資料なし）

~~~diff
- 0056ed2c ["INT_ADD", "register:40f0:8", ["const:56ed2c:8", "const:4:8"]]
- 0056ed2c ["CALL", null, ["ram:56ccec:8"]]
+ 00591bc4 ["INT_ADD", "register:40f0:8", ["const:591bc4:8", "const:4:8"]]
+ 00591bc4 ["CALL", null, ["ram:58fb84:8"]]
- 0056ed2c bytes f0f7ff97
+ 00591bc4 bytes f0f7ff97
- 0056ecfc ["COPY", "register:4008:8", ["const:bf0000:8"]]
+ 00591b94 ["COPY", "register:4008:8", ["const:c6c000:8"]]
- 0056ecfc bytes 013400d0
+ 00591b94 bytes c13600f0
- 0056ed00 ["COPY", "tmp:0:8", ["const:160:8"]]
- 0056ed00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056ed00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056ed00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591b98 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00591b98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591b98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591b98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056ed00 bytes 21800591
+ 00591b98 bytes 21803491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03d1cb034fa20f5c7320eb462f13fc90"></a>

### [`0056eda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eda4.md) → [`00591c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591c3c.md) FUN_00591c3c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0056ccec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056ccec.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) [`00bdd520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd520.md) [`00bdd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd550.md) [`00bdd680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd680.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0058fb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb84.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c59fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fa0.md) [`00c5a0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.90% / 新版 93.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591c7c",
      "incomplete_value": true,
      "site": "00591c88",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ede4",
      "incomplete_value": true,
      "site": "0056edf0",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591ca0",
      "incomplete_value": false,
      "site": "00591cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ee08",
      "incomplete_value": false,
      "site": "0056ee18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "definition_site": "00591ca8",
      "incomplete_value": false,
      "site": "00591cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ee10",
      "incomplete_value": false,
      "site": "0056ee18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "00591c74",
      "PARAM",
      [
        "storage",
        "00bf0160",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591c7c",
      "PARAM",
      [
        "storage",
        "00bf0170",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591ca0",
      "PARAM",
      [
        "storage",
        "00bf0188",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00591c74",
      "PARAM",
      [
        "storage",
        "00c6cd20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591c7c",
      "PARAM",
      [
        "storage",
        "00c6cd30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591ca0",
      "PARAM",
      [
        "storage",
        "00c6cd48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056edf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eda4.md#insn-0056edf0) · [`0056ee18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eda4.md#insn-0056ee18) · [`0056eec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eda4.md#insn-0056eec4)
- 新版 `00591c88`（命令位置の公開資料なし） · `00591cb0`（命令位置の公開資料なし） · `00591d5c`（命令位置の公開資料なし）

~~~diff
- 0056edf0 ["INT_ADD", "register:40f0:8", ["const:56edf0:8", "const:4:8"]]
- 0056edf0 ["CALL", null, ["callee:00c58210:8"]]
+ 00591c88 ["INT_ADD", "register:40f0:8", ["const:591c88:8", "const:4:8"]]
+ 00591c88 ["CALL", null, ["callee:00c58210:8"]]
- 0056edf0 bytes 74b21994
+ 00591c88 bytes 62191b94
- 0056ee18 ["INT_ADD", "register:40f0:8", ["const:56ee18:8", "const:4:8"]]
- 0056ee18 ["CALL", null, ["callee:00c58210:8"]]
+ 00591cb0 ["INT_ADD", "register:40f0:8", ["const:591cb0:8", "const:4:8"]]
+ 00591cb0 ["CALL", null, ["callee:00c58210:8"]]
- 0056ee18 bytes 6ab21994
+ 00591cb0 bytes 58191b94
- 0056eec4 ["INT_ADD", "register:40f0:8", ["const:56eec4:8", "const:4:8"]]
- 0056eec4 ["CALL", null, ["ram:56ccec:8"]]
+ 00591d5c ["INT_ADD", "register:40f0:8", ["const:591d5c:8", "const:4:8"]]
+ 00591d5c ["CALL", null, ["ram:58fb84:8"]]
- 0056eec4 bytes 8af7ff97
+ 00591d5c bytes 8af7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-043772695f0d8e2819f1333f348dac56"></a>

### [`0056eeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eeec.md) → [`00591d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591d84.md) FUN_00591d84

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0056ccec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056ccec.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) [`00bdd520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd520.md) [`00bdd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd550.md) [`00bdd680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd680.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0058fb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb84.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c59fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fa0.md) [`00c5a0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591df4",
      "incomplete_value": false,
      "site": "00591dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ef5c",
      "incomplete_value": false,
      "site": "0056ef64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591e10",
      "incomplete_value": false,
      "site": "00591e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ef78",
      "incomplete_value": false,
      "site": "0056ef88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "definition_site": "00591e18",
      "incomplete_value": false,
      "site": "00591e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ef80",
      "incomplete_value": false,
      "site": "0056ef88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "00591dc4",
      "PARAM",
      [
        "storage",
        "00bf0160",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591dcc",
      "PARAM",
      [
        "storage",
        "00bf0170",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591dec",
      "PARAM",
      [
        "storage",
        "00bf0188",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00591dc4",
      "PARAM",
      [
        "storage",
        "00c6cd20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591dcc",
      "PARAM",
      [
        "storage",
        "00c6cd30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591dec",
      "PARAM",
      [
        "storage",
        "00c6cd48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ef64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eeec.md#insn-0056ef64) · [`0056ef88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eeec.md#insn-0056ef88) · [`0056f058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056eeec.md#insn-0056f058)
- 新版 `00591dfc`（命令位置の公開資料なし） · `00591e20`（命令位置の公開資料なし） · `00591ef0`（命令位置の公開資料なし）

~~~diff
- 0056ef64 ["INT_ADD", "register:40f0:8", ["const:56ef64:8", "const:4:8"]]
- 0056ef64 ["CALL", null, ["callee:00c58210:8"]]
+ 00591dfc ["INT_ADD", "register:40f0:8", ["const:591dfc:8", "const:4:8"]]
+ 00591dfc ["CALL", null, ["callee:00c58210:8"]]
- 0056ef64 bytes 17b21994
+ 00591dfc bytes 05191b94
- 0056ef88 ["INT_ADD", "register:40f0:8", ["const:56ef88:8", "const:4:8"]]
- 0056ef88 ["CALL", null, ["callee:00c58210:8"]]
+ 00591e20 ["INT_ADD", "register:40f0:8", ["const:591e20:8", "const:4:8"]]
+ 00591e20 ["CALL", null, ["callee:00c58210:8"]]
- 0056ef88 bytes 0eb21994
+ 00591e20 bytes fc181b94
- 0056f058 ["INT_ADD", "register:40f0:8", ["const:56f058:8", "const:4:8"]]
- 0056f058 ["CALL", null, ["ram:56ccec:8"]]
+ 00591ef0 ["INT_ADD", "register:40f0:8", ["const:591ef0:8", "const:4:8"]]
+ 00591ef0 ["CALL", null, ["ram:58fb84:8"]]
- 0056f058 bytes 25f7ff97
+ 00591ef0 bytes 25f7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e1e67fe4e2a42d3aeda7a3466b3fb0c"></a>

### [`0056f1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f1e8.md) → [`00592080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592080.md) FUN_00592080

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056f270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f270.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00592108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592108.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005920a8",
      "incomplete_value": false,
      "site": "005920c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056f210",
      "incomplete_value": false,
      "site": "0056f22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005920b0",
      "incomplete_value": false,
      "site": "005920c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056f218",
      "incomplete_value": false,
      "site": "0056f22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
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
      "005920a8",
      "PARAM",
      [
        "storage",
        "00bf01b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005920b0",
      "PARAM",
      [
        "storage",
        "00bf01c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005920a8",
      "PARAM",
      [
        "storage",
        "00c6cd70",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005920b0",
      "PARAM",
      [
        "storage",
        "00c6cd80",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056f22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f1e8.md#insn-0056f22c) · [`0056f20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f1e8.md#insn-0056f20c) · [`0056f210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f1e8.md#insn-0056f210)
- 新版 `005920c4`（命令位置の公開資料なし） · `005920a4`（命令位置の公開資料なし） · `005920a8`（命令位置の公開資料なし）

~~~diff
- 0056f22c ["INT_ADD", "register:40f0:8", ["const:56f22c:8", "const:4:8"]]
- 0056f22c ["CALL", null, ["callee:00c58210:8"]]
+ 005920c4 ["INT_ADD", "register:40f0:8", ["const:5920c4:8", "const:4:8"]]
+ 005920c4 ["CALL", null, ["callee:00c58210:8"]]
- 0056f22c bytes 65b11994
+ 005920c4 bytes 53181b94
- 0056f20c ["COPY", "register:4008:8", ["const:bf0000:8"]]
+ 005920a4 ["COPY", "register:4008:8", ["const:c6c000:8"]]
- 0056f20c bytes 013400b0
+ 005920a4 bytes c13600d0
- 0056f210 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 0056f210 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056f210 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056f210 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005920a8 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 005920a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005920a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005920a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056f210 bytes 21c00691
+ 005920a8 bytes 21c03591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cae566c3ea91193ac1272319a19dace7"></a>

### [`0056f4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f4d8.md) → [`00592370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592370.md) FUN_00592370

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`004185a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004185a8.md) · 呼出先 2件 [`0056dee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dee0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0043b0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b0a8.md) · 呼出先 2件 [`00590d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00592394",
      "incomplete_value": false,
      "site": "005923a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056f4fc",
      "incomplete_value": false,
      "site": "0056f508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005923a0",
      "DATA",
      [
        "storage",
        "00bf04a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005923a0",
      "DATA",
      [
        "storage",
        "00c6d060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056f4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f4d8.md#insn-0056f4f0) · [`0056f4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f4d8.md#insn-0056f4f8) · [`0056f4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f4d8.md#insn-0056f4fc)
- 新版 `00592388`（命令位置の公開資料なし） · `00592390`（命令位置の公開資料なし） · `00592394`（命令位置の公開資料なし）

~~~diff
- 0056f4f0 ["INT_ADD", "register:40f0:8", ["const:56f4f0:8", "const:4:8"]]
- 0056f4f0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00592388 ["INT_ADD", "register:40f0:8", ["const:592388:8", "const:4:8"]]
+ 00592388 ["CALL", null, ["callee:00c57a90:8"]]
- 0056f4f0 bytes d4ae1994
+ 00592388 bytes c2151b94
- 0056f4f8 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00592390 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0056f4f8 bytes 083400b0
+ 00592390 bytes c83600f0
- 0056f4fc ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 0056f4fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056f4fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056f4fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592394 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 00592394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056f4fc bytes 08811291
+ 00592394 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-712e6d960ef253350192925f5c54a582"></a>

### [`0056f544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f544.md) → [`005923dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005923dc.md) FUN_005923dc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "005923f4",
      "incomplete_value": false,
      "site": "005923f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056f55c",
      "incomplete_value": false,
      "site": "0056f560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:50:8"
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
      "005923f8",
      "DATA",
      [
        "storage",
        "00bf0050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005923f8",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056f558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f544.md#insn-0056f558) · [`0056f55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f544.md#insn-0056f55c) · [`0056f570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f544.md#insn-0056f570)
- 新版 `005923f0`（命令位置の公開資料なし） · `005923f4`（命令位置の公開資料なし） · `00592408`（命令位置の公開資料なし）

~~~diff
- 0056f558 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 005923f0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056f558 bytes 083400b0
+ 005923f0 bytes c83600d0
- 0056f55c ["COPY", "tmp:0:8", ["const:50:8"]]
- 0056f55c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056f55c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056f55c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005923f4 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 005923f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005923f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005923f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056f55c bytes 08410191
+ 005923f4 bytes 08413091
- 0056f570 ["INT_ADD", "register:40f0:8", ["const:56f570:8", "const:4:8"]]
- 0056f570 ["CALL", null, ["callee:00c538e0:8"]]
+ 00592408 ["INT_ADD", "register:40f0:8", ["const:592408:8", "const:4:8"]]
+ 00592408 ["CALL", null, ["callee:00c538e0:8"]]
- 0056f570 bytes 489e1994
+ 00592408 bytes 36051b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc7eac1f2195926e1e27dd7e590850d7"></a>

### [`0056f5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f5e0.md) → [`00592478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592478.md) FUN_00592478

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00592490",
      "incomplete_value": false,
      "site": "00592494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056f5f8",
      "incomplete_value": false,
      "site": "0056f5fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:50:8"
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
      "00592494",
      "DATA",
      [
        "storage",
        "00bf0050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592494",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056f5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f5e0.md#insn-0056f5f4) · [`0056f5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f5e0.md#insn-0056f5f8) · [`0056f60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f5e0.md#insn-0056f60c)
- 新版 `0059248c`（命令位置の公開資料なし） · `00592490`（命令位置の公開資料なし） · `005924a4`（命令位置の公開資料なし）

~~~diff
- 0056f5f4 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0059248c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056f5f4 bytes 083400b0
+ 0059248c bytes c83600d0
- 0056f5f8 ["COPY", "tmp:0:8", ["const:50:8"]]
- 0056f5f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056f5f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056f5f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592490 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00592490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056f5f8 bytes 08410191
+ 00592490 bytes 08413091
- 0056f60c ["INT_ADD", "register:40f0:8", ["const:56f60c:8", "const:4:8"]]
- 0056f60c ["CALL", null, ["callee:00c538e0:8"]]
+ 005924a4 ["INT_ADD", "register:40f0:8", ["const:5924a4:8", "const:4:8"]]
+ 005924a4 ["CALL", null, ["callee:00c538e0:8"]]
- 0056f60c bytes 219e1994
+ 005924a4 bytes 0f051b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a95bc2fcc00e21908a4a2acc8c21535f"></a>

### [`0056f73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f73c.md) → [`005925d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005925d4.md) FUN_005925d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00bdd700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd700.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c5a150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a150.md)

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
      "definition_site": "005925ec",
      "incomplete_value": false,
      "site": "005925f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056f754",
      "incomplete_value": false,
      "site": "0056f758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "005925f0",
      "DATA",
      [
        "storage",
        "00bf0270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005925f0",
      "DATA",
      [
        "storage",
        "00c6ce30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056f750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f73c.md#insn-0056f750) · [`0056f754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f73c.md#insn-0056f754) · [`0056f75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f73c.md#insn-0056f75c)
- 新版 `005925e8`（命令位置の公開資料なし） · `005925ec`（命令位置の公開資料なし） · `005925f4`（命令位置の公開資料なし）

~~~diff
- 0056f750 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 005925e8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056f750 bytes 083400b0
+ 005925e8 bytes c83600d0
- 0056f754 ["COPY", "tmp:0:8", ["const:270:8"]]
- 0056f754 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056f754 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056f754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005925ec ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 005925ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005925ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005925ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056f754 bytes 08c10991
+ 005925ec bytes 08c13891
- 0056f75c ["INT_ADD", "register:40f0:8", ["const:56f75c:8", "const:4:8"]]
- 0056f75c ["CALL", null, ["callee:00555248:8"]]
+ 005925f4 ["INT_ADD", "register:40f0:8", ["const:5925f4:8", "const:4:8"]]
+ 005925f4 ["CALL", null, ["callee:00555248:8"]]
- 0056f75c bytes 150bff97
+ 005925f4 bytes 150bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62093b674ab94e37d088380a57eefc53"></a>

### [`0056f784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f784.md) → [`0059261c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059261c.md) FUN_0059261c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd700.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a150.md)

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
      "definition_site": "00592634",
      "incomplete_value": false,
      "site": "00592638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056f79c",
      "incomplete_value": false,
      "site": "0056f7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "00592638",
      "DATA",
      [
        "storage",
        "00bf0270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592638",
      "DATA",
      [
        "storage",
        "00c6ce30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056f798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f784.md#insn-0056f798) · [`0056f79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f784.md#insn-0056f79c) · [`0056f7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f784.md#insn-0056f7a4)
- 新版 `00592630`（命令位置の公開資料なし） · `00592634`（命令位置の公開資料なし） · `0059263c`（命令位置の公開資料なし）

~~~diff
- 0056f798 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00592630 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056f798 bytes 083400b0
+ 00592630 bytes c83600d0
- 0056f79c ["COPY", "tmp:0:8", ["const:270:8"]]
- 0056f79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056f79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056f79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592634 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 00592634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056f79c bytes 08c10991
+ 00592634 bytes 08c13891
- 0056f7a4 ["INT_ADD", "register:40f0:8", ["const:56f7a4:8", "const:4:8"]]
- 0056f7a4 ["CALL", null, ["callee:00555248:8"]]
+ 0059263c ["INT_ADD", "register:40f0:8", ["const:59263c:8", "const:4:8"]]
+ 0059263c ["CALL", null, ["callee:00555248:8"]]
- 0056f7a4 bytes 030bff97
+ 0059263c bytes 030bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff7d69a250f3a59223244ae779ce4227"></a>

### [`0056f9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f9c4.md) → [`0059285c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059285c.md) FUN_0059285c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00bdd710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd710.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c5a160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a160.md)

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
      "definition_site": "00592874",
      "incomplete_value": false,
      "site": "00592878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056f9dc",
      "incomplete_value": false,
      "site": "0056f9e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "00592878",
      "DATA",
      [
        "storage",
        "00bf0328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592878",
      "DATA",
      [
        "storage",
        "00c6cee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056f9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f9c4.md#insn-0056f9d8) · [`0056f9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f9c4.md#insn-0056f9dc) · [`0056f9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f9c4.md#insn-0056f9e4)
- 新版 `00592870`（命令位置の公開資料なし） · `00592874`（命令位置の公開資料なし） · `0059287c`（命令位置の公開資料なし）

~~~diff
- 0056f9d8 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00592870 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056f9d8 bytes 083400b0
+ 00592870 bytes c83600d0
- 0056f9dc ["COPY", "tmp:0:8", ["const:328:8"]]
- 0056f9dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056f9dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056f9dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592874 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 00592874 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592874 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592874 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056f9dc bytes 08a10c91
+ 00592874 bytes 08a13b91
- 0056f9e4 ["INT_ADD", "register:40f0:8", ["const:56f9e4:8", "const:4:8"]]
- 0056f9e4 ["CALL", null, ["callee:00555248:8"]]
+ 0059287c ["INT_ADD", "register:40f0:8", ["const:59287c:8", "const:4:8"]]
+ 0059287c ["CALL", null, ["callee:00555248:8"]]
- 0056f9e4 bytes 730aff97
+ 0059287c bytes 730aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d963a5fc57b4dcc39b2b1c75c80fa7be"></a>

### [`0056fa0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fa0c.md) → [`005928a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005928a4.md) FUN_005928a4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd710.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a160.md)

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
      "definition_site": "005928bc",
      "incomplete_value": false,
      "site": "005928c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056fa24",
      "incomplete_value": false,
      "site": "0056fa28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "005928c0",
      "DATA",
      [
        "storage",
        "00bf0328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005928c0",
      "DATA",
      [
        "storage",
        "00c6cee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056fa20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fa0c.md#insn-0056fa20) · [`0056fa24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fa0c.md#insn-0056fa24) · [`0056fa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fa0c.md#insn-0056fa2c)
- 新版 `005928b8`（命令位置の公開資料なし） · `005928bc`（命令位置の公開資料なし） · `005928c4`（命令位置の公開資料なし）

~~~diff
- 0056fa20 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 005928b8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056fa20 bytes 083400b0
+ 005928b8 bytes c83600d0
- 0056fa24 ["COPY", "tmp:0:8", ["const:328:8"]]
- 0056fa24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056fa24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056fa24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005928bc ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 005928bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005928bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005928bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056fa24 bytes 08a10c91
+ 005928bc bytes 08a13b91
- 0056fa2c ["INT_ADD", "register:40f0:8", ["const:56fa2c:8", "const:4:8"]]
- 0056fa2c ["CALL", null, ["callee:00555248:8"]]
+ 005928c4 ["INT_ADD", "register:40f0:8", ["const:5928c4:8", "const:4:8"]]
+ 005928c4 ["CALL", null, ["callee:00555248:8"]]
- 0056fa2c bytes 610aff97
+ 005928c4 bytes 610aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3763cd6f24b26abde60a7dd8ed141ea"></a>

### [`0056faf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056faf0.md) → [`00592988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592988.md) FUN_00592988

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00bdd720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd720.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c5a170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a170.md)

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
      "definition_site": "005929a0",
      "incomplete_value": false,
      "site": "005929a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056fb08",
      "incomplete_value": false,
      "site": "0056fb0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "005929a4",
      "DATA",
      [
        "storage",
        "00bf03e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005929a4",
      "DATA",
      [
        "storage",
        "00c6cfa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056fb04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056faf0.md#insn-0056fb04) · [`0056fb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056faf0.md#insn-0056fb08) · [`0056fb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056faf0.md#insn-0056fb10)
- 新版 `0059299c`（命令位置の公開資料なし） · `005929a0`（命令位置の公開資料なし） · `005929a8`（命令位置の公開資料なし）

~~~diff
- 0056fb04 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0059299c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056fb04 bytes 083400b0
+ 0059299c bytes c83600d0
- 0056fb08 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0056fb08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056fb08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056fb08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005929a0 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 005929a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005929a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005929a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056fb08 bytes 08810f91
+ 005929a0 bytes 08813e91
- 0056fb10 ["INT_ADD", "register:40f0:8", ["const:56fb10:8", "const:4:8"]]
- 0056fb10 ["CALL", null, ["callee:00555248:8"]]
+ 005929a8 ["INT_ADD", "register:40f0:8", ["const:5929a8:8", "const:4:8"]]
+ 005929a8 ["CALL", null, ["callee:00555248:8"]]
- 0056fb10 bytes 280aff97
+ 005929a8 bytes 280aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f53103020c97e0b276f521e8d3019b0"></a>

### [`0056fb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fb38.md) → [`005929d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005929d0.md) FUN_005929d0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd720.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a170.md)

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
      "definition_site": "005929e8",
      "incomplete_value": false,
      "site": "005929ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056fb50",
      "incomplete_value": false,
      "site": "0056fb54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "005929ec",
      "DATA",
      [
        "storage",
        "00bf03e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005929ec",
      "DATA",
      [
        "storage",
        "00c6cfa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056fb4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fb38.md#insn-0056fb4c) · [`0056fb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fb38.md#insn-0056fb50) · [`0056fb58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fb38.md#insn-0056fb58)
- 新版 `005929e4`（命令位置の公開資料なし） · `005929e8`（命令位置の公開資料なし） · `005929f0`（命令位置の公開資料なし）

~~~diff
- 0056fb4c ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 005929e4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056fb4c bytes 083400b0
+ 005929e4 bytes c83600d0
- 0056fb50 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0056fb50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056fb50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056fb50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005929e8 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 005929e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005929e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005929e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056fb50 bytes 08810f91
+ 005929e8 bytes 08813e91
- 0056fb58 ["INT_ADD", "register:40f0:8", ["const:56fb58:8", "const:4:8"]]
- 0056fb58 ["CALL", null, ["callee:00555248:8"]]
+ 005929f0 ["INT_ADD", "register:40f0:8", ["const:5929f0:8", "const:4:8"]]
+ 005929f0 ["CALL", null, ["callee:00555248:8"]]
- 0056fb58 bytes 160aff97
+ 005929f0 bytes 160aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24c7d3db3a898430cc8b567806339ca4"></a>

### [`0056fc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fc94.md) → [`00592b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592b2c.md) FUN_00592b2c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0056e7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e7f4.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdd760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd760.md)
- 新版 呼出元 1件 [`0059168c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059168c.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a1b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592b54",
      "incomplete_value": false,
      "site": "00592b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056fcbc",
      "incomplete_value": false,
      "site": "0056fcd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "definition_site": "00592b70",
      "incomplete_value": false,
      "site": "00592b70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056fcd8",
      "incomplete_value": false,
      "site": "0056fcd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "00592b6c",
      "DATA",
      [
        "storage",
        "00bf0418",
        null,
        "undefined *"
      ]
    ],
    [
      "00592b70",
      "DATA",
      [
        "storage",
        "00bf0468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592b6c",
      "DATA",
      [
        "storage",
        "00c6cfd8",
        null,
        "undefined *"
      ]
    ],
    [
      "00592b70",
      "DATA",
      [
        "storage",
        "00c6d028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056fcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fc94.md#insn-0056fcac) · [`0056fcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fc94.md#insn-0056fcb8) · [`0056fcbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fc94.md#insn-0056fcbc)
- 新版 `00592b44`（命令位置の公開資料なし） · `00592b50`（命令位置の公開資料なし） · `00592b54`（命令位置の公開資料なし）

~~~diff
- 0056fcac ["INT_ADD", "register:40f0:8", ["const:56fcac:8", "const:4:8"]]
- 0056fcac ["CALL", null, ["callee:00c57a90:8"]]
+ 00592b44 ["INT_ADD", "register:40f0:8", ["const:592b44:8", "const:4:8"]]
+ 00592b44 ["CALL", null, ["callee:00c57a90:8"]]
- 0056fcac bytes e5ac1994
+ 00592b44 bytes d3131b94
- 0056fcb8 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00592b50 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056fcb8 bytes 083400b0
+ 00592b50 bytes c83600d0
- 0056fcbc ["COPY", "tmp:0:8", ["const:418:8"]]
- 0056fcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056fcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056fcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592b54 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 00592b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056fcbc bytes 08611091
+ 00592b54 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16dc61977ee556b92aa3f75553e1ef71"></a>

### [`0056fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fddc.md) → [`00592c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592c74.md) FUN_00592c74

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592c8c",
      "incomplete_value": false,
      "site": "00592c90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056fdf4",
      "incomplete_value": false,
      "site": "0056fdf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "00592c90",
      "DATA",
      [
        "storage",
        "00bf0468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592c90",
      "DATA",
      [
        "storage",
        "00c6d028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fddc.md#insn-0056fdf0) · [`0056fdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fddc.md#insn-0056fdf4) · [`0056fe08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fddc.md#insn-0056fe08)
- 新版 `00592c88`（命令位置の公開資料なし） · `00592c8c`（命令位置の公開資料なし） · `00592ca0`（命令位置の公開資料なし）

~~~diff
- 0056fdf0 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00592c88 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0056fdf0 bytes 083400b0
+ 00592c88 bytes c83600f0
- 0056fdf4 ["COPY", "tmp:0:8", ["const:468:8"]]
- 0056fdf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056fdf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056fdf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592c8c ["COPY", "tmp:0:8", ["const:28:8"]]
+ 00592c8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056fdf4 bytes 08a11191
+ 00592c8c bytes 08a10091
- 0056fe08 ["INT_ADD", "register:40f0:8", ["const:56fe08:8", "const:4:8"]]
- 0056fe08 ["CALL", null, ["callee:00c538e0:8"]]
+ 00592ca0 ["INT_ADD", "register:40f0:8", ["const:592ca0:8", "const:4:8"]]
+ 00592ca0 ["CALL", null, ["callee:00c538e0:8"]]
- 0056fe08 bytes 229c1994
+ 00592ca0 bytes 10031b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb0508e0894d634bef7bf0c9685038ff"></a>

### [`0056fea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fea8.md) → [`00592d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592d40.md) FUN_00592d40

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00592d58",
      "incomplete_value": false,
      "site": "00592d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056fec0",
      "incomplete_value": false,
      "site": "0056fec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "00592d5c",
      "DATA",
      [
        "storage",
        "00bf0468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592d5c",
      "DATA",
      [
        "storage",
        "00c6d028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056febc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fea8.md#insn-0056febc) · [`0056fec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fea8.md#insn-0056fec0) · [`0056fed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056fea8.md#insn-0056fed4)
- 新版 `00592d54`（命令位置の公開資料なし） · `00592d58`（命令位置の公開資料なし） · `00592d6c`（命令位置の公開資料なし）

~~~diff
- 0056febc ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00592d54 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0056febc bytes 083400b0
+ 00592d54 bytes c83600f0
- 0056fec0 ["COPY", "tmp:0:8", ["const:468:8"]]
- 0056fec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056fec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056fec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592d58 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 00592d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056fec0 bytes 08a11191
+ 00592d58 bytes 08a10091
- 0056fed4 ["INT_ADD", "register:40f0:8", ["const:56fed4:8", "const:4:8"]]
- 0056fed4 ["CALL", null, ["callee:00c538e0:8"]]
+ 00592d6c ["INT_ADD", "register:40f0:8", ["const:592d6c:8", "const:4:8"]]
+ 00592d6c ["CALL", null, ["callee:00c538e0:8"]]
- 0056fed4 bytes ef9b1994
+ 00592d6c bytes dd021b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f27d3f3c7e77186a15dca35c50419ae"></a>

### [`005700e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005700e0.md) → [`00592f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592f78.md) FUN_00592f78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb080.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00592fb0",
      "incomplete_value": false,
      "site": "00592fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570118",
      "incomplete_value": false,
      "site": "0057012c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "definition_site": "00592fb8",
      "incomplete_value": false,
      "site": "00592fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570120",
      "incomplete_value": false,
      "site": "0057012c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "00592fb0",
      "PARAM",
      [
        "storage",
        "00bf0160",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00592fb8",
      "PARAM",
      [
        "storage",
        "00bf0170",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00592fb0",
      "PARAM",
      [
        "storage",
        "00c6cd20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00592fb8",
      "PARAM",
      [
        "storage",
        "00c6cd30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057012c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005700e0.md#insn-0057012c) · [`00570114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005700e0.md#insn-00570114) · [`00570118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005700e0.md#insn-00570118)
- 新版 `00592fc4`（命令位置の公開資料なし） · `00592fac`（命令位置の公開資料なし） · `00592fb0`（命令位置の公開資料なし）

~~~diff
- 0057012c ["INT_ADD", "register:40f0:8", ["const:57012c:8", "const:4:8"]]
- 0057012c ["CALL", null, ["callee:00c58210:8"]]
+ 00592fc4 ["INT_ADD", "register:40f0:8", ["const:592fc4:8", "const:4:8"]]
+ 00592fc4 ["CALL", null, ["callee:00c58210:8"]]
- 0057012c bytes a5ad1994
+ 00592fc4 bytes 93141b94
- 00570114 ["COPY", "register:4008:8", ["const:bf0000:8"]]
+ 00592fac ["COPY", "register:4008:8", ["const:c6c000:8"]]
- 00570114 bytes 01340090
+ 00592fac bytes c13600d0
- 00570118 ["COPY", "tmp:0:8", ["const:160:8"]]
- 00570118 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00570118 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00570118 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00592fb0 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00592fb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00592fb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00592fb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00570118 bytes 21800591
+ 00592fb0 bytes 21803491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8016d80f422ebb16163e72f76ea0a112"></a>

### [`0057029c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/0057029c.md) → [`00593134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593134.md) FUN_00593134

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb080.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00593174",
      "incomplete_value": true,
      "site": "00593180",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005702dc",
      "incomplete_value": true,
      "site": "005702e8",
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
            "const:170:8"
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
      "0059316c",
      "PARAM",
      [
        "storage",
        "00bf0160",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00593174",
      "PARAM",
      [
        "storage",
        "00bf0170",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0059316c",
      "PARAM",
      [
        "storage",
        "00c6cd20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00593174",
      "PARAM",
      [
        "storage",
        "00c6cd30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005702e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/0057029c.md#insn-005702e8) · [`005702d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/0057029c.md#insn-005702d0) · [`005702d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/0057029c.md#insn-005702d4)
- 新版 `00593180`（命令位置の公開資料なし） · `00593168`（命令位置の公開資料なし） · `0059316c`（命令位置の公開資料なし）

~~~diff
- 005702e8 ["INT_ADD", "register:40f0:8", ["const:5702e8:8", "const:4:8"]]
- 005702e8 ["CALL", null, ["callee:00c58210:8"]]
+ 00593180 ["INT_ADD", "register:40f0:8", ["const:593180:8", "const:4:8"]]
+ 00593180 ["CALL", null, ["callee:00c58210:8"]]
- 005702e8 bytes 36ad1994
+ 00593180 bytes 24141b94
- 005702d0 ["COPY", "register:4008:8", ["const:bf0000:8"]]
+ 00593168 ["COPY", "register:4008:8", ["const:c6c000:8"]]
- 005702d0 bytes 01340090
+ 00593168 bytes c13600b0
- 005702d4 ["COPY", "tmp:0:8", ["const:160:8"]]
- 005702d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005702d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005702d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0059316c ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 0059316c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0059316c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0059316c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005702d4 bytes 21800591
+ 0059316c bytes 21803491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aad542debf249c2be4f7bf1f48e249e2"></a>

### [`005704a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005704a8.md) → [`00593340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md) FUN_00593340

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00570dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570dcc.md) · 呼出先 14件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00424230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424230.md) [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`005708ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005708ec.md)
- 新版 呼出元 1件 [`00593c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593c64.md) · 呼出先 14件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00446d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d30.md) [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00593784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593784.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "00593380",
      "incomplete_value": false,
      "site": "00593384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005704e8",
      "incomplete_value": false,
      "site": "005704ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "00593384",
      "DATA",
      [
        "storage",
        "00bf04f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593384",
      "DATA",
      [
        "storage",
        "00c6d0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005704e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005704a8.md#insn-005704e4) · [`005704e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005704a8.md#insn-005704e8) · [`005704f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005704a8.md#insn-005704f0)
- 新版 `0059337c`（命令位置の公開資料なし） · `00593380`（命令位置の公開資料なし） · `00593388`（命令位置の公開資料なし）

~~~diff
- 005704e4 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0059337c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005704e4 bytes 08340090
+ 0059337c bytes c83600d0
- 005704e8 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 005704e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005704e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005704e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593380 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 00593380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005704e8 bytes 08c11391
+ 00593380 bytes 08c10291
- 005704f0 ["INT_ADD", "register:40f0:8", ["const:5704f0:8", "const:4:8"]]
- 005704f0 ["CALL", null, ["callee:00555248:8"]]
+ 00593388 ["INT_ADD", "register:40f0:8", ["const:593388:8", "const:4:8"]]
+ 00593388 ["CALL", null, ["callee:00555248:8"]]
- 005704f0 bytes b007ff97
+ 00593388 bytes b007ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-597b66ad864d150665a36ead62e70421"></a>

### [`00570dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570dcc.md) → [`00593c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593c64.md) FUN_00593c64

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0056e384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e384.md) · 呼出先 21件 [`005704a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005704a8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`0059121c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059121c.md) · 呼出先 21件 [`00593340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00594150",
      "incomplete_value": false,
      "site": "0059415c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005712b8",
      "incomplete_value": false,
      "site": "005712c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00593d50",
      "incomplete_value": false,
      "site": "00593d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570eb8",
      "incomplete_value": false,
      "site": "00570ec4",
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
            "const:7ba:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00593d7c",
      "incomplete_value": false,
      "site": "00593d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570ee4",
      "incomplete_value": false,
      "site": "00570eec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:333:8"
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
      "00593d50",
      "PARAM",
      [
        "storage",
        "002a57ba",
        null,
        "string"
      ]
    ],
    [
      "00593d7c",
      "PARAM",
      [
        "storage",
        "002a4333",
        null,
        null
      ]
    ],
    [
      "00593e94",
      "PARAM",
      [
        "storage",
        "00290c2b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00593d50",
      "PARAM",
      [
        "storage",
        "002b61e8",
        null,
        "string"
      ]
    ],
    [
      "00593d7c",
      "PARAM",
      [
        "storage",
        "002b4ba0",
        null,
        null
      ]
    ],
    [
      "00593e94",
      "PARAM",
      [
        "storage",
        "002a016d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570dcc.md#insn-00570ec4) · [`00570eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570dcc.md#insn-00570eec) · [`00571008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570dcc.md#insn-00571008)
- 新版 `00593d5c`（命令位置の公開資料なし） · `00593d84`（命令位置の公開資料なし） · `00593ea0`（命令位置の公開資料なし）

~~~diff
- 00570ec4 ["INT_ADD", "register:40f0:8", ["const:570ec4:8", "const:4:8"]]
- 00570ec4 ["CALL", null, ["callee:00c57b60:8"]]
+ 00593d5c ["INT_ADD", "register:40f0:8", ["const:593d5c:8", "const:4:8"]]
+ 00593d5c ["CALL", null, ["callee:00c57b60:8"]]
- 00570ec4 bytes 93a81994
+ 00593d5c bytes 810f1b94
- 00570eec ["INT_ADD", "register:40f0:8", ["const:570eec:8", "const:4:8"]]
- 00570eec ["CALL", null, ["callee:00c57b70:8"]]
+ 00593d84 ["INT_ADD", "register:40f0:8", ["const:593d84:8", "const:4:8"]]
+ 00593d84 ["CALL", null, ["callee:00c57b70:8"]]
- 00570eec bytes 8da81994
+ 00593d84 bytes 7b0f1b94
- 00571008 ["INT_ADD", "register:40f0:8", ["const:571008:8", "const:4:8"]]
- 00571008 ["CALL", null, ["callee:00c57b60:8"]]
+ 00593ea0 ["INT_ADD", "register:40f0:8", ["const:593ea0:8", "const:4:8"]]
+ 00593ea0 ["CALL", null, ["callee:00c57b60:8"]]
- 00571008 bytes 42a81994
+ 00593ea0 bytes 300f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea6654c5cf3c0d49ea5e7eaa0d73b59"></a>

### [`00571a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a08.md) → [`005948a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948a0.md) FUN_005948a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`005323b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323b0.md) [`00571468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571468.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd7f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00594300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a240.md)

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
      "definition_site": "005948b4",
      "incomplete_value": false,
      "site": "005948b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571a1c",
      "incomplete_value": false,
      "site": "00571a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "005948b8",
      "DATA",
      [
        "storage",
        "00bf04f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005948b8",
      "DATA",
      [
        "storage",
        "00c6d0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a08.md#insn-00571a18) · [`00571a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a08.md#insn-00571a1c) · [`00571a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a08.md#insn-00571a24)
- 新版 `005948b0`（命令位置の公開資料なし） · `005948b4`（命令位置の公開資料なし） · `005948bc`（命令位置の公開資料なし）

~~~diff
- 00571a18 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 005948b0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00571a18 bytes e83300f0
+ 005948b0 bytes c83600b0
- 00571a1c ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 00571a1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571a1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571a1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005948b4 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 005948b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005948b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005948b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571a1c bytes 08c11391
+ 005948b4 bytes 08c10291
- 00571a24 ["INT_ADD", "register:40f0:8", ["const:571a24:8", "const:4:8"]]
- 00571a24 ["CALL", null, ["callee:00555248:8"]]
+ 005948bc ["INT_ADD", "register:40f0:8", ["const:5948bc:8", "const:4:8"]]
+ 005948bc ["CALL", null, ["callee:00555248:8"]]
- 00571a24 bytes 6302ff97
+ 005948bc bytes 6302ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f12b79d17217321a9888d4e1385b6210"></a>

### [`00571a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a60.md) → [`005948f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948f8.md) FUN_005948f8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005655f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005655f0.md) · 呼出先 7件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00571c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571c94.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00588488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588488.md) · 呼出先 7件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00594b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059492c",
      "incomplete_value": false,
      "site": "0059493c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571a94",
      "incomplete_value": false,
      "site": "00571aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:598:8"
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
      "definition_site": "00594a60",
      "incomplete_value": true,
      "site": "00594a6c",
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
                "const:cf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571bc8",
      "incomplete_value": true,
      "site": "00571bd4",
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
                "const:628:8"
              ]
            ]
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
      "0059493c",
      "DATA",
      [
        "storage",
        "00bf0598",
        null,
        "undefined *"
      ]
    ],
    [
      "00594a60",
      "READ",
      [
        "storage",
        "002b2628",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0059493c",
      "DATA",
      [
        "storage",
        "00c6d158",
        null,
        "undefined *"
      ]
    ],
    [
      "00594a60",
      "READ",
      [
        "storage",
        "002c3cf8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a60.md#insn-00571a90) · [`00571a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a60.md#insn-00571a94) · [`00571ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a60.md#insn-00571ac8)
- 新版 `00594928`（命令位置の公開資料なし） · `0059492c`（命令位置の公開資料なし） · `00594960`（命令位置の公開資料なし）

~~~diff
- 00571a90 ["COPY", "register:4048:8", ["const:bf0000:8"]]
+ 00594928 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00571a90 bytes e93300f0
+ 00594928 bytes c93600b0
- 00571a94 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00571a94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00571a94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00571a94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059492c ["COPY", "tmp:0:8", ["const:158:8"]]
+ 0059492c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059492c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059492c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00571a94 bytes 29611691
+ 0059492c bytes 29610591
- 00571ac8 ["INT_ADD", "register:40f0:8", ["const:571ac8:8", "const:4:8"]]
- 00571ac8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00594960 ["INT_ADD", "register:40f0:8", ["const:594960:8", "const:4:8"]]
+ 00594960 ["CALL", null, ["callee:00c57a90:8"]]
- 00571ac8 bytes 5ea51994
+ 00594960 bytes 4c0c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17503fab7edbd788cbcae40e5cecc1b3"></a>

### [`00571c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571c94.md) → [`00594b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md) FUN_00594b2c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00571a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a60.md) · 呼出先 12件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c654.md) [`0053c668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c668.md) [`0053c688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c688.md) [`005722b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005722b8.md)
- 新版 呼出元 1件 [`005948f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948f8.md) · 呼出先 12件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4ec.md) [`0055f500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f500.md) [`0055f520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f520.md) [`00595150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595150.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.23% / 新版 97.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00594cb4",
      "incomplete_value": true,
      "site": "00594cc4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:b1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571e1c",
      "incomplete_value": true,
      "site": "00571e2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:70c:8"
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
      "00594cb4",
      "READ",
      [
        "storage",
        "0029f70c",
        null,
        "string"
      ]
    ],
    [
      "00594cb8",
      "READ",
      [
        "storage",
        "0029f717",
        null,
        "string"
      ]
    ],
    [
      "00594cbc",
      "READ",
      [
        "storage",
        "002b1030",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00594cb4",
      "READ",
      [
        "storage",
        "002afb1f",
        null,
        "string"
      ]
    ],
    [
      "00594cb8",
      "READ",
      [
        "storage",
        "002afb2a",
        null,
        "string"
      ]
    ],
    [
      "00594cbc",
      "READ",
      [
        "storage",
        "002c2640",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571c94.md#insn-00571ce8) · [`00571d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571c94.md#insn-00571d04) · [`00571d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571c94.md#insn-00571d24)
- 新版 `00594b80`（命令位置の公開資料なし） · `00594b9c`（命令位置の公開資料なし） · `00594bbc`（命令位置の公開資料なし）

~~~diff
- 00571ce8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00571ce8 ["INT_ADD", "register:40f0:8", ["const:571ce8:8", "const:4:8"]]
- 00571ce8 ["CALLIND", null, ["register:0:8"]]
+ 00594b80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00594b80 ["INT_ADD", "register:40f0:8", ["const:594b80:8", "const:4:8"]]
+ 00594b80 ["CALLIND", null, ["register:0:8"]]
- 00571ce8 bytes 00013fd6
+ 00594b80 bytes 00013fd6
- 00571d04 ["COPY", "register:0:8", ["register:4048:8"]]
- 00571d04 ["INT_ADD", "register:40f0:8", ["const:571d04:8", "const:4:8"]]
- 00571d04 ["CALLIND", null, ["register:0:8"]]
+ 00594b9c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00594b9c ["INT_ADD", "register:40f0:8", ["const:594b9c:8", "const:4:8"]]
+ 00594b9c ["CALLIND", null, ["register:0:8"]]
- 00571d04 bytes 20013fd6
+ 00594b9c bytes 20013fd6
- 00571d24 ["INT_ADD", "register:40f0:8", ["const:571d24:8", "const:4:8"]]
- 00571d24 ["CALL", null, ["callee:0055f484:8"]]
+ 00594bbc ["INT_ADD", "register:40f0:8", ["const:594bbc:8", "const:4:8"]]
+ 00594bbc ["CALL", null, ["callee:0055f484:8"]]
- 00571d24 bytes 322aff97
+ 00594bbc bytes 322aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecaa59bd88dbcc0eb23a5c6c7faa62f8"></a>

### [`005720e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005720e0.md) → [`00594f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594f78.md) FUN_00594f78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005656c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005656c4.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0058855c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/0058855c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00594f90",
      "incomplete_value": false,
      "site": "00594f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005720f8",
      "incomplete_value": false,
      "site": "005720fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "00594f94",
      "DATA",
      [
        "storage",
        "00bf0598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594f94",
      "DATA",
      [
        "storage",
        "00c6d158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005720f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005720e0.md#insn-005720f4) · [`005720f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005720e0.md#insn-005720f8) · [`00572108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005720e0.md#insn-00572108)
- 新版 `00594f8c`（命令位置の公開資料なし） · `00594f90`（命令位置の公開資料なし） · `00594fa0`（命令位置の公開資料なし）

~~~diff
- 005720f4 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00594f8c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005720f4 bytes e83300d0
+ 00594f8c bytes c83600b0
- 005720f8 ["COPY", "tmp:0:8", ["const:598:8"]]
- 005720f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005720f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005720f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594f90 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00594f90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594f90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594f90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005720f8 bytes 08611691
+ 00594f90 bytes 08610591
- 00572108 ["INT_ADD", "register:40f0:8", ["const:572108:8", "const:4:8"]]
- 00572108 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00594fa0 ["INT_ADD", "register:40f0:8", ["const:594fa0:8", "const:4:8"]]
+ 00594fa0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00572108 bytes d6a31994
+ 00594fa0 bytes c40a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0619b3cc52294b0816ae9c1f12300819"></a>

### [`00572494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572494.md) → [`0059532c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059532c.md) FUN_0059532c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00595404",
      "incomplete_value": false,
      "site": "00595408",
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
            "const:5a2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057256c",
      "incomplete_value": false,
      "site": "00572570",
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
            "const:949:8"
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
      "definition_site": "00595434",
      "incomplete_value": false,
      "site": "00595438",
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
    "old": {
      "definition_site": "0057259c",
      "incomplete_value": false,
      "site": "005725a0",
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
      "005953a4",
      "PARAM",
      [
        "storage",
        "0029e335",
        null,
        null
      ]
    ],
    [
      "005953a4",
      "PARAM",
      [
        "storage",
        "0028f920",
        null,
        "string"
      ]
    ],
    [
      "00595404",
      "PARAM",
      [
        "storage",
        "00297949",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005953a4",
      "PARAM",
      [
        "storage",
        "002ae6ba",
        null,
        null
      ]
    ],
    [
      "005953a4",
      "PARAM",
      [
        "storage",
        "0029ed60",
        null,
        "string"
      ]
    ],
    [
      "00595404",
      "PARAM",
      [
        "storage",
        "002a75a2",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572494.md#insn-00572570) · [`005725a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572494.md#insn-005725a0) · [`005724f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572494.md#insn-005724f4)
- 新版 `00595408`（命令位置の公開資料なし） · `00595438`（命令位置の公開資料なし） · `0059538c`（命令位置の公開資料なし）

~~~diff
- 00572570 ["INT_ADD", "register:40f0:8", ["const:572570:8", "const:4:8"]]
- 00572570 ["CALL", null, ["callee:00c57be0:8"]]
+ 00595408 ["INT_ADD", "register:40f0:8", ["const:595408:8", "const:4:8"]]
+ 00595408 ["CALL", null, ["callee:00c57be0:8"]]
- 00572570 bytes 08a31994
+ 00595408 bytes f6091b94
- 005725a0 ["INT_ADD", "register:40f0:8", ["const:5725a0:8", "const:4:8"]]
- 005725a0 ["CALL", null, ["callee:00c57be0:8"]]
+ 00595438 ["INT_ADD", "register:40f0:8", ["const:595438:8", "const:4:8"]]
+ 00595438 ["CALL", null, ["callee:00c57be0:8"]]
- 005725a0 bytes fca21994
+ 00595438 bytes ea091b94
- 005724f4 ["COPY", "register:4048:8", ["const:29e000:8"]]
+ 0059538c ["COPY", "register:4048:8", ["const:2ae000:8"]]
- 005724f4 bytes 69e9ff90
+ 0059538c bytes c9e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6abf4ab5f1f4e1ced2504e7b3a3ed38a"></a>

### [`005726a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005726a8.md) → [`00595540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595540.md) FUN_00595540

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) · 呼出先 2件 [`005727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 1件 [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) · 呼出先 2件 [`0059564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "00595554",
      "incomplete_value": false,
      "site": "0059555c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005726bc",
      "incomplete_value": false,
      "site": "005726c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "0059555c",
      "DATA",
      [
        "storage",
        "00bf0628",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059555c",
      "DATA",
      [
        "storage",
        "00c6d1e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005726b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005726a8.md#insn-005726b8) · [`005726bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005726a8.md#insn-005726bc) · [`005726ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005726a8.md#insn-005726ec)
- 新版 `00595550`（命令位置の公開資料なし） · `00595554`（命令位置の公開資料なし） · `00595584`（命令位置の公開資料なし）

~~~diff
- 005726b8 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00595550 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005726b8 bytes e83300d0
+ 00595550 bytes c8360090
- 005726bc ["COPY", "tmp:0:8", ["const:628:8"]]
- 005726bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005726bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005726bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595554 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 00595554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005726bc bytes 08a11891
+ 00595554 bytes 08a10791
- 005726ec ["INT_ADD", "register:40f0:8", ["const:5726ec:8", "const:4:8"]]
- 005726ec ["CALL", null, ["callee:00c538b0:8"]]
+ 00595584 ["INT_ADD", "register:40f0:8", ["const:595584:8", "const:4:8"]]
+ 00595584 ["CALL", null, ["callee:00c538b0:8"]]
- 005726ec bytes dd911994
+ 00595584 bytes cbf81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7af754d4f8615462c3b7f4dbff341cb1"></a>

### [`005727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md) → [`0059564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md) FUN_0059564c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005726a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005726a8.md) · 呼出先 4件 [`00572998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572998.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00595540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595540.md) · 呼出先 4件 [`00595830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005956a0",
      "incomplete_value": false,
      "site": "005956a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572808",
      "incomplete_value": false,
      "site": "0057280c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
      "definition_site": "005956f4",
      "incomplete_value": false,
      "site": "005956f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057285c",
      "incomplete_value": false,
      "site": "00572860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "005956a4",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ],
    [
      "005956f8",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005956a4",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ],
    [
      "005956f8",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005727d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md#insn-005727d0) · [`005727f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md#insn-005727f0) · [`00572804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md#insn-00572804)
- 新版 `00595668`（命令位置の公開資料なし） · `00595688`（命令位置の公開資料なし） · `0059569c`（命令位置の公開資料なし）

~~~diff
- 005727d0 ["INT_ADD", "register:40f0:8", ["const:5727d0:8", "const:4:8"]]
- 005727d0 ["CALL", null, ["callee:00595830:8"]]
+ 00595668 ["INT_ADD", "register:40f0:8", ["const:595668:8", "const:4:8"]]
+ 00595668 ["CALL", null, ["callee:00595830:8"]]
- 005727d0 bytes 72000094
+ 00595668 bytes 72000094
- 005727f0 ["INT_ADD", "register:40f0:8", ["const:5727f0:8", "const:4:8"]]
- 005727f0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00595688 ["INT_ADD", "register:40f0:8", ["const:595688:8", "const:4:8"]]
+ 00595688 ["CALL", null, ["callee:00c57a90:8"]]
- 005727f0 bytes 14a21994
+ 00595688 bytes 02091b94
- 00572804 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0059569c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00572804 bytes e83300d0
+ 0059569c bytes c8360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08db55c7bd9b508bc2d56c592dade27c"></a>

### [`005728ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005728ac.md) → [`00595744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595744.md) FUN_00595744

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059575c",
      "incomplete_value": false,
      "site": "00595764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005728c4",
      "incomplete_value": false,
      "site": "005728cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "00595764",
      "DATA",
      [
        "storage",
        "00bf0628",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00595764",
      "DATA",
      [
        "storage",
        "00c6d1e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005728c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005728ac.md#insn-005728c0) · [`005728c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005728ac.md#insn-005728c4) · [`005728dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005728ac.md#insn-005728dc)
- 新版 `00595758`（命令位置の公開資料なし） · `0059575c`（命令位置の公開資料なし） · `00595774`（命令位置の公開資料なし）

~~~diff
- 005728c0 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00595758 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005728c0 bytes e83300d0
+ 00595758 bytes c8360090
- 005728c4 ["COPY", "tmp:0:8", ["const:628:8"]]
- 005728c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005728c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005728c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059575c ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 0059575c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059575c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059575c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005728c4 bytes 08a11891
+ 0059575c bytes 08a10791
- 005728dc ["COPY", "register:0:8", ["register:4040:8"]]
- 005728dc ["INT_ADD", "register:40f0:8", ["const:5728dc:8", "const:4:8"]]
- 005728dc ["CALLIND", null, ["register:0:8"]]
+ 00595774 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00595774 ["INT_ADD", "register:40f0:8", ["const:595774:8", "const:4:8"]]
+ 00595774 ["CALLIND", null, ["register:0:8"]]
- 005728dc bytes 00013fd6
+ 00595774 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a40bc5a1f4bc0a09509f4990c2553fb8"></a>

### [`00572924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572924.md) → [`005957bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/005957bc.md) FUN_005957bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "005957d4",
      "incomplete_value": false,
      "site": "005957dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057293c",
      "incomplete_value": false,
      "site": "00572944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "005957dc",
      "DATA",
      [
        "storage",
        "00bf0628",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005957dc",
      "DATA",
      [
        "storage",
        "00c6d1e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572924.md#insn-00572938) · [`0057293c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572924.md#insn-0057293c) · [`00572954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572924.md#insn-00572954)
- 新版 `005957d0`（命令位置の公開資料なし） · `005957d4`（命令位置の公開資料なし） · `005957ec`（命令位置の公開資料なし）

~~~diff
- 00572938 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 005957d0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00572938 bytes e83300d0
+ 005957d0 bytes c8360090
- 0057293c ["COPY", "tmp:0:8", ["const:628:8"]]
- 0057293c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057293c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057293c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005957d4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 005957d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005957d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005957d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057293c bytes 08a11891
+ 005957d4 bytes 08a10791
- 00572954 ["COPY", "register:0:8", ["register:4040:8"]]
- 00572954 ["INT_ADD", "register:40f0:8", ["const:572954:8", "const:4:8"]]
- 00572954 ["CALLIND", null, ["register:0:8"]]
+ 005957ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005957ec ["INT_ADD", "register:40f0:8", ["const:5957ec:8", "const:4:8"]]
+ 005957ec ["CALLIND", null, ["register:0:8"]]
- 00572954 bytes 00013fd6
+ 005957ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07c268e4cf31abd6f5c273c9bffdbdbc"></a>

### [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) → [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) FUN_0059599c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) · 呼出先 13件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00438f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f20.md) [`00572998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572998.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md)
- 新版 呼出元 3件 [`0059564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 13件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`0045bdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md) [`00595830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595a34",
      "incomplete_value": false,
      "site": "00595a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572b9c",
      "incomplete_value": false,
      "site": "00572ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
      "definition_site": "00595ac8",
      "incomplete_value": false,
      "site": "00595acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572c30",
      "incomplete_value": false,
      "site": "00572c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00595c58",
      "incomplete_value": true,
      "site": "00595c5c",
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
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572dc0",
      "incomplete_value": true,
      "site": "00572dc4",
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
                "const:4f8:8"
              ]
            ]
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
      "00595a38",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ],
    [
      "00595acc",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ],
    [
      "00595c1c",
      "READ",
      [
        "storage",
        "00be6b28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00595a38",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ],
    [
      "00595acc",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "00595c1c",
      "READ",
      [
        "storage",
        "00c636e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md#insn-00572dc4) · [`00572b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md#insn-00572b28) · [`00572b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md#insn-00572b48)
- 新版 `00595c5c`（命令位置の公開資料なし） · `005959c0`（命令位置の公開資料なし） · `005959e0`（命令位置の公開資料なし）

~~~diff
- 00572dc4 ["INT_ADD", "register:40f0:8", ["const:572dc4:8", "const:4:8"]]
- 00572dc4 ["CALL", null, ["callee:00459490:8"]]
+ 00595c5c ["INT_ADD", "register:40f0:8", ["const:595c5c:8", "const:4:8"]]
+ 00595c5c ["CALL", null, ["callee:00459490:8"]]
- 00572dc4 bytes 0d0efb97
+ 00595c5c bytes 0d0efb97
- 00572b28 ["INT_ADD", "register:40f0:8", ["const:572b28:8", "const:4:8"]]
- 00572b28 ["CALL", null, ["callee:00595830:8"]]
+ 005959c0 ["INT_ADD", "register:40f0:8", ["const:5959c0:8", "const:4:8"]]
+ 005959c0 ["CALL", null, ["callee:00595830:8"]]
- 00572b28 bytes 9cffff97
+ 005959c0 bytes 9cffff97
- 00572b48 ["INT_ADD", "register:40f0:8", ["const:572b48:8", "const:4:8"]]
- 00572b48 ["CALL", null, ["callee:00595830:8"]]
+ 005959e0 ["INT_ADD", "register:40f0:8", ["const:5959e0:8", "const:4:8"]]
+ 005959e0 ["CALL", null, ["callee:00595830:8"]]
- 00572b48 bytes 94ffff97
+ 005959e0 bytes 94ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-292bc3cb37cb326819e3ff9a4dc3d93a"></a>

### [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) → [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) FUN_00595cdc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`005727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) · 呼出先 15件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00436bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436bf8.md) [`00438f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f20.md) [`00572998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572998.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md)
- 新版 呼出元 3件 [`0059564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 15件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md) [`0045bdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md) [`00595830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.46% / 新版 93.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00595fa4",
      "incomplete_value": true,
      "site": "00595fa8",
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
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057310c",
      "incomplete_value": true,
      "site": "00573110",
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
                "const:4f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00595ffc",
      "incomplete_value": false,
      "site": "00596000",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573164",
      "incomplete_value": false,
      "site": "00573168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:be1:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596010",
      "incomplete_value": true,
      "site": "00596014",
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
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573178",
      "incomplete_value": true,
      "site": "0057317c",
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
                "const:4f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00595dbc",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ],
    [
      "00595e40",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ],
    [
      "00595f04",
      "READ",
      [
        "storage",
        "00be6b28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00595dbc",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "00595e40",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ],
    [
      "00595f04",
      "READ",
      [
        "storage",
        "00c636e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00573110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md#insn-00573110) · [`00573168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md#insn-00573168) · [`0057317c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md#insn-0057317c)
- 新版 `00595fa8`（命令位置の公開資料なし） · `00596000`（命令位置の公開資料なし） · `00596014`（命令位置の公開資料なし）

~~~diff
- 00573110 ["INT_ADD", "register:40f0:8", ["const:573110:8", "const:4:8"]]
- 00573110 ["CALL", null, ["callee:00459490:8"]]
+ 00595fa8 ["INT_ADD", "register:40f0:8", ["const:595fa8:8", "const:4:8"]]
+ 00595fa8 ["CALL", null, ["callee:00459490:8"]]
- 00573110 bytes 3a0dfb97
+ 00595fa8 bytes 3a0dfb97
- 00573168 ["INT_ADD", "register:40f0:8", ["const:573168:8", "const:4:8"]]
- 00573168 ["CALL", null, ["callee:00c57be0:8"]]
+ 00596000 ["INT_ADD", "register:40f0:8", ["const:596000:8", "const:4:8"]]
+ 00596000 ["CALL", null, ["callee:00c57be0:8"]]
- 00573168 bytes 0aa01994
+ 00596000 bytes f8061b94
- 0057317c ["INT_ADD", "register:40f0:8", ["const:57317c:8", "const:4:8"]]
- 0057317c ["CALL", null, ["callee:00459490:8"]]
+ 00596014 ["INT_ADD", "register:40f0:8", ["const:596014:8", "const:4:8"]]
+ 00596014 ["CALL", null, ["callee:00459490:8"]]
- 0057317c bytes 1f0dfb97
+ 00596014 bytes 1f0dfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bb131a39b4d9edca09205e4b87ccecb"></a>

### [`0057321c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/0057321c.md) → [`005960b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005960b4.md) FUN_005960b4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) · 呼出先 3件 [`005735cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005735cc.md) [`00573960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573960.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 3件 [`00596464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596464.md) [`005967f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005967f8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596118",
      "incomplete_value": false,
      "site": "00596120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573280",
      "incomplete_value": false,
      "site": "00573288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596140",
      "incomplete_value": false,
      "site": "00596148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005732a8",
      "incomplete_value": false,
      "site": "005732b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00596120",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "00596148",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "00596174",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00596120",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "00596148",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "00596174",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00573278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/0057321c.md#insn-00573278) · [`0057327c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/0057321c.md#insn-0057327c) · [`00573280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/0057321c.md#insn-00573280)
- 新版 `00596110`（命令位置の公開資料なし） · `00596114`（命令位置の公開資料なし） · `00596118`（命令位置の公開資料なし）

~~~diff
- 00573278 ["INT_ADD", "register:40f0:8", ["const:573278:8", "const:4:8"]]
- 00573278 ["CALL", null, ["callee:00c57a90:8"]]
+ 00596110 ["INT_ADD", "register:40f0:8", ["const:596110:8", "const:4:8"]]
+ 00596110 ["CALL", null, ["callee:00c57a90:8"]]
- 00573278 bytes 729f1994
+ 00596110 bytes 60061b94
- 0057327c ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00596114 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057327c bytes e83300b0
+ 00596114 bytes a83600f0
- 00573280 ["COPY", "tmp:0:8", ["const:648:8"]]
- 00573280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00573280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00573280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596118 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 00596118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00573280 bytes 08211991
+ 00596118 bytes 08210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26cffe3cb77682a454bda4b80a5c11ed"></a>

### [`005735cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005735cc.md) → [`00596464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596464.md) FUN_00596464

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0057321c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/0057321c.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005960b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005960b4.md) · 呼出先 12件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.73% / 新版 95.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005965b4",
      "incomplete_value": false,
      "site": "005965b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057371c",
      "incomplete_value": false,
      "site": "00573720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "definition_site": "00596654",
      "incomplete_value": false,
      "site": "00596658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005737bc",
      "incomplete_value": false,
      "site": "005737c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "definition_site": "00596754",
      "incomplete_value": false,
      "site": "0059675c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005738bc",
      "incomplete_value": false,
      "site": "005738c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "00596548",
      "PARAM",
      [
        "storage",
        "002a827d",
        null,
        null
      ]
    ],
    [
      "00596574",
      "PARAM",
      [
        "storage",
        "002a827d",
        null,
        null
      ]
    ],
    [
      "005965b8",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00596548",
      "PARAM",
      [
        "storage",
        "002b8f1f",
        null,
        null
      ]
    ],
    [
      "00596574",
      "PARAM",
      [
        "storage",
        "002b8f1f",
        null,
        null
      ]
    ],
    [
      "005965b8",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005736b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005735cc.md#insn-005736b4) · [`0057366c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005735cc.md#insn-0057366c) · [`0057368c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005735cc.md#insn-0057368c)
- 新版 `0059654c`（命令位置の公開資料なし） · `00596504`（命令位置の公開資料なし） · `00596524`（命令位置の公開資料なし）

~~~diff
- 005736b4 ["INT_ADD", "register:40f0:8", ["const:5736b4:8", "const:4:8"]]
- 005736b4 ["CALL", null, ["callee:00c57be0:8"]]
+ 0059654c ["INT_ADD", "register:40f0:8", ["const:59654c:8", "const:4:8"]]
+ 0059654c ["CALL", null, ["callee:00c57be0:8"]]
- 005736b4 bytes b79e1994
+ 0059654c bytes a5051b94
- 0057366c ["INT_ADD", "register:40f0:8", ["const:57366c:8", "const:4:8"]]
- 0057366c ["CALL", null, ["callee:00c57a90:8"]]
+ 00596504 ["INT_ADD", "register:40f0:8", ["const:596504:8", "const:4:8"]]
+ 00596504 ["CALL", null, ["callee:00c57a90:8"]]
- 0057366c bytes 759e1994
+ 00596504 bytes 63051b94
- 0057368c ["INT_ADD", "register:40f0:8", ["const:57368c:8", "const:4:8"]]
- 0057368c ["CALL", null, ["callee:00c57b40:8"]]
+ 00596524 ["INT_ADD", "register:40f0:8", ["const:596524:8", "const:4:8"]]
+ 00596524 ["CALL", null, ["callee:00c57b40:8"]]
- 0057368c bytes 999e1994
+ 00596524 bytes 87051b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b063b43cda7845b670ffc645d63028aa"></a>

### [`00573960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573960.md) → [`005967f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005967f8.md) FUN_005967f8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0057321c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/0057321c.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005960b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005960b4.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596bb4",
      "incomplete_value": false,
      "site": "00596bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573d1c",
      "incomplete_value": false,
      "site": "00573d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059696c",
      "incomplete_value": false,
      "site": "00596978",
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
            "const:a71:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573ad4",
      "incomplete_value": false,
      "site": "00573ae0",
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
            "const:6ec:8"
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
      "0059684c",
      "READ",
      [
        "storage",
        "00c1b4f8",
        null,
        "pointer"
      ]
    ],
    [
      "005968c8",
      "PARAM",
      [
        "storage",
        "0029e6ec",
        null,
        null
      ]
    ],
    [
      "00596938",
      "PARAM",
      [
        "storage",
        "00293a25",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0059684c",
      "READ",
      [
        "storage",
        "00c9aee8",
        null,
        "pointer"
      ]
    ],
    [
      "005968c8",
      "PARAM",
      [
        "storage",
        "002aea71",
        null,
        null
      ]
    ],
    [
      "00596938",
      "PARAM",
      [
        "storage",
        "002a321e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00573ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573960.md#insn-00573ae0) · [`005739a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573960.md#insn-005739a8) · [`005739ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573960.md#insn-005739ac)
- 新版 `00596978`（命令位置の公開資料なし） · `00596840`（命令位置の公開資料なし） · `00596844`（命令位置の公開資料なし）

~~~diff
- 00573ae0 ["INT_ADD", "register:40f0:8", ["const:573ae0:8", "const:4:8"]]
- 00573ae0 ["CALL", null, ["callee:00c57be0:8"]]
+ 00596978 ["INT_ADD", "register:40f0:8", ["const:596978:8", "const:4:8"]]
+ 00596978 ["CALL", null, ["callee:00c57be0:8"]]
- 00573ae0 bytes ac9d1994
+ 00596978 bytes 9a041b94
- 005739a8 ["COPY", "register:40a8:8", ["const:c1b000:8"]]
+ 00596840 ["COPY", "register:40a8:8", ["const:c9a000:8"]]
- 005739a8 bytes 55350090
+ 00596840 bytes 35380090
- 005739ac ["COPY", "register:40a0:8", ["const:293000:8"]]
+ 00596844 ["COPY", "register:40a0:8", ["const:2a3000:8"]]
- 005739ac bytes 14e9ff90
+ 00596844 bytes 74e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21bf2546903a5427b2eff05ad272f9f7"></a>

### [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) → [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) FUN_00596cd0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 14件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`00437118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437118.md) [`00437898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437898.md) [`0043d234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d234.md) · 呼出先 5件 [`005726a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005726a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 14件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00459fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md) [`0045a730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a730.md) [`004600cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600cc.md) · 呼出先 5件 [`00595540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595540.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596d28",
      "incomplete_value": false,
      "site": "00596d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573e90",
      "incomplete_value": false,
      "site": "00573e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "definition_site": "00596d58",
      "incomplete_value": false,
      "site": "00596d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00573ec0",
      "incomplete_value": false,
      "site": "00573ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "00596d28",
      "DATA",
      [
        "storage",
        "00bf0718",
        null,
        "undefined *"
      ]
    ],
    [
      "00596d60",
      "DATA",
      [
        "storage",
        "00bf0628",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00596d28",
      "DATA",
      [
        "storage",
        "00c6d2d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00596d60",
      "DATA",
      [
        "storage",
        "00c6d1e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00573e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md#insn-00573e6c) · [`00573e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md#insn-00573e80) · [`00573e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md#insn-00573e84)
- 新版 `00596d04`（命令位置の公開資料なし） · `00596d18`（命令位置の公開資料なし） · `00596d1c`（命令位置の公開資料なし）

~~~diff
- 00573e6c ["INT_ADD", "register:40f0:8", ["const:573e6c:8", "const:4:8"]]
- 00573e6c ["CALL", null, ["callee:00595540:8"]]
+ 00596d04 ["INT_ADD", "register:40f0:8", ["const:596d04:8", "const:4:8"]]
+ 00596d04 ["CALL", null, ["callee:00595540:8"]]
- 00573e6c bytes 0ffaff97
+ 00596d04 bytes 0ffaff97
- 00573e80 ["INT_ADD", "register:40f0:8", ["const:573e80:8", "const:4:8"]]
- 00573e80 ["CALL", null, ["callee:00c57a90:8"]]
+ 00596d18 ["INT_ADD", "register:40f0:8", ["const:596d18:8", "const:4:8"]]
+ 00596d18 ["CALL", null, ["callee:00c57a90:8"]]
- 00573e80 bytes 709c1994
+ 00596d18 bytes 5e031b94
- 00573e84 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00596d1c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00573e84 bytes e83300b0
+ 00596d1c bytes a83600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49911959c224d96bb1e16c8535f1b2cc"></a>

### [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) → [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) FUN_00596eec

採用 · 移動量 `+0x22e98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 34件 [`0042d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d484.md) [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) [`0054e408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e408.md) [`0054fd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md) [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) · 呼出先 6件 [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 42件 [`0045031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md) [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) · 呼出先 6件 [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596f2c",
      "incomplete_value": false,
      "site": "00596f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574094",
      "incomplete_value": false,
      "site": "005740a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "definition_site": "00596f34",
      "incomplete_value": false,
      "site": "00596f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057409c",
      "incomplete_value": false,
      "site": "005740a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b58:8"
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
      "00596f2c",
      "PARAM",
      [
        "storage",
        "00be67d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00596f34",
      "PARAM",
      [
        "storage",
        "00be6b58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00596f2c",
      "PARAM",
      [
        "storage",
        "00c63398",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00596f34",
      "PARAM",
      [
        "storage",
        "00c63718",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005740a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md#insn-005740a4) · [`00574078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md#insn-00574078) · [`00574090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md#insn-00574090)
- 新版 `00596f3c`（命令位置の公開資料なし） · `00596f10`（命令位置の公開資料なし） · `00596f28`（命令位置の公開資料なし）

~~~diff
- 005740a4 ["INT_ADD", "register:40f0:8", ["const:5740a4:8", "const:4:8"]]
- 005740a4 ["CALL", null, ["callee:00c58210:8"]]
+ 00596f3c ["INT_ADD", "register:40f0:8", ["const:596f3c:8", "const:4:8"]]
+ 00596f3c ["CALL", null, ["callee:00c58210:8"]]
- 005740a4 bytes c79d1994
+ 00596f3c bytes b5041b94
- 00574078 ["INT_ADD", "register:40f0:8", ["const:574078:8", "const:4:8"]]
- 00574078 ["CALL", null, ["callee:00596cd0:8"]]
+ 00596f10 ["INT_ADD", "register:40f0:8", ["const:596f10:8", "const:4:8"]]
+ 00596f10 ["CALL", null, ["callee:00596cd0:8"]]
- 00574078 bytes 70ffff97
+ 00596f10 bytes 70ffff97
- 00574090 ["COPY", "register:4008:8", ["const:be6000:8"]]
+ 00596f28 ["COPY", "register:4008:8", ["const:c63000:8"]]
- 00574090 bytes 813300d0
+ 00596f28 bytes 613600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b441aaaaae78758fdf5ef4918d9a8e06"></a>

### [`00574144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574144.md) → [`00596fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md) FUN_00596fdc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00473b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473b84.md) [`0073bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md) · 呼出先 6件 [`00573f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573f44.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00496a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496a1c.md) [`00765ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md) · 呼出先 6件 [`00596ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596ddc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059701c",
      "incomplete_value": false,
      "site": "0059702c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574184",
      "incomplete_value": false,
      "site": "00574194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "definition_site": "00597024",
      "incomplete_value": false,
      "site": "0059702c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057418c",
      "incomplete_value": false,
      "site": "00574194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b58:8"
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
      "0059701c",
      "PARAM",
      [
        "storage",
        "00be67d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00597024",
      "PARAM",
      [
        "storage",
        "00be6b58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0059701c",
      "PARAM",
      [
        "storage",
        "00c63398",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00597024",
      "PARAM",
      [
        "storage",
        "00c63718",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574144.md#insn-00574194) · [`00574168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574144.md#insn-00574168) · [`00574180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574144.md#insn-00574180)
- 新版 `0059702c`（命令位置の公開資料なし） · `00597000`（命令位置の公開資料なし） · `00597018`（命令位置の公開資料なし）

~~~diff
- 00574194 ["INT_ADD", "register:40f0:8", ["const:574194:8", "const:4:8"]]
- 00574194 ["CALL", null, ["callee:00c58210:8"]]
+ 0059702c ["INT_ADD", "register:40f0:8", ["const:59702c:8", "const:4:8"]]
+ 0059702c ["CALL", null, ["callee:00c58210:8"]]
- 00574194 bytes 8b9d1994
+ 0059702c bytes 79041b94
- 00574168 ["INT_ADD", "register:40f0:8", ["const:574168:8", "const:4:8"]]
- 00574168 ["CALL", null, ["callee:00596ddc:8"]]
+ 00597000 ["INT_ADD", "register:40f0:8", ["const:597000:8", "const:4:8"]]
+ 00597000 ["CALL", null, ["callee:00596ddc:8"]]
- 00574168 bytes 77ffff97
+ 00597000 bytes 77ffff97
- 00574180 ["COPY", "register:4008:8", ["const:be6000:8"]]
+ 00597018 ["COPY", "register:4008:8", ["const:c63000:8"]]
- 00574180 bytes 813300d0
+ 00597018 bytes 61360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b49f61200ae96b34f4bfec479b109ec"></a>

### [`0057423c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057423c.md) → [`005970d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d4.md) FUN_005970d4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005970ec",
      "incomplete_value": false,
      "site": "005970f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574254",
      "incomplete_value": false,
      "site": "00574258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
      "005970f0",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005970f0",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057423c.md#insn-00574250) · [`00574254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057423c.md#insn-00574254) · [`00574294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057423c.md#insn-00574294)
- 新版 `005970e8`（命令位置の公開資料なし） · `005970ec`（命令位置の公開資料なし） · `0059712c`（命令位置の公開資料なし）

~~~diff
- 00574250 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 005970e8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00574250 bytes e8330090
+ 005970e8 bytes a83600d0
- 00574254 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00574254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005970ec ["COPY", "tmp:0:8", ["const:278:8"]]
+ 005970ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005970ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005970ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574254 bytes 08e11a91
+ 005970ec bytes 08e10991
- 00574294 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574294 ["INT_ADD", "register:40f0:8", ["const:574294:8", "const:4:8"]]
- 00574294 ["CALLIND", null, ["register:0:8"]]
+ 0059712c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059712c ["INT_ADD", "register:40f0:8", ["const:59712c:8", "const:4:8"]]
+ 0059712c ["CALLIND", null, ["register:0:8"]]
- 00574294 bytes 00013fd6
+ 0059712c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-053b9c3f67ced29d2841533136330c25"></a>

### [`005742c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005742c4.md) → [`0059715c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059715c.md) FUN_0059715c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) [`0073bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md) [`0076e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 6件 [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) [`005a1430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md) [`00765ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md) [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00597178",
      "incomplete_value": false,
      "site": "0059717c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005742e0",
      "incomplete_value": false,
      "site": "005742e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
      "0059717c",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059717c",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005742dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005742c4.md#insn-005742dc) · [`005742e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005742c4.md#insn-005742e0) · [`0057431c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005742c4.md#insn-0057431c)
- 新版 `00597174`（命令位置の公開資料なし） · `00597178`（命令位置の公開資料なし） · `005971b4`（命令位置の公開資料なし）

~~~diff
- 005742dc ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00597174 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005742dc bytes e8330090
+ 00597174 bytes a83600d0
- 005742e0 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 005742e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005742e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005742e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597178 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 00597178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005742e0 bytes 08e11a91
+ 00597178 bytes 08e10991
- 0057431c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057431c ["INT_ADD", "register:40f0:8", ["const:57431c:8", "const:4:8"]]
- 0057431c ["CALLIND", null, ["register:0:8"]]
+ 005971b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005971b4 ["INT_ADD", "register:40f0:8", ["const:5971b4:8", "const:4:8"]]
+ 005971b4 ["CALLIND", null, ["register:0:8"]]
- 0057431c bytes 00013fd6
+ 005971b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af053946b1b3535e0f9b0f4afed9855f"></a>

### [`00574344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574344.md) → [`005971dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971dc.md) FUN_005971dc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`0057462c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057462c.md) [`0073ccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073ccd0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`005974c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md) [`00766fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/00766fdc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005971ec",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00574354",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005971e8",
      "incomplete_value": false,
      "site": "005971ec",
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
    "old": {
      "definition_site": "00574350",
      "incomplete_value": false,
      "site": "00574354",
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
      "005971e8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "005971ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005971e8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005971ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574344.md#insn-00574354) · [`0057434c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574344.md#insn-0057434c) · [`00574350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574344.md#insn-00574350)
- 新版 `005971ec`（命令位置の公開資料なし） · `005971e4`（命令位置の公開資料なし） · `005971e8`（命令位置の公開資料なし）

~~~diff
- 00574354 ["INT_ADD", "register:40f0:8", ["const:574354:8", "const:4:8"]]
- 00574354 ["CALL", null, ["ram:418c38:8"]]
+ 005971ec ["INT_ADD", "register:40f0:8", ["const:5971ec:8", "const:4:8"]]
+ 005971ec ["CALL", null, ["ram:43b738:8"]]
- 00574354 bytes 3992fa97
+ 005971ec bytes 5391fa97
- 0057434c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 005971e4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0057434c bytes 80e9fff0
+ 005971e4 bytes 00e9ff90
- 00574350 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00574350 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00574350 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00574350 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005971e8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 005971e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005971e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005971e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00574350 bytes 00740e91
+ 005971e8 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4ed60e52a2a277596bd0c9dd9f7ab54"></a>

### [`00574a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574a08.md) → [`005978a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005978a0.md) FUN_005978a0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005748e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748e4.md) · 呼出先 8件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 1件 [`0059777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059777c.md) · 呼出先 8件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005978dc",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00574a44",
      "value": [
        "leaf",
        "ram:bdcf80:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00597908",
      "incomplete_value": true,
      "site": "0059790c",
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574a70",
      "incomplete_value": true,
      "site": "00574a74",
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:500:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00597918",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00574a80",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "005978dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "00597908",
      "READ",
      [
        "storage",
        "00c1b500",
        null,
        "pointer"
      ]
    ],
    [
      "00597908",
      "PARAM",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005978dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00597908",
      "READ",
      [
        "storage",
        "00c9aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00597908",
      "PARAM",
      [
        "storage",
        "011277b8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574a08.md#insn-00574a44) · [`00574a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574a08.md#insn-00574a74) · [`00574a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574a08.md#insn-00574a80)
- 新版 `005978dc`（命令位置の公開資料なし） · `0059790c`（命令位置の公開資料なし） · `00597918`（命令位置の公開資料なし）

~~~diff
- 00574a44 ["INT_ADD", "register:40f0:8", ["const:574a44:8", "const:4:8"]]
- 00574a44 ["CALL", null, ["ram:bdcf80:8"]]
+ 005978dc ["INT_ADD", "register:40f0:8", ["const:5978dc:8", "const:4:8"]]
+ 005978dc ["CALL", null, ["ram:c599d0:8"]]
- 00574a44 bytes 4fa11994
+ 005978dc bytes 3d081b94
- 00574a74 ["INT_ADD", "register:40f0:8", ["const:574a74:8", "const:4:8"]]
- 00574a74 ["CALL", null, ["callee:00c57e80:8"]]
+ 0059790c ["INT_ADD", "register:40f0:8", ["const:59790c:8", "const:4:8"]]
+ 0059790c ["CALL", null, ["callee:00c57e80:8"]]
- 00574a74 bytes 6f9a1994
+ 0059790c bytes 5d011b94
- 00574a80 ["INT_ADD", "register:40f0:8", ["const:574a80:8", "const:4:8"]]
- 00574a80 ["CALL", null, ["ram:bdb440:8"]]
+ 00597918 ["INT_ADD", "register:40f0:8", ["const:597918:8", "const:4:8"]]
+ 00597918 ["CALL", null, ["ram:c57e90:8"]]
- 00574a80 bytes 709a1994
+ 00597918 bytes 5e011b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02b11167c77b18b2608fdf12afb0abd4"></a>

### [`00574bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bbc.md) → [`00597a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a54.md) FUN_00597a54

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0055664c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/0055664c.md) [`00985084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00985/00985084.md) · 呼出先 9件 [`00574d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574d68.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md)
- 新版 呼出元 2件 [`005794e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md) [`009bab64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009bab64.md) · 呼出先 9件 [`00597c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597c00.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00597b0c",
      "incomplete_value": true,
      "site": "00597b10",
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
      "definition_site": "00574c74",
      "incomplete_value": true,
      "site": "00574c78",
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
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00597a88",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "00597a8c",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00597aa4",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00597a88",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "00597a8c",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00597aa4",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bbc.md#insn-00574be0) · [`00574be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bbc.md#insn-00574be4) · [`00574bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bbc.md#insn-00574bf0)
- 新版 `00597a78`（命令位置の公開資料なし） · `00597a7c`（命令位置の公開資料なし） · `00597a88`（命令位置の公開資料なし）

~~~diff
- 00574be0 ["COPY", "register:40d0:8", ["const:c1a000:8"]]
+ 00597a78 ["COPY", "register:40d0:8", ["const:c9a000:8"]]
- 00574be0 bytes 3a3500d0
+ 00597a78 bytes 1a3800f0
- 00574be4 ["COPY", "register:40c8:8", ["const:c1a000:8"]]
+ 00597a7c ["COPY", "register:40c8:8", ["const:c9a000:8"]]
- 00574be4 bytes 393500d0
+ 00597a7c bytes 193800f0
- 00574bf0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e98:8"]]
- 00574bf0 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00597a88 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:888:8"]]
+ 00597a88 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00574bf0 bytes 5a4f47f9
+ 00597a88 bytes 5a4744f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3208831265911c74e8a9a10a9834b04"></a>

### [`00574d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574d68.md) → [`00597c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597c00.md) FUN_00597c00

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bbc.md) · 呼出先 9件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md)
- 新版 呼出元 1件 [`00597a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a54.md) · 呼出先 9件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00597c60",
      "incomplete_value": true,
      "site": "00597c64",
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574dc8",
      "incomplete_value": true,
      "site": "00574dcc",
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
                "const:508:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00597c70",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00574dd8",
      "value": [
        "leaf",
        "ram:bdb440:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00597ca4",
      "incomplete_value": true,
      "site": "00597ca8",
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574e0c",
      "incomplete_value": true,
      "site": "00574e10",
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
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
              ]
            ]
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
      "00597c60",
      "READ",
      [
        "storage",
        "00c1b508",
        null,
        "pointer"
      ]
    ],
    [
      "00597c60",
      "PARAM",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00597c70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00597c60",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ],
    [
      "00597c60",
      "PARAM",
      [
        "storage",
        "011277d8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00597c70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574d68.md#insn-00574dcc) · [`00574dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574d68.md#insn-00574dd8) · [`00574e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574d68.md#insn-00574e10)
- 新版 `00597c64`（命令位置の公開資料なし） · `00597c70`（命令位置の公開資料なし） · `00597ca8`（命令位置の公開資料なし）

~~~diff
- 00574dcc ["INT_ADD", "register:40f0:8", ["const:574dcc:8", "const:4:8"]]
- 00574dcc ["CALL", null, ["callee:00c57e80:8"]]
+ 00597c64 ["INT_ADD", "register:40f0:8", ["const:597c64:8", "const:4:8"]]
+ 00597c64 ["CALL", null, ["callee:00c57e80:8"]]
- 00574dcc bytes 99991994
+ 00597c64 bytes 87001b94
- 00574dd8 ["INT_ADD", "register:40f0:8", ["const:574dd8:8", "const:4:8"]]
- 00574dd8 ["CALL", null, ["ram:bdb440:8"]]
+ 00597c70 ["INT_ADD", "register:40f0:8", ["const:597c70:8", "const:4:8"]]
+ 00597c70 ["CALL", null, ["ram:c57e90:8"]]
- 00574dd8 bytes 9a991994
+ 00597c70 bytes 88001b94
- 00574e10 ["INT_ADD", "register:40f0:8", ["const:574e10:8", "const:4:8"]]
- 00574e10 ["CALL", null, ["callee:00c57e80:8"]]
+ 00597ca8 ["INT_ADD", "register:40f0:8", ["const:597ca8:8", "const:4:8"]]
+ 00597ca8 ["CALL", null, ["callee:00c57e80:8"]]
- 00574e10 bytes 88991994
+ 00597ca8 bytes 76001b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-604d6f114a3baa94db354ee56666b473"></a>

### [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) → [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) FUN_00597e90

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 15件 [`00588310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588310.md) [`00592b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592b14.md) [`0059313c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/0059313c.md) [`00593688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593688.md) [`00593a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593a6c.md) · 呼出先 0件 
- 新版 呼出元 18件 [`005ac9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac9d0.md) [`005b7144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7144.md) [`005b776c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b776c.md) [`005b7cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7cb8.md) [`005b809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b809c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00597e98",
      "incomplete_value": false,
      "site": "00597e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575000",
      "incomplete_value": false,
      "site": "00575004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
      "00597e9c",
      "DATA",
      [
        "storage",
        "00bf0768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00597e9c",
      "DATA",
      [
        "storage",
        "00c6d328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md#insn-00574ffc) · [`00575000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md#insn-00575000)
- 新版 `00597e94`（命令位置の公開資料なし） · `00597e98`（命令位置の公開資料なし）

~~~diff
- 00574ffc ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00597e94 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00574ffc bytes e8330090
+ 00597e94 bytes a83600d0
- 00575000 ["COPY", "tmp:0:8", ["const:768:8"]]
- 00575000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00575000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00575000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597e98 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00597e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00575000 bytes 08a11d91
+ 00597e98 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-894c4ebf55979576fea48a120b94a232"></a>

### [`005760b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760b0.md) → [`00598afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598afc.md) FUN_00598afc

採用 · 移動量 `+0x22a4c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005760a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760a8.md) · 呼出先 3件 [`005778b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005778b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) · 呼出先 3件 [`0059a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a188.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 95.70% / 新版 95.70%

CFGの説明率　旧版 87.88% / 新版 93.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005760d0"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00598b9c",
      "incomplete_value": false,
      "site": "00598ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576150",
      "incomplete_value": false,
      "site": "00576154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00598b1c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005760d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00598ba0",
      "DATA",
      [
        "storage",
        "00bf07d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00598b1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00598ba0",
      "DATA",
      [
        "storage",
        "00c6d390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005760d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760b0.md#insn-005760d0) · [`005760cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760b0.md#insn-005760cc)
- 新版 `00598b1c`（命令位置の公開資料なし）

~~~diff
- 005760d0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005760d0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005760d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005760d0 bytes a8831ff8
+ 00598b1c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00598b1c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00598b1c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00598b1c bytes a8831ff8
- 005760cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:28:8"]]
- 005760cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005760cc bytes a81640f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7db966d4cb7146b58732f29ee1d3d234"></a>

### [`00576d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md) → [`00599674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md) FUN_00599674

採用 · 移動量 `+0x228d8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00577df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577df0.md) [`00578500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578500.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00576eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576eec.md) [`0073ed78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ed78.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md)
- 新版 呼出元 2件 [`0059a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md) [`0059add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md) · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) [`00769084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769084.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 90.91% / 新版 86.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059969c",
      "incomplete_value": false,
      "site": "005996ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576dc4",
      "incomplete_value": false,
      "site": "00576dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005996f4",
      "value": [
        "leaf",
        "ram:769084:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00576e1c",
      "value": [
        "leaf",
        "ram:73ed78:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00576e20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0059969c",
      "PARAM",
      [
        "storage",
        "00c266b0",
        null,
        "undefined1"
      ]
    ],
    [
      "005996f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073ed78"
      ]
    ],
    [
      "unmatched:00576e20",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ],
  "added": [
    [
      "0059969c",
      "PARAM",
      [
        "storage",
        "00ca6170",
        null,
        "undefined1"
      ]
    ],
    [
      "005996f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00769084"
      ]
    ],
    [
      "005996f8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md#insn-00576dd4) · [`00576e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md#insn-00576e1c) · [`00576e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md#insn-00576e20)
- 新版 `005996ac`（命令位置の公開資料なし） · `005996f4`（命令位置の公開資料なし）

~~~diff
- 00576dd4 ["INT_ADD", "register:40f0:8", ["const:576dd4:8", "const:4:8"]]
- 00576dd4 ["CALL", null, ["callee:0044104c:8"]]
+ 005996ac ["INT_ADD", "register:40f0:8", ["const:5996ac:8", "const:4:8"]]
+ 005996ac ["CALL", null, ["callee:0044104c:8"]]
- 00576dd4 bytes de9dfa97
+ 005996ac bytes 689efa97
- 00576e1c ["INT_ADD", "register:40f0:8", ["const:576e1c:8", "const:4:8"]]
- 00576e1c ["CALL", null, ["ram:73ed78:8"]]
+ 005996f4 ["INT_ADD", "register:40f0:8", ["const:5996f4:8", "const:4:8"]]
+ 005996f4 ["CALL", null, ["ram:769084:8"]]
- 00576e1c bytes d71f0794
+ 005996f4 bytes 643e0794
- 00576e20 ["INT_ADD", "register:40f0:8", ["const:576e20:8", "const:4:8"]]
- 00576e20 ["CALL", null, ["callee:008514b8:8"]]
- 00576e20 bytes d8a10a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb37646fbcf56fdb1326dd7fd014ff4b"></a>

### [`00576eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576eec.md) → [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) FUN_005997c4

採用 · 移動量 `+0x228d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00576d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md) · 呼出先 12件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00578a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578a28.md) [`00578a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578a78.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md)
- 新版 呼出元 1件 [`00599674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md) · 呼出先 12件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`0059b300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b300.md) [`0059b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b350.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 94.12% / 新版 91.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599864",
      "incomplete_value": false,
      "site": "00599864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576f8c",
      "incomplete_value": false,
      "site": "00576f8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005997f0",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00576f18",
      "value": [
        "leaf",
        "ram:73a038:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00576f1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005997f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073a038"
      ]
    ],
    [
      "unmatched:00576f1c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "005997fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073e258"
      ]
    ]
  ],
  "added": [
    [
      "005997f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "005997f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "005997fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768564"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576eec.md#insn-00576f18) · [`00576f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576eec.md#insn-00576f1c) · [`00576f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576eec.md#insn-00576f24)
- 新版 `005997f0`（命令位置の公開資料なし） · `005997fc`（命令位置の公開資料なし）

~~~diff
- 00576f18 ["INT_ADD", "register:40f0:8", ["const:576f18:8", "const:4:8"]]
- 00576f18 ["CALL", null, ["ram:73a038:8"]]
+ 005997f0 ["INT_ADD", "register:40f0:8", ["const:5997f0:8", "const:4:8"]]
+ 005997f0 ["CALL", null, ["ram:764344:8"]]
- 00576f18 bytes 480c0794
+ 005997f0 bytes d52a0794
- 00576f1c ["INT_ADD", "register:40f0:8", ["const:576f1c:8", "const:4:8"]]
- 00576f1c ["CALL", null, ["callee:008514b8:8"]]
- 00576f1c bytes 99a10a94
- 00576f24 ["INT_ADD", "register:40f0:8", ["const:576f24:8", "const:4:8"]]
- 00576f24 ["CALL", null, ["ram:73e258:8"]]
+ 005997fc ["INT_ADD", "register:40f0:8", ["const:5997fc:8", "const:4:8"]]
+ 005997fc ["CALL", null, ["ram:768564:8"]]
- 00576f24 bytes cd1c0794
+ 005997fc bytes 5a3b0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e1423267780d78f8132f80d3ad7666d"></a>

### [`0057715c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057715c.md) → [`00599a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599a34.md) FUN_00599a34

採用 · 移動量 `+0x228d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00577df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577df0.md) [`00578500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578500.md) · 呼出先 4件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`0059a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md) [`0059add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md) · 呼出先 4件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 82.50% / 新版 80.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005772fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00599bd4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00599a68",
      "incomplete_value": false,
      "site": "00599a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577190",
      "incomplete_value": false,
      "site": "005771a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "00599a68",
      "PARAM",
      [
        "storage",
        "00c266c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00599adc",
      "PARAM",
      [
        "storage",
        "00c266b0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:005772fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00599c2c"
      ]
    ]
  ],
  "added": [
    [
      "00599a68",
      "PARAM",
      [
        "storage",
        "00ca6188",
        null,
        "undefined1"
      ]
    ],
    [
      "00599adc",
      "PARAM",
      [
        "storage",
        "00ca6170",
        null,
        "undefined1"
      ]
    ],
    [
      "00599bd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00599c2c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005771a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057715c.md#insn-005771a0) · [`0057720c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057715c.md#insn-0057720c) · [`005772fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057715c.md#insn-005772fc)
- 新版 `00599a78`（命令位置の公開資料なし） · `00599ae4`（命令位置の公開資料なし）

~~~diff
- 005771a0 ["INT_ADD", "register:40f0:8", ["const:5771a0:8", "const:4:8"]]
- 005771a0 ["CALL", null, ["callee:0044104c:8"]]
+ 00599a78 ["INT_ADD", "register:40f0:8", ["const:599a78:8", "const:4:8"]]
+ 00599a78 ["CALL", null, ["callee:0044104c:8"]]
- 005771a0 bytes eb9cfa97
+ 00599a78 bytes 759dfa97
- 0057720c ["INT_ADD", "register:40f0:8", ["const:57720c:8", "const:4:8"]]
- 0057720c ["CALL", null, ["callee:0044104c:8"]]
+ 00599ae4 ["INT_ADD", "register:40f0:8", ["const:599ae4:8", "const:4:8"]]
+ 00599ae4 ["CALL", null, ["callee:0044104c:8"]]
- 0057720c bytes d09cfa97
+ 00599ae4 bytes 5a9dfa97
- 005772fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005772fc ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 005772fc bytes c1020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1040e63f7f0555c2f4ce056ea0a3c60b"></a>

### [`005774ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005774ec.md) → [`00599dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599dc4.md) FUN_00599dc4

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 2件 [`005891dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/005891dc.md) [`0058a2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a2e0.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005774fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005774ec.md#insn-005774fc) · [`00577508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005774ec.md#insn-00577508) · [`0057750c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005774ec.md#insn-0057750c)
- 新版 `00599dd4`（命令位置の公開資料なし） · `00599de0`（命令位置の公開資料なし） · `00599de4`（命令位置の公開資料なし）

~~~diff
- 005774fc ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 005774fc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00599dd4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00599dd4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 005774fc bytes b30000b4
+ 00599dd4 bytes b30000b4
- 00577508 ["INT_ADD", "register:40f0:8", ["const:577508:8", "const:4:8"]]
- 00577508 ["CALL", null, ["callee:00c538e0:8"]]
+ 00599de0 ["INT_ADD", "register:40f0:8", ["const:599de0:8", "const:4:8"]]
+ 00599de0 ["CALL", null, ["callee:00c538e0:8"]]
- 00577508 bytes 627e1994
+ 00599de0 bytes c0e61a94
- 0057750c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0057750c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00599de4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00599de4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0057750c bytes 800000b4
+ 00599de4 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f89a38094f92af1ea74fe462208b240"></a>

### [`0057753c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057753c.md) → [`00599e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599e14.md) FUN_00599e14

採用 · 移動量 `+0x228d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00577620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577620.md) [`00588e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588e80.md) [`00588f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588f0c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 3件 [`00599ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599ef8.md) [`005ad444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad444.md) [`005ad4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad4d0.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599e2c",
      "incomplete_value": false,
      "site": "00599e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577554",
      "incomplete_value": false,
      "site": "00577558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
      "00599e30",
      "DATA",
      [
        "storage",
        "00bf0768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599e30",
      "DATA",
      [
        "storage",
        "00c6d328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057753c.md#insn-00577550) · [`00577554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057753c.md#insn-00577554) · [`00577568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057753c.md#insn-00577568)
- 新版 `00599e28`（命令位置の公開資料なし） · `00599e2c`（命令位置の公開資料なし） · `00599e40`（命令位置の公開資料なし）

~~~diff
- 00577550 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00599e28 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00577550 bytes c83300b0
+ 00599e28 bytes a8360090
- 00577554 ["COPY", "tmp:0:8", ["const:768:8"]]
- 00577554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00577554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00577554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00599e2c ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00599e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00599e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00599e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00577554 bytes 08a11d91
+ 00599e2c bytes 08a10c91
- 00577568 ["INT_ADD", "register:40f0:8", ["const:577568:8", "const:4:8"]]
- 00577568 ["CALL", null, ["callee:00c538e0:8"]]
+ 00599e40 ["INT_ADD", "register:40f0:8", ["const:599e40:8", "const:4:8"]]
+ 00599e40 ["CALL", null, ["callee:00c538e0:8"]]
- 00577568 bytes 4a7e1994
+ 00599e40 bytes a8e61a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e847eb7ded7805367449d5a3537b4677"></a>

### [`00577644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577644.md) → [`00599f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599f1c.md) FUN_00599f1c

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 37.50% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599f28",
      "incomplete_value": false,
      "site": "00599f34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577650",
      "incomplete_value": false,
      "site": "0057765c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
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
      "00599f34",
      "DATA",
      [
        "storage",
        "00bf07d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599f34",
      "DATA",
      [
        "storage",
        "00c6d390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057764c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577644.md#insn-0057764c) · [`00577650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577644.md#insn-00577650) · [`00577664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577644.md#insn-00577664)
- 新版 `00599f24`（命令位置の公開資料なし） · `00599f28`（命令位置の公開資料なし） · `00599f3c`（命令位置の公開資料なし）

~~~diff
- 0057764c ["COPY", "register:4050:8", ["const:bf0000:8"]]
+ 00599f24 ["COPY", "register:4050:8", ["const:c6d000:8"]]
- 0057764c bytes ca3300b0
+ 00599f24 bytes aa360090
- 00577650 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 00577650 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00577650 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00577650 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00599f28 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00599f28 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00599f28 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00599f28 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00577650 bytes 4a411f91
+ 00599f28 bytes 4a410e91
- 00577664 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00577664 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00599f3c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00599f3c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00577664 bytes 000100b4
+ 00599f3c bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-134d7112d11ebdfb149838d62d9555b7"></a>

### [`00577688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577688.md) → [`00599f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599f60.md) FUN_00599f60

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00599f78",
      "incomplete_value": false,
      "site": "00599f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005776a0",
      "incomplete_value": false,
      "site": "005776ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "00599f84",
      "DATA",
      [
        "storage",
        "00bf07d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599f84",
      "DATA",
      [
        "storage",
        "00c6d390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057769c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577688.md#insn-0057769c) · [`005776a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577688.md#insn-005776a0) · [`005776d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577688.md#insn-005776d0)
- 新版 `00599f74`（命令位置の公開資料なし） · `00599f78`（命令位置の公開資料なし） · `00599fa8`（命令位置の公開資料なし）

~~~diff
- 0057769c ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00599f74 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057769c bytes c83300b0
+ 00599f74 bytes a8360090
- 005776a0 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 005776a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005776a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005776a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00599f78 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00599f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00599f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00599f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005776a0 bytes 08411f91
+ 00599f78 bytes 08410e91
- 005776d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005776d0 ["INT_ADD", "register:40f0:8", ["const:5776d0:8", "const:4:8"]]
- 005776d0 ["CALLIND", null, ["register:0:8"]]
+ 00599fa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599fa8 ["INT_ADD", "register:40f0:8", ["const:599fa8:8", "const:4:8"]]
+ 00599fa8 ["CALLIND", null, ["register:0:8"]]
- 005776d0 bytes 00013fd6
+ 00599fa8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52a49a44fa0a18fc039f4ab6c9141c5d"></a>

### [`005776e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005776e4.md) → [`00599fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599fbc.md) FUN_00599fbc

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00599fe8",
      "incomplete_value": false,
      "site": "00599fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577710",
      "incomplete_value": false,
      "site": "00577710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "00599fe8",
      "DATA",
      [
        "storage",
        "00bf07d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599fe8",
      "DATA",
      [
        "storage",
        "00c6d390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005776f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005776e4.md#insn-005776f8) · [`00577704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005776e4.md#insn-00577704) · [`00577708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005776e4.md#insn-00577708)
- 新版 `00599fd0`（命令位置の公開資料なし） · `00599fdc`（命令位置の公開資料なし） · `00599fe0`（命令位置の公開資料なし）

~~~diff
- 005776f8 ["INT_ADD", "register:40f0:8", ["const:5776f8:8", "const:4:8"]]
- 005776f8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00599fd0 ["INT_ADD", "register:40f0:8", ["const:599fd0:8", "const:4:8"]]
+ 00599fd0 ["CALL", null, ["callee:00c57a90:8"]]
- 005776f8 bytes 528e1994
+ 00599fd0 bytes b0f61a94
- 00577704 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 00599fdc ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00577704 bytes c83300b0
+ 00599fdc bytes a8360090
- 00577708 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 00577708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00577708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00577708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00599fe0 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00599fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00599fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00599fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00577708 bytes 08411f91
+ 00599fe0 bytes 08410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1c7fde39477e0483e4454cbc23e2b60"></a>

### [`0057776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057776c.md) → [`0059a044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a044.md) FUN_0059a044

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0059a060",
      "incomplete_value": false,
      "site": "0059a060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577788",
      "incomplete_value": false,
      "site": "00577788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "0059a060",
      "DATA",
      [
        "storage",
        "00bf07d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a060",
      "DATA",
      [
        "storage",
        "00c6d390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057776c.md#insn-00577780) · [`00577784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057776c.md#insn-00577784) · [`005777a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057776c.md#insn-005777a8)
- 新版 `0059a058`（命令位置の公開資料なし） · `0059a05c`（命令位置の公開資料なし） · `0059a080`（命令位置の公開資料なし）

~~~diff
- 00577780 ["COPY", "register:4048:8", ["const:bf0000:8"]]
+ 0059a058 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00577780 bytes c93300b0
+ 0059a058 bytes 893600f0
- 00577784 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 00577784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00577784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00577784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a05c ["COPY", "tmp:0:8", ["const:390:8"]]
+ 0059a05c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a05c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a05c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00577784 bytes 29411f91
+ 0059a05c bytes 29410e91
- 005777a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005777a8 ["INT_ADD", "register:40f0:8", ["const:5777a8:8", "const:4:8"]]
- 005777a8 ["CALLIND", null, ["register:0:8"]]
+ 0059a080 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059a080 ["INT_ADD", "register:40f0:8", ["const:59a080:8", "const:4:8"]]
+ 0059a080 ["CALLIND", null, ["register:0:8"]]
- 005777a8 bytes 20013fd6
+ 0059a080 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d1d5a78d034fca51229f4f00ed6ef35"></a>

### [`00577bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577bb4.md) → [`0059a48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a48c.md) FUN_0059a48c

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a4a4",
      "incomplete_value": false,
      "site": "0059a4a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577bcc",
      "incomplete_value": false,
      "site": "00577bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "0059a4a8",
      "DATA",
      [
        "storage",
        "00bf08c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a4a8",
      "DATA",
      [
        "storage",
        "00c6d480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577bb4.md#insn-00577bc8) · [`00577bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577bb4.md#insn-00577bcc) · [`00577bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577bb4.md#insn-00577bdc)
- 新版 `0059a4a0`（命令位置の公開資料なし） · `0059a4a4`（命令位置の公開資料なし） · `0059a4b4`（命令位置の公開資料なし）

~~~diff
- 00577bc8 ["COPY", "register:4048:8", ["const:bf0000:8"]]
+ 0059a4a0 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00577bc8 bytes c93300b0
+ 0059a4a0 bytes 893600f0
- 00577bcc ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00577bcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00577bcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00577bcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a4a4 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 0059a4a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a4a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a4a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00577bcc bytes 29012391
+ 0059a4a4 bytes 29011291
- 00577bdc ["INT_ADD", "register:40f0:8", ["const:577bdc:8", "const:4:8"]]
- 00577bdc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0059a4b4 ["INT_ADD", "register:40f0:8", ["const:59a4b4:8", "const:4:8"]]
+ 0059a4b4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00577bdc bytes 218d1994
+ 0059a4b4 bytes 7ff51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41884e49522c8e2b27cf900907be9d87"></a>

### [`00577c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577c00.md) → [`0059a4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a4d8.md) FUN_0059a4d8

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a4f0",
      "incomplete_value": false,
      "site": "0059a4f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577c18",
      "incomplete_value": false,
      "site": "00577c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "0059a4f4",
      "DATA",
      [
        "storage",
        "00bf08c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a4f4",
      "DATA",
      [
        "storage",
        "00c6d480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577c00.md#insn-00577c14) · [`00577c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577c00.md#insn-00577c18) · [`00577c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577c00.md#insn-00577c28)
- 新版 `0059a4ec`（命令位置の公開資料なし） · `0059a4f0`（命令位置の公開資料なし） · `0059a500`（命令位置の公開資料なし）

~~~diff
- 00577c14 ["COPY", "register:4048:8", ["const:bf0000:8"]]
+ 0059a4ec ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00577c14 bytes c93300b0
+ 0059a4ec bytes 893600f0
- 00577c18 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00577c18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00577c18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00577c18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a4f0 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 0059a4f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a4f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a4f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00577c18 bytes 29012391
+ 0059a4f0 bytes 29011291
- 00577c28 ["INT_ADD", "register:40f0:8", ["const:577c28:8", "const:4:8"]]
- 00577c28 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0059a500 ["INT_ADD", "register:40f0:8", ["const:59a500:8", "const:4:8"]]
+ 0059a500 ["CALL", null, ["callee:00c57ab0:8"]]
- 00577c28 bytes 0e8d1994
+ 0059a500 bytes 6cf51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82668ad5747b4ba7e26280f22f853f28"></a>

### [`00577c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577c48.md) → [`0059a520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a520.md) FUN_0059a520

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a548",
      "incomplete_value": false,
      "site": "0059a548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577c70",
      "incomplete_value": false,
      "site": "00577c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "0059a548",
      "DATA",
      [
        "storage",
        "00bf08c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a548",
      "DATA",
      [
        "storage",
        "00c6d480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577c48.md#insn-00577c5c) · [`00577c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577c48.md#insn-00577c68) · [`00577c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577c48.md#insn-00577c6c)
- 新版 `0059a534`（命令位置の公開資料なし） · `0059a540`（命令位置の公開資料なし） · `0059a544`（命令位置の公開資料なし）

~~~diff
- 00577c5c ["INT_ADD", "register:40f0:8", ["const:577c5c:8", "const:4:8"]]
- 00577c5c ["CALL", null, ["callee:00c57a90:8"]]
+ 0059a534 ["INT_ADD", "register:40f0:8", ["const:59a534:8", "const:4:8"]]
+ 0059a534 ["CALL", null, ["callee:00c57a90:8"]]
- 00577c5c bytes f98c1994
+ 0059a534 bytes 57f51a94
- 00577c68 ["COPY", "register:4048:8", ["const:bf0000:8"]]
+ 0059a540 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00577c68 bytes c93300b0
+ 0059a540 bytes 893600f0
- 00577c6c ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00577c6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00577c6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00577c6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a544 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 0059a544 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a544 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a544 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00577c6c bytes 29012391
+ 0059a544 bytes 29011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ac6927d7756b6352602d730355587df"></a>

### [`00577ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577ce8.md) → [`0059a5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a5c0.md) FUN_0059a5c0

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "0059a5e0",
      "incomplete_value": false,
      "site": "0059a5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577d08",
      "incomplete_value": false,
      "site": "00577d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "0059a5e0",
      "DATA",
      [
        "storage",
        "00bf08c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a5e0",
      "DATA",
      [
        "storage",
        "00c6d480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577ce8.md#insn-00577d00) · [`00577d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577ce8.md#insn-00577d04) · [`00577d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577ce8.md#insn-00577d1c)
- 新版 `0059a5d8`（命令位置の公開資料なし） · `0059a5dc`（命令位置の公開資料なし） · `0059a5f4`（命令位置の公開資料なし）

~~~diff
- 00577d00 ["COPY", "register:4048:8", ["const:bf0000:8"]]
+ 0059a5d8 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00577d00 bytes c93300b0
+ 0059a5d8 bytes 893600f0
- 00577d04 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00577d04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00577d04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00577d04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a5dc ["COPY", "tmp:0:8", ["const:480:8"]]
+ 0059a5dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a5dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a5dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00577d04 bytes 29012391
+ 0059a5dc bytes 29011291
- 00577d1c ["INT_ADD", "register:40f0:8", ["const:577d1c:8", "const:4:8"]]
- 00577d1c ["CALL", null, ["callee:00c538b0:8"]]
+ 0059a5f4 ["INT_ADD", "register:40f0:8", ["const:59a5f4:8", "const:4:8"]]
+ 0059a5f4 ["CALL", null, ["callee:00c538b0:8"]]
- 00577d1c bytes 517c1994
+ 0059a5f4 bytes afe41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61464699a0c8b76ae77a174f1b7625f1"></a>

### [`00577db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577db4.md) → [`0059a68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a68c.md) FUN_0059a68c

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00576334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576334.md) · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00598d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00577dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577db4.md#insn-00577dd0) · [`00577ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577db4.md#insn-00577ddc)
- 新版 `0059a6a8`（命令位置の公開資料なし） · `0059a6b4`（命令位置の公開資料なし）

~~~diff
- 00577dd0 ["INT_ADD", "register:40f0:8", ["const:577dd0:8", "const:4:8"]]
- 00577dd0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0059a6a8 ["INT_ADD", "register:40f0:8", ["const:59a6a8:8", "const:4:8"]]
+ 0059a6a8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00577dd0 bytes a48c1994
+ 0059a6a8 bytes 02f51a94
- 00577ddc ["INT_ADD", "register:40f0:8", ["const:577ddc:8", "const:4:8"]]
- 00577ddc ["CALL", null, ["callee:00c57a80:8"]]
+ 0059a6b4 ["INT_ADD", "register:40f0:8", ["const:59a6b4:8", "const:4:8"]]
+ 0059a6b4 ["CALL", null, ["callee:00c57a80:8"]]
- 00577ddc bytes 958c1994
+ 0059a6b4 bytes f3f41a94
~~~


<a id="compare-4bca033cc9342bd535fa398dabe2f064"></a>

### [`00577df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577df0.md) → [`0059a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md) FUN_0059a6c8

採用 · 移動量 `+0x228d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`00576d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md) [`0057715c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057715c.md) [`00577358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577358.md) [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`00599674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md) [`00599a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599a34.md) [`00599c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 69.23% / 新版 71.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00577df4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00577df4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00577df8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00577df4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00577df8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00577dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0059a6cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0059a6d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0059a6d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577df0.md#insn-00577df4) · [`00577df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577df0.md#insn-00577df8) · [`00577dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577df0.md#insn-00577dfc)

~~~diff
- 00577df4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00577df4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00577df4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00577df4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00577df4 bytes fd7b06a9
- 00577df8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00577df8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00577df8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00577df8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00577df8 bytes fa6707a9
- 00577dfc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00577dfc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00577dfc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00577dfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00577dfc bytes f85f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3b7efa9f409ded04dae30d232063c4f"></a>

### [`00578220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578220.md) → [`0059aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059aaf8.md) FUN_0059aaf8

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0059ab10",
      "incomplete_value": false,
      "site": "0059ab14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578238",
      "incomplete_value": false,
      "site": "0057823c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0059ab14",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ab14",
      "DATA",
      [
        "storage",
        "00c6d500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578220.md#insn-00578234) · [`00578238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578220.md#insn-00578238) · [`00578248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578220.md#insn-00578248)
- 新版 `0059ab0c`（命令位置の公開資料なし） · `0059ab10`（命令位置の公開資料なし） · `0059ab20`（命令位置の公開資料なし）

~~~diff
- 00578234 ["COPY", "register:4048:8", ["const:bf0000:8"]]
+ 0059ab0c ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00578234 bytes c9330090
+ 0059ab0c bytes 893600f0
- 00578238 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00578238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00578238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00578238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059ab10 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0059ab10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ab10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ab10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00578238 bytes 29012591
+ 0059ab10 bytes 29011491
- 00578248 ["INT_ADD", "register:40f0:8", ["const:578248:8", "const:4:8"]]
- 00578248 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0059ab20 ["INT_ADD", "register:40f0:8", ["const:59ab20:8", "const:4:8"]]
+ 0059ab20 ["CALL", null, ["callee:00c57ab0:8"]]
- 00578248 bytes 868b1994
+ 0059ab20 bytes e4f31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91c8c65b4156d45ccbaabb08e8e90ddf"></a>

### [`00578290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578290.md) → [`0059ab68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ab68.md) FUN_0059ab68

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059ab80",
      "incomplete_value": false,
      "site": "0059ab84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005782a8",
      "incomplete_value": false,
      "site": "005782ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0059ab84",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ab84",
      "DATA",
      [
        "storage",
        "00c6d500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005782a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578290.md#insn-005782a4) · [`005782a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578290.md#insn-005782a8) · [`005782b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578290.md#insn-005782b8)
- 新版 `0059ab7c`（命令位置の公開資料なし） · `0059ab80`（命令位置の公開資料なし） · `0059ab90`（命令位置の公開資料なし）

~~~diff
- 005782a4 ["COPY", "register:4048:8", ["const:bf0000:8"]]
+ 0059ab7c ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 005782a4 bytes c9330090
+ 0059ab7c bytes 893600f0
- 005782a8 ["COPY", "tmp:0:8", ["const:940:8"]]
- 005782a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005782a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005782a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059ab80 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0059ab80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ab80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ab80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005782a8 bytes 29012591
+ 0059ab80 bytes 29011491
- 005782b8 ["INT_ADD", "register:40f0:8", ["const:5782b8:8", "const:4:8"]]
- 005782b8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0059ab90 ["INT_ADD", "register:40f0:8", ["const:59ab90:8", "const:4:8"]]
+ 0059ab90 ["CALL", null, ["callee:00c57ab0:8"]]
- 005782b8 bytes 6a8b1994
+ 0059ab90 bytes c8f31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-590e7ea3c7c4ec20029c6d10c76eaa65"></a>

### [`005782fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005782fc.md) → [`0059abd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059abd4.md) FUN_0059abd4

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 44.44% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059abf4",
      "incomplete_value": false,
      "site": "0059abfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057831c",
      "incomplete_value": false,
      "site": "00578324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "definition_site": "0059ac44",
      "incomplete_value": true,
      "site": "0059ac48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059ac40",
      "incomplete_value": true,
      "site": "0059ac48",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
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
      "0059abfc",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059abfc",
      "DATA",
      [
        "storage",
        "00c6d500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005782fc.md#insn-00578370) · [`00578384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005782fc.md#insn-00578384)
- 新版 `0059ac48`（命令位置の公開資料なし） · `0059ac5c`（命令位置の公開資料なし）

~~~diff
- 00578370 ["INT_ADD", "register:40f0:8", ["const:578370:8", "const:4:8"]]
- 00578370 ["CALL", null, ["callee:0043bae0:8"]]
+ 0059ac48 ["INT_ADD", "register:40f0:8", ["const:59ac48:8", "const:4:8"]]
+ 0059ac48 ["CALL", null, ["callee:0043bae0:8"]]
- 00578370 bytes 1c83fa97
+ 0059ac48 bytes a683fa97
- 00578384 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00578384 ["RETURN", null, ["register:0:8"]]
- 00578384 bytes c0035fd6
+ 0059ac5c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 0059ac5c ["RETURN", null, ["register:0:8"]]
+ 0059ac5c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd75bdc16cbb0abd0c042d7217e6d668"></a>

### [`0057843c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/0057843c.md) → [`0059ad14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad14.md) FUN_0059ad14

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 30.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057843c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057843c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578440"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0057843c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00578440",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0057848c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0059ad14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0059ad18",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0059ad64",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057843c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/0057843c.md#insn-0057843c) · [`00578440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/0057843c.md#insn-00578440) · [`00578458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/0057843c.md#insn-00578458)
- 新版 `0059ad30`（命令位置の公開資料なし）

~~~diff
- 0057843c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0057843c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0057843c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0057843c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0057843c bytes fd7bbea9
- 00578440 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00578440 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00578440 bytes f30b00f9
- 00578458 ["INT_ADD", "register:40f0:8", ["const:578458:8", "const:4:8"]]
- 00578458 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0059ad30 ["INT_ADD", "register:40f0:8", ["const:59ad30:8", "const:4:8"]]
+ 0059ad30 ["CALL", null, ["callee:00c57ab0:8"]]
- 00578458 bytes 028b1994
+ 0059ad30 bytes 60f31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57b9eb4e3982c6dc7ae7918c646d27c3"></a>

### [`00578500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578500.md) → [`0059add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md) FUN_0059add8

採用 · 移動量 `+0x228d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`00576d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md) [`0057715c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057715c.md) [`00577358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577358.md) [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`00599674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md) [`00599a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599a34.md) [`00599c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 54.05% / 新版 54.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057852c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005786f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005786f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0057852c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0057864c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538b0"
      ]
    ],
    [
      "unmatched:00578668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059af64"
      ]
    ]
  ],
  "added": [
    [
      "0059ae04",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0059af24",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538b0"
      ]
    ],
    [
      "0059af40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059af64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057852c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578500.md#insn-0057852c) · [`0057864c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578500.md#insn-0057864c) · [`00578668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578500.md#insn-00578668)

~~~diff
- 0057852c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0057852c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0057852c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0057852c bytes a8831ff8
- 0057864c ["INT_ADD", "register:40f0:8", ["const:57864c:8", "const:4:8"]]
- 0057864c ["CALL", null, ["callee:00c538b0:8"]]
- 0057864c bytes 057a1994
- 00578668 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00578668 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00578668 bytes 200100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c71257bf32cfafe217a8c14ac1f369c"></a>

### [`005789a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005789a4.md) → [`0059b27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b27c.md) FUN_0059b27c

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0059b2a0",
      "incomplete_value": false,
      "site": "0059b2a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005789c8",
      "incomplete_value": false,
      "site": "005789c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "0059b2a0",
      "DATA",
      [
        "storage",
        "00bf09c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059b2a0",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005789b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005789a4.md#insn-005789b8) · [`005789c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005789a4.md#insn-005789c0) · [`005789c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005789a4.md#insn-005789c4)
- 新版 `0059b290`（命令位置の公開資料なし） · `0059b298`（命令位置の公開資料なし） · `0059b29c`（命令位置の公開資料なし）

~~~diff
- 005789b8 ["INT_ADD", "register:40f0:8", ["const:5789b8:8", "const:4:8"]]
- 005789b8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0059b290 ["INT_ADD", "register:40f0:8", ["const:59b290:8", "const:4:8"]]
+ 0059b290 ["CALL", null, ["callee:00c57a90:8"]]
- 005789b8 bytes a2891994
+ 0059b290 bytes 00f21a94
- 005789c0 ["COPY", "register:4048:8", ["const:bf0000:8"]]
+ 0059b298 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 005789c0 bytes c9330090
+ 0059b298 bytes 893600d0
- 005789c4 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 005789c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005789c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005789c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059b29c ["COPY", "tmp:0:8", ["const:580:8"]]
+ 0059b29c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059b29c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059b29c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005789c4 bytes 29012791
+ 0059b29c bytes 29011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

