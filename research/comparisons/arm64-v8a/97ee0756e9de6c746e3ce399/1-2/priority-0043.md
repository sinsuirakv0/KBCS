# v15.7.3 → v15.7.4 · 最優先の変更候補 (43)

[一覧の目次](README.md)

<a id="compare-ca0df2c501295f1d1ddaa9d6ce537d84"></a>

### [`008605f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008605f0.md) → [`008605f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008605f0.md) _INIT_162

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
      "definition_site": "0086062c",
      "incomplete_value": true,
      "site": "00860648",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0086062c",
      "incomplete_value": true,
      "site": "00860648",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00860670",
      "incomplete_value": true,
      "site": "0086068c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00860670",
      "incomplete_value": true,
      "site": "0086068c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008606ac",
      "incomplete_value": true,
      "site": "008606c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008606ac",
      "incomplete_value": true,
      "site": "008606c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0086062c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00860650",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00860670",
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
      "0086062c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00860650",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00860670",
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

- 旧版 [`0086061c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008605f0.md#insn-0086061c) · [`00860624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008605f0.md#insn-00860624)
- 新版 `0086061c`（命令位置の公開資料なし） · `00860624`（命令位置の公開資料なし）

~~~diff
- 0086061c ["COPY", "tmp:0:8", ["const:618:8"]]
- 0086061c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0086061c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0086061c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0086061c ["COPY", "tmp:0:8", ["const:658:8"]]
+ 0086061c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0086061c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0086061c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0086061c bytes 73621891
+ 0086061c bytes 73621991
- 00860624 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00860624 bytes 29d2fff0
+ 00860624 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00860624 bytes 29d2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-994f6e0f49818c9e62b65dae5d6694d0"></a>

### [`008609f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008609f4.md) → [`008609f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008609f4.md) FUN_008609f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046c4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c4c0.md) [`0046fd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fd28.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046c4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md) [`0046fd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fd28.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.88% / 新版 93.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00860aa0",
      "incomplete_value": true,
      "site": "00860ab0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fd1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860aa0",
      "incomplete_value": true,
      "site": "00860ab0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5e:8"
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
      "definition_site": "00860aa4",
      "incomplete_value": true,
      "site": "00860ab8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00860aa4",
      "incomplete_value": true,
      "site": "00860ab8",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00860aa0",
      "READ",
      [
        "storage",
        "0029605e",
        null,
        "string"
      ]
    ],
    [
      "00860aa4",
      "READ",
      [
        "storage",
        "0029606b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00860aa0",
      "READ",
      [
        "storage",
        "00295fd1",
        null,
        "string"
      ]
    ],
    [
      "00860aa4",
      "READ",
      [
        "storage",
        "00295fde",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008609f4.md#insn-00860a94) · [`00860a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008609f4.md#insn-00860a98) · [`00860aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008609f4.md#insn-00860aa8)
- 新版 `00860a94`（命令位置の公開資料なし） · `00860a98`（命令位置の公開資料なし）

~~~diff
- 00860a94 ["COPY", "register:4040:8", ["const:296000:8"]]
+ 00860a94 ["COPY", "register:4040:8", ["const:295000:8"]]
- 00860a94 bytes a8d1ffd0
+ 00860a94 bytes a8d1ffb0
- 00860a98 ["COPY", "tmp:0:8", ["const:5e:8"]]
- 00860a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00860a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00860a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00860a98 ["COPY", "tmp:0:8", ["const:fd1:8"]]
+ 00860a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00860a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00860a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00860a98 bytes 08790191
+ 00860a98 bytes 08453f91
- 00860aa8 ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 00860aa8 bytes 88d2ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee235b40652f4a01e3b678116af506f9"></a>

### [`00860de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860de0.md) → [`00860de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860de0.md) FUN_00860de0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 52件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c894.md) [`0041c8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md)
- 新版 呼出元 0件  · 呼出先 52件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c894.md) [`0041c8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 33件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00860e80",
      "incomplete_value": true,
      "site": "00860e94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cd5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860e80",
      "incomplete_value": true,
      "site": "00860e94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c4a:8"
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
      "definition_site": "00860e80",
      "incomplete_value": true,
      "site": "00860e94",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00860e80",
      "incomplete_value": true,
      "site": "00860e94",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00860e98",
      "incomplete_value": true,
      "site": "00860ea8",
      "value": [
        "LOAD",
        "16",
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
                "const:1e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860e98",
      "incomplete_value": true,
      "site": "00860ea8",
      "value": [
        "LOAD",
        "16",
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
                "const:1e:8"
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
      "00860e80",
      "READ",
      [
        "storage",
        "002a5c4a",
        null,
        "string"
      ]
    ],
    [
      "00860e80",
      "READ",
      [
        "storage",
        "002a5c5a",
        null,
        "string"
      ]
    ],
    [
      "00860e98",
      "READ",
      [
        "storage",
        "002a5c68",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00860e80",
      "READ",
      [
        "storage",
        "002a5cd5",
        null,
        "string"
      ]
    ],
    [
      "00860e80",
      "READ",
      [
        "storage",
        "002a5ce5",
        null,
        "string"
      ]
    ],
    [
      "00860e98",
      "READ",
      [
        "storage",
        "002a5cf3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860de0.md#insn-00860e78) · [`00860e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860de0.md#insn-00860e7c)
- 新版 `00860e78`（命令位置の公開資料なし） · `00860e7c`（命令位置の公開資料なし）

~~~diff
- 00860e78 ["COPY", "tmp:0:8", ["const:c4a:8"]]
- 00860e78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00860e78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00860e78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00860e78 ["COPY", "tmp:0:8", ["const:cd5:8"]]
+ 00860e78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00860e78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00860e78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00860e78 bytes 08293191
+ 00860e78 bytes 08553391
- 00860e7c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00860e7c bytes 89d2ff90
+ 00860e7c ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 00860e7c bytes 89d2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-544bf39a01424343cffc91a331b3fb31"></a>

### [`008629ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md) → [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) FUN_008629ec

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 99件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0041cc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cc4c.md)
- 新版 呼出元 0件  · 呼出先 99件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041cc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cc4c.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.53% / 新版 94.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 23件, `store_value` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00862a98",
      "incomplete_value": true,
      "site": "00862aa4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:663:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00862a98",
      "incomplete_value": true,
      "site": "00862aa4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c9:8"
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
      "definition_site": "00862b44",
      "incomplete_value": true,
      "site": "00862b58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00862b44",
      "incomplete_value": true,
      "site": "00862b58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00862be0",
      "incomplete_value": true,
      "site": "00862be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a87:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00862be0",
      "incomplete_value": true,
      "site": "00862be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00862a98",
      "READ",
      [
        "storage",
        "002a65c9",
        null,
        "string"
      ]
    ],
    [
      "00862b44",
      "READ",
      [
        "storage",
        "002a79d8",
        null,
        "string"
      ]
    ],
    [
      "00862bc8",
      "READ",
      [
        "storage",
        "002a79ed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00862a98",
      "READ",
      [
        "storage",
        "002a6663",
        null,
        "string"
      ]
    ],
    [
      "00862b44",
      "READ",
      [
        "storage",
        "002a7a72",
        null,
        "string"
      ]
    ],
    [
      "00862bc8",
      "READ",
      [
        "storage",
        "002a7a87",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00862a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md#insn-00862a90) · [`00862b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md#insn-00862b3c) · [`00862bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md#insn-00862bc4)
- 新版 `00862a90`（命令位置の公開資料なし） · `00862b3c`（命令位置の公開資料なし） · `00862bc4`（命令位置の公開資料なし）

~~~diff
- 00862a90 ["COPY", "tmp:0:8", ["const:5c9:8"]]
- 00862a90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00862a90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00862a90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00862a90 ["COPY", "tmp:0:8", ["const:663:8"]]
+ 00862a90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00862a90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00862a90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00862a90 bytes 29251791
+ 00862a90 bytes 298d1991
- 00862b3c ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 00862b3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00862b3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00862b3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00862b3c ["COPY", "tmp:0:8", ["const:a72:8"]]
+ 00862b3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00862b3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00862b3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00862b3c bytes 29612791
+ 00862b3c bytes 29c92991
- 00862bc4 ["COPY", "tmp:0:8", ["const:9ed:8"]]
- 00862bc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00862bc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00862bc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00862bc4 ["COPY", "tmp:0:8", ["const:a87:8"]]
+ 00862bc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00862bc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00862bc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00862bc4 bytes 29b52791
+ 00862bc4 bytes 291d2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63eb6a0a993fd9af29db8158f5408a8b"></a>

### [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) → [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) FUN_008648a8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 57件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`004264e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md)
- 新版 呼出元 0件  · 呼出先 57件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`004264e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.28% / 新版 93.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `call_target` 4件, `store_value` 56件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008649a0",
      "incomplete_value": true,
      "site": "008649c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:997:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008649a0",
      "incomplete_value": true,
      "site": "008649c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:90c:8"
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
      "definition_site": "008649a0",
      "incomplete_value": true,
      "site": "008649c0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008649a0",
      "incomplete_value": true,
      "site": "008649c0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008649b8",
      "incomplete_value": true,
      "site": "008649c4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008649b8",
      "incomplete_value": true,
      "site": "008649c4",
      "value": [
        "LOAD",
        "16",
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
      "00864940",
      "PARAM",
      [
        "storage",
        "0029ba1e",
        null,
        "string"
      ]
    ],
    [
      "008649a0",
      "READ",
      [
        "storage",
        "0029d90c",
        null,
        "string"
      ]
    ],
    [
      "008649a0",
      "READ",
      [
        "storage",
        "0029d91c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00864940",
      "PARAM",
      [
        "storage",
        "0029ba1c",
        null,
        "string"
      ]
    ],
    [
      "008649a0",
      "READ",
      [
        "storage",
        "0029d997",
        null,
        "string"
      ]
    ],
    [
      "008649a0",
      "READ",
      [
        "storage",
        "0029d9a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00864940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md#insn-00864940) · [`00864998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md#insn-00864998) · [`00864a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md#insn-00864a48)
- 新版 `00864940`（命令位置の公開資料なし） · `00864998`（命令位置の公開資料なし） · `00864a48`（命令位置の公開資料なし）

~~~diff
- 00864940 ["COPY", "tmp:0:8", ["const:a1e:8"]]
- 00864940 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00864940 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00864940 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00864940 ["COPY", "tmp:0:8", ["const:a1c:8"]]
+ 00864940 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00864940 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00864940 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00864940 bytes 42782891
+ 00864940 bytes 42702891
- 00864998 ["COPY", "tmp:0:8", ["const:90c:8"]]
- 00864998 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00864998 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00864998 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00864998 ["COPY", "tmp:0:8", ["const:997:8"]]
+ 00864998 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00864998 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00864998 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00864998 bytes 4a312491
+ 00864998 bytes 4a5d2691
- 00864a48 ["COPY", "tmp:0:8", ["const:b5:8"]]
- 00864a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00864a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00864a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00864a48 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 00864a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00864a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00864a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00864a48 bytes 08d50291
+ 00864a48 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdb5695f5e07d38aa7105bf13a50682c"></a>

### [`008673f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00867/008673f0.md) → [`008673f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00867/008673f0.md) FUN_008673f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 14件 [`004512c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00451/004512c0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fdf4.md) [`006fd890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd890.md) [`006fdbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdbdc.md)
- 新版 呼出元 2件 [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 14件 [`004512c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fdf4.md) [`006fd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.76% / 新版 92.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008675d8",
      "incomplete_value": true,
      "site": "008675e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:346:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008675d8",
      "incomplete_value": true,
      "site": "008675e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:348:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008675d8",
      "incomplete_value": true,
      "site": "008675e8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008675d8",
      "incomplete_value": true,
      "site": "008675e8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008677a0",
      "incomplete_value": true,
      "site": "008677b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008677a0",
      "incomplete_value": true,
      "site": "008677b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:be3:8"
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
      "00867480",
      "READ",
      [
        "storage",
        "00295047",
        null,
        "string"
      ]
    ],
    [
      "00867480",
      "READ",
      [
        "storage",
        "00295057",
        null,
        "string"
      ]
    ],
    [
      "0086748c",
      "PARAM",
      [
        "storage",
        "0029e2aa",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00867480",
      "READ",
      [
        "storage",
        "00294fba",
        null,
        "string"
      ]
    ],
    [
      "00867480",
      "READ",
      [
        "storage",
        "00294fca",
        null,
        "string"
      ]
    ],
    [
      "0086748c",
      "PARAM",
      [
        "storage",
        "0029e335",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00867470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00867/008673f0.md#insn-00867470) · [`00867478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00867/008673f0.md#insn-00867478) · [`0086747c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00867/008673f0.md#insn-0086747c)
- 新版 `00867470`（命令位置の公開資料なし） · `00867478`（命令位置の公開資料なし） · `0086747c`（命令位置の公開資料なし）

~~~diff
- 00867470 ["COPY", "tmp:0:8", ["const:2aa:8"]]
- 00867470 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00867470 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00867470 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00867470 ["COPY", "tmp:0:8", ["const:335:8"]]
+ 00867470 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00867470 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00867470 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00867470 bytes f7aa0a91
+ 00867470 bytes f7d60c91
- 00867478 ["COPY", "register:4040:8", ["const:295000:8"]]
+ 00867478 ["COPY", "register:4040:8", ["const:294000:8"]]
- 00867478 bytes 68d1ffd0
+ 00867478 bytes 68d1ffb0
- 0086747c ["COPY", "tmp:0:8", ["const:47:8"]]
- 0086747c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086747c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086747c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086747c ["COPY", "tmp:0:8", ["const:fba:8"]]
+ 0086747c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086747c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086747c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086747c bytes 081d0191
+ 0086747c bytes 08e93e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba7a09f5980fcee39e30b69f8c029409"></a>

### [`00868124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) → [`00868124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) FUN_00868124

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`00428714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428714.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 0件  · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`00428714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428714.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.65% / 新版 99.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008687f0",
      "incomplete_value": false,
      "site": "008687f8",
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
            "const:c2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008687f0",
      "incomplete_value": false,
      "site": "008687f8",
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
            "const:cb8:8"
          ]
        ]
      ]
    },
    "ordinal": 104,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008688e8",
      "incomplete_value": false,
      "site": "008688f0",
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
            "const:93f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008688e8",
      "incomplete_value": false,
      "site": "008688f0",
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
            "const:8a5:8"
          ]
        ]
      ]
    },
    "ordinal": 118,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008687f0",
      "PARAM",
      [
        "storage",
        "00293cb8",
        null,
        "string"
      ]
    ],
    [
      "008688e8",
      "PARAM",
      [
        "storage",
        "002a78a5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008687f0",
      "PARAM",
      [
        "storage",
        "00293c2b",
        null,
        "string"
      ]
    ],
    [
      "008688e8",
      "PARAM",
      [
        "storage",
        "002a793f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008687f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md#insn-008687f0) · [`008688e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md#insn-008688e8)
- 新版 `008687f0`（命令位置の公開資料なし） · `008688e8`（命令位置の公開資料なし）

~~~diff
- 008687f0 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 008687f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008687f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008687f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008687f0 ["COPY", "tmp:0:8", ["const:c2b:8"]]
+ 008687f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008687f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008687f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008687f0 bytes 21e03291
+ 008687f0 bytes 21ac3091
- 008688e8 ["COPY", "tmp:0:8", ["const:8a5:8"]]
- 008688e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008688e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008688e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008688e8 ["COPY", "tmp:0:8", ["const:93f:8"]]
+ 008688e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008688e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008688e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008688e8 bytes 21942291
+ 008688e8 bytes 21fc2491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61551355b534cba7b048d878c427739c"></a>

### [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) → [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) FUN_00868b14

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 69件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md)
- 新版 呼出元 0件  · 呼出先 69件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.42% / 新版 95.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_value` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00868ecc",
      "incomplete_value": true,
      "site": "00868edc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:ac8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00868ecc",
      "incomplete_value": true,
      "site": "00868edc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:a2e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00868ed0",
      "incomplete_value": true,
      "site": "00868ee0",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00868ed0",
      "incomplete_value": true,
      "site": "00868ee0",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00869020",
      "incomplete_value": true,
      "site": "00869038",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00869020",
      "incomplete_value": true,
      "site": "00869038",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00868dec",
      "READ",
      [
        "storage",
        "0029b9fb",
        null,
        "string"
      ]
    ],
    [
      "00868dec",
      "READ",
      [
        "storage",
        "0029ba0b",
        null,
        "string"
      ]
    ],
    [
      "00868ecc",
      "READ",
      [
        "storage",
        "002a7a2e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00868dec",
      "READ",
      [
        "storage",
        "0029b9f9",
        null,
        "string"
      ]
    ],
    [
      "00868dec",
      "READ",
      [
        "storage",
        "0029ba09",
        null,
        "string"
      ]
    ],
    [
      "00868ecc",
      "READ",
      [
        "storage",
        "002a7ac8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00868de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md#insn-00868de8) · [`00868ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md#insn-00868ec4) · [`00869018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md#insn-00869018)
- 新版 `00868de8`（命令位置の公開資料なし） · `00868ec4`（命令位置の公開資料なし） · `00869018`（命令位置の公開資料なし）

~~~diff
- 00868de8 ["COPY", "tmp:0:8", ["const:9fb:8"]]
- 00868de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00868de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00868de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00868de8 ["COPY", "tmp:0:8", ["const:9f9:8"]]
+ 00868de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00868de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00868de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00868de8 bytes 08ed2791
+ 00868de8 bytes 08e52791
- 00868ec4 ["COPY", "tmp:0:8", ["const:a2e:8"]]
- 00868ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00868ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00868ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00868ec4 ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 00868ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00868ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00868ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00868ec4 bytes 08b92891
+ 00868ec4 bytes 08212b91
- 00869018 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 00869018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00869018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00869018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00869018 ["COPY", "tmp:0:8", ["const:a72:8"]]
+ 00869018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00869018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00869018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00869018 bytes 29612791
+ 00869018 bytes 29c92991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c64788a7b1eafeaeb1c42a76009db8c5"></a>

### [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) → [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) FUN_0086b704

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 153件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b014.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md)
- 新版 呼出元 0件  · 呼出先 153件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b014.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 98.05% / 新版 98.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `call_target` 1件, `store_destination` 1件, `store_value` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086b7b8",
      "incomplete_value": true,
      "site": "0086b7c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:997:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b7b8",
      "incomplete_value": true,
      "site": "0086b7c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:90c:8"
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
      "definition_site": "0086b7b8",
      "incomplete_value": true,
      "site": "0086b7c8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0086b7b8",
      "incomplete_value": true,
      "site": "0086b7c8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086b7cc",
      "incomplete_value": true,
      "site": "0086b7e0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0086b7cc",
      "incomplete_value": true,
      "site": "0086b7e0",
      "value": [
        "LOAD",
        "16",
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
      "0086b75c",
      "PARAM",
      [
        "storage",
        "0029ba1e",
        null,
        "string"
      ]
    ],
    [
      "0086b7b8",
      "READ",
      [
        "storage",
        "0029d90c",
        null,
        "string"
      ]
    ],
    [
      "0086b7b8",
      "READ",
      [
        "storage",
        "0029d91c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0086b75c",
      "PARAM",
      [
        "storage",
        "0029ba1c",
        null,
        "string"
      ]
    ],
    [
      "0086b7b8",
      "READ",
      [
        "storage",
        "0029d997",
        null,
        "string"
      ]
    ],
    [
      "0086b7b8",
      "READ",
      [
        "storage",
        "0029d9a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md#insn-0086bd8c) · [`0086c938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md#insn-0086c938) · [`0086b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md#insn-0086b75c)
- 新版 `0086bd8c`（命令位置の公開資料なし） · `0086c938`（命令位置の公開資料なし） · `0086b75c`（命令位置の公開資料なし）

~~~diff
- 0086bd8c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0086bd8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:6b0:8"]]
- 0086bd8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0086bd8c ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0086bd8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:6f0:8"]]
+ 0086bd8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0086bd8c bytes 09c11a39
+ 0086bd8c bytes 09c11b39
- 0086c938 ["INT_ADD", "register:40f0:8", ["const:86c938:8", "const:4:8"]]
- 0086c938 ["CALL", null, ["ram:a26cbc:8"]]
+ 0086c938 ["INT_ADD", "register:40f0:8", ["const:86c938:8", "const:4:8"]]
+ 0086c938 ["CALL", null, ["ram:a26d00:8"]]
- 0086c938 bytes e1e80694
+ 0086c938 bytes f2e80694
- 0086b75c ["COPY", "tmp:0:8", ["const:a1e:8"]]
- 0086b75c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0086b75c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0086b75c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0086b75c ["COPY", "tmp:0:8", ["const:a1c:8"]]
+ 0086b75c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0086b75c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0086b75c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0086b75c bytes 42782891
+ 0086b75c bytes 42702891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ad6af174ec28730cc20d221fcfd1b08"></a>

### [`008710b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008710b4.md) → [`008710b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008710b4.md) FUN_008710b4

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
      "definition_site": "008710b8",
      "incomplete_value": false,
      "site": "008710bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008710b8",
      "incomplete_value": false,
      "site": "008710bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "008710bc",
      "DATA",
      [
        "storage",
        "00c04178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008710bc",
      "DATA",
      [
        "storage",
        "00c041c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008710b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008710b4.md#insn-008710b8)
- 新版 `008710b8`（命令位置の公開資料なし）

~~~diff
- 008710b8 ["COPY", "tmp:0:8", ["const:178:8"]]
- 008710b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008710b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008710b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008710b8 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 008710b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008710b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008710b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008710b8 bytes 08e10591
+ 008710b8 bytes 08210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfb2ba9f6ae397b1b83f2a86d5125b35"></a>

### [`008710cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008710cc.md) → [`008710cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008710cc.md) FUN_008710cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00871200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871200.md) [`00871204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871204.md) [`00ada5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada5ac.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00871200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871200.md) [`00871204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871204.md) [`00ada5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "008710e4",
      "incomplete_value": false,
      "site": "008710f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008710e4",
      "incomplete_value": false,
      "site": "008710f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "008710f4",
      "DATA",
      [
        "storage",
        "00c041e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00871128",
      "READ",
      [
        "storage",
        "00c04208",
        null,
        "pointer"
      ]
    ],
    [
      "00871128",
      "READ",
      [
        "storage",
        "00c04210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008710f4",
      "DATA",
      [
        "storage",
        "00c04238",
        null,
        "undefined *"
      ]
    ],
    [
      "00871128",
      "READ",
      [
        "storage",
        "00c04258",
        null,
        "pointer"
      ]
    ],
    [
      "00871128",
      "READ",
      [
        "storage",
        "00c04260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008710e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008710cc.md#insn-008710e4)
- 新版 `008710e4`（命令位置の公開資料なし）

~~~diff
- 008710e4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008710e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008710e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008710e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008710e4 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 008710e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008710e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008710e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008710e4 bytes 29a10791
+ 008710e4 bytes 29e10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-083a464e30c0b9fff06c046313ab7705"></a>

### [`008711cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008711cc.md) → [`008711cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008711cc.md) FUN_008711cc

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
      "definition_site": "008711e0",
      "incomplete_value": false,
      "site": "008711e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008711e0",
      "incomplete_value": false,
      "site": "008711e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "008711e4",
      "DATA",
      [
        "storage",
        "00c041e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008711e4",
      "DATA",
      [
        "storage",
        "00c04238",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008711e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008711cc.md#insn-008711e0)
- 新版 `008711e0`（命令位置の公開資料なし）

~~~diff
- 008711e0 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008711e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008711e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008711e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008711e0 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 008711e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008711e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008711e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008711e0 bytes 08a10791
+ 008711e0 bytes 08e10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-617cce8e95fd999a79fb4fb209c234c3"></a>

### [`008711f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008711f0.md) → [`008711f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008711f0.md) FUN_008711f0

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
      "definition_site": "008711f4",
      "incomplete_value": false,
      "site": "008711f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008711f4",
      "incomplete_value": false,
      "site": "008711f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "008711f8",
      "DATA",
      [
        "storage",
        "00c041e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008711f8",
      "DATA",
      [
        "storage",
        "00c04238",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008711f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008711f0.md#insn-008711f4)
- 新版 `008711f4`（命令位置の公開資料なし）

~~~diff
- 008711f4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008711f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008711f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008711f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008711f4 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 008711f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008711f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008711f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008711f4 bytes 08a10791
+ 008711f4 bytes 08e10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0372397e0e6acf7b7ace16e46c470493"></a>

### [`00871208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871208.md) → [`00871208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871208.md) FUN_00871208

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00871348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871348.md) [`0087134c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/0087134c.md) [`00ada774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada774.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00871348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871348.md) [`0087134c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/0087134c.md) [`00ada7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "00871234",
      "incomplete_value": false,
      "site": "0087123c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871234",
      "incomplete_value": false,
      "site": "0087123c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "0087123c",
      "DATA",
      [
        "storage",
        "00c04258",
        null,
        "undefined *"
      ]
    ],
    [
      "00871270",
      "READ",
      [
        "storage",
        "00c04278",
        null,
        "pointer"
      ]
    ],
    [
      "00871270",
      "READ",
      [
        "storage",
        "00c04280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087123c",
      "DATA",
      [
        "storage",
        "00c042a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00871270",
      "READ",
      [
        "storage",
        "00c042c8",
        null,
        "pointer"
      ]
    ],
    [
      "00871270",
      "READ",
      [
        "storage",
        "00c042d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871208.md#insn-00871234)
- 新版 `00871234`（命令位置の公開資料なし）

~~~diff
- 00871234 ["COPY", "tmp:0:8", ["const:258:8"]]
- 00871234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871234 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 00871234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871234 bytes 08610991
+ 00871234 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b76188116fb96b8f22973d80e25665a3"></a>

### [`00871314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871314.md) → [`00871314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871314.md) FUN_00871314

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
      "definition_site": "00871328",
      "incomplete_value": false,
      "site": "0087132c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871328",
      "incomplete_value": false,
      "site": "0087132c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "0087132c",
      "DATA",
      [
        "storage",
        "00c04258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087132c",
      "DATA",
      [
        "storage",
        "00c042a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871314.md#insn-00871328)
- 新版 `00871328`（命令位置の公開資料なし）

~~~diff
- 00871328 ["COPY", "tmp:0:8", ["const:258:8"]]
- 00871328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871328 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 00871328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871328 bytes 08610991
+ 00871328 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c39ced9e62424127600d266c5b158e48"></a>

### [`00871338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871338.md) → [`00871338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871338.md) FUN_00871338

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
      "definition_site": "0087133c",
      "incomplete_value": false,
      "site": "00871340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087133c",
      "incomplete_value": false,
      "site": "00871340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "00871340",
      "DATA",
      [
        "storage",
        "00c04258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871340",
      "DATA",
      [
        "storage",
        "00c042a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087133c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871338.md#insn-0087133c)
- 新版 `0087133c`（命令位置の公開資料なし）

~~~diff
- 0087133c ["COPY", "tmp:0:8", ["const:258:8"]]
- 0087133c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087133c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087133c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087133c ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 0087133c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087133c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087133c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087133c bytes 08610991
+ 0087133c bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-062e62dcc07026dc0439f2dd0d15e883"></a>

### [`00871350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871350.md) → [`00871350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871350.md) FUN_00871350

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008713c0",
      "incomplete_value": true,
      "site": "008713d0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:b96:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008713c0",
      "incomplete_value": true,
      "site": "008713d0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:c23:8"
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
      "definition_site": "00871498",
      "incomplete_value": true,
      "site": "00871498",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871498",
      "incomplete_value": true,
      "site": "00871498",
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
            "const:2c8:8"
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
      "008713c0",
      "READ",
      [
        "storage",
        "00293c23",
        null,
        "string"
      ]
    ],
    [
      "00871498",
      "DATA",
      [
        "storage",
        "00c042c8",
        null,
        "undefined *"
      ]
    ],
    [
      "008714f0",
      "READ",
      [
        "storage",
        "00c042e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008713c0",
      "READ",
      [
        "storage",
        "00293b96",
        null,
        "string"
      ]
    ],
    [
      "00871498",
      "DATA",
      [
        "storage",
        "00c04318",
        null,
        "undefined *"
      ]
    ],
    [
      "008714f0",
      "READ",
      [
        "storage",
        "00c04338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008713b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871350.md#insn-008713b8) · [`00871490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871350.md#insn-00871490)
- 新版 `008713b8`（命令位置の公開資料なし） · `00871490`（命令位置の公開資料なし）

~~~diff
- 008713b8 ["COPY", "tmp:0:8", ["const:c23:8"]]
- 008713b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008713b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008713b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008713b8 ["COPY", "tmp:0:8", ["const:b96:8"]]
+ 008713b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008713b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008713b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008713b8 bytes 298d3091
+ 008713b8 bytes 29592e91
- 00871490 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 00871490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871490 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00871490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871490 bytes 08210b91
+ 00871490 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d30c69aadae46e41803391887305dcb"></a>

### [`008716f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008716f8.md) → [`008716f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008716f8.md) FUN_008716f8

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
      "definition_site": "0087170c",
      "incomplete_value": false,
      "site": "00871710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087170c",
      "incomplete_value": false,
      "site": "00871710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
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
      "00871710",
      "DATA",
      [
        "storage",
        "00c042c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871710",
      "DATA",
      [
        "storage",
        "00c04318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087170c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008716f8.md#insn-0087170c)
- 新版 `0087170c`（命令位置の公開資料なし）

~~~diff
- 0087170c ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 0087170c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087170c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087170c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087170c ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0087170c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087170c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087170c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087170c bytes 08210b91
+ 0087170c bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a8a33ebb4abe298f40471c79bacead0"></a>

### [`0087171c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/0087171c.md) → [`0087171c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/0087171c.md) FUN_0087171c

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
      "definition_site": "00871720",
      "incomplete_value": false,
      "site": "00871724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871720",
      "incomplete_value": false,
      "site": "00871724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
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
      "00871724",
      "DATA",
      [
        "storage",
        "00c042c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871724",
      "DATA",
      [
        "storage",
        "00c04318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/0087171c.md#insn-00871720)
- 新版 `00871720`（命令位置の公開資料なし）

~~~diff
- 00871720 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 00871720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871720 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00871720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871720 bytes 08210b91
+ 00871720 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37d251572a63a75b8b19c5cab264e68a"></a>

### [`008717a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008717a8.md) → [`008717a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008717a8.md) FUN_008717a8

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
      "definition_site": "008717bc",
      "incomplete_value": false,
      "site": "008717c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008717bc",
      "incomplete_value": false,
      "site": "008717c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "008717c0",
      "DATA",
      [
        "storage",
        "00c04378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008717c0",
      "DATA",
      [
        "storage",
        "00c043c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008717bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008717a8.md#insn-008717bc)
- 新版 `008717bc`（命令位置の公開資料なし）

~~~diff
- 008717bc ["COPY", "tmp:0:8", ["const:378:8"]]
- 008717bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008717bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008717bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008717bc ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 008717bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008717bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008717bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008717bc bytes 08e10d91
+ 008717bc bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d170754b39cf53e4ddaa5891b16a9fc3"></a>

### [`008717cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008717cc.md) → [`008717cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008717cc.md) FUN_008717cc

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
      "definition_site": "008717d0",
      "incomplete_value": false,
      "site": "008717d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008717d0",
      "incomplete_value": false,
      "site": "008717d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "008717d4",
      "DATA",
      [
        "storage",
        "00c04378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008717d4",
      "DATA",
      [
        "storage",
        "00c043c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008717d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008717cc.md#insn-008717d0)
- 新版 `008717d0`（命令位置の公開資料なし）

~~~diff
- 008717d0 ["COPY", "tmp:0:8", ["const:378:8"]]
- 008717d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008717d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008717d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008717d0 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 008717d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008717d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008717d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008717d0 bytes 08e10d91
+ 008717d0 bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4d2454bfc35670e60a0a60e5bd6a6a6"></a>

### [`008717e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008717e4.md) → [`008717e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008717e4.md) FUN_008717e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00470050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470050.md) [`00470a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470a98.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00470050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470050.md) [`00470a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470a98.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00871840",
      "incomplete_value": true,
      "site": "00871840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871840",
      "incomplete_value": true,
      "site": "00871840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:189:8"
              ]
            ]
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
      "0087182c",
      "READ",
      [
        "storage",
        "00296189",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087182c",
      "READ",
      [
        "storage",
        "002960fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008717e4.md#insn-00871824)
- 新版 `00871824`（命令位置の公開資料なし）

~~~diff
- 00871824 ["COPY", "tmp:0:8", ["const:189:8"]]
- 00871824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871824 ["COPY", "tmp:0:8", ["const:fc:8"]]
+ 00871824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871824 bytes 29250691
+ 00871824 bytes 29f10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b4bef5a825a2c2caa220cc6585dd496"></a>

### [`00871910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871910.md) → [`00871910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871910.md) FUN_00871910

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
      "definition_site": "00871924",
      "incomplete_value": false,
      "site": "00871928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871924",
      "incomplete_value": false,
      "site": "00871928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "00871928",
      "DATA",
      [
        "storage",
        "00c043f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871928",
      "DATA",
      [
        "storage",
        "00c04448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871910.md#insn-00871924)
- 新版 `00871924`（命令位置の公開資料なし）

~~~diff
- 00871924 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 00871924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871924 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 00871924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871924 bytes 08e10f91
+ 00871924 bytes 08211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6f21ae915bcb3afbb16cfa1b4ef2b57"></a>

### [`00871934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871934.md) → [`00871934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871934.md) FUN_00871934

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
      "definition_site": "00871938",
      "incomplete_value": false,
      "site": "0087193c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871938",
      "incomplete_value": false,
      "site": "0087193c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "0087193c",
      "DATA",
      [
        "storage",
        "00c043f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087193c",
      "DATA",
      [
        "storage",
        "00c04448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871934.md#insn-00871938)
- 新版 `00871938`（命令位置の公開資料なし）

~~~diff
- 00871938 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 00871938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871938 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 00871938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871938 bytes 08e10f91
+ 00871938 bytes 08211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e6fe7088a31d5db90006f18189683f5"></a>

### [`008719c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008719c0.md) → [`008719c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008719c0.md) FUN_008719c0

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
      "definition_site": "008719d4",
      "incomplete_value": false,
      "site": "008719d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008719d4",
      "incomplete_value": false,
      "site": "008719d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "008719d8",
      "DATA",
      [
        "storage",
        "00c04478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008719d8",
      "DATA",
      [
        "storage",
        "00c044c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008719d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008719c0.md#insn-008719d4)
- 新版 `008719d4`（命令位置の公開資料なし）

~~~diff
- 008719d4 ["COPY", "tmp:0:8", ["const:478:8"]]
- 008719d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008719d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008719d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008719d4 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 008719d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008719d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008719d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008719d4 bytes 08e11191
+ 008719d4 bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38421f5c108aded409d5f701a19cfd2e"></a>

### [`008719e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008719e4.md) → [`008719e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008719e4.md) FUN_008719e4

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
      "definition_site": "008719e8",
      "incomplete_value": true,
      "site": "008719ec",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008719e8",
      "incomplete_value": true,
      "site": "008719ec",
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
      "008719ec",
      "DATA",
      [
        "storage",
        "00c04478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008719ec",
      "DATA",
      [
        "storage",
        "00c044c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008719e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008719e4.md#insn-008719e8)
- 新版 `008719e8`（命令位置の公開資料なし）

~~~diff
- 008719e8 ["COPY", "tmp:0:8", ["const:478:8"]]
- 008719e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008719e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008719e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008719e8 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 008719e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008719e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008719e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008719e8 bytes 08e11191
+ 008719e8 bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f920d29e3c6cce8b962e9a767daf8c9"></a>

### [`00871a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a30.md) → [`00871a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871a30.md) FUN_00871a30

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
      "definition_site": "00871a44",
      "incomplete_value": false,
      "site": "00871a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871a44",
      "incomplete_value": false,
      "site": "00871a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "00871a48",
      "DATA",
      [
        "storage",
        "00c044f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871a48",
      "DATA",
      [
        "storage",
        "00c04548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a30.md#insn-00871a44)
- 新版 `00871a44`（命令位置の公開資料なし）

~~~diff
- 00871a44 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00871a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871a44 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 00871a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871a44 bytes 08e11391
+ 00871a44 bytes 08211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-047d405f2f39e3054a68f12ed77e1146"></a>

### [`00871a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a6c.md) → [`00871a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871a6c.md) FUN_00871a6c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0042be48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042be48.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046c018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c018.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0042be48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042be48.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046c018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c018.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00871bb0",
      "incomplete_value": false,
      "site": "00871bb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871bb0",
      "incomplete_value": false,
      "site": "00871bb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "00871bb0",
      "DATA",
      [
        "storage",
        "00c04568",
        null,
        "undefined *"
      ]
    ],
    [
      "00871c2c",
      "READ",
      [
        "storage",
        "00c04588",
        null,
        "pointer"
      ]
    ],
    [
      "00871c2c",
      "READ",
      [
        "storage",
        "00c04590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871bb0",
      "DATA",
      [
        "storage",
        "00c045b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00871c2c",
      "READ",
      [
        "storage",
        "00c045d8",
        null,
        "pointer"
      ]
    ],
    [
      "00871c2c",
      "READ",
      [
        "storage",
        "00c045e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a6c.md#insn-00871ba8)
- 新版 `00871ba8`（命令位置の公開資料なし）

~~~diff
- 00871ba8 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00871ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871ba8 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00871ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871ba8 bytes 08a11591
+ 00871ba8 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d9b967d7382a69ff6478008149a4a67"></a>

### [`00871d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871d80.md) → [`00871d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871d80.md) FUN_00871d80

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
      "definition_site": "00871d94",
      "incomplete_value": false,
      "site": "00871d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871d94",
      "incomplete_value": false,
      "site": "00871d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "00871d98",
      "DATA",
      [
        "storage",
        "00c04568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871d98",
      "DATA",
      [
        "storage",
        "00c045b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871d80.md#insn-00871d94)
- 新版 `00871d94`（命令位置の公開資料なし）

~~~diff
- 00871d94 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00871d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871d94 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00871d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871d94 bytes 08a11591
+ 00871d94 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab0d27c64a5c9367dad7a12e1bec8f8c"></a>

### [`00871da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871da4.md) → [`00871da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871da4.md) FUN_00871da4

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
      "definition_site": "00871da8",
      "incomplete_value": false,
      "site": "00871dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871da8",
      "incomplete_value": false,
      "site": "00871dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "00871dac",
      "DATA",
      [
        "storage",
        "00c04568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871dac",
      "DATA",
      [
        "storage",
        "00c045b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871da4.md#insn-00871da8)
- 新版 `00871da8`（命令位置の公開資料なし）

~~~diff
- 00871da8 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00871da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871da8 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00871da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871da8 bytes 08a11591
+ 00871da8 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87b2b5726997ec0970f69cc8d64b8d21"></a>

### [`00871e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871e30.md) → [`00871e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871e30.md) FUN_00871e30

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
      "definition_site": "00871e44",
      "incomplete_value": false,
      "site": "00871e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871e44",
      "incomplete_value": false,
      "site": "00871e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "00871e48",
      "DATA",
      [
        "storage",
        "00c045f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871e48",
      "DATA",
      [
        "storage",
        "00c04648",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871e30.md#insn-00871e44)
- 新版 `00871e44`（命令位置の公開資料なし）

~~~diff
- 00871e44 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00871e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871e44 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 00871e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871e44 bytes 08e11791
+ 00871e44 bytes 08211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70c735b408eb2d0179febe9918107661"></a>

### [`00871e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871e54.md) → [`00871e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871e54.md) FUN_00871e54

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
      "definition_site": "00871e58",
      "incomplete_value": false,
      "site": "00871e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871e58",
      "incomplete_value": false,
      "site": "00871e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "00871e5c",
      "DATA",
      [
        "storage",
        "00c045f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871e5c",
      "DATA",
      [
        "storage",
        "00c04648",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871e54.md#insn-00871e58)
- 新版 `00871e58`（命令位置の公開資料なし）

~~~diff
- 00871e58 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00871e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871e58 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 00871e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871e58 bytes 08e11791
+ 00871e58 bytes 08211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64a98a6cb9f8e3917bb037e84481787f"></a>

### [`00871eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871eb8.md) → [`00871eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871eb8.md) FUN_00871eb8

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
      "definition_site": "00871ecc",
      "incomplete_value": false,
      "site": "00871ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871ecc",
      "incomplete_value": false,
      "site": "00871ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "00871ed0",
      "DATA",
      [
        "storage",
        "00c04678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871ed0",
      "DATA",
      [
        "storage",
        "00c046c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871eb8.md#insn-00871ecc)
- 新版 `00871ecc`（命令位置の公開資料なし）

~~~diff
- 00871ecc ["COPY", "tmp:0:8", ["const:678:8"]]
- 00871ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871ecc ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00871ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871ecc bytes 08e11991
+ 00871ecc bytes 08211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a19effb66977f6424ae8dfad962d1574"></a>

### [`00871edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871edc.md) → [`00871edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871edc.md) FUN_00871edc

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
      "definition_site": "00871ee0",
      "incomplete_value": false,
      "site": "00871ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871ee0",
      "incomplete_value": false,
      "site": "00871ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "00871ee4",
      "DATA",
      [
        "storage",
        "00c04678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871ee4",
      "DATA",
      [
        "storage",
        "00c046c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871edc.md#insn-00871ee0)
- 新版 `00871ee0`（命令位置の公開資料なし）

~~~diff
- 00871ee0 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00871ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871ee0 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00871ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871ee0 bytes 08e11991
+ 00871ee0 bytes 08211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2c382b2d17169e62fe0c687ceaf3c5c"></a>

### [`00871ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871ef4.md) → [`00871ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871ef4.md) FUN_00871ef4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0051c140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c140.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0051c140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.58% / 新版 95.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00871fc0",
      "incomplete_value": true,
      "site": "00871fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871fc0",
      "incomplete_value": true,
      "site": "00871fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a8f:8"
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
      "definition_site": "00871fd4",
      "incomplete_value": true,
      "site": "00871fd4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00871fd4",
      "incomplete_value": true,
      "site": "00871fd4",
      "value": [
        "LOAD",
        "8",
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
      "00871fc0",
      "READ",
      [
        "storage",
        "002a3a8f",
        null,
        "string"
      ]
    ],
    [
      "00871fc4",
      "READ",
      [
        "storage",
        "002a3a9d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00871fc0",
      "READ",
      [
        "storage",
        "002a3b1a",
        null,
        "string"
      ]
    ],
    [
      "00871fc4",
      "READ",
      [
        "storage",
        "002a3b28",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871ef4.md#insn-00871fb8)
- 新版 `00871fb8`（命令位置の公開資料なし）

~~~diff
- 00871fb8 ["COPY", "tmp:0:8", ["const:a8f:8"]]
- 00871fb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871fb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871fb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871fb8 ["COPY", "tmp:0:8", ["const:b1a:8"]]
+ 00871fb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871fb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871fb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871fb8 bytes 293d2a91
+ 00871fb8 bytes 29692c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7a8217cd3bc22f22e676be64e4e31dd"></a>

### [`0087213c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/0087213c.md) → [`0087213c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/0087213c.md) FUN_0087213c

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
      "definition_site": "00872150",
      "incomplete_value": false,
      "site": "00872154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872150",
      "incomplete_value": false,
      "site": "00872154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "00872154",
      "DATA",
      [
        "storage",
        "00c046f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872154",
      "DATA",
      [
        "storage",
        "00c04748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/0087213c.md#insn-00872150)
- 新版 `00872150`（命令位置の公開資料なし）

~~~diff
- 00872150 ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00872150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872150 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00872150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872150 bytes 08e11b91
+ 00872150 bytes 08211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4d5747414a110274fb58d3a00453eaf"></a>

### [`00872160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872160.md) → [`00872160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872160.md) FUN_00872160

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
      "definition_site": "00872164",
      "incomplete_value": false,
      "site": "00872168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872164",
      "incomplete_value": false,
      "site": "00872168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "00872168",
      "DATA",
      [
        "storage",
        "00c046f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872168",
      "DATA",
      [
        "storage",
        "00c04748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872160.md#insn-00872164)
- 新版 `00872164`（命令位置の公開資料なし）

~~~diff
- 00872164 ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00872164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872164 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00872164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872164 bytes 08e11b91
+ 00872164 bytes 08211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d2951e724844cf29072a695ffa0fc19"></a>

### [`00872178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872178.md) → [`00872178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872178.md) FUN_00872178

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008721ac",
      "incomplete_value": true,
      "site": "008721c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008721ac",
      "incomplete_value": true,
      "site": "008721c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
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
      "008721ac",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008721ac",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008721a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872178.md#insn-008721a4)
- 新版 `008721a4`（命令位置の公開資料なし）

~~~diff
- 008721a4 ["COPY", "tmp:0:8", ["const:de3:8"]]
- 008721a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008721a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008721a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008721a4 ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 008721a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008721a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008721a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008721a4 bytes 298d3791
+ 008721a4 bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e89c1a75efcceeea77e08ac01792775"></a>

### [`00872294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872294.md) → [`00872294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872294.md) FUN_00872294

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
      "definition_site": "008722a8",
      "incomplete_value": false,
      "site": "008722ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008722a8",
      "incomplete_value": false,
      "site": "008722ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "008722ac",
      "DATA",
      [
        "storage",
        "00c04778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008722ac",
      "DATA",
      [
        "storage",
        "00c047c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008722a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872294.md#insn-008722a8)
- 新版 `008722a8`（命令位置の公開資料なし）

~~~diff
- 008722a8 ["COPY", "tmp:0:8", ["const:778:8"]]
- 008722a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008722a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008722a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008722a8 ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 008722a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008722a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008722a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008722a8 bytes 08e11d91
+ 008722a8 bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49eafab882d6d9ae68bfad1e4556458a"></a>

### [`008722b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722b8.md) → [`008722b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/008722b8.md) FUN_008722b8

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
      "definition_site": "008722bc",
      "incomplete_value": true,
      "site": "008722c0",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008722bc",
      "incomplete_value": true,
      "site": "008722c0",
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
      "008722c0",
      "DATA",
      [
        "storage",
        "00c04778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008722c0",
      "DATA",
      [
        "storage",
        "00c047c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008722bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722b8.md#insn-008722bc)
- 新版 `008722bc`（命令位置の公開資料なし）

~~~diff
- 008722bc ["COPY", "tmp:0:8", ["const:778:8"]]
- 008722bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008722bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008722bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008722bc ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 008722bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008722bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008722bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008722bc bytes 08e11d91
+ 008722bc bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e53c78bb86ca1d9547e5ce7cf517701c"></a>

### [`008722d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722d0.md) → [`008722d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/008722d0.md) FUN_008722d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00872368",
      "incomplete_value": true,
      "site": "00872378",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e33:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872368",
      "incomplete_value": true,
      "site": "00872378",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d99:8"
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
      "definition_site": "0087236c",
      "incomplete_value": true,
      "site": "0087237c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0087236c",
      "incomplete_value": true,
      "site": "0087237c",
      "value": [
        "LOAD",
        "8",
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
      "00872368",
      "READ",
      [
        "storage",
        "002a6d99",
        null,
        "string"
      ]
    ],
    [
      "0087236c",
      "READ",
      [
        "storage",
        "002a6da9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00872368",
      "READ",
      [
        "storage",
        "002a6e33",
        null,
        "string"
      ]
    ],
    [
      "0087236c",
      "READ",
      [
        "storage",
        "002a6e43",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722d0.md#insn-00872360) · [`00872364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722d0.md#insn-00872364)
- 新版 `00872360`（命令位置の公開資料なし） · `00872364`（命令位置の公開資料なし）

~~~diff
- 00872360 ["COPY", "tmp:0:8", ["const:d99:8"]]
- 00872360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872360 ["COPY", "tmp:0:8", ["const:e33:8"]]
+ 00872360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872360 bytes 08653691
+ 00872360 bytes 08cd3891
- 00872364 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00872364 bytes e9d1ffd0
+ 00872364 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 00872364 bytes e9d1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d4746d024cb988be535c77d88d1d02a"></a>

### [`008725f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008725f4.md) → [`008725f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/008725f4.md) FUN_008725f4

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
      "definition_site": "00872608",
      "incomplete_value": false,
      "site": "0087260c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872608",
      "incomplete_value": false,
      "site": "0087260c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "0087260c",
      "DATA",
      [
        "storage",
        "00c047f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087260c",
      "DATA",
      [
        "storage",
        "00c04848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008725f4.md#insn-00872608)
- 新版 `00872608`（命令位置の公開資料なし）

~~~diff
- 00872608 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00872608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872608 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00872608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872608 bytes 08e11f91
+ 00872608 bytes 08212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2f4a25567c817ec2678bf50a9106d6d"></a>

### [`00872618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872618.md) → [`00872618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872618.md) FUN_00872618

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
      "definition_site": "0087261c",
      "incomplete_value": false,
      "site": "00872620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087261c",
      "incomplete_value": false,
      "site": "00872620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "00872620",
      "DATA",
      [
        "storage",
        "00c047f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872620",
      "DATA",
      [
        "storage",
        "00c04848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087261c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872618.md#insn-0087261c)
- 新版 `0087261c`（命令位置の公開資料なし）

~~~diff
- 0087261c ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 0087261c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087261c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087261c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087261c ["COPY", "tmp:0:8", ["const:848:8"]]
+ 0087261c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087261c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087261c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087261c bytes 08e11f91
+ 0087261c bytes 08212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03ab1f0ab3e640fc6479c2fb23a92147"></a>

### [`00872630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872630.md) → [`00872630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872630.md) FUN_00872630

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008726c4",
      "incomplete_value": true,
      "site": "008726d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008726c4",
      "incomplete_value": true,
      "site": "008726d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
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
      "008726c4",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008726c4",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008726bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872630.md#insn-008726bc)
- 新版 `008726bc`（命令位置の公開資料なし）

~~~diff
- 008726bc ["COPY", "tmp:0:8", ["const:de3:8"]]
- 008726bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008726bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008726bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008726bc ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 008726bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008726bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008726bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008726bc bytes 298d3791
+ 008726bc bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f2d163789827d8968d2194b47dc414e"></a>

### [`00872790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872790.md) → [`00872790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872790.md) FUN_00872790

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
      "definition_site": "008727a4",
      "incomplete_value": false,
      "site": "008727a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008727a4",
      "incomplete_value": false,
      "site": "008727a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:878:8"
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
      "008727a8",
      "DATA",
      [
        "storage",
        "00c04878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008727a8",
      "DATA",
      [
        "storage",
        "00c048c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008727a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872790.md#insn-008727a4)
- 新版 `008727a4`（命令位置の公開資料なし）

~~~diff
- 008727a4 ["COPY", "tmp:0:8", ["const:878:8"]]
- 008727a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008727a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008727a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008727a4 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 008727a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008727a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008727a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008727a4 bytes 08e12191
+ 008727a4 bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9455caf8e8ebf87e94c20cbc7ada237f"></a>

### [`008727b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008727b4.md) → [`008727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/008727b4.md) FUN_008727b4

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
      "definition_site": "008727b8",
      "incomplete_value": false,
      "site": "008727bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008727b8",
      "incomplete_value": false,
      "site": "008727bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:878:8"
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
      "008727bc",
      "DATA",
      [
        "storage",
        "00c04878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008727bc",
      "DATA",
      [
        "storage",
        "00c048c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008727b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008727b4.md#insn-008727b8)
- 新版 `008727b8`（命令位置の公開資料なし）

~~~diff
- 008727b8 ["COPY", "tmp:0:8", ["const:878:8"]]
- 008727b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008727b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008727b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008727b8 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 008727b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008727b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008727b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008727b8 bytes 08e12191
+ 008727b8 bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1d9eb110a6addc95d4c93c42df45c4b"></a>

### [`008727cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008727cc.md) → [`008727cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/008727cc.md) FUN_008727cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087292c",
      "incomplete_value": true,
      "site": "00872940",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a52:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087292c",
      "incomplete_value": true,
      "site": "00872940",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9c7:8"
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
      "definition_site": "00872944",
      "incomplete_value": true,
      "site": "00872944",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00872944",
      "incomplete_value": true,
      "site": "00872944",
      "value": [
        "LOAD",
        "8",
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
      "0087292c",
      "READ",
      [
        "storage",
        "0029d9c7",
        null,
        "string"
      ]
    ],
    [
      "00872934",
      "READ",
      [
        "storage",
        "0029d9d4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087292c",
      "READ",
      [
        "storage",
        "0029da52",
        null,
        "string"
      ]
    ],
    [
      "00872934",
      "READ",
      [
        "storage",
        "0029da5f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008727cc.md#insn-00872928)
- 新版 `00872928`（命令位置の公開資料なし）

~~~diff
- 00872928 ["COPY", "tmp:0:8", ["const:9c7:8"]]
- 00872928 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00872928 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00872928 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872928 ["COPY", "tmp:0:8", ["const:a52:8"]]
+ 00872928 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872928 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872928 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00872928 bytes 291d2791
+ 00872928 bytes 29492991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98021090d20766d814e200a99e026df7"></a>

### [`00872a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a54.md) → [`00872a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872a54.md) FUN_00872a54

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
      "definition_site": "00872a68",
      "incomplete_value": false,
      "site": "00872a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872a68",
      "incomplete_value": false,
      "site": "00872a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "00872a6c",
      "DATA",
      [
        "storage",
        "00c048f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872a6c",
      "DATA",
      [
        "storage",
        "00c04948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a54.md#insn-00872a68)
- 新版 `00872a68`（命令位置の公開資料なし）

~~~diff
- 00872a68 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00872a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872a68 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 00872a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872a68 bytes 08e12391
+ 00872a68 bytes 08212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc33d7320755f44f0c952164b616e0ba"></a>

### [`00872a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a78.md) → [`00872a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872a78.md) FUN_00872a78

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
      "definition_site": "00872a7c",
      "incomplete_value": false,
      "site": "00872a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872a7c",
      "incomplete_value": false,
      "site": "00872a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "00872a80",
      "DATA",
      [
        "storage",
        "00c048f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872a80",
      "DATA",
      [
        "storage",
        "00c04948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a78.md#insn-00872a7c)
- 新版 `00872a7c`（命令位置の公開資料なし）

~~~diff
- 00872a7c ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00872a7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872a7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872a7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872a7c ["COPY", "tmp:0:8", ["const:948:8"]]
+ 00872a7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872a7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872a7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872a7c bytes 08e12391
+ 00872a7c bytes 08212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d25435ad6c669e003aceb1eed2785794"></a>

### [`00872a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a90.md) → [`00872a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872a90.md) FUN_00872a90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00872ac4",
      "incomplete_value": true,
      "site": "00872ad8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872ac4",
      "incomplete_value": true,
      "site": "00872ad8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
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
      "00872ac4",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00872ac4",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a90.md#insn-00872abc)
- 新版 `00872abc`（命令位置の公開資料なし）

~~~diff
- 00872abc ["COPY", "tmp:0:8", ["const:de3:8"]]
- 00872abc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00872abc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00872abc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872abc ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 00872abc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872abc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872abc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00872abc bytes 298d3791
+ 00872abc bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e56eca55cf03991377d78c4c2752d6d2"></a>

### [`00872bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872bbc.md) → [`00872bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872bbc.md) FUN_00872bbc

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
      "definition_site": "00872bd0",
      "incomplete_value": false,
      "site": "00872bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872bd0",
      "incomplete_value": false,
      "site": "00872bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "00872bd4",
      "DATA",
      [
        "storage",
        "00c04978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872bd4",
      "DATA",
      [
        "storage",
        "00c049c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872bbc.md#insn-00872bd0)
- 新版 `00872bd0`（命令位置の公開資料なし）

~~~diff
- 00872bd0 ["COPY", "tmp:0:8", ["const:978:8"]]
- 00872bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872bd0 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00872bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872bd0 bytes 08e12591
+ 00872bd0 bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2a23f90d9667f6558a140f7d93ead0b"></a>

### [`00872be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872be0.md) → [`00872be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872be0.md) FUN_00872be0

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
      "definition_site": "00872be4",
      "incomplete_value": false,
      "site": "00872be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872be4",
      "incomplete_value": false,
      "site": "00872be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "00872be8",
      "DATA",
      [
        "storage",
        "00c04978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872be8",
      "DATA",
      [
        "storage",
        "00c049c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872be0.md#insn-00872be4)
- 新版 `00872be4`（命令位置の公開資料なし）

~~~diff
- 00872be4 ["COPY", "tmp:0:8", ["const:978:8"]]
- 00872be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872be4 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00872be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872be4 bytes 08e12591
+ 00872be4 bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0cb754e9910dc5356fd7f10339e7431"></a>

### [`00872bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872bf8.md) → [`00872bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872bf8.md) FUN_00872bf8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`007f96a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f96a4.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`007f96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f96a4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.60% / 新版 96.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00872d80",
      "incomplete_value": true,
      "site": "00872d94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872d80",
      "incomplete_value": true,
      "site": "00872d94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a8f:8"
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
      "definition_site": "00872d98",
      "incomplete_value": true,
      "site": "00872d98",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00872d98",
      "incomplete_value": true,
      "site": "00872d98",
      "value": [
        "LOAD",
        "8",
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
      "00872d80",
      "READ",
      [
        "storage",
        "002a3a8f",
        null,
        "string"
      ]
    ],
    [
      "00872d88",
      "READ",
      [
        "storage",
        "002a3a9d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00872d80",
      "READ",
      [
        "storage",
        "002a3b1a",
        null,
        "string"
      ]
    ],
    [
      "00872d88",
      "READ",
      [
        "storage",
        "002a3b28",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872bf8.md#insn-00872d7c)
- 新版 `00872d7c`（命令位置の公開資料なし）

~~~diff
- 00872d7c ["COPY", "tmp:0:8", ["const:a8f:8"]]
- 00872d7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00872d7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00872d7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872d7c ["COPY", "tmp:0:8", ["const:b1a:8"]]
+ 00872d7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872d7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872d7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00872d7c bytes 293d2a91
+ 00872d7c bytes 29692c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b4bdc99644b73a4bfc62fd736dd4058"></a>

### [`00872eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872eb4.md) → [`00872eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872eb4.md) FUN_00872eb4

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
      "definition_site": "00872ec8",
      "incomplete_value": false,
      "site": "00872ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872ec8",
      "incomplete_value": false,
      "site": "00872ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "00872ecc",
      "DATA",
      [
        "storage",
        "00c049f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872ecc",
      "DATA",
      [
        "storage",
        "00c04a48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872eb4.md#insn-00872ec8)
- 新版 `00872ec8`（命令位置の公開資料なし）

~~~diff
- 00872ec8 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00872ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872ec8 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 00872ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872ec8 bytes 08e12791
+ 00872ec8 bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-194529b795b7cb3215064fa4ed1e0706"></a>

### [`00872ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872ed8.md) → [`00872ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872ed8.md) FUN_00872ed8

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
      "definition_site": "00872edc",
      "incomplete_value": false,
      "site": "00872ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872edc",
      "incomplete_value": false,
      "site": "00872ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "00872ee0",
      "DATA",
      [
        "storage",
        "00c049f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872ee0",
      "DATA",
      [
        "storage",
        "00c04a48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872ed8.md#insn-00872edc)
- 新版 `00872edc`（命令位置の公開資料なし）

~~~diff
- 00872edc ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00872edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872edc ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 00872edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872edc bytes 08e12791
+ 00872edc bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e891e98ae561930f3a20c1e9457eb89"></a>

### [`00872ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872ef0.md) → [`00872ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872ef0.md) FUN_00872ef0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00872f84",
      "incomplete_value": true,
      "site": "00872f98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872f84",
      "incomplete_value": true,
      "site": "00872f98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
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
      "00872f84",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00872f84",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872ef0.md#insn-00872f7c)
- 新版 `00872f7c`（命令位置の公開資料なし）

~~~diff
- 00872f7c ["COPY", "tmp:0:8", ["const:de3:8"]]
- 00872f7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00872f7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00872f7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872f7c ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 00872f7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872f7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872f7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00872f7c bytes 298d3791
+ 00872f7c bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e32b863149d160e83fb48677a4ca57cc"></a>

### [`00873050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873050.md) → [`00873050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873050.md) FUN_00873050

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
      "definition_site": "00873064",
      "incomplete_value": false,
      "site": "00873068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873064",
      "incomplete_value": false,
      "site": "00873068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:a78:8"
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
      "00873068",
      "DATA",
      [
        "storage",
        "00c04a78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873068",
      "DATA",
      [
        "storage",
        "00c04ac8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873050.md#insn-00873064)
- 新版 `00873064`（命令位置の公開資料なし）

~~~diff
- 00873064 ["COPY", "tmp:0:8", ["const:a78:8"]]
- 00873064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873064 ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 00873064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873064 bytes 08e12991
+ 00873064 bytes 08212b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e8b2cdba581ffc8ba5a9afc90a1912e"></a>

### [`00873074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873074.md) → [`00873074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873074.md) FUN_00873074

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
      "definition_site": "00873078",
      "incomplete_value": false,
      "site": "0087307c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873078",
      "incomplete_value": false,
      "site": "0087307c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:a78:8"
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
      "0087307c",
      "DATA",
      [
        "storage",
        "00c04a78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087307c",
      "DATA",
      [
        "storage",
        "00c04ac8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873074.md#insn-00873078)
- 新版 `00873078`（命令位置の公開資料なし）

~~~diff
- 00873078 ["COPY", "tmp:0:8", ["const:a78:8"]]
- 00873078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873078 ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 00873078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873078 bytes 08e12991
+ 00873078 bytes 08212b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34e2183bee44dea0c40a7332dd797864"></a>

### [`00873294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873294.md) → [`00873294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873294.md) FUN_00873294

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
      "definition_site": "008732a8",
      "incomplete_value": false,
      "site": "008732ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008732a8",
      "incomplete_value": false,
      "site": "008732ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "008732ac",
      "DATA",
      [
        "storage",
        "00c04af8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008732ac",
      "DATA",
      [
        "storage",
        "00c04b48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008732a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873294.md#insn-008732a8)
- 新版 `008732a8`（命令位置の公開資料なし）

~~~diff
- 008732a8 ["COPY", "tmp:0:8", ["const:af8:8"]]
- 008732a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008732a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008732a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008732a8 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 008732a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008732a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008732a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008732a8 bytes 08e12b91
+ 008732a8 bytes 08212d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6209ccbeffa15fd9db7e56ca50138946"></a>

### [`008732b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008732b8.md) → [`008732b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/008732b8.md) FUN_008732b8

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
      "definition_site": "008732bc",
      "incomplete_value": false,
      "site": "008732c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008732bc",
      "incomplete_value": false,
      "site": "008732c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "008732c0",
      "DATA",
      [
        "storage",
        "00c04af8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008732c0",
      "DATA",
      [
        "storage",
        "00c04b48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008732bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008732b8.md#insn-008732bc)
- 新版 `008732bc`（命令位置の公開資料なし）

~~~diff
- 008732bc ["COPY", "tmp:0:8", ["const:af8:8"]]
- 008732bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008732bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008732bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008732bc ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 008732bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008732bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008732bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008732bc bytes 08e12b91
+ 008732bc bytes 08212d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a9c47fae12a6a95f427076ab55a3a64"></a>

### [`008732d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008732d0.md) → [`008732d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/008732d0.md) FUN_008732d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00873304",
      "incomplete_value": true,
      "site": "00873318",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873304",
      "incomplete_value": true,
      "site": "00873318",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
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
      "00873304",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00873304",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008732fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008732d0.md#insn-008732fc)
- 新版 `008732fc`（命令位置の公開資料なし）

~~~diff
- 008732fc ["COPY", "tmp:0:8", ["const:de3:8"]]
- 008732fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008732fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008732fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008732fc ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 008732fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008732fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008732fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008732fc bytes 298d3791
+ 008732fc bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-399ac29e0b35b166a7eedcf85586e33d"></a>

### [`008733fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008733fc.md) → [`008733fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/008733fc.md) FUN_008733fc

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
      "definition_site": "00873410",
      "incomplete_value": false,
      "site": "00873414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873410",
      "incomplete_value": false,
      "site": "00873414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "00873414",
      "DATA",
      [
        "storage",
        "00c04b78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873414",
      "DATA",
      [
        "storage",
        "00c04bc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008733fc.md#insn-00873410)
- 新版 `00873410`（命令位置の公開資料なし）

~~~diff
- 00873410 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 00873410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873410 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 00873410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873410 bytes 08e12d91
+ 00873410 bytes 08212f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-532b843abb4b36d19be0446aadd4a7d1"></a>

### [`00873420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873420.md) → [`00873420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873420.md) FUN_00873420

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
      "definition_site": "00873424",
      "incomplete_value": false,
      "site": "00873428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873424",
      "incomplete_value": false,
      "site": "00873428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "00873428",
      "DATA",
      [
        "storage",
        "00c04b78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873428",
      "DATA",
      [
        "storage",
        "00c04bc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873420.md#insn-00873424)
- 新版 `00873424`（命令位置の公開資料なし）

~~~diff
- 00873424 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 00873424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873424 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 00873424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873424 bytes 08e12d91
+ 00873424 bytes 08212f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-773345511204bbd4ca8fba88a6efb602"></a>

### [`00873438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873438.md) → [`00873438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873438.md) FUN_00873438

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0051c140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c140.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0051c140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c140.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008734ac",
      "incomplete_value": true,
      "site": "008734bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008734ac",
      "incomplete_value": true,
      "site": "008734bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b11:8"
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
      "definition_site": "008734b0",
      "incomplete_value": true,
      "site": "008734c0",
      "value": [
        "LOAD",
        "16",
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008734b0",
      "incomplete_value": true,
      "site": "008734c0",
      "value": [
        "LOAD",
        "16",
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
                "const:c:8"
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
      "008734ac",
      "READ",
      [
        "storage",
        "002a4b11",
        null,
        "string"
      ]
    ],
    [
      "008734b0",
      "READ",
      [
        "storage",
        "002a4b1d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008734ac",
      "READ",
      [
        "storage",
        "002a4b9c",
        null,
        "string"
      ]
    ],
    [
      "008734b0",
      "READ",
      [
        "storage",
        "002a4ba8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008734a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873438.md#insn-008734a4) · [`008734a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873438.md#insn-008734a8)
- 新版 `008734a4`（命令位置の公開資料なし） · `008734a8`（命令位置の公開資料なし）

~~~diff
- 008734a4 ["COPY", "tmp:0:8", ["const:b11:8"]]
- 008734a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008734a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008734a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008734a4 ["COPY", "tmp:0:8", ["const:b9c:8"]]
+ 008734a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008734a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008734a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008734a4 bytes 08452c91
+ 008734a4 bytes 08712e91
- 008734a8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 008734a8 bytes e9d1ffd0
+ 008734a8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 008734a8 bytes e9d1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1ba29facb9dd863e14aa86402e2c5f0"></a>

### [`0087363c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/0087363c.md) → [`0087363c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/0087363c.md) FUN_0087363c

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
      "definition_site": "00873650",
      "incomplete_value": false,
      "site": "00873654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873650",
      "incomplete_value": false,
      "site": "00873654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "00873654",
      "DATA",
      [
        "storage",
        "00c04bf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873654",
      "DATA",
      [
        "storage",
        "00c04c48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/0087363c.md#insn-00873650)
- 新版 `00873650`（命令位置の公開資料なし）

~~~diff
- 00873650 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00873650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873650 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00873650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873650 bytes 08e12f91
+ 00873650 bytes 08213191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87c8d367453800c081e325ab0ce42fe4"></a>

### [`00873660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873660.md) → [`00873660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873660.md) FUN_00873660

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
      "definition_site": "00873664",
      "incomplete_value": false,
      "site": "00873668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873664",
      "incomplete_value": false,
      "site": "00873668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "00873668",
      "DATA",
      [
        "storage",
        "00c04bf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873668",
      "DATA",
      [
        "storage",
        "00c04c48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873660.md#insn-00873664)
- 新版 `00873664`（命令位置の公開資料なし）

~~~diff
- 00873664 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00873664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873664 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00873664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873664 bytes 08e12f91
+ 00873664 bytes 08213191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cc3d25332d75b26fb70f5009d8032e2"></a>

### [`00873678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873678.md) → [`00873678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873678.md) FUN_00873678

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008736ac",
      "incomplete_value": true,
      "site": "008736c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008736ac",
      "incomplete_value": true,
      "site": "008736c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
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
      "008736ac",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008736ac",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008736a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873678.md#insn-008736a4)
- 新版 `008736a4`（命令位置の公開資料なし）

~~~diff
- 008736a4 ["COPY", "tmp:0:8", ["const:de3:8"]]
- 008736a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008736a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008736a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008736a4 ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 008736a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008736a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008736a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008736a4 bytes 298d3791
+ 008736a4 bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea349c2abad004f68989338298572bc2"></a>

### [`008737a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008737a4.md) → [`008737a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/008737a4.md) FUN_008737a4

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
      "definition_site": "008737b8",
      "incomplete_value": false,
      "site": "008737bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008737b8",
      "incomplete_value": false,
      "site": "008737bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "008737bc",
      "DATA",
      [
        "storage",
        "00c04c78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008737bc",
      "DATA",
      [
        "storage",
        "00c04cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008737b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008737a4.md#insn-008737b8)
- 新版 `008737b8`（命令位置の公開資料なし）

~~~diff
- 008737b8 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 008737b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008737b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008737b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008737b8 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 008737b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008737b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008737b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008737b8 bytes 08e13191
+ 008737b8 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c1c12b35f22d7cecca9d98b9b5840eb"></a>

### [`008737c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008737c8.md) → [`008737c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/008737c8.md) FUN_008737c8

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
      "definition_site": "008737cc",
      "incomplete_value": false,
      "site": "008737d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008737cc",
      "incomplete_value": false,
      "site": "008737d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "008737d0",
      "DATA",
      [
        "storage",
        "00c04c78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008737d0",
      "DATA",
      [
        "storage",
        "00c04cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008737cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008737c8.md#insn-008737cc)
- 新版 `008737cc`（命令位置の公開資料なし）

~~~diff
- 008737cc ["COPY", "tmp:0:8", ["const:c78:8"]]
- 008737cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008737cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008737cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008737cc ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 008737cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008737cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008737cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008737cc bytes 08e13191
+ 008737cc bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-131776bb740ede30d48551b7cccf92bf"></a>

### [`00873a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873a0c.md) → [`00873a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873a0c.md) FUN_00873a0c

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
      "definition_site": "00873a20",
      "incomplete_value": false,
      "site": "00873a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873a20",
      "incomplete_value": false,
      "site": "00873a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "00873a24",
      "DATA",
      [
        "storage",
        "00c04cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873a24",
      "DATA",
      [
        "storage",
        "00c04d48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873a0c.md#insn-00873a20)
- 新版 `00873a20`（命令位置の公開資料なし）

~~~diff
- 00873a20 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00873a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873a20 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00873a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873a20 bytes 08e13391
+ 00873a20 bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b42bc34e96ecdffbffaf2334635075b"></a>

### [`00873a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873a30.md) → [`00873a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873a30.md) FUN_00873a30

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
      "definition_site": "00873a34",
      "incomplete_value": false,
      "site": "00873a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873a34",
      "incomplete_value": false,
      "site": "00873a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "00873a38",
      "DATA",
      [
        "storage",
        "00c04cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873a38",
      "DATA",
      [
        "storage",
        "00c04d48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873a30.md#insn-00873a34)
- 新版 `00873a34`（命令位置の公開資料なし）

~~~diff
- 00873a34 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00873a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873a34 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00873a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873a34 bytes 08e13391
+ 00873a34 bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c84122e894b4439126b87a23e6c77f89"></a>

### [`00873a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873a48.md) → [`00873a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873a48.md) FUN_00873a48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.59% / 新版 96.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00873b4c",
      "incomplete_value": true,
      "site": "00873b60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873b4c",
      "incomplete_value": true,
      "site": "00873b60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
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
      "00873b4c",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00873b4c",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873a48.md#insn-00873b44)
- 新版 `00873b44`（命令位置の公開資料なし）

~~~diff
- 00873b44 ["COPY", "tmp:0:8", ["const:de3:8"]]
- 00873b44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00873b44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00873b44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00873b44 ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 00873b44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00873b44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00873b44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00873b44 bytes 298d3791
+ 00873b44 bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-904cf257bb89c6e94b0dd60bc2a47bca"></a>

### [`00873c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c2c.md) → [`00873c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873c2c.md) FUN_00873c2c

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
      "definition_site": "00873c40",
      "incomplete_value": false,
      "site": "00873c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873c40",
      "incomplete_value": false,
      "site": "00873c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "00873c44",
      "DATA",
      [
        "storage",
        "00c04d78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873c44",
      "DATA",
      [
        "storage",
        "00c04dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c2c.md#insn-00873c40)
- 新版 `00873c40`（命令位置の公開資料なし）

~~~diff
- 00873c40 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00873c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873c40 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00873c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873c40 bytes 08e13591
+ 00873c40 bytes 08213791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-748179722a8318a1bdb72392d6cd823f"></a>

### [`00873c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c50.md) → [`00873c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873c50.md) FUN_00873c50

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
      "definition_site": "00873c54",
      "incomplete_value": false,
      "site": "00873c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873c54",
      "incomplete_value": false,
      "site": "00873c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "00873c58",
      "DATA",
      [
        "storage",
        "00c04d78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873c58",
      "DATA",
      [
        "storage",
        "00c04dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c50.md#insn-00873c54)
- 新版 `00873c54`（命令位置の公開資料なし）

~~~diff
- 00873c54 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00873c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873c54 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00873c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873c54 bytes 08e13591
+ 00873c54 bytes 08213791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eb7bf66658cdadb6114fc8b82fb9fe2"></a>

### [`00873c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c68.md) → [`00873c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873c68.md) FUN_00873c68

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c9c0.md) [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c9c0.md) [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873e1c",
      "incomplete_value": false,
      "site": "00873e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873e1c",
      "incomplete_value": false,
      "site": "00873e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "00873e1c",
      "DATA",
      [
        "storage",
        "00c04de8",
        null,
        "undefined *"
      ]
    ],
    [
      "00873ea0",
      "READ",
      [
        "storage",
        "00c04e08",
        null,
        "pointer"
      ]
    ],
    [
      "00873ea0",
      "READ",
      [
        "storage",
        "00c04e10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873e1c",
      "DATA",
      [
        "storage",
        "00c04e38",
        null,
        "undefined *"
      ]
    ],
    [
      "00873ea0",
      "READ",
      [
        "storage",
        "00c04e58",
        null,
        "pointer"
      ]
    ],
    [
      "00873ea0",
      "READ",
      [
        "storage",
        "00c04e60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c68.md#insn-00873e14)
- 新版 `00873e14`（命令位置の公開資料なし）

~~~diff
- 00873e14 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 00873e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873e14 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 00873e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873e14 bytes 08a13791
+ 00873e14 bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efad4ab70e214bec6ee067a543ee6b65"></a>

### [`00874088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874088.md) → [`00874088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874088.md) FUN_00874088

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
      "definition_site": "0087409c",
      "incomplete_value": false,
      "site": "008740a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087409c",
      "incomplete_value": false,
      "site": "008740a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "008740a0",
      "DATA",
      [
        "storage",
        "00c04de8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008740a0",
      "DATA",
      [
        "storage",
        "00c04e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087409c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874088.md#insn-0087409c)
- 新版 `0087409c`（命令位置の公開資料なし）

~~~diff
- 0087409c ["COPY", "tmp:0:8", ["const:de8:8"]]
- 0087409c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087409c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087409c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087409c ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 0087409c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087409c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087409c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087409c bytes 08a13791
+ 0087409c bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-971c7dc99a410977239540856a290ffb"></a>

### [`008740ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008740ac.md) → [`008740ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008740ac.md) FUN_008740ac

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
      "definition_site": "008740b0",
      "incomplete_value": false,
      "site": "008740b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008740b0",
      "incomplete_value": false,
      "site": "008740b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "008740b4",
      "DATA",
      [
        "storage",
        "00c04de8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008740b4",
      "DATA",
      [
        "storage",
        "00c04e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008740b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008740ac.md#insn-008740b0)
- 新版 `008740b0`（命令位置の公開資料なし）

~~~diff
- 008740b0 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 008740b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008740b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008740b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008740b0 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 008740b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008740b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008740b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008740b0 bytes 08a13791
+ 008740b0 bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90d1e44438a376ea114cc80f883f9c62"></a>

### [`008740c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008740c4.md) → [`008740c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008740c4.md) FUN_008740c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0042c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c9c0.md) [`0058e620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058e620.md) [`0058e878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058e878.md) [`005902dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/005902dc.md) [`0073eb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073eb44.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0042c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c9c0.md) [`0058e620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e620.md) [`0058e878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e878.md) [`005902dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/005902dc.md) [`0073eb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073eb44.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087410c",
      "incomplete_value": false,
      "site": "00874114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087410c",
      "incomplete_value": false,
      "site": "00874114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "definition_site": "00874190",
      "incomplete_value": false,
      "site": "00874198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874190",
      "incomplete_value": false,
      "site": "00874198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "00874114",
      "DATA",
      [
        "storage",
        "00c04e58",
        null,
        "undefined *"
      ]
    ],
    [
      "00874184",
      "READ",
      [
        "storage",
        "00c04e78",
        null,
        "pointer"
      ]
    ],
    [
      "00874184",
      "READ",
      [
        "storage",
        "00c04e80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874114",
      "DATA",
      [
        "storage",
        "00c04ea8",
        null,
        "undefined *"
      ]
    ],
    [
      "00874184",
      "READ",
      [
        "storage",
        "00c04ec8",
        null,
        "pointer"
      ]
    ],
    [
      "00874184",
      "READ",
      [
        "storage",
        "00c04ed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087410c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008740c4.md#insn-0087410c) · [`00874190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008740c4.md#insn-00874190)
- 新版 `0087410c`（命令位置の公開資料なし） · `00874190`（命令位置の公開資料なし）

~~~diff
- 0087410c ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0087410c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087410c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087410c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087410c ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 0087410c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087410c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087410c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087410c bytes 08613991
+ 0087410c bytes 08a13a91
- 00874190 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00874190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874190 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 00874190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874190 bytes 08613b91
+ 00874190 bytes 08a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b730c5bd23de4f0ccd320dacb9fe7aeb"></a>

### [`00874288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874288.md) → [`00874288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874288.md) FUN_00874288

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
      "definition_site": "0087429c",
      "incomplete_value": false,
      "site": "008742a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087429c",
      "incomplete_value": false,
      "site": "008742a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "008742a0",
      "DATA",
      [
        "storage",
        "00c04e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008742a0",
      "DATA",
      [
        "storage",
        "00c04ea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087429c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874288.md#insn-0087429c)
- 新版 `0087429c`（命令位置の公開資料なし）

~~~diff
- 0087429c ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0087429c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087429c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087429c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087429c ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 0087429c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087429c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087429c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087429c bytes 08613991
+ 0087429c bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47c58fcd17fd82dab039ef9331df566e"></a>

### [`008742ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008742ac.md) → [`008742ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008742ac.md) FUN_008742ac

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
      "definition_site": "008742b0",
      "incomplete_value": false,
      "site": "008742b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008742b0",
      "incomplete_value": false,
      "site": "008742b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "008742b4",
      "DATA",
      [
        "storage",
        "00c04e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008742b4",
      "DATA",
      [
        "storage",
        "00c04ea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008742b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008742ac.md#insn-008742b0)
- 新版 `008742b0`（命令位置の公開資料なし）

~~~diff
- 008742b0 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 008742b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008742b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008742b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008742b0 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 008742b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008742b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008742b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008742b0 bytes 08613991
+ 008742b0 bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-481f828409ea0606cace026348c3ad02"></a>

### [`00874328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874328.md) → [`00874328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874328.md) FUN_00874328

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
      "definition_site": "0087433c",
      "incomplete_value": false,
      "site": "00874340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087433c",
      "incomplete_value": false,
      "site": "00874340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "00874340",
      "DATA",
      [
        "storage",
        "00c04ed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874340",
      "DATA",
      [
        "storage",
        "00c04f28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087433c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874328.md#insn-0087433c)
- 新版 `0087433c`（命令位置の公開資料なし）

~~~diff
- 0087433c ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 0087433c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087433c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087433c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087433c ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 0087433c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087433c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087433c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087433c bytes 08613b91
+ 0087433c bytes 08a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdcbc17df989fa2681bb7f687687c7d3"></a>

### [`0087434c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/0087434c.md) → [`0087434c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/0087434c.md) FUN_0087434c

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
      "definition_site": "00874350",
      "incomplete_value": false,
      "site": "00874354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874350",
      "incomplete_value": false,
      "site": "00874354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "00874354",
      "DATA",
      [
        "storage",
        "00c04ed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874354",
      "DATA",
      [
        "storage",
        "00c04f28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/0087434c.md#insn-00874350)
- 新版 `00874350`（命令位置の公開資料なし）

~~~diff
- 00874350 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00874350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874350 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 00874350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874350 bytes 08613b91
+ 00874350 bytes 08a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22a91b9e32fcdcbfaffd0c21d10e28a5"></a>

### [`008743b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008743b0.md) → [`008743b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008743b0.md) FUN_008743b0

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
      "definition_site": "008743c4",
      "incomplete_value": false,
      "site": "008743c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008743c4",
      "incomplete_value": false,
      "site": "008743c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "008743c8",
      "DATA",
      [
        "storage",
        "00c04f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008743c8",
      "DATA",
      [
        "storage",
        "00c04fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008743c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008743b0.md#insn-008743c4)
- 新版 `008743c4`（命令位置の公開資料なし）

~~~diff
- 008743c4 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008743c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008743c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008743c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008743c4 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 008743c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008743c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008743c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008743c4 bytes 08e13d91
+ 008743c4 bytes 08213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0e0f087c705f4b698e38460c49d8a1b"></a>

### [`008743d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008743d4.md) → [`008743d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008743d4.md) FUN_008743d4

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
      "definition_site": "008743d8",
      "incomplete_value": false,
      "site": "008743dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008743d8",
      "incomplete_value": false,
      "site": "008743dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "008743dc",
      "DATA",
      [
        "storage",
        "00c04f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008743dc",
      "DATA",
      [
        "storage",
        "00c04fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008743d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008743d4.md#insn-008743d8)
- 新版 `008743d8`（命令位置の公開資料なし）

~~~diff
- 008743d8 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008743d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008743d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008743d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008743d8 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 008743d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008743d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008743d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008743d8 bytes 08e13d91
+ 008743d8 bytes 08213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c691d5261d6e5f8f3857c8365abcac91"></a>

### [`008743ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008743ec.md) → [`008743ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008743ec.md) FUN_008743ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00833158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833158.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00833158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/00833158.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.92% / 新版 94.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874474",
      "incomplete_value": true,
      "site": "00874484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874474",
      "incomplete_value": true,
      "site": "00874484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
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
      "00874474",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00874474",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087446c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008743ec.md#insn-0087446c)
- 新版 `0087446c`（命令位置の公開資料なし）

~~~diff
- 0087446c ["COPY", "tmp:0:8", ["const:de3:8"]]
- 0087446c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087446c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087446c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087446c ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 0087446c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087446c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087446c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087446c bytes 298d3791
+ 0087446c bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ae6453d862ad737f235ce39b2f3ebd9"></a>

### [`00874538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874538.md) → [`00874538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874538.md) FUN_00874538

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
      "definition_site": "0087454c",
      "incomplete_value": false,
      "site": "00874550",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087454c",
      "incomplete_value": false,
      "site": "00874550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "00874550",
      "DATA",
      [
        "storage",
        "00c04ff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874550",
      "DATA",
      [
        "storage",
        "00c05048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874538.md#insn-00874548) · [`0087454c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874538.md#insn-0087454c)
- 新版 `00874548`（命令位置の公開資料なし） · `0087454c`（命令位置の公開資料なし）

~~~diff
- 00874548 ["COPY", "register:4040:8", ["const:c04000:8"]]
+ 00874548 ["COPY", "register:4040:8", ["const:c05000:8"]]
- 00874548 bytes 881c0090
+ 00874548 bytes 881c00b0
- 0087454c ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 0087454c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087454c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087454c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087454c ["COPY", "tmp:0:8", ["const:48:8"]]
+ 0087454c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087454c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087454c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087454c bytes 08e13f91
+ 0087454c bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9910656aab506bd52e87458948ff806"></a>

### [`0087455c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/0087455c.md) → [`0087455c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/0087455c.md) FUN_0087455c

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
      "definition_site": "00874560",
      "incomplete_value": false,
      "site": "00874564",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874560",
      "incomplete_value": false,
      "site": "00874564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "00874564",
      "DATA",
      [
        "storage",
        "00c04ff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874564",
      "DATA",
      [
        "storage",
        "00c05048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087455c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/0087455c.md#insn-0087455c) · [`00874560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/0087455c.md#insn-00874560)
- 新版 `0087455c`（命令位置の公開資料なし） · `00874560`（命令位置の公開資料なし）

~~~diff
- 0087455c ["COPY", "register:4040:8", ["const:c04000:8"]]
+ 0087455c ["COPY", "register:4040:8", ["const:c05000:8"]]
- 0087455c bytes 881c0090
+ 0087455c bytes 881c00b0
- 00874560 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 00874560 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874560 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874560 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874560 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00874560 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874560 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874560 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874560 bytes 08e13f91
+ 00874560 bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ea48cd8ff2b95b4f9206669b3ee3afe"></a>

### [`00874684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874684.md) → [`00874684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874684.md) FUN_00874684

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
      "definition_site": "00874698",
      "incomplete_value": false,
      "site": "0087469c",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874698",
      "incomplete_value": false,
      "site": "0087469c",
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
            "const:88:8"
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
      "0087469c",
      "DATA",
      [
        "storage",
        "00c05088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087469c",
      "DATA",
      [
        "storage",
        "00c050d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874684.md#insn-00874698)
- 新版 `00874698`（命令位置の公開資料なし）

~~~diff
- 00874698 ["COPY", "tmp:0:8", ["const:88:8"]]
- 00874698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874698 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 00874698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874698 bytes 08210291
+ 00874698 bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2afbaefffd7ec70a898218107b7e0d1"></a>

### [`008746a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008746a8.md) → [`008746a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008746a8.md) FUN_008746a8

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
      "definition_site": "008746ac",
      "incomplete_value": false,
      "site": "008746b0",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008746ac",
      "incomplete_value": false,
      "site": "008746b0",
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
            "const:88:8"
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
      "008746b0",
      "DATA",
      [
        "storage",
        "00c05088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008746b0",
      "DATA",
      [
        "storage",
        "00c050d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008746ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008746a8.md#insn-008746ac)
- 新版 `008746ac`（命令位置の公開資料なし）

~~~diff
- 008746ac ["COPY", "tmp:0:8", ["const:88:8"]]
- 008746ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008746ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008746ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008746ac ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 008746ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008746ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008746ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008746ac bytes 08210291
+ 008746ac bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c455694dab02f7e19555cae0c9142cd"></a>

### [`008746c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008746c0.md) → [`008746c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008746c0.md) FUN_008746c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042c07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c07c.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042c07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c07c.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874748",
      "incomplete_value": true,
      "site": "0087475c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c73:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874748",
      "incomplete_value": true,
      "site": "0087475c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:be8:8"
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
      "00874748",
      "READ",
      [
        "storage",
        "002a1be8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00874748",
      "READ",
      [
        "storage",
        "002a1c73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008746c0.md#insn-00874740)
- 新版 `00874740`（命令位置の公開資料なし）

~~~diff
- 00874740 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00874740 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874740 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874740 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874740 ["COPY", "tmp:0:8", ["const:c73:8"]]
+ 00874740 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874740 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874740 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874740 bytes 29a12f91
+ 00874740 bytes 29cd3191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9932d1080d155d4589d877aa753676b"></a>

### [`0087491c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/0087491c.md) → [`0087491c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/0087491c.md) FUN_0087491c

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
      "definition_site": "00874930",
      "incomplete_value": false,
      "site": "00874934",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874930",
      "incomplete_value": false,
      "site": "00874934",
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
            "const:108:8"
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
      "00874934",
      "DATA",
      [
        "storage",
        "00c05108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874934",
      "DATA",
      [
        "storage",
        "00c05158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/0087491c.md#insn-00874930)
- 新版 `00874930`（命令位置の公開資料なし）

~~~diff
- 00874930 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00874930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874930 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00874930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874930 bytes 08210491
+ 00874930 bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6a74441e1247f646fbb5e03aa775b85"></a>

### [`00874940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874940.md) → [`00874940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874940.md) FUN_00874940

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
      "definition_site": "00874944",
      "incomplete_value": false,
      "site": "00874948",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874944",
      "incomplete_value": false,
      "site": "00874948",
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
            "const:108:8"
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
      "00874948",
      "DATA",
      [
        "storage",
        "00c05108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874948",
      "DATA",
      [
        "storage",
        "00c05158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874940.md#insn-00874944)
- 新版 `00874944`（命令位置の公開資料なし）

~~~diff
- 00874944 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00874944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874944 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00874944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874944 bytes 08210491
+ 00874944 bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-843b9035744e1a760fbd3d6cae0ff391"></a>

### [`00874958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874958.md) → [`00874958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874958.md) FUN_00874958

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0042c07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c07c.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0042c07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c07c.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874a1c",
      "incomplete_value": true,
      "site": "00874a34",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:c86:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874a1c",
      "incomplete_value": true,
      "site": "00874a34",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:bfb:8"
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
      "00874a1c",
      "READ",
      [
        "storage",
        "002a1bfb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00874a1c",
      "READ",
      [
        "storage",
        "002a1c86",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874958.md#insn-00874a14)
- 新版 `00874a14`（命令位置の公開資料なし）

~~~diff
- 00874a14 ["COPY", "tmp:0:8", ["const:bfb:8"]]
- 00874a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874a14 ["COPY", "tmp:0:8", ["const:c86:8"]]
+ 00874a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874a14 bytes 29ed2f91
+ 00874a14 bytes 29193291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4235db5b70f275b62b74d464f57e869b"></a>

### [`00874ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874ae8.md) → [`00874ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874ae8.md) FUN_00874ae8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) [`00874ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874ae8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) [`00874ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874ae8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.49% / 新版 98.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00874c40",
      "incomplete_value": true,
      "site": "00874c48",
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
      "definition_site": "00874c40",
      "incomplete_value": true,
      "site": "00874c48",
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
      "definition_site": "00874c64",
      "incomplete_value": false,
      "site": "00874c70",
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
      "definition_site": "00874c64",
      "incomplete_value": false,
      "site": "00874c70",
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
      "definition_site": "00874da0",
      "incomplete_value": false,
      "site": "00874da8",
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
      "definition_site": "00874da0",
      "incomplete_value": false,
      "site": "00874da8",
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
      "00874c40",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00874c64",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00874da0",
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
      "00874c40",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00874c64",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00874da0",
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

- 旧版 [`00874c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874ae8.md#insn-00874c40) · [`00874c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874ae8.md#insn-00874c64) · [`00874da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874ae8.md#insn-00874da0)
- 新版 `00874c40`（命令位置の公開資料なし） · `00874c64`（命令位置の公開資料なし） · `00874da0`（命令位置の公開資料なし）

~~~diff
- 00874c40 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00874c40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00874c40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00874c40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00874c40 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00874c40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00874c40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00874c40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00874c40 bytes 21280c91
+ 00874c40 bytes 21900e91
- 00874c64 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00874c64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00874c64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00874c64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00874c64 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00874c64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00874c64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00874c64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00874c64 bytes 21642491
+ 00874c64 bytes 21142291
- 00874da0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00874da0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00874da0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00874da0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00874da0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00874da0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00874da0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00874da0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00874da0 bytes 21b80b91
+ 00874da0 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58fd5436752e42dce1b71bf17883c6de"></a>

### [`008752f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/008752f4.md) → [`008752f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00875/008752f4.md) FUN_008752f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) [`00874ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874ae8.md) [`008752f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/008752f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) [`00874ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874ae8.md) [`008752f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00875/008752f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00875444",
      "incomplete_value": false,
      "site": "0087544c",
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
      "definition_site": "00875444",
      "incomplete_value": false,
      "site": "0087544c",
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
      "definition_site": "00875468",
      "incomplete_value": false,
      "site": "00875474",
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
      "definition_site": "00875468",
      "incomplete_value": false,
      "site": "00875474",
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
      "definition_site": "008755a0",
      "incomplete_value": false,
      "site": "008755a8",
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
      "definition_site": "008755a0",
      "incomplete_value": false,
      "site": "008755a8",
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
      "00875444",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00875468",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "008755a0",
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
      "00875444",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00875468",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "008755a0",
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

- 旧版 [`00875444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/008752f4.md#insn-00875444) · [`00875468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/008752f4.md#insn-00875468) · [`008755a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/008752f4.md#insn-008755a0)
- 新版 `00875444`（命令位置の公開資料なし） · `00875468`（命令位置の公開資料なし） · `008755a0`（命令位置の公開資料なし）

~~~diff
- 00875444 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00875444 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00875444 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00875444 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00875444 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00875444 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00875444 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00875444 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00875444 bytes 21280c91
+ 00875444 bytes 21900e91
- 00875468 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00875468 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00875468 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00875468 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00875468 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00875468 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00875468 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00875468 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00875468 bytes 21642491
+ 00875468 bytes 21142291
- 008755a0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 008755a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008755a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008755a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008755a0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 008755a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008755a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008755a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008755a0 bytes 21b80b91
+ 008755a0 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f600eff365b3cc2b64b3aaf53bc64c7"></a>

### [`00875c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875c24.md) → [`00875c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00875/00875c24.md) FUN_00875c24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00875adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875adc.md) [`00875c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875c24.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00875adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00875/00875adc.md) [`00875c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00875/00875c24.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.83% / 新版 98.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00875da0",
      "incomplete_value": false,
      "site": "00875da8",
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
      "definition_site": "00875da0",
      "incomplete_value": false,
      "site": "00875da8",
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
      "definition_site": "00875e68",
      "incomplete_value": false,
      "site": "00875e70",
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
      "definition_site": "00875e68",
      "incomplete_value": false,
      "site": "00875e70",
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
      "definition_site": "00875e84",
      "incomplete_value": false,
      "site": "00875e90",
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
      "definition_site": "00875e84",
      "incomplete_value": false,
      "site": "00875e90",
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
      "00875da0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00875e68",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00875e84",
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
      "00875da0",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00875e68",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00875e84",
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

- 旧版 [`00875da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875c24.md#insn-00875da0) · [`00875e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875c24.md#insn-00875e68) · [`00875e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875c24.md#insn-00875e84)
- 新版 `00875da0`（命令位置の公開資料なし） · `00875e68`（命令位置の公開資料なし） · `00875e84`（命令位置の公開資料なし）

~~~diff
- 00875da0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00875da0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00875da0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00875da0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00875da0 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00875da0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00875da0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00875da0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00875da0 bytes 21280c91
+ 00875da0 bytes 21900e91
- 00875e68 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00875e68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00875e68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00875e68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00875e68 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00875e68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00875e68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00875e68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00875e68 bytes 21b80b91
+ 00875e68 bytes 21e40d91
- 00875e84 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00875e84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00875e84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00875e84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00875e84 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00875e84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00875e84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00875e84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00875e84 bytes 21642491
+ 00875e84 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d4c5097cd69ea0d6a8022e3a2111f85"></a>

### [`00876698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00876/00876698.md) → [`00876698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00876/00876698.md) FUN_00876698

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00875c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875c24.md) [`00876698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00876/00876698.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00875c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00875/00875c24.md) [`00876698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00876/00876698.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.71% / 新版 98.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008767fc",
      "incomplete_value": false,
      "site": "00876804",
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
      "definition_site": "008767fc",
      "incomplete_value": false,
      "site": "00876804",
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
      "definition_site": "00876820",
      "incomplete_value": false,
      "site": "0087682c",
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
      "definition_site": "00876820",
      "incomplete_value": false,
      "site": "0087682c",
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
      "definition_site": "0087695c",
      "incomplete_value": false,
      "site": "00876964",
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
      "definition_site": "0087695c",
      "incomplete_value": false,
      "site": "00876964",
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
      "008767fc",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00876820",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0087695c",
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
      "008767fc",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00876820",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0087695c",
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

- 旧版 [`008767fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00876/00876698.md#insn-008767fc) · [`00876820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00876/00876698.md#insn-00876820) · [`0087695c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00876/00876698.md#insn-0087695c)
- 新版 `008767fc`（命令位置の公開資料なし） · `00876820`（命令位置の公開資料なし） · `0087695c`（命令位置の公開資料なし）

~~~diff
- 008767fc ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008767fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008767fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008767fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008767fc ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 008767fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008767fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008767fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008767fc bytes 21280c91
+ 008767fc bytes 21900e91
- 00876820 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00876820 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00876820 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00876820 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00876820 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00876820 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00876820 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00876820 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00876820 bytes 21642491
+ 00876820 bytes 21142291
- 0087695c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0087695c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087695c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087695c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087695c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0087695c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087695c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087695c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087695c bytes 21b80b91
+ 0087695c bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d102df2733478a6c49383daa4c20ef4b"></a>

### [`00877014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877014.md) → [`00877014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877014.md) FUN_00877014

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00876698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00876/00876698.md) [`00877014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877014.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00876698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00876/00876698.md) [`00877014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877014.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087716c",
      "incomplete_value": false,
      "site": "00877174",
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
      "definition_site": "0087716c",
      "incomplete_value": false,
      "site": "00877174",
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
      "definition_site": "00877190",
      "incomplete_value": false,
      "site": "0087719c",
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
      "definition_site": "00877190",
      "incomplete_value": false,
      "site": "0087719c",
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
      "definition_site": "008772c8",
      "incomplete_value": false,
      "site": "008772d0",
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
      "definition_site": "008772c8",
      "incomplete_value": false,
      "site": "008772d0",
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
      "0087716c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00877190",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "008772c8",
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
      "0087716c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00877190",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "008772c8",
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

- 旧版 [`0087716c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877014.md#insn-0087716c) · [`00877190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877014.md#insn-00877190) · [`008772c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877014.md#insn-008772c8)
- 新版 `0087716c`（命令位置の公開資料なし） · `00877190`（命令位置の公開資料なし） · `008772c8`（命令位置の公開資料なし）

~~~diff
- 0087716c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0087716c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087716c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087716c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087716c ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0087716c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087716c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087716c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087716c bytes 21280c91
+ 0087716c bytes 21900e91
- 00877190 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00877190 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00877190 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00877190 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00877190 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00877190 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00877190 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00877190 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00877190 bytes 21642491
+ 00877190 bytes 21142291
- 008772c8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 008772c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008772c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008772c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008772c8 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 008772c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008772c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008772c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008772c8 bytes 21b80b91
+ 008772c8 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a362fa844bd0a3f8bd31567bfed6a0e"></a>

### [`0087796c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/0087796c.md) → [`0087796c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/0087796c.md) FUN_0087796c

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
      "definition_site": "00877980",
      "incomplete_value": false,
      "site": "00877984",
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
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877980",
      "incomplete_value": false,
      "site": "00877984",
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
            "const:188:8"
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
      "00877984",
      "DATA",
      [
        "storage",
        "00c05188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00877984",
      "DATA",
      [
        "storage",
        "00c051d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/0087796c.md#insn-00877980)
- 新版 `00877980`（命令位置の公開資料なし）

~~~diff
- 00877980 ["COPY", "tmp:0:8", ["const:188:8"]]
- 00877980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00877980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00877980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00877980 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 00877980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00877980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00877980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00877980 bytes 08210691
+ 00877980 bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca2f26c0492c5c2509e183526497bd4"></a>

### [`00877990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877990.md) → [`00877990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877990.md) FUN_00877990

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
      "definition_site": "00877994",
      "incomplete_value": false,
      "site": "00877998",
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
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877994",
      "incomplete_value": false,
      "site": "00877998",
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
            "const:188:8"
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
      "00877998",
      "DATA",
      [
        "storage",
        "00c05188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00877998",
      "DATA",
      [
        "storage",
        "00c051d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877990.md#insn-00877994)
- 新版 `00877994`（命令位置の公開資料なし）

~~~diff
- 00877994 ["COPY", "tmp:0:8", ["const:188:8"]]
- 00877994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00877994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00877994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00877994 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 00877994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00877994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00877994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00877994 bytes 08210691
+ 00877994 bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

