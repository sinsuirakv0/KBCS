# v15.7.4 → v16.0.0 · 最優先の変更候補 (50)

[一覧の目次](README.md)

### [`0085bee8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085b/0085bee8.md) → [`0088ee80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088e/0088ee80.md) FUN_0088ee80

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00859898`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 5件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`0088c830`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 5件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088eea4",
      "incomplete_value": true,
      "site": "0088eeb0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085bf18",
      "value": [
        "live",
        "register:4048:8"
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0088ef70",
      "incomplete_value": true,
      "site": "0088ef70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_MULT",
            "8",
            [
              [
                "live",
                "register:40a0:8"
              ],
              [
                "live",
                "register:4040:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085bfd8",
      "incomplete_value": true,
      "site": "0085bfd8",
      "value": [
        "live",
        "register:4050:8"
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0088ef78",
      "incomplete_value": true,
      "site": "0088ef78",
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
              "INT_MULT"
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
      "definition_site": "0085bfe0",
      "incomplete_value": true,
      "site": "0085bfe0",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  }
]
~~~


~~~diff
- 0085bf08 ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
+ 0088eea0 ["CBRANCH", null, ["local:b2:8", "register:102:1"]]
- 0085bf28 ["BRANCH", null, ["local:b13:8"]]
+ 0088eec0 ["BRANCH", null, ["local:b11:8"]]
- 0085bf54 ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
+ 0088eeec ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
~~~


### [`0085c0e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c0e8.md) → [`0088f080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f080.md) FUN_0088f080

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00859898`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 4件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00613984`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00613/00613984.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0088c830`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 4件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0063947c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/0063947c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0088f088",
      "incomplete_value": true,
      "site": "0088f088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:50:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c0f0",
      "incomplete_value": true,
      "site": "0085c0f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0088f08c",
      "incomplete_value": true,
      "site": "0088f08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:50:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c0f4",
      "incomplete_value": true,
      "site": "0085c0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0088f08c",
      "incomplete_value": true,
      "site": "0088f08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:30:8"
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
      "definition_site": "0085c0f4",
      "incomplete_value": true,
      "site": "0085c0f4",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:30:8"
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
  }
]
~~~


~~~diff
- 0085c11c ["INT_ADD", "register:40f0:8", ["const:85c11c:8", "const:4:8"]]
+ 0088f0b4 ["INT_ADD", "register:40f0:8", ["const:88f0b4:8", "const:4:8"]]
- 0085c124 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0088f0bc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0085c130 ["INT_ADD", "register:40f0:8", ["const:85c130:8", "const:4:8"]]
+ 0088f0c8 ["INT_ADD", "register:40f0:8", ["const:88f0c8:8", "const:4:8"]]
~~~


### [`0085c1c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c1c0.md) → [`0088f158`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f158.md) FUN_0088f158

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00859898`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 1件 [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`0088c830`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 1件 [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0088f224",
      "incomplete_value": true,
      "site": "0088f23c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 0
  }
]
~~~


~~~diff
- 0085c1dc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 0088f174 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0085c204 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 0088f19c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0085c238 ["INT_ADD", "register:40f0:8", ["const:85c238:8", "const:4:8"]]
+ 0088f1d0 ["INT_ADD", "register:40f0:8", ["const:88f1d0:8", "const:4:8"]]
~~~


### [`0085c31c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c31c.md) → [`0088f2b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f2b4.md) FUN_0088f2b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00859898`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 2件 [`0044a7d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a7d4.md) [`00541408`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541408.md)
- 新版 呼出元 1件 [`0088c830`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 2件 [`0046d66c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d66c.md) [`005642a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

~~~diff
- 0085c32c ["INT_ADD", "register:40f0:8", ["const:85c32c:8", "const:4:8"]]
+ 0088f2c4 ["INT_ADD", "register:40f0:8", ["const:88f2c4:8", "const:4:8"]]
- 0085c338 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 0088f2d0 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 0085c344 ["INT_ADD", "register:40f0:8", ["const:85c344:8", "const:4:8"]]
+ 0088f2dc ["INT_ADD", "register:40f0:8", ["const:88f2dc:8", "const:4:8"]]
~~~


### [`0085c3a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c3a8.md) → [`0088f340`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f340.md) FUN_0088f340

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00859898`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 3件 [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 1件 [`0088c830`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 3件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0088f3b0",
      "incomplete_value": true,
      "site": "0088f3b0",
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
      "definition_site": "0085c418",
      "incomplete_value": true,
      "site": "0085c418",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
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
      "definition_site": "0088f37c",
      "incomplete_value": true,
      "site": "0088f384",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c3e4",
      "incomplete_value": true,
      "site": "0085c3ec",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


~~~diff
- 0085c3ec ["INT_ADD", "register:40f0:8", ["const:85c3ec:8", "const:4:8"]]
+ 0088f384 ["INT_ADD", "register:40f0:8", ["const:88f384:8", "const:4:8"]]
- 0085c3fc ["INT_ADD", "register:40f0:8", ["const:85c3fc:8", "const:4:8"]]
+ 0088f394 ["INT_ADD", "register:40f0:8", ["const:88f394:8", "const:4:8"]]
- 0085c408 ["INT_ADD", "register:40f0:8", ["const:85c408:8", "const:4:8"]]
+ 0088f3a0 ["INT_ADD", "register:40f0:8", ["const:88f3a0:8", "const:4:8"]]
~~~


### [`0085c46c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c46c.md) → [`0088f404`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f404.md) FUN_0088f404

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088f424",
      "incomplete_value": false,
      "site": "0088f428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c48c",
      "incomplete_value": false,
      "site": "0085c490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c038b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c81688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085c480 ["INT_ADD", "register:40f0:8", ["const:85c480:8", "const:4:8"]]
+ 0088f418 ["INT_ADD", "register:40f0:8", ["const:88f418:8", "const:4:8"]]
- 0085c488 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085c48c ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 0088f420 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088f424 ["COPY", "tmp:0:8", ["const:688:8"]]
~~~


### [`0085c4c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c4c4.md) → [`0088f45c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f45c.md) FUN_0088f45c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0051d884`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`0073ef14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ef14.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008594d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/008594d4.md) [`009877e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009877e0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0054071c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00769220`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769220.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0088c46c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c46c.md) [`009bd2c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd2c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0088f49c",
      "value": [
        "leaf",
        "ram:9bd2c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085c504",
      "value": [
        "leaf",
        "ram:9877e0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0088f494",
      "incomplete_value": true,
      "site": "0088f49c",
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
              [
                "live",
                "register:40a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0088f494",
      "incomplete_value": true,
      "site": "0088f49c",
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
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009877e0"
      ]
    ],
    [
      160,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073ef14"
      ]
    ]
  ],
  "added": [
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009bd2c0"
      ]
    ],
    [
      160,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00769220"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085c4f0 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
+ 0088f488 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 0085c504 ["INT_ADD", "register:40f0:8", ["const:85c504:8", "const:4:8"]]
- 0085c504 ["CALL", null, ["ram:9877e0:8"]]
+ 0088f49c ["INT_ADD", "register:40f0:8", ["const:88f49c:8", "const:4:8"]]
+ 0088f49c ["CALL", null, ["ram:9bd2c0:8"]]
- 0085c514 ["INT_ADD", "register:40f0:8", ["const:85c514:8", "const:4:8"]]
+ 0088f4ac ["INT_ADD", "register:40f0:8", ["const:88f4ac:8", "const:4:8"]]
~~~


### [`0085c648`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c648.md) → [`0088f5e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f5e0.md) FUN_0088f5e0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088f604",
      "incomplete_value": false,
      "site": "0088f604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c66c",
      "incomplete_value": false,
      "site": "0085c66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c03940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c81718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085c65c ["INT_ADD", "register:40f0:8", ["const:85c65c:8", "const:4:8"]]
+ 0088f5f4 ["INT_ADD", "register:40f0:8", ["const:88f5f4:8", "const:4:8"]]
- 0085c664 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085c668 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 0088f5fc ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088f600 ["COPY", "tmp:0:8", ["const:718:8"]]
~~~


### [`0085c6c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c6c8.md) → [`0088f660`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f660.md) FUN_0088f660

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088f674",
      "incomplete_value": false,
      "site": "0088f678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c6dc",
      "incomplete_value": false,
      "site": "0085c6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c039c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085c6d4 ["INT_ADD", "register:40f0:8", ["const:85c6d4:8", "const:4:8"]]
+ 0088f66c ["INT_ADD", "register:40f0:8", ["const:88f66c:8", "const:4:8"]]
- 0085c6d8 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085c6dc ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 0088f670 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088f674 ["COPY", "tmp:0:8", ["const:798:8"]]
~~~


### [`0085c704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c704.md) → [`0088f69c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f69c.md) FUN_0088f69c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0052db3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db3c.md) [`0085cc88`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc88.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ce14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005509d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d4.md) [`0088fc20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc20.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088f6d0",
      "incomplete_value": true,
      "site": "0088f6e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c738",
      "incomplete_value": true,
      "site": "0085c748",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cdd:8"
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
      "definition_site": "0088f6e4",
      "incomplete_value": true,
      "site": "0088f6e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0085c74c",
      "incomplete_value": true,
      "site": "0085c74c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088f6d8",
      "incomplete_value": true,
      "site": "0088f6e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:410:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c740",
      "incomplete_value": true,
      "site": "0085c750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e10:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "READ",
      [
        "storage",
        "00294cdd",
        null,
        "string"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00294cec",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "002b0e10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      52,
      "READ",
      [
        "storage",
        "002a45ff",
        null,
        "string"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "002a460e",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0085c728 ["INT_ADD", "register:40f0:8", ["const:85c728:8", "const:4:8"]]
+ 0088f6c0 ["INT_ADD", "register:40f0:8", ["const:88f6c0:8", "const:4:8"]]
- 0085c72c ["COPY", "register:4040:8", ["const:294000:8"]]
- 0085c730 ["COPY", "tmp:0:8", ["const:cdd:8"]]
+ 0088f6c4 ["COPY", "register:4040:8", ["const:2a4000:8"]]
+ 0088f6c8 ["COPY", "tmp:0:8", ["const:5ff:8"]]
- 0085c734 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0088f6cc ["COPY", "register:4048:8", ["const:2c2000:8"]]
~~~


### [`0085cb4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cb4c.md) → [`0088fae4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fae4.md) FUN_0088fae4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088faf8",
      "incomplete_value": false,
      "site": "0088fafc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cb60",
      "incomplete_value": false,
      "site": "0085cb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085cb5c ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085cb60 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 0088faf4 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088faf8 ["COPY", "tmp:0:8", ["const:808:8"]]
- 0085cb74 ["INT_ADD", "register:40f0:8", ["const:85cb74:8", "const:4:8"]]
+ 0088fb0c ["INT_ADD", "register:40f0:8", ["const:88fb0c:8", "const:4:8"]]
- 0085cb94 ["INT_ADD", "register:40f0:8", ["const:85cb94:8", "const:4:8"]]
+ 0088fb2c ["INT_ADD", "register:40f0:8", ["const:88fb2c:8", "const:4:8"]]
~~~


### [`0085cba8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cba8.md) → [`0088fb40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fb40.md) FUN_0088fb40

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fb58",
      "incomplete_value": false,
      "site": "0088fb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cbc0",
      "incomplete_value": false,
      "site": "0085cbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      28,
      "DATA",
      [
        "storage",
        "00c81808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085cbbc ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085cbc0 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 0088fb54 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088fb58 ["COPY", "tmp:0:8", ["const:808:8"]]
- 0085cbd4 ["INT_ADD", "register:40f0:8", ["const:85cbd4:8", "const:4:8"]]
+ 0088fb6c ["INT_ADD", "register:40f0:8", ["const:88fb6c:8", "const:4:8"]]
- 0085cbe8 ["INT_ADD", "register:40f0:8", ["const:85cbe8:8", "const:4:8"]]
+ 0088fb80 ["INT_ADD", "register:40f0:8", ["const:88fb80:8", "const:4:8"]]
~~~


### [`0085cc04`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc04.md) → [`0088fb9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fb9c.md) FUN_0088fb9c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fbc0",
      "incomplete_value": false,
      "site": "0088fbc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cc28",
      "incomplete_value": false,
      "site": "0085cc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fbc0",
      "incomplete_value": true,
      "site": "0088fbc0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cc28",
      "incomplete_value": true,
      "site": "0085cc28",
      "value": [
        "live",
        "register:4050:8"
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fbb4",
      "incomplete_value": true,
      "site": "0088fbc4",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085cc2c",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c81808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085cc18 ["INT_ADD", "register:40f0:8", ["const:85cc18:8", "const:4:8"]]
+ 0088fbb0 ["INT_ADD", "register:40f0:8", ["const:88fbb0:8", "const:4:8"]]
- 0085cc20 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 0085cc24 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 0088fbb8 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 0088fbbc ["COPY", "tmp:0:8", ["const:808:8"]]
- 0085cc30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0088fbc8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
~~~


### [`0085cc54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc54.md) → [`0088fbec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fbec.md) FUN_0088fbec

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fbf8",
      "incomplete_value": false,
      "site": "0088fbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cc60",
      "incomplete_value": false,
      "site": "0085cc60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      12,
      "DATA",
      [
        "storage",
        "00c81808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085cc58 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 0085cc5c ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 0088fbf0 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 0088fbf4 ["COPY", "tmp:0:8", ["const:808:8"]]
- 0085cc7c ["INT_ADD", "register:40f0:8", ["const:85cc7c:8", "const:4:8"]]
+ 0088fc14 ["INT_ADD", "register:40f0:8", ["const:88fc14:8", "const:4:8"]]
~~~


### [`0085ccd8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085ccd8.md) → [`0088fc70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc70.md) FUN_0088fc70

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0085c704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c704.md) · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0088f69c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f69c.md) · 呼出先 3件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

~~~diff
- 0085ccec ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0088fc84 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0085ccf8 ["INT_ADD", "register:40f0:8", ["const:85ccf8:8", "const:4:8"]]
+ 0088fc90 ["INT_ADD", "register:40f0:8", ["const:88fc90:8", "const:4:8"]]
- 0085ccfc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0088fc94 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`0085cd84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cd84.md) → [`0088fd1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd1c.md) FUN_0088fd1c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fd30",
      "incomplete_value": false,
      "site": "0088fd34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cd98",
      "incomplete_value": false,
      "site": "0085cd9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c03ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085cd90 ["INT_ADD", "register:40f0:8", ["const:85cd90:8", "const:4:8"]]
+ 0088fd28 ["INT_ADD", "register:40f0:8", ["const:88fd28:8", "const:4:8"]]
- 0085cd94 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085cd98 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0088fd2c ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088fd30 ["COPY", "tmp:0:8", ["const:898:8"]]
~~~


### [`0085cdc0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cdc0.md) → [`0088fd58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd58.md) FUN_0088fd58

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0052db3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db3c.md) [`0085d1d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d1d8.md) [`0085d228`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d228.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0048ce14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005509d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d4.md) [`00890170`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890170.md) [`008901c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008901c0.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 7件, `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fd90",
      "incomplete_value": true,
      "site": "0088fd90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:88e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cdf8",
      "incomplete_value": true,
      "site": "0085cdf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:daf:8"
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
      "definition_site": "0088fd88",
      "incomplete_value": true,
      "site": "0088fd94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0085cdf0",
      "incomplete_value": true,
      "site": "0085cdfc",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fe24",
      "incomplete_value": false,
      "site": "0088fe24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085ce8c",
      "incomplete_value": false,
      "site": "0085ce8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "002a6daf",
        null,
        "string"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002a6db6",
        null,
        "string"
      ]
    ],
    [
      204,
      "DATA",
      [
        "storage",
        "00c03b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "002b788e",
        null,
        "string"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002b7895",
        null,
        "string"
      ]
    ],
    [
      204,
      "DATA",
      [
        "storage",
        "00c81908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085cdd8 ["COPY", "register:4048:8", ["const:2a6000:8"]]
- 0085cddc ["COPY", "tmp:0:8", ["const:daf:8"]]
+ 0088fd70 ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 0088fd74 ["COPY", "tmp:0:8", ["const:88e:8"]]
- 0085ce0c ["INT_ADD", "register:40f0:8", ["const:85ce0c:8", "const:4:8"]]
+ 0088fda4 ["INT_ADD", "register:40f0:8", ["const:88fda4:8", "const:4:8"]]
- 0085ce18 ["INT_ADD", "register:40f0:8", ["const:85ce18:8", "const:4:8"]]
+ 0088fdb0 ["INT_ADD", "register:40f0:8", ["const:88fdb0:8", "const:4:8"]]
~~~


### [`0085d04c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d04c.md) → [`0088ffe4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088ffe4.md) FUN_0088ffe4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

~~~diff
- 0085d05c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 0088fff4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0085d068 ["INT_ADD", "register:40f0:8", ["const:85d068:8", "const:4:8"]]
+ 00890000 ["INT_ADD", "register:40f0:8", ["const:890000:8", "const:4:8"]]
- 0085d06c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00890004 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
~~~


### [`0085d09c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d09c.md) → [`00890034`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890034.md) FUN_00890034

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00890048",
      "incomplete_value": false,
      "site": "0089004c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d0b0",
      "incomplete_value": false,
      "site": "0085d0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c03b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085d0ac ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085d0b0 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00890044 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00890048 ["COPY", "tmp:0:8", ["const:908:8"]]
- 0085d0c4 ["INT_ADD", "register:40f0:8", ["const:85d0c4:8", "const:4:8"]]
+ 0089005c ["INT_ADD", "register:40f0:8", ["const:89005c:8", "const:4:8"]]
- 0085d0e4 ["INT_ADD", "register:40f0:8", ["const:85d0e4:8", "const:4:8"]]
+ 0089007c ["INT_ADD", "register:40f0:8", ["const:89007c:8", "const:4:8"]]
~~~


### [`0085d0f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d0f8.md) → [`00890090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890090.md) FUN_00890090

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008900a8",
      "incomplete_value": false,
      "site": "008900ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d110",
      "incomplete_value": false,
      "site": "0085d114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "DATA",
      [
        "storage",
        "00c03b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      28,
      "DATA",
      [
        "storage",
        "00c81908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085d10c ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085d110 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 008900a4 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008900a8 ["COPY", "tmp:0:8", ["const:908:8"]]
- 0085d124 ["INT_ADD", "register:40f0:8", ["const:85d124:8", "const:4:8"]]
+ 008900bc ["INT_ADD", "register:40f0:8", ["const:8900bc:8", "const:4:8"]]
- 0085d138 ["INT_ADD", "register:40f0:8", ["const:85d138:8", "const:4:8"]]
+ 008900d0 ["INT_ADD", "register:40f0:8", ["const:8900d0:8", "const:4:8"]]
~~~


### [`0085d154`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d154.md) → [`008900ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008900ec.md) FUN_008900ec

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00890110",
      "incomplete_value": false,
      "site": "00890110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d178",
      "incomplete_value": false,
      "site": "0085d178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c03b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c81908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085d168 ["INT_ADD", "register:40f0:8", ["const:85d168:8", "const:4:8"]]
+ 00890100 ["INT_ADD", "register:40f0:8", ["const:890100:8", "const:4:8"]]
- 0085d170 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 0085d174 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00890108 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 0089010c ["COPY", "tmp:0:8", ["const:908:8"]]
- 0085d190 ["INT_ADD", "register:40f0:8", ["const:85d190:8", "const:4:8"]]
+ 00890128 ["INT_ADD", "register:40f0:8", ["const:890128:8", "const:4:8"]]
~~~


### [`0085d1a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d1a4.md) → [`0089013c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/0089013c.md) FUN_0089013c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00890148",
      "incomplete_value": false,
      "site": "00890148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d1b0",
      "incomplete_value": false,
      "site": "0085d1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00c03b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      12,
      "DATA",
      [
        "storage",
        "00c81908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085d1a8 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 0085d1ac ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00890140 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00890144 ["COPY", "tmp:0:8", ["const:908:8"]]
- 0085d1b8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00890150 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0085d1cc ["INT_ADD", "register:40f0:8", ["const:85d1cc:8", "const:4:8"]]
+ 00890164 ["INT_ADD", "register:40f0:8", ["const:890164:8", "const:4:8"]]
~~~


### [`0085d1d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d1d8.md) → [`00890170`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890170.md) FUN_00890170

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0085cdc0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cdc0.md) · 呼出先 2件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0088fd58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd58.md) · 呼出先 2件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

~~~diff
- 0085d1f4 ["INT_ADD", "register:40f0:8", ["const:85d1f4:8", "const:4:8"]]
+ 0089018c ["INT_ADD", "register:40f0:8", ["const:89018c:8", "const:4:8"]]
- 0085d1f8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00890190 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0085d214 ["INT_ADD", "register:40f0:8", ["const:85d214:8", "const:4:8"]]
+ 008901ac ["INT_ADD", "register:40f0:8", ["const:8901ac:8", "const:4:8"]]
~~~


### [`0085d228`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d228.md) → [`008901c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008901c0.md) FUN_008901c0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0085cdc0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cdc0.md) · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0088fd58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd58.md) · 呼出先 3件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008901c4",
      "incomplete_value": true,
      "site": "008901c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d22c",
      "incomplete_value": true,
      "site": "0085d22c",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:ffffffffffffffe0:8"
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
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008901c4",
      "incomplete_value": true,
      "site": "008901c4",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:10:8"
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
      "definition_site": "0085d22c",
      "incomplete_value": true,
      "site": "0085d22c",
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
                "const:10:8"
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
  }
]
~~~


~~~diff
- 0085d23c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008901d4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0085d248 ["INT_ADD", "register:40f0:8", ["const:85d248:8", "const:4:8"]]
+ 008901e0 ["INT_ADD", "register:40f0:8", ["const:8901e0:8", "const:4:8"]]
- 0085d24c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008901e4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
~~~


### [`0085d2a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d2a4.md) → [`0089023c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/0089023c.md) _INIT_166

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 39件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0089026c",
      "incomplete_value": true,
      "site": "0089026c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d2d4",
      "incomplete_value": true,
      "site": "0085d2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0089026c",
      "incomplete_value": true,
      "site": "0089026c",
      "value": [
        "live",
        "register:4048:8"
      ]
    },
    "old": {
      "definition_site": "0085d2d4",
      "incomplete_value": true,
      "site": "0085d2d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:1660:8"
              ],
              [
                "leaf",
                "const:28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00890280",
      "incomplete_value": true,
      "site": "00890280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:21:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d2e8",
      "incomplete_value": true,
      "site": "0085d2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:120:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:21:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      60,
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085d2cc ["COPY", "register:4098:8", ["const:109e000:8"]]
- 0085d2d0 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00890264 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 00890268 ["COPY", "tmp:0:8", ["const:470:8"]]
- 0085d2d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0085d2dc ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00890270 ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 00890274 ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 0085d2f4 ["COPY", "register:4050:8", ["const:2a7000:8"]]
- 0085d2f8 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 0089028c ["COPY", "register:4050:8", ["const:2b7000:8"]]
+ 00890290 ["COPY", "tmp:0:8", ["const:ef9:8"]]
~~~


### [`0085d634`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d634.md) → [`008905cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md) FUN_008905cc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 2件 [`0085dbf4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085dbf4.md) [`0085edec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085edec.md) · 呼出先 3件 [`0056c55c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c55c.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb5e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5e0.md)
- 新版 呼出元 2件 [`00890b8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890b8c.md) [`00891d84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891d84.md) · 呼出先 3件 [`0058f3f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008905d4",
      "incomplete_value": true,
      "site": "008905d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d63c",
      "incomplete_value": true,
      "site": "0085d63c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:70:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008905d4",
      "incomplete_value": true,
      "site": "008905d4",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:50:8"
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
      "definition_site": "0085d63c",
      "incomplete_value": true,
      "site": "0085d63c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:50:8"
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
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008905d8",
      "incomplete_value": true,
      "site": "008905d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d640",
      "incomplete_value": true,
      "site": "0085d640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:70:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


~~~diff
- 0085d66c ["INT_ADD", "register:40f0:8", ["const:85d66c:8", "const:4:8"]]
+ 00890604 ["INT_ADD", "register:40f0:8", ["const:890604:8", "const:4:8"]]
- 0085d67c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00890614 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 0085d684 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 0089061c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
~~~


### [`0085d778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d778.md) → [`00890710`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md) FUN_00890710

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0081f58c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) · 呼出先 8件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0085dbf4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085dbf4.md) [`0085ddb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085ddb0.md) [`0085f5e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f5e8.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`008514c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 8件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00890b8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890b8c.md) [`00890d48`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890d48.md) [`00892580`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892580.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 2件, `store_destination` 64件, `store_value` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00890758",
      "incomplete_value": true,
      "site": "00890758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:fffffffffffffff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d7c0",
      "incomplete_value": true,
      "site": "0085d7c0",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:ffffffffffffffa0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:fffffffffffffff0:8"
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
      "definition_site": "00890758",
      "incomplete_value": true,
      "site": "00890758",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d7c0",
      "incomplete_value": true,
      "site": "0085d7c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:1660:8"
              ],
              [
                "leaf",
                "const:28:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00890768",
      "incomplete_value": true,
      "site": "00890768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d7d0",
      "incomplete_value": true,
      "site": "0085d7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:1b0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      84,
      "READ",
      [
        "storage",
        "002dff66",
        null,
        "string"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "002dff72",
        null,
        "string"
      ]
    ],
    [
      144,
      "READ",
      [
        "storage",
        "002dff7e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      84,
      "READ",
      [
        "storage",
        "002f31bf",
        null,
        "string"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "002f31cb",
        null,
        "string"
      ]
    ],
    [
      144,
      "READ",
      [
        "storage",
        "002f31d7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085d7c4 ["COPY", "register:4040:8", ["const:2df000:8"]]
- 0085d7c8 ["COPY", "tmp:0:8", ["const:f66:8"]]
+ 0089075c ["COPY", "register:4040:8", ["const:2f3000:8"]]
+ 00890760 ["COPY", "tmp:0:8", ["const:1bf:8"]]
- 0085d7d4 ["COPY", "register:4048:8", ["const:2df000:8"]]
- 0085d7d8 ["COPY", "tmp:0:8", ["const:f72:8"]]
+ 0089076c ["COPY", "register:4048:8", ["const:2f3000:8"]]
+ 00890770 ["COPY", "tmp:0:8", ["const:1cb:8"]]
- 0085d800 ["COPY", "register:4048:8", ["const:2df000:8"]]
- 0085d804 ["COPY", "tmp:0:8", ["const:f7e:8"]]
+ 00890798 ["COPY", "register:4048:8", ["const:2f3000:8"]]
+ 0089079c ["COPY", "tmp:0:8", ["const:1d7:8"]]
~~~


### [`0085dbf4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085dbf4.md) → [`00890b8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890b8c.md) FUN_00890b8c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0085d778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d778.md) · 呼出先 5件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0085d634`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d634.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00890710`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md) · 呼出先 5件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008905cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0085dc18",
      "incomplete_value": false,
      "site": "0085dc20",
      "value": [
        "leaf",
        "const:70:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0085dc44",
      "incomplete_value": true,
      "site": "0085dc4c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0085dc44",
      "incomplete_value": true,
      "site": "0085dc4c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


~~~diff
- 0085dc20 ["INT_ADD", "register:40f0:8", ["const:85dc20:8", "const:4:8"]]
+ 00890bb8 ["INT_ADD", "register:40f0:8", ["const:890bb8:8", "const:4:8"]]
- 0085dc2c ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
+ 00890bc4 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
- 0085dc40 ["BRANCH", null, ["local:b3:8"]]
+ 00890bd8 ["BRANCH", null, ["local:b5:8"]]
~~~


### [`0085ddb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085ddb0.md) → [`00890d48`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890d48.md) FUN_00890d48

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0085d778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d778.md) · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00890710`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md) · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0085de4c",
      "incomplete_value": true,
      "site": "0085de50",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:178:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


~~~diff
- 0085ddcc ["CBRANCH", null, ["local:b18:8", "tmp:3:1"]]
+ 00890d64 ["CBRANCH", null, ["local:b20:8", "tmp:3:1"]]
- 0085ddd4 ["CBRANCH", null, ["local:b19:8", "tmp:3:1"]]
+ 00890d6c ["CBRANCH", null, ["local:b21:8", "tmp:3:1"]]
- 0085dddc ["CBRANCH", null, ["local:b20:8", "tmp:3:1"]]
+ 00890d74 ["CBRANCH", null, ["local:b22:8", "tmp:3:1"]]
~~~


### [`0085df4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085df4c.md) → [`00890ee4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890ee4.md) FUN_00890ee4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 0085df80 ["INT_ADD", "register:40f0:8", ["const:85df80:8", "const:4:8"]]
+ 00890f18 ["INT_ADD", "register:40f0:8", ["const:890f18:8", "const:4:8"]]
- 0085dfc4 ["INT_ADD", "register:40f0:8", ["const:85dfc4:8", "const:4:8"]]
+ 00890f5c ["INT_ADD", "register:40f0:8", ["const:890f5c:8", "const:4:8"]]
- 0085dfd4 ["INT_ADD", "register:40f0:8", ["const:85dfd4:8", "const:4:8"]]
+ 00890f6c ["INT_ADD", "register:40f0:8", ["const:890f6c:8", "const:4:8"]]
~~~


### [`0085e130`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e130.md) → [`008910c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008910c8.md) FUN_008910c8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 2件 [`0073496c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`00824eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 14件 [`006fd890`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) [`0085e2f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e2f8.md) [`0085fc14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc14.md) [`0085fc18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc18.md) [`00ad9118`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9118.md)
- 新版 呼出元 2件 [`0075eb40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00856dec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 14件 [`00727990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`00891290`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891290.md) [`00892bac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892bac.md) [`00892bb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892bb0.md) [`00b38af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38af0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `call_target` 2件, `store_destination` 7件, `store_value` 10件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008910cc",
      "incomplete_value": true,
      "site": "008910cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e134",
      "incomplete_value": true,
      "site": "0085e134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008910cc",
      "incomplete_value": true,
      "site": "008910cc",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:60:8"
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
      "definition_site": "0085e134",
      "incomplete_value": true,
      "site": "0085e134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:60:8"
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008910d0",
      "incomplete_value": true,
      "site": "008910d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e138",
      "incomplete_value": true,
      "site": "0085e138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "0109e6a0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fd890"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "0109e670",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "011234d0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00727990"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "011234a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085e14c ["COPY", "register:4040:8", ["const:109e000:8"]]
- 0085e150 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 008910e4 ["COPY", "register:4040:8", ["const:1123000:8"]]
+ 008910e8 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0085e158 ["CBRANCH", null, ["local:b13:8", "tmp:3:1"]]
- 0085e15c ["INT_ADD", "register:40f0:8", ["const:85e15c:8", "const:4:8"]]
+ 008910f0 ["CBRANCH", null, ["local:b25:8", "tmp:3:1"]]
+ 008910f4 ["INT_ADD", "register:40f0:8", ["const:8910f4:8", "const:4:8"]]
- 0085e160 ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
- 0085e164 ["INT_ADD", "register:40f0:8", ["const:85e164:8", "const:4:8"]]
- 0085e164 ["CALL", null, ["ram:6fd890:8"]]
- 0085e168 ["INT_ADD", "register:40f0:8", ["const:85e168:8", "const:4:8"]]
+ 008910f8 ["CBRANCH", null, ["local:b10:8", "tmp:3:1"]]
+ 008910fc ["INT_ADD", "register:40f0:8", ["const:8910fc:8", "const:4:8"]]
+ 008910fc ["CALL", null, ["ram:727990:8"]]
+ 00891100 ["INT_ADD", "register:40f0:8", ["const:891100:8", "const:4:8"]]
~~~


### [`0085e328`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md) → [`008912c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md) FUN_008912c0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0085ef84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) · 呼出先 23件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00891f1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) · 呼出先 23件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0048ce14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048ce44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 4件, `call_target` 2件, `store_condition` 1件, `store_destination` 11件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008912cc",
      "incomplete_value": true,
      "site": "008912cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:190:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e334",
      "incomplete_value": true,
      "site": "0085e334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008912cc",
      "incomplete_value": true,
      "site": "008912cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:150:8"
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
      "definition_site": "0085e334",
      "incomplete_value": true,
      "site": "0085e334",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:150:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008912d0",
      "incomplete_value": true,
      "site": "008912d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:190:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e338",
      "incomplete_value": true,
      "site": "0085e338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      708,
      "READ",
      [
        "storage",
        "002afd1c",
        null,
        "string"
      ]
    ],
    [
      836,
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ],
    [
      924,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00887594"
      ]
    ]
  ],
  "added": [
    [
      708,
      "READ",
      [
        "storage",
        "002c12ba",
        null,
        "string"
      ]
    ],
    [
      836,
      "DATA",
      [
        "storage",
        "00c81c28",
        null,
        "undefined *"
      ]
    ],
    [
      924,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008ba824"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085e364 ["INT_ADD", "register:40f0:8", ["const:85e364:8", "const:4:8"]]
+ 008912fc ["INT_ADD", "register:40f0:8", ["const:8912fc:8", "const:4:8"]]
- 0085e368 ["CBRANCH", null, ["local:b25:8", "tmp:3:1"]]
+ 00891300 ["CBRANCH", null, ["local:b16:8", "tmp:3:1"]]
- 0085e374 ["CBRANCH", null, ["local:b26:8", "register:101:1"]]
+ 0089130c ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
~~~


### [`0085eb90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085eb90.md) → [`00891b28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md) FUN_00891b28

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 4件 [`0085ef84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) [`0085f460`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f460.md) [`00860170`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860170.md) [`008602c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008602c0.md) · 呼出先 9件 [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0085fcb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fcb4.md) [`0085fcb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fcb8.md) [`008865b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/008865b0.md)
- 新版 呼出元 4件 [`00891f1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) [`008923f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008923f8.md) [`00893108`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893108.md) [`00893258`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893258.md) · 呼出先 9件 [`0048ce14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00892c4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c4c.md) [`00892c50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c50.md) [`008b9814`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9814.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00891b84",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "old": {
      "definition_site": "0085ebdc",
      "incomplete_value": true,
      "site": "0085ebec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb8:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00891b88",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "0085ebe0",
      "incomplete_value": true,
      "site": "0085ebf0",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00891b8c",
      "value": [
        "live",
        "register:5020:16"
      ]
    },
    "old": {
      "definition_site": "0085ebe4",
      "incomplete_value": true,
      "site": "0085ebf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c60:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      76,
      "READ",
      [
        "storage",
        "00295fb8",
        null,
        "string"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "00295fc8",
        null,
        "string"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "002b0c60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      76,
      "READ",
      [
        "storage",
        "002a5a0e",
        null,
        "string"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "002a5a1e",
        null,
        "string"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "002c2260",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0085ebb4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00891b4c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 0085ebbc ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00891b54 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 0085ebc4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00891b5c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
~~~


### [`0085edec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085edec.md) → [`00891d84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891d84.md) FUN_00891d84

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0085e328`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md) · 呼出先 5件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0085d634`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d634.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`008912c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md) · 呼出先 5件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008905cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00891db4",
      "incomplete_value": true,
      "site": "00891db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085ee1c",
      "incomplete_value": true,
      "site": "0085ee1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:60:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00891db4",
      "incomplete_value": true,
      "site": "00891db4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085ee1c",
      "incomplete_value": true,
      "site": "0085ee1c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:1660:8"
              ],
              [
                "leaf",
                "const:28:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00891dd4",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "0085ee34",
      "incomplete_value": true,
      "site": "0085ee3c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
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
  }
]
~~~


~~~diff
- 0085ee20 ["INT_ADD", "register:40f0:8", ["const:85ee20:8", "const:4:8"]]
+ 00891db8 ["INT_ADD", "register:40f0:8", ["const:891db8:8", "const:4:8"]]
- 0085ee2c ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
+ 00891dc4 ["CBRANCH", null, ["local:b6:8", "tmp:3:1"]]
- 0085ee40 ["BRANCH", null, ["local:b3:8"]]
+ 00891dd8 ["BRANCH", null, ["local:b7:8"]]
~~~


### [`0085ef84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) → [`00891f1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) FUN_00891f1c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 3件 [`0085fed0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fed0.md) [`00860de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860de0.md) [`0086a350`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) · 呼出先 16件 [`00436e9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459f48`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f48.md) [`00459f50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f50.md) [`0056c55c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c55c.md)
- 新版 呼出元 3件 [`00892e68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e68.md) [`00893d78`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) [`0089d484`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 16件 [`00459d34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cde0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde0.md) [`0047cde8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde8.md) [`0058f3f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_value

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 5件, `return_value_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0089224c",
      "incomplete_value": false,
      "site": "00892254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f2b4",
      "incomplete_value": false,
      "site": "0085f2bc",
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
            "const:50:8"
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
      "definition_site": "00892260",
      "incomplete_value": false,
      "site": "00892260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f2c8",
      "incomplete_value": true,
      "site": "0085f2c8",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00892250",
      "incomplete_value": true,
      "site": "0089226c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085f2d4",
      "value": [
        "live",
        "register:4048:8"
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      792,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      804,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      824,
      "DATA",
      [
        "storage",
        "00c04050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      792,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      804,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      824,
      "DATA",
      [
        "storage",
        "00c81e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085eff0 ["INT_ADD", "register:40f0:8", ["const:85eff0:8", "const:4:8"]]
+ 00891f88 ["INT_ADD", "register:40f0:8", ["const:891f88:8", "const:4:8"]]
- 0085f06c ["INT_ADD", "register:40f0:8", ["const:85f06c:8", "const:4:8"]]
+ 00892004 ["INT_ADD", "register:40f0:8", ["const:892004:8", "const:4:8"]]
- 0085f0a8 ["INT_ADD", "register:40f0:8", ["const:85f0a8:8", "const:4:8"]]
+ 00892040 ["INT_ADD", "register:40f0:8", ["const:892040:8", "const:4:8"]]
~~~


### [`0085f460`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f460.md) → [`008923f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008923f8.md) FUN_008923f8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00824eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 7件 [`00469fac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0085eb90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085eb90.md) [`00885f80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md) [`0088823c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/0088823c.md)
- 新版 呼出元 1件 [`00856dec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 7件 [`0048ce44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00891b28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008bb4cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb4cc.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00892400",
      "incomplete_value": true,
      "site": "00892400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f468",
      "incomplete_value": true,
      "site": "0085f468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00892400",
      "incomplete_value": true,
      "site": "00892400",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:20:8"
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
      "definition_site": "0085f468",
      "incomplete_value": true,
      "site": "0085f468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:20:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00892404",
      "incomplete_value": true,
      "site": "00892404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f46c",
      "incomplete_value": true,
      "site": "0085f46c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


~~~diff
- 0085f4b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00892450 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0085f4d8 ["INT_ADD", "register:40f0:8", ["const:85f4d8:8", "const:4:8"]]
+ 00892470 ["INT_ADD", "register:40f0:8", ["const:892470:8", "const:4:8"]]
- 0085f4e0 ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
+ 00892478 ["CBRANCH", null, ["local:b17:8", "tmp:1:1"]]
~~~


### [`0085f5e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f5e8.md) → [`00892580`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892580.md) FUN_00892580

根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0085d778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d778.md) [`0085e328`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00890710`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md) [`008912c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892590",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085f5f8",
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
      "definition_site": "0089258c",
      "incomplete_value": false,
      "site": "00892590",
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
      "definition_site": "0085f5f4",
      "incomplete_value": false,
      "site": "0085f5f8",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      16,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      12,
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      16,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085f5f0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 0085f5f4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00892588 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0089258c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0085f5f8 ["INT_ADD", "register:40f0:8", ["const:85f5f8:8", "const:4:8"]]
- 0085f5f8 ["CALL", null, ["ram:418c38:8"]]
+ 00892590 ["INT_ADD", "register:40f0:8", ["const:892590:8", "const:4:8"]]
+ 00892590 ["CALL", null, ["ram:43b738:8"]]
~~~


### [`0085f600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f600.md) → [`00892598`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892598.md) FUN_00892598

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008925ac",
      "incomplete_value": false,
      "site": "008925b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f614",
      "incomplete_value": false,
      "site": "0085f618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c03bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085f60c ["INT_ADD", "register:40f0:8", ["const:85f60c:8", "const:4:8"]]
+ 008925a4 ["INT_ADD", "register:40f0:8", ["const:8925a4:8", "const:4:8"]]
- 0085f610 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085f614 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 008925a8 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008925ac ["COPY", "tmp:0:8", ["const:998:8"]]
~~~


### [`0085f624`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f624.md) → [`008925bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008925bc.md) FUN_008925bc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008925c0",
      "incomplete_value": false,
      "site": "008925c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f628",
      "incomplete_value": false,
      "site": "0085f62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c03bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c81998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085f624 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085f628 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 008925bc ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008925c0 ["COPY", "tmp:0:8", ["const:998:8"]]
~~~


### [`0085f63c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f63c.md) → [`008925d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008925d4.md) FUN_008925d4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0085f780`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f780.md) [`0085f784`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f784.md) [`00ada7b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00892718`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892718.md) [`0089271c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/0089271c.md) [`00b3a190`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a190.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00892600",
      "incomplete_value": false,
      "site": "00892608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085f670",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00892604",
      "incomplete_value": true,
      "site": "0089260c",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085f674",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00892650",
      "incomplete_value": true,
      "site": "00892650",
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
      "definition_site": "0085f6b8",
      "incomplete_value": true,
      "site": "0085f6b8",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "DATA",
      [
        "storage",
        "00c03c40",
        null,
        "undefined *"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c03c60",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c03c68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      52,
      "DATA",
      [
        "storage",
        "00c81a18",
        null,
        "undefined *"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c81a38",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c81a40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085f660 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 0085f664 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085f668 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 008925f8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 008925fc ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00892600 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 0085f67c ["INT_ADD", "register:40f0:8", ["const:85f67c:8", "const:4:8"]]
+ 00892614 ["INT_ADD", "register:40f0:8", ["const:892614:8", "const:4:8"]]
- 0085f688 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 00892620 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
~~~


### [`0085f74c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f74c.md) → [`008926e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926e4.md) FUN_008926e4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008926f8",
      "incomplete_value": false,
      "site": "008926fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f760",
      "incomplete_value": false,
      "site": "0085f764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c03c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81a18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085f758 ["INT_ADD", "register:40f0:8", ["const:85f758:8", "const:4:8"]]
+ 008926f0 ["INT_ADD", "register:40f0:8", ["const:8926f0:8", "const:4:8"]]
- 0085f75c ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085f760 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 008926f4 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008926f8 ["COPY", "tmp:0:8", ["const:a18:8"]]
~~~


### [`0085f770`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f770.md) → [`00892708`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892708.md) FUN_00892708

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0089270c",
      "incomplete_value": false,
      "site": "00892710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f774",
      "incomplete_value": false,
      "site": "0085f778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c03c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c81a18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085f770 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085f774 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00892708 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0089270c ["COPY", "tmp:0:8", ["const:a18:8"]]
~~~


### [`0085f788`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f788.md) → [`00892720`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892720.md) FUN_00892720

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006f23b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`00447eb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0071c420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 6件, `call_target` 1件, `store_destination` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00892728",
      "incomplete_value": true,
      "site": "00892728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f790",
      "incomplete_value": true,
      "site": "0085f790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:100:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0089272c",
      "incomplete_value": true,
      "site": "0089272c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f794",
      "incomplete_value": true,
      "site": "0085f794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:100:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0089272c",
      "incomplete_value": true,
      "site": "0089272c",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:f0:8"
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
      "definition_site": "0085f794",
      "incomplete_value": true,
      "site": "0085f794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:f0:8"
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
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f23b4"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00293b96",
        null,
        "string"
      ]
    ],
    [
      328,
      "DATA",
      [
        "storage",
        "00c03cb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "002a338f",
        null,
        "string"
      ]
    ],
    [
      328,
      "DATA",
      [
        "storage",
        "00c81a88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085f7b0 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
+ 00892748 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
- 0085f7c0 ["INT_ADD", "register:40f0:8", ["const:85f7c0:8", "const:4:8"]]
- 0085f7c0 ["CALL", null, ["ram:6f23b4:8"]]
- 0085f7c4 ["INT_ADD", "register:40f0:8", ["const:85f7c4:8", "const:4:8"]]
+ 00892758 ["INT_ADD", "register:40f0:8", ["const:892758:8", "const:4:8"]]
+ 00892758 ["CALL", null, ["ram:71c420:8"]]
+ 0089275c ["INT_ADD", "register:40f0:8", ["const:89275c:8", "const:4:8"]]
- 0085f7c8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:21c8:8"]]
+ 00892760 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:22b0:8"]]
~~~


### [`0085fb30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fb30.md) → [`00892ac8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892ac8.md) FUN_00892ac8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892adc",
      "incomplete_value": false,
      "site": "00892ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fb44",
      "incomplete_value": false,
      "site": "0085fb48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c03cb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81a88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fb3c ["INT_ADD", "register:40f0:8", ["const:85fb3c:8", "const:4:8"]]
+ 00892ad4 ["INT_ADD", "register:40f0:8", ["const:892ad4:8", "const:4:8"]]
- 0085fb40 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085fb44 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 00892ad8 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00892adc ["COPY", "tmp:0:8", ["const:a88:8"]]
~~~


### [`0085fb54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fb54.md) → [`00892aec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892aec.md) FUN_00892aec

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892af0",
      "incomplete_value": false,
      "site": "00892af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fb58",
      "incomplete_value": false,
      "site": "0085fb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c03cb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c81a88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fb54 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085fb58 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 00892aec ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00892af0 ["COPY", "tmp:0:8", ["const:a88:8"]]
~~~


### [`0085fb6c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fb6c.md) → [`00892b04`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b04.md) FUN_00892b04

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892b28",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085fb90",
      "value": [
        "leaf",
        "ram:457e1c:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fb90 ["INT_ADD", "register:40f0:8", ["const:85fb90:8", "const:4:8"]]
- 0085fb90 ["CALL", null, ["ram:457e1c:8"]]
+ 00892b28 ["INT_ADD", "register:40f0:8", ["const:892b28:8", "const:4:8"]]
+ 00892b28 ["CALL", null, ["ram:47acb4:8"]]
- 0085fb9c ["INT_ADD", "register:40f0:8", ["const:85fb9c:8", "const:4:8"]]
+ 00892b34 ["INT_ADD", "register:40f0:8", ["const:892b34:8", "const:4:8"]]
~~~


### [`0085fbe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fbe0.md) → [`00892b78`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b78.md) FUN_00892b78

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892b8c",
      "incomplete_value": false,
      "site": "00892b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fbf4",
      "incomplete_value": false,
      "site": "0085fbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c03d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81b28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fbec ["INT_ADD", "register:40f0:8", ["const:85fbec:8", "const:4:8"]]
+ 00892b84 ["INT_ADD", "register:40f0:8", ["const:892b84:8", "const:4:8"]]
- 0085fbf0 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085fbf4 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00892b88 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00892b8c ["COPY", "tmp:0:8", ["const:b28:8"]]
~~~


### [`0085fc04`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc04.md) → [`00892b9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b9c.md) FUN_00892b9c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892ba0",
      "incomplete_value": false,
      "site": "00892ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fc08",
      "incomplete_value": false,
      "site": "0085fc0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c03d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c81b28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fc04 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085fc08 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00892b9c ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00892ba0 ["COPY", "tmp:0:8", ["const:b28:8"]]
~~~


### [`0085fc1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc1c.md) → [`00892bb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892bb4.md) FUN_00892bb4

根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00646dc4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646dc4.md) [`006fd890`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) [`00ad9480`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9480.md) [`00ada5f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0066d09c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d09c.md) [`00727990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`00b38e58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38e58.md) [`00b39fc8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39fc8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892bcc",
      "value": [
        "leaf",
        "ram:727990:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085fc34",
      "value": [
        "leaf",
        "ram:6fd890:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fd890"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0109e670",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      24,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00727990"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "011234a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fc30 ["INT_ADD", "register:40f0:8", ["const:85fc30:8", "const:4:8"]]
+ 00892bc8 ["INT_ADD", "register:40f0:8", ["const:892bc8:8", "const:4:8"]]
- 0085fc34 ["INT_ADD", "register:40f0:8", ["const:85fc34:8", "const:4:8"]]
- 0085fc34 ["CALL", null, ["ram:6fd890:8"]]
- 0085fc38 ["INT_ADD", "register:40f0:8", ["const:85fc38:8", "const:4:8"]]
+ 00892bcc ["INT_ADD", "register:40f0:8", ["const:892bcc:8", "const:4:8"]]
+ 00892bcc ["CALL", null, ["ram:727990:8"]]
+ 00892bd0 ["INT_ADD", "register:40f0:8", ["const:892bd0:8", "const:4:8"]]
- 0085fc3c ["COPY", "register:4000:8", ["const:109e000:8"]]
- 0085fc40 ["COPY", "tmp:0:8", ["const:670:8"]]
+ 00892bd4 ["COPY", "register:4000:8", ["const:1123000:8"]]
+ 00892bd8 ["COPY", "tmp:0:8", ["const:4a0:8"]]
~~~


### [`0085fc80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc80.md) → [`00892c18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c18.md) FUN_00892c18

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892c2c",
      "incomplete_value": false,
      "site": "00892c30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fc94",
      "incomplete_value": false,
      "site": "0085fc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c03dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81ba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fc8c ["INT_ADD", "register:40f0:8", ["const:85fc8c:8", "const:4:8"]]
+ 00892c24 ["INT_ADD", "register:40f0:8", ["const:892c24:8", "const:4:8"]]
- 0085fc90 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085fc94 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00892c28 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00892c2c ["COPY", "tmp:0:8", ["const:ba8:8"]]
~~~


### [`0085fca4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fca4.md) → [`00892c3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c3c.md) FUN_00892c3c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892c44",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "0085fca8",
      "incomplete_value": false,
      "site": "0085fcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c03dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c81ba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fca4 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085fca8 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00892c3c ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00892c40 ["COPY", "tmp:0:8", ["const:ba8:8"]]
~~~


### [`0085fcbc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fcbc.md) → [`00892c54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c54.md) FUN_00892c54

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892c78",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085fce0",
      "value": [
        "leaf",
        "ram:457e1c:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fce0 ["INT_ADD", "register:40f0:8", ["const:85fce0:8", "const:4:8"]]
- 0085fce0 ["CALL", null, ["ram:457e1c:8"]]
+ 00892c78 ["INT_ADD", "register:40f0:8", ["const:892c78:8", "const:4:8"]]
+ 00892c78 ["CALL", null, ["ram:47acb4:8"]]
- 0085fcec ["INT_ADD", "register:40f0:8", ["const:85fcec:8", "const:4:8"]]
+ 00892c84 ["INT_ADD", "register:40f0:8", ["const:892c84:8", "const:4:8"]]
~~~


### [`0085fd2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd2c.md) → [`00892cc4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md) FUN_00892cc4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0085e328`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md) [`0085ef84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) [`0085fed0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fed0.md) [`00860170`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860170.md) [`008602c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008602c0.md) · 呼出先 1件 [`0041fdf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 7件 [`008912c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md) [`00891f1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) [`00892e68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e68.md) [`00893108`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893108.md) [`00893258`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893258.md) · 呼出先 1件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892cd4",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085fd3c",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00892cd0",
      "incomplete_value": false,
      "site": "00892cd4",
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
      "definition_site": "0085fd38",
      "incomplete_value": false,
      "site": "0085fd3c",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      16,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      12,
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      16,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fd34 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 0085fd38 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00892ccc ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00892cd0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0085fd3c ["INT_ADD", "register:40f0:8", ["const:85fd3c:8", "const:4:8"]]
- 0085fd3c ["CALL", null, ["ram:41fdf0:8"]]
+ 00892cd4 ["INT_ADD", "register:40f0:8", ["const:892cd4:8", "const:4:8"]]
+ 00892cd4 ["CALL", null, ["ram:4428f0:8"]]
~~~


### [`0085fd40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd40.md) → [`00892cd8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cd8.md) FUN_00892cd8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892ce0",
      "incomplete_value": false,
      "site": "00892ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fd48",
      "incomplete_value": false,
      "site": "0085fd4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      12,
      "DATA",
      [
        "storage",
        "00c81c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fd44 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 0085fd48 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00892cdc ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00892ce0 ["COPY", "tmp:0:8", ["const:c28:8"]]
~~~


### [`0085fd60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd60.md) → [`00892cf8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cf8.md) FUN_00892cf8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892d00",
      "incomplete_value": false,
      "site": "00892d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fd68",
      "incomplete_value": false,
      "site": "0085fd6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "definition_site": "00892d20",
      "incomplete_value": true,
      "site": "00892d24",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fd88",
      "incomplete_value": true,
      "site": "0085fd8c",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      12,
      "DATA",
      [
        "storage",
        "00c81c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fd64 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 0085fd68 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00892cfc ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00892d00 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 0085fd70 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00892d08 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
- 0085fd8c ["INT_ADD", "register:40f0:8", ["const:85fd8c:8", "const:4:8"]]
+ 00892d24 ["INT_ADD", "register:40f0:8", ["const:892d24:8", "const:4:8"]]
~~~


### [`0085fda0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fda0.md) → [`00892d38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892d38.md) FUN_00892d38

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892d68",
      "incomplete_value": false,
      "site": "00892d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fdd0",
      "incomplete_value": false,
      "site": "0085fdd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      48,
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      48,
      "DATA",
      [
        "storage",
        "00c81c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fdb4 ["INT_ADD", "register:40f0:8", ["const:85fdb4:8", "const:4:8"]]
+ 00892d4c ["INT_ADD", "register:40f0:8", ["const:892d4c:8", "const:4:8"]]
- 0085fdc0 ["COPY", "register:4058:8", ["const:c03000:8"]]
- 0085fdc4 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00892d58 ["COPY", "register:4058:8", ["const:c81000:8"]]
+ 00892d5c ["COPY", "tmp:0:8", ["const:c28:8"]]
- 0085fdf4 ["INT_ADD", "register:40f0:8", ["const:85fdf4:8", "const:4:8"]]
+ 00892d8c ["INT_ADD", "register:40f0:8", ["const:892d8c:8", "const:4:8"]]
~~~


### [`0085fe24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fe24.md) → [`00892dbc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892dbc.md) FUN_00892dbc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892ddc",
      "incomplete_value": false,
      "site": "00892ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fe44",
      "incomplete_value": false,
      "site": "0085fe44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      32,
      "DATA",
      [
        "storage",
        "00c81c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085fe34 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 0085fe38 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00892dcc ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00892dd0 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 0085fe70 ["INT_ADD", "register:40f0:8", ["const:85fe70:8", "const:4:8"]]
+ 00892e08 ["INT_ADD", "register:40f0:8", ["const:892e08:8", "const:4:8"]]
~~~


### [`0085fed0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fed0.md) → [`00892e68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e68.md) FUN_00892e68

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0085ef84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) [`0085fd2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd2c.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00891f1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) [`00892cc4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 9件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00892e74",
      "incomplete_value": true,
      "site": "00892e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fedc",
      "incomplete_value": true,
      "site": "0085fedc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:a0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00892e74",
      "incomplete_value": true,
      "site": "00892e74",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:60:8"
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
      "definition_site": "0085fedc",
      "incomplete_value": true,
      "site": "0085fedc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:60:8"
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
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00892e78",
      "incomplete_value": true,
      "site": "00892e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fee0",
      "incomplete_value": true,
      "site": "0085fee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:a0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 0085ff04 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
+ 00892e9c ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 0085ff18 ["CBRANCH", null, ["local:b23:8", "register:101:1"]]
+ 00892eb0 ["CBRANCH", null, ["local:b28:8", "register:101:1"]]
- 0085ff3c ["BRANCH", null, ["local:b5:8"]]
+ 00892ed4 ["BRANCH", null, ["local:b6:8"]]
~~~


### [`00860118`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860118.md) → [`008930b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008930b0.md) FUN_008930b0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008930d0",
      "incomplete_value": false,
      "site": "008930d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860138",
      "incomplete_value": false,
      "site": "0086013c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c03ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c81ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0086012c ["INT_ADD", "register:40f0:8", ["const:86012c:8", "const:4:8"]]
+ 008930c4 ["INT_ADD", "register:40f0:8", ["const:8930c4:8", "const:4:8"]]
- 00860134 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 00860138 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 008930cc ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008930d0 ["COPY", "tmp:0:8", ["const:ca8:8"]]
~~~


### [`00860150`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860150.md) → [`008930e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008930e8.md) FUN_008930e8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008930ec",
      "incomplete_value": false,
      "site": "008930f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860154",
      "incomplete_value": false,
      "site": "00860158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c03ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c81ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00860150 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 00860154 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 008930e8 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008930ec ["COPY", "tmp:0:8", ["const:ca8:8"]]
~~~


### [`00860170`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860170.md) → [`00893108`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893108.md) FUN_00893108

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00469fac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0085eb90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085eb90.md) [`0085fd2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd2c.md) [`00885f80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0048ce44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00891b28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md) [`00892cc4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008931b4",
      "incomplete_value": true,
      "site": "008931b8",
      "value": [
        "FLOAT_ADD",
        "8",
        [
          [
            "live",
            "register:5000:8"
          ],
          [
            "INT_OR",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:409c000000000000:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00860220",
      "value": [
        "live",
        "register:5000:8"
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0089317c",
      "incomplete_value": true,
      "site": "00893180",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
          [
            "INT_SRIGHT",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:3:4"
              ]
            ]
          ],
          [
            "INT_SEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008601e8",
      "value": [
        "live",
        "register:102:1"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0089319c",
      "incomplete_value": true,
      "site": "008931a0",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
          [
            "INT_SRIGHT",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:3:4"
              ]
            ]
          ],
          [
            "INT_SEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00860208",
      "value": [
        "live",
        "register:102:1"
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


~~~diff
- 00860190 ["INT_ADD", "register:40f0:8", ["const:860190:8", "const:4:8"]]
+ 00893128 ["INT_ADD", "register:40f0:8", ["const:893128:8", "const:4:8"]]
- 00860194 ["CBRANCH", null, ["local:b14:8", "tmp:3:1"]]
+ 0089312c ["CBRANCH", null, ["local:b9:8", "tmp:3:1"]]
- 0086019c ["INT_ADD", "register:40f0:8", ["const:86019c:8", "const:4:8"]]
+ 00893134 ["INT_ADD", "register:40f0:8", ["const:893134:8", "const:4:8"]]
~~~


### [`00860268`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860268.md) → [`00893200`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893200.md) FUN_00893200

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00893220",
      "incomplete_value": true,
      "site": "00893224",
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
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086028c",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c03f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c81d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0086027c ["INT_ADD", "register:40f0:8", ["const:86027c:8", "const:4:8"]]
+ 00893214 ["INT_ADD", "register:40f0:8", ["const:893214:8", "const:4:8"]]
- 00860284 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 00860288 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0089321c ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00893220 ["COPY", "tmp:0:8", ["const:d28:8"]]
~~~


### [`008602a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008602a0.md) → [`00893238`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893238.md) FUN_00893238

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0089323c",
      "incomplete_value": false,
      "site": "00893240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008602a4",
      "incomplete_value": false,
      "site": "008602a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "definition_site": "00893244",
      "incomplete_value": true,
      "site": "00893248",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008602b0",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c03f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c81d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008602a0 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 008602a4 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00893238 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0089323c ["COPY", "tmp:0:8", ["const:d28:8"]]
~~~


### [`008602c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008602c0.md) → [`00893258`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893258.md) FUN_00893258

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469fac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0085eb90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085eb90.md) [`0085fd2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd2c.md) [`00885f80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048ce44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00891b28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md) [`00892cc4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0089325c",
      "incomplete_value": true,
      "site": "0089325c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008602c4",
      "incomplete_value": true,
      "site": "008602c4",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:ffffffffffffffe0:8"
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
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0089325c",
      "incomplete_value": true,
      "site": "0089325c",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:10:8"
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
      "definition_site": "008602c4",
      "incomplete_value": true,
      "site": "008602c4",
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
                "const:10:8"
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
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008932e0",
      "incomplete_value": true,
      "site": "008932e0",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_LESSEQUAL"
            ]
          ],
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
      "definition_site": "00860348",
      "incomplete_value": true,
      "site": "00860348",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_LESSEQUAL"
            ]
          ],
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
    "ordinal": 3,
    "slot": 0
  }
]
~~~


~~~diff
- 008602d8 ["INT_ADD", "register:40f0:8", ["const:8602d8:8", "const:4:8"]]
+ 00893270 ["INT_ADD", "register:40f0:8", ["const:893270:8", "const:4:8"]]
- 008602e4 ["INT_ADD", "register:40f0:8", ["const:8602e4:8", "const:4:8"]]
+ 0089327c ["INT_ADD", "register:40f0:8", ["const:89327c:8", "const:4:8"]]
- 008602e8 ["COPY", "register:4040:8", ["const:2e18:8"]]
+ 00893280 ["COPY", "register:4040:8", ["const:2f08:8"]]
~~~


### [`008603b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008603b4.md) → [`0089334c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089334c.md) FUN_0089334c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0089336c",
      "incomplete_value": false,
      "site": "00893370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008603d4",
      "incomplete_value": false,
      "site": "008603d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c03fd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c81da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008603c8 ["INT_ADD", "register:40f0:8", ["const:8603c8:8", "const:4:8"]]
+ 00893360 ["INT_ADD", "register:40f0:8", ["const:893360:8", "const:4:8"]]
- 008603d0 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 008603d4 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 00893368 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0089336c ["COPY", "tmp:0:8", ["const:da8:8"]]
~~~


### [`008603ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008603ec.md) → [`00893384`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893384.md) FUN_00893384

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00893388",
      "incomplete_value": false,
      "site": "0089338c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008603f0",
      "incomplete_value": false,
      "site": "008603f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c03fd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c81da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008603ec ["COPY", "register:4040:8", ["const:c03000:8"]]
- 008603f0 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 00893384 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00893388 ["COPY", "tmp:0:8", ["const:da8:8"]]
~~~


### [`0086040c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/0086040c.md) → [`008933a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008933a4.md) FUN_008933a4

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0085fd2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd2c.md) [`00885f80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md) [`0088823c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/0088823c.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00892cc4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008bb4cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb4cc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008933c8",
      "incomplete_value": true,
      "site": "008933cc",
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
            "const:2f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860430",
      "incomplete_value": true,
      "site": "00860434",
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
            "const:2e18:8"
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
      "definition_site": "008933dc",
      "incomplete_value": true,
      "site": "008933e0",
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
            "const:2f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860444",
      "incomplete_value": true,
      "site": "00860448",
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
            "const:2e18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


~~~diff
- 00860428 ["INT_ADD", "register:40f0:8", ["const:860428:8", "const:4:8"]]
+ 008933c0 ["INT_ADD", "register:40f0:8", ["const:8933c0:8", "const:4:8"]]
- 0086042c ["COPY", "register:4040:8", ["const:2e18:8"]]
+ 008933c4 ["COPY", "register:4040:8", ["const:2f08:8"]]
- 00860434 ["INT_ADD", "register:40f0:8", ["const:860434:8", "const:4:8"]]
+ 008933cc ["INT_ADD", "register:40f0:8", ["const:8933cc:8", "const:4:8"]]
~~~


### [`008604b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008604b0.md) → [`00893448`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893448.md) FUN_00893448

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0089345c",
      "incomplete_value": false,
      "site": "00893460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008604c4",
      "incomplete_value": false,
      "site": "008604c8",
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
            "const:50:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c04050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008604bc ["INT_ADD", "register:40f0:8", ["const:8604bc:8", "const:4:8"]]
+ 00893454 ["INT_ADD", "register:40f0:8", ["const:893454:8", "const:4:8"]]
- 008604c0 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 008604c4 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 00893458 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0089345c ["COPY", "tmp:0:8", ["const:e28:8"]]
~~~


### [`008604d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008604d4.md) → [`0089346c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089346c.md) FUN_0089346c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00893470",
      "incomplete_value": false,
      "site": "00893474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008604d8",
      "incomplete_value": false,
      "site": "008604dc",
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
            "const:50:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c04050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c81e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008604d4 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 008604d8 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 0089346c ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00893470 ["COPY", "tmp:0:8", ["const:e28:8"]]
~~~


### [`0086051c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/0086051c.md) → [`008934b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934b4.md) FUN_008934b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008934d4",
      "incomplete_value": false,
      "site": "008934d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086053c",
      "incomplete_value": false,
      "site": "00860540",
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
            "const:d0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c040d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      36,
      "DATA",
      [
        "storage",
        "00c81ea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00860530 ["INT_ADD", "register:40f0:8", ["const:860530:8", "const:4:8"]]
+ 008934c8 ["INT_ADD", "register:40f0:8", ["const:8934c8:8", "const:4:8"]]
- 00860538 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 0086053c ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 008934d0 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008934d4 ["COPY", "tmp:0:8", ["const:ea8:8"]]
~~~


### [`00860554`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860554.md) → [`008934ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934ec.md) FUN_008934ec

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008934f0",
      "incomplete_value": false,
      "site": "008934f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860558",
      "incomplete_value": false,
      "site": "0086055c",
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
            "const:d0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c040d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c81ea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00860554 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 00860558 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 008934ec ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008934f0 ["COPY", "tmp:0:8", ["const:ea8:8"]]
~~~


### [`00860574`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860574.md) → [`0089350c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089350c.md) FUN_0089350c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459f48`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f48.md) [`0045a030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md) [`0085fd2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd2c.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cde0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde0.md) [`0047cec8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md) [`00892cc4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0089353c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008605a4",
      "value": [
        "leaf",
        "ram:457e1c:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00893548",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008605b0",
      "value": [
        "leaf",
        "ram:457e1c:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      48,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      48,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


~~~diff
- 008605a4 ["INT_ADD", "register:40f0:8", ["const:8605a4:8", "const:4:8"]]
- 008605a4 ["CALL", null, ["ram:457e1c:8"]]
- 008605a8 ["INT_ADD", "register:40f0:8", ["const:8605a8:8", "const:4:8"]]
+ 0089353c ["INT_ADD", "register:40f0:8", ["const:89353c:8", "const:4:8"]]
+ 0089353c ["CALL", null, ["ram:47acb4:8"]]
+ 00893540 ["INT_ADD", "register:40f0:8", ["const:893540:8", "const:4:8"]]
- 008605b0 ["INT_ADD", "register:40f0:8", ["const:8605b0:8", "const:4:8"]]
- 008605b0 ["CALL", null, ["ram:457e1c:8"]]
+ 00893548 ["INT_ADD", "register:40f0:8", ["const:893548:8", "const:4:8"]]
+ 00893548 ["CALL", null, ["ram:47acb4:8"]]
- 008605c4 ["INT_ADD", "register:40f0:8", ["const:8605c4:8", "const:4:8"]]
+ 0089355c ["INT_ADD", "register:40f0:8", ["const:89355c:8", "const:4:8"]]
~~~


### [`008605f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008605f0.md) → [`00893588`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893588.md) _INIT_167

根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008935c4",
      "incomplete_value": true,
      "site": "008935e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00893604",
      "incomplete_value": true,
      "site": "00893604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:120:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086066c",
      "incomplete_value": true,
      "site": "0086066c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:31:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008935e8",
      "incomplete_value": true,
      "site": "00893604",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086066c",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      60,
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00860618 ["COPY", "register:4098:8", ["const:109e000:8"]]
- 0086061c ["COPY", "tmp:0:8", ["const:658:8"]]
+ 008935b0 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 008935b4 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00860624 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00860628 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 008935bc ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 008935c0 ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 00860640 ["COPY", "register:4050:8", ["const:2a7000:8"]]
- 00860644 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 008935d8 ["COPY", "register:4050:8", ["const:2b7000:8"]]
+ 008935dc ["COPY", "tmp:0:8", ["const:ef9:8"]]
~~~


### [`0086470c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/0086470c.md) → [`008976ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/008976ac.md) FUN_008976ac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`008629ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 2件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0089598c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 2件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008976fc",
      "incomplete_value": true,
      "site": "008976fc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SLESS",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:4"
              ]
            ]
          ],
          [
            "INT_SBORROW",
            "1",
            [
              [
                "live",
                "register:4040:4"
              ],
              [
                "live",
                "register:40a8:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086475c",
      "incomplete_value": true,
      "site": "0086475c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:100:1"
          ],
          [
            "live",
            "register:103:1"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


~~~diff
- 00864738 ["BRANCH", null, ["local:b8:8"]]
+ 008976d8 ["BRANCH", null, ["local:b7:8"]]
- 00864744 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 008976e4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0086475c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 008976fc ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
~~~


### [`008647dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008647dc.md) → [`0089777c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/0089777c.md) FUN_0089777c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`008629ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 2件 [`00870f24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870f24.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0089598c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 2件 [`008a40c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a40c4.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "008977b8",
      "incomplete_value": true,
      "site": "008977b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00864818",
      "incomplete_value": true,
      "site": "00864818",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
              ]
            ]
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
    "new": null,
    "old": {
      "definition_site": "00864810",
      "incomplete_value": true,
      "site": "00864818",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


~~~diff
- 00864800 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008977a0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00864808 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 008977a8 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00864818 ["INT_ADD", "register:40f0:8", ["const:864818:8", "const:4:8"]]
+ 008977b8 ["INT_ADD", "register:40f0:8", ["const:8977b8:8", "const:4:8"]]
~~~


### [`008672ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00867/008672ac.md) → [`0089a3d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a3d0.md) FUN_0089a3d0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`008648a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00875adc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00875/00875adc.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00897848`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008a8c7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a8/008a8c7c.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0089a408",
      "incomplete_value": true,
      "site": "0089a408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:fffffffffffffff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008672e4",
      "incomplete_value": true,
      "site": "008672e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:fffffffffffffff0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0089a408",
      "incomplete_value": true,
      "site": "0089a408",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:1660:8"
              ],
              [
                "leaf",
                "const:28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008672e4",
      "incomplete_value": true,
      "site": "008672e4",
      "value": [
        "live",
        "register:4048:8"
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0089a414",
      "incomplete_value": true,
      "site": "0089a41c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4008:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008672f8",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


~~~diff
- 008672ec ["CBRANCH", null, ["local:b7:8", "tmp:3:1"]]
+ 0089a410 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
- 00867304 ["CBRANCH", null, ["local:b8:8", "tmp:3:1"]]
+ 0089a428 ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
- 00867310 ["INT_ADD", "register:40f0:8", ["const:867310:8", "const:4:8"]]
+ 0089a434 ["INT_ADD", "register:40f0:8", ["const:89a434:8", "const:4:8"]]
~~~


### [`00870980`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870980.md) → [`008a3b20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3b20.md) FUN_008a3b20

根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0087acb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087acb4.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008ade54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ade54.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a3b88",
      "incomplete_value": true,
      "site": "008a3b8c",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a3b84",
      "incomplete_value": true,
      "site": "008a3b8c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a3b84",
      "incomplete_value": true,
      "site": "008a3b8c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4018:8"
              ],
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
    "ordinal": 1,
    "slot": 3
  }
]
~~~


~~~diff
- 008709d0 ["CBRANCH", null, ["local:b6:8", "tmp:3:1"]]
+ 008a3b70 ["CBRANCH", null, ["local:b5:8", "tmp:3:1"]]
- 008709dc ["INT_ADD", "register:40f0:8", ["const:8709dc:8", "const:4:8"]]
+ 008a3b7c ["INT_ADD", "register:40f0:8", ["const:8a3b7c:8", "const:4:8"]]
- 008709e0 ["BRANCH", null, ["local:b7:8"]]
+ 008a3b80 ["BRANCH", null, ["local:b6:8"]]
~~~


### [`00870ab4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870ab4.md) → [`008a3c54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3c54.md) FUN_008a3c54

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 2件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`007205e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007205e8.md)
- 新版 呼出元 1件 [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0074a794`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a794.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a3c80",
      "incomplete_value": true,
      "site": "008a3c80",
      "value": [
        "live",
        "register:4048:8"
      ]
    },
    "old": {
      "definition_site": "00870ae0",
      "incomplete_value": true,
      "site": "00870ae0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


~~~diff
- 00870ac8 ["INT_ADD", "register:40f0:8", ["const:870ac8:8", "const:4:8"]]
+ 008a3c68 ["INT_ADD", "register:40f0:8", ["const:8a3c68:8", "const:4:8"]]
- 00870ad4 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
+ 008a3c74 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
- 00870ae8 ["BRANCH", null, ["local:b3:8"]]
+ 008a3c88 ["BRANCH", null, ["local:b4:8"]]
~~~


### [`00870b18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870b18.md) → [`008a3cb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3cb8.md) FUN_008a3cb8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 2件 [`0071e944`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e944.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`00748af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

~~~diff
- 00870b2c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 008a3ccc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00870b40 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 008a3ce0 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00870b50 ["INT_ADD", "register:40f0:8", ["const:870b50:8", "const:4:8"]]
+ 008a3cf0 ["INT_ADD", "register:40f0:8", ["const:8a3cf0:8", "const:4:8"]]
~~~


### [`00870b84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870b84.md) → [`008a3d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3d24.md) FUN_008a3d24

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 2件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 1件, `store_condition` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a3dd0",
      "incomplete_value": true,
      "site": "008a3dd4",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00870c34",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008a3d5c",
      "incomplete_value": true,
      "site": "008a3d5c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870bbc",
      "incomplete_value": true,
      "site": "00870bbc",
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
                "live",
                "register:40a0:8"
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008a3db8",
      "incomplete_value": true,
      "site": "008a3db8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870c18",
      "incomplete_value": true,
      "site": "00870c18",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


~~~diff
- 00870ba8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008a3d48 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00870bd4 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 008a3d74 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00870bdc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008a3d7c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
~~~


### [`00870c50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870c50.md) → [`008a3df0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3df0.md) FUN_008a3df0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`0087d888`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d888.md)
- 新版 呼出元 1件 [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`008b0a28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0a28.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008a3e14",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "00870c70",
      "incomplete_value": true,
      "site": "00870c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              [
                "live",
                "register:4008:8"
              ],
              [
                "leaf",
                "const:3:4"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "008a3e00",
      "incomplete_value": true,
      "site": "008a3e00",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_LESSEQUAL"
            ]
          ],
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
      "definition_site": "00870c60",
      "incomplete_value": true,
      "site": "00870c60",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_LESSEQUAL"
            ]
          ],
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
    "ordinal": 0,
    "slot": 0
  }
]
~~~


~~~diff
- 00870c6c ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
+ 008a3e0c ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
~~~


### [`00870c7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870c7c.md) → [`008a3e1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3e1c.md) FUN_008a3e1c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0087d9b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d9b4.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008b0b54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0b54.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a3edc",
      "incomplete_value": true,
      "site": "008a3edc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e8:8"
              ],
              [
                "leaf",
                "const:68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870d3c",
      "incomplete_value": true,
      "site": "00870d3c",
      "value": [
        "live",
        "register:4048:8"
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a3edc",
      "incomplete_value": true,
      "site": "008a3edc",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "00870d3c",
      "incomplete_value": true,
      "site": "00870d3c",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008a3f24",
      "incomplete_value": true,
      "site": "008a3f24",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870d84",
      "incomplete_value": true,
      "site": "00870d84",
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
    "ordinal": 5,
    "slot": 0
  }
]
~~~


~~~diff
- 00870ccc ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
+ 008a3e6c ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
- 00870ce4 ["CBRANCH", null, ["local:b5:8", "tmp:3:1"]]
+ 008a3e84 ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
- 00870cf0 ["INT_ADD", "register:40f0:8", ["const:870cf0:8", "const:4:8"]]
+ 008a3e90 ["INT_ADD", "register:40f0:8", ["const:8a3e90:8", "const:4:8"]]
~~~


### [`00870df0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870df0.md) → [`008a3f90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3f90.md) FUN_008a3f90

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`008820ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00882/008820ac.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008b524c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b5/008b524c.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_destination` 8件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a3f94",
      "incomplete_value": true,
      "site": "008a3f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870df4",
      "incomplete_value": true,
      "site": "00870df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a3f94",
      "incomplete_value": true,
      "site": "008a3f94",
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
                "register:8:8"
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
      "definition_site": "00870df4",
      "incomplete_value": true,
      "site": "00870df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a3f98",
      "incomplete_value": true,
      "site": "008a3f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870df8",
      "incomplete_value": true,
      "site": "00870df8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


~~~diff
- 00870e28 ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
+ 008a3fc8 ["CBRANCH", null, ["local:b7:8", "tmp:3:1"]]
- 00870e40 ["CBRANCH", null, ["local:b5:8", "tmp:3:1"]]
+ 008a3fe0 ["CBRANCH", null, ["local:b9:8", "tmp:3:1"]]
- 00870e4c ["INT_ADD", "register:40f0:8", ["const:870e4c:8", "const:4:8"]]
+ 008a3fec ["INT_ADD", "register:40f0:8", ["const:8a3fec:8", "const:4:8"]]
~~~


### [`00870f24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870f24.md) → [`008a40c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a40c4.md) FUN_008a40c4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`008647dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008647dc.md) · 呼出先 1件 [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0089777c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/0089777c.md) · 呼出先 1件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008a4100",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00870f5c",
      "incomplete_value": true,
      "site": "00870f60",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:4000:8"
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "008a4160",
      "incomplete_value": true,
      "site": "008a4160",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "00870fc0",
      "incomplete_value": true,
      "site": "00870fc0",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "008a4170",
      "incomplete_value": true,
      "site": "008a4170",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870fd0",
      "incomplete_value": true,
      "site": "00870fd0",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


~~~diff
- 00870f48 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 008a40e8 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00870f60 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 008a4100 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00870f68 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 008a4108 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
~~~


### [`00871090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871090.md) → [`008a4230`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4230.md) FUN_008a4230

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a4244",
      "incomplete_value": false,
      "site": "008a4248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008710a8",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c041c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c81fa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0087109c ["INT_ADD", "register:40f0:8", ["const:87109c:8", "const:4:8"]]
+ 008a423c ["INT_ADD", "register:40f0:8", ["const:8a423c:8", "const:4:8"]]
- 008710a0 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 008710a4 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 008a4240 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008a4244 ["COPY", "tmp:0:8", ["const:fa0:8"]]
~~~


### [`008710cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008710cc.md) → [`008a426c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a426c.md) FUN_008a426c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00871200`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871200.md) [`00871204`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871204.md) [`00ada5f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008a43a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a43a0.md) [`008a43a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a43a4.md) [`00b39fc8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39fc8.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a4284",
      "incomplete_value": false,
      "site": "008a4294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:10:8"
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
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008a42dc",
      "incomplete_value": true,
      "site": "008a42dc",
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
      "definition_site": "0087113c",
      "incomplete_value": true,
      "site": "0087113c",
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
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "DATA",
      [
        "storage",
        "00c04238",
        null,
        "undefined *"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c04258",
        null,
        "pointer"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c04260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      40,
      "DATA",
      [
        "storage",
        "00c82010",
        null,
        "undefined *"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c82030",
        null,
        "pointer"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c82038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008710e0 ["COPY", "register:4048:8", ["const:c04000:8"]]
- 008710e4 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 008a4280 ["COPY", "register:4048:8", ["const:c82000:8"]]
+ 008a4284 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00871100 ["INT_ADD", "register:40f0:8", ["const:871100:8", "const:4:8"]]
+ 008a42a0 ["INT_ADD", "register:40f0:8", ["const:8a42a0:8", "const:4:8"]]
- 0087112c ["INT_ADD", "register:40f0:8", ["const:87112c:8", "const:4:8"]]
+ 008a42cc ["INT_ADD", "register:40f0:8", ["const:8a42cc:8", "const:4:8"]]
~~~


### [`008711cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008711cc.md) → [`008a436c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a436c.md) FUN_008a436c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a4380",
      "incomplete_value": true,
      "site": "008a4384",
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
            "const:10:8"
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
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c04238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c82010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008711d8 ["INT_ADD", "register:40f0:8", ["const:8711d8:8", "const:4:8"]]
+ 008a4378 ["INT_ADD", "register:40f0:8", ["const:8a4378:8", "const:4:8"]]
- 008711dc ["COPY", "register:4040:8", ["const:c04000:8"]]
- 008711e0 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 008a437c ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a4380 ["COPY", "tmp:0:8", ["const:10:8"]]
~~~


### [`008711f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008711f0.md) → [`008a4390`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4390.md) FUN_008a4390

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a4394",
      "incomplete_value": false,
      "site": "008a4398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:10:8"
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
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c04238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c82010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008711f0 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 008711f4 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 008a4390 ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a4394 ["COPY", "tmp:0:8", ["const:10:8"]]
~~~


### [`00871208`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871208.md) → [`008a43a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a43a8.md) FUN_008a43a8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00871348`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871348.md) [`0087134c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/0087134c.md) [`00ada7b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008a44e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44e8.md) [`008a44ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44ec.md) [`00b3a190`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a190.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008a43dc",
      "value": [
        "live",
        "register:4040:8"
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008a43e0",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": {
      "definition_site": "00871238",
      "incomplete_value": true,
      "site": "00871240",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a43e4",
      "incomplete_value": true,
      "site": "008a43e8",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "DATA",
      [
        "storage",
        "00c042a8",
        null,
        "undefined *"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c042c8",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c042d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      52,
      "DATA",
      [
        "storage",
        "00c82080",
        null,
        "undefined *"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c820a0",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c820a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0087122c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00871230 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 00871234 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 008a43cc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 008a43d0 ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a43d4 ["COPY", "tmp:0:8", ["const:80:8"]]
- 00871248 ["INT_ADD", "register:40f0:8", ["const:871248:8", "const:4:8"]]
+ 008a43e8 ["INT_ADD", "register:40f0:8", ["const:8a43e8:8", "const:4:8"]]
- 00871254 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 008a43f4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
~~~


### [`00871314`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871314.md) → [`008a44b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44b4.md) FUN_008a44b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a44c8",
      "incomplete_value": false,
      "site": "008a44cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:80:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c042a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c82080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00871320 ["INT_ADD", "register:40f0:8", ["const:871320:8", "const:4:8"]]
+ 008a44c0 ["INT_ADD", "register:40f0:8", ["const:8a44c0:8", "const:4:8"]]
- 00871324 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 00871328 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 008a44c4 ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a44c8 ["COPY", "tmp:0:8", ["const:80:8"]]
~~~


### [`00871338`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871338.md) → [`008a44d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44d8.md) FUN_008a44d8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a44dc",
      "incomplete_value": false,
      "site": "008a44e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:80:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c042a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c82080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00871338 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 0087133c ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 008a44d8 ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a44dc ["COPY", "tmp:0:8", ["const:80:8"]]
~~~


### [`00871350`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871350.md) → [`008a44f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44f0.md) FUN_008a44f0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006f23b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`00447eb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0071c420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 15件, `call_target` 1件, `store_destination` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a44fc",
      "incomplete_value": true,
      "site": "008a44fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:100:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087135c",
      "incomplete_value": true,
      "site": "0087135c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a44fc",
      "incomplete_value": true,
      "site": "008a44fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:f0:8"
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
      "definition_site": "0087135c",
      "incomplete_value": true,
      "site": "0087135c",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:f0:8"
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
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a450c",
      "incomplete_value": true,
      "site": "008a450c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:d0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087136c",
      "incomplete_value": true,
      "site": "0087136c",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:d0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f23b4"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00293b96",
        null,
        "string"
      ]
    ],
    [
      328,
      "DATA",
      [
        "storage",
        "00c04318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "002a338f",
        null,
        "string"
      ]
    ],
    [
      328,
      "DATA",
      [
        "storage",
        "00c820f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00871378 ["CBRANCH", null, ["local:b33:8", "tmp:0:1"]]
+ 008a4518 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
- 00871388 ["INT_ADD", "register:40f0:8", ["const:871388:8", "const:4:8"]]
- 00871388 ["CALL", null, ["ram:6f23b4:8"]]
- 0087138c ["INT_ADD", "register:40f0:8", ["const:87138c:8", "const:4:8"]]
+ 008a4528 ["INT_ADD", "register:40f0:8", ["const:8a4528:8", "const:4:8"]]
+ 008a4528 ["CALL", null, ["ram:71c420:8"]]
+ 008a452c ["INT_ADD", "register:40f0:8", ["const:8a452c:8", "const:4:8"]]
- 00871390 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:21c8:8"]]
+ 008a4530 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:22b0:8"]]
~~~


### [`008716f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008716f8.md) → [`008a4898`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4898.md) FUN_008a4898

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a48ac",
      "incomplete_value": false,
      "site": "008a48b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
            "const:318:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c04318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c820f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00871704 ["INT_ADD", "register:40f0:8", ["const:871704:8", "const:4:8"]]
+ 008a48a4 ["INT_ADD", "register:40f0:8", ["const:8a48a4:8", "const:4:8"]]
- 00871708 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 0087170c ["COPY", "tmp:0:8", ["const:318:8"]]
+ 008a48a8 ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a48ac ["COPY", "tmp:0:8", ["const:f0:8"]]
~~~


### [`0087171c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/0087171c.md) → [`008a48bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a48bc.md) FUN_008a48bc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a48c0",
      "incomplete_value": false,
      "site": "008a48c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c04318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c820f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0087171c ["COPY", "register:4040:8", ["const:c04000:8"]]
- 00871720 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 008a48bc ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a48c0 ["COPY", "tmp:0:8", ["const:f0:8"]]
~~~


### [`00871734`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871734.md) → [`008a48d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a48d4.md) FUN_008a48d4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008a48dc",
      "incomplete_value": true,
      "site": "008a48dc",
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
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087173c",
      "incomplete_value": true,
      "site": "0087173c",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008a48f8",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00871758",
      "value": [
        "leaf",
        "ram:457e1c:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a48fc",
      "incomplete_value": false,
      "site": "008a4904",
      "value": [
        "leaf",
        "const:b:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0087173c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 008a48dc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00871744 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 008a48e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00871758 ["INT_ADD", "register:40f0:8", ["const:871758:8", "const:4:8"]]
- 00871758 ["CALL", null, ["ram:457e1c:8"]]
+ 008a48f8 ["INT_ADD", "register:40f0:8", ["const:8a48f8:8", "const:4:8"]]
+ 008a48f8 ["CALL", null, ["ram:47acb4:8"]]
~~~


### [`008717a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008717a8.md) → [`008a4948`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4948.md) FUN_008a4948

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a495c",
      "incomplete_value": false,
      "site": "008a4960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c043c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c821a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008717b4 ["INT_ADD", "register:40f0:8", ["const:8717b4:8", "const:4:8"]]
+ 008a4954 ["INT_ADD", "register:40f0:8", ["const:8a4954:8", "const:4:8"]]
- 008717b8 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 008717bc ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 008a4958 ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a495c ["COPY", "tmp:0:8", ["const:1a0:8"]]
~~~


### [`008717e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008717e4.md) → [`008a4984`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4984.md) FUN_008a4984

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00469e20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00470050`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470050.md) [`00470a98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470a98.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0048ccb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492ee8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md) [`00493930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493930.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a498c",
      "incomplete_value": true,
      "site": "008a498c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:60:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008717ec",
      "incomplete_value": true,
      "site": "008717ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a498c",
      "incomplete_value": true,
      "site": "008a498c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:50:8"
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
      "definition_site": "008717ec",
      "incomplete_value": true,
      "site": "008717ec",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:50:8"
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
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a499c",
      "incomplete_value": true,
      "site": "008a499c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008717fc",
      "incomplete_value": true,
      "site": "008717fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      52,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "002960fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      52,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "002a5b52",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00871804 ["CBRANCH", null, ["local:b7:8", "tmp:3:1"]]
+ 008a49a4 ["CBRANCH", null, ["local:b8:8", "tmp:3:1"]]
- 0087180c ["INT_ADD", "register:40f0:8", ["const:87180c:8", "const:4:8"]]
- 0087180c ["CALL", null, ["ram:469e20:8"]]
+ 008a49ac ["INT_ADD", "register:40f0:8", ["const:8a49ac:8", "const:4:8"]]
+ 008a49ac ["CALL", null, ["ram:48ccb8:8"]]
- 00871814 ["INT_ADD", "register:40f0:8", ["const:871814:8", "const:4:8"]]
+ 008a49b4 ["INT_ADD", "register:40f0:8", ["const:8a49b4:8", "const:4:8"]]
~~~


### [`00871910`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871910.md) → [`008a4ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ab0.md) FUN_008a4ab0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a4ac4",
      "incomplete_value": false,
      "site": "008a4ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:220:8"
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
            "const:448:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c04448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c82220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0087191c ["INT_ADD", "register:40f0:8", ["const:87191c:8", "const:4:8"]]
+ 008a4abc ["INT_ADD", "register:40f0:8", ["const:8a4abc:8", "const:4:8"]]
- 00871920 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 00871924 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 008a4ac0 ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a4ac4 ["COPY", "tmp:0:8", ["const:220:8"]]
~~~


### [`0087194c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/0087194c.md) → [`008a4aec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4aec.md) FUN_008a4aec

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008a4b10",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00871970",
      "value": [
        "leaf",
        "ram:457e1c:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a4b14",
      "incomplete_value": false,
      "site": "008a4b1c",
      "value": [
        "leaf",
        "const:b:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00871954 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 008a4af4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0087195c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 008a4afc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00871970 ["INT_ADD", "register:40f0:8", ["const:871970:8", "const:4:8"]]
- 00871970 ["CALL", null, ["ram:457e1c:8"]]
+ 008a4b10 ["INT_ADD", "register:40f0:8", ["const:8a4b10:8", "const:4:8"]]
+ 008a4b10 ["CALL", null, ["ram:47acb4:8"]]
~~~


### [`008719c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008719c0.md) → [`008a4b60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4b60.md) FUN_008a4b60

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a4b74",
      "incomplete_value": false,
      "site": "008a4b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c044c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      24,
      "DATA",
      [
        "storage",
        "00c822a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008719cc ["INT_ADD", "register:40f0:8", ["const:8719cc:8", "const:4:8"]]
+ 008a4b6c ["INT_ADD", "register:40f0:8", ["const:8a4b6c:8", "const:4:8"]]
- 008719d0 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 008719d4 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 008a4b70 ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a4b74 ["COPY", "tmp:0:8", ["const:2a0:8"]]
~~~


