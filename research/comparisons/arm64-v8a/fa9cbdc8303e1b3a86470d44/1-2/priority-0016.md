# v15.7.4 → v16.0.0 · 最優先の変更候補 (16)

[一覧の目次](README.md)

### [`005242cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/005242cc.md) → [`00547164`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547164.md) FUN_00547164

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00522d64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522d64.md) [`00523df4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/00523df4.md) · 呼出先 3件 [`005240ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/005240ec.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`00545bfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) [`00546c8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546c8c.md) · 呼出先 3件 [`00546f84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546f84.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 3件, `store_destination` 9件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054716c",
      "incomplete_value": true,
      "site": "0054716c",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005242d4",
      "incomplete_value": true,
      "site": "005242d4",
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
                "const:d0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:90:8"
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
      "definition_site": "0054716c",
      "incomplete_value": true,
      "site": "0054716c",
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
                "const:90:8"
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
      "definition_site": "005242d4",
      "incomplete_value": true,
      "site": "005242d4",
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
                "const:90:8"
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
      "definition_site": "00547170",
      "incomplete_value": true,
      "site": "00547170",
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
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005242d8",
      "incomplete_value": true,
      "site": "005242d8",
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
                "const:d0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:a0:8"
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
- 0052430c ["INT_ADD", "register:40f0:8", ["const:52430c:8", "const:4:8"]]
+ 005471a4 ["INT_ADD", "register:40f0:8", ["const:5471a4:8", "const:4:8"]]
- 00524348 ["INT_ADD", "register:40f0:8", ["const:524348:8", "const:4:8"]]
+ 005471e0 ["INT_ADD", "register:40f0:8", ["const:5471e0:8", "const:4:8"]]
- 00524364 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 005471fc ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
~~~


### [`0052452c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/0052452c.md) → [`005473c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005473c4.md) FUN_005473c4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00522d64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522d64.md) · 呼出先 2件 [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00545bfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 2件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 10件, `store_condition` 3件, `store_destination` 9件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005473d0",
      "incomplete_value": true,
      "site": "005473d0",
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
      "definition_site": "00524538",
      "incomplete_value": true,
      "site": "00524538",
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
                "const:b0:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005473d0",
      "incomplete_value": true,
      "site": "005473d0",
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
                "const:70:8"
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
      "definition_site": "00524538",
      "incomplete_value": true,
      "site": "00524538",
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
                "const:70:8"
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
      "definition_site": "005473d4",
      "incomplete_value": true,
      "site": "005473d4",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052453c",
      "incomplete_value": true,
      "site": "0052453c",
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
                "const:b0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


~~~diff
- 0052455c ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
+ 005473f4 ["CBRANCH", null, ["local:b46:8", "tmp:0:1"]]
- 00524584 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
+ 0054741c ["CBRANCH", null, ["local:b46:8", "tmp:0:1"]]
- 005245a8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00547440 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
~~~


### [`00524810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524810.md) → [`005476a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005476a8.md) FUN_005476a8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00522d64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522d64.md) · 呼出先 4件 [`00524990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524990.md) [`00524ab4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524ab4.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00545bfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 4件 [`00547828`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547828.md) [`0054794c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/0054794c.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 9件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005476b4",
      "incomplete_value": true,
      "site": "005476b4",
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
      "definition_site": "0052481c",
      "incomplete_value": true,
      "site": "0052481c",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005476b4",
      "incomplete_value": true,
      "site": "005476b4",
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
      "definition_site": "0052481c",
      "incomplete_value": true,
      "site": "0052481c",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005476b8",
      "incomplete_value": true,
      "site": "005476b8",
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
      "definition_site": "00524820",
      "incomplete_value": true,
      "site": "00524820",
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
    "ordinal": 6,
    "slot": 1
  }
]
~~~


~~~diff
- 00524844 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 005476dc ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00524864 ["BRANCH", null, ["local:b7:8"]]
+ 005476fc ["BRANCH", null, ["local:b5:8"]]
- 005248a8 ["INT_ADD", "register:40f0:8", ["const:5248a8:8", "const:4:8"]]
+ 00547740 ["INT_ADD", "register:40f0:8", ["const:547740:8", "const:4:8"]]
~~~


### [`00524990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524990.md) → [`00547828`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547828.md) FUN_00547828

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00524810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524810.md) · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`005476a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005476a8.md) · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `return_value_candidate` 1件, `store_destination` 10件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054782c",
      "incomplete_value": true,
      "site": "0054782c",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00524994",
      "incomplete_value": true,
      "site": "00524994",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054782c",
      "incomplete_value": true,
      "site": "0054782c",
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
    "old": {
      "definition_site": "00524994",
      "incomplete_value": true,
      "site": "00524994",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00547830",
      "incomplete_value": true,
      "site": "00547830",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00524998",
      "incomplete_value": true,
      "site": "00524998",
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
    "ordinal": 4,
    "slot": 1
  }
]
~~~


~~~diff
- 005249cc ["BRANCH", null, ["local:b5:8"]]
+ 00547864 ["BRANCH", null, ["local:b3:8"]]
- 005249ec ["CBRANCH", null, ["local:b12:8", "tmp:2:1"]]
+ 00547884 ["CBRANCH", null, ["local:b10:8", "tmp:2:1"]]
- 00524a0c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 005478a4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
~~~


### [`00524ab4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524ab4.md) → [`0054794c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/0054794c.md) FUN_0054794c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00524810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524810.md) · 呼出先 2件 [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`005476a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005476a8.md) · 呼出先 2件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 5件, `store_destination` 12件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00547950",
      "incomplete_value": true,
      "site": "00547950",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00524ab8",
      "incomplete_value": true,
      "site": "00524ab8",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00547950",
      "incomplete_value": true,
      "site": "00547950",
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
    "old": {
      "definition_site": "00524ab8",
      "incomplete_value": true,
      "site": "00524ab8",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00547954",
      "incomplete_value": true,
      "site": "00547954",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00524abc",
      "incomplete_value": true,
      "site": "00524abc",
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
    "ordinal": 2,
    "slot": 1
  }
]
~~~


~~~diff
- 00524ae4 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
+ 0054797c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00524b34 ["INT_ADD", "register:40f0:8", ["const:524b34:8", "const:4:8"]]
+ 005479cc ["INT_ADD", "register:40f0:8", ["const:5479cc:8", "const:4:8"]]
- 00524b50 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
+ 005479e8 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
~~~


### [`00524c44`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c44.md) → [`00547adc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547adc.md) FUN_00547adc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00547afc",
      "incomplete_value": false,
      "site": "00547b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00524c64",
      "incomplete_value": false,
      "site": "00524c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
        "00bed6f0",
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
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00524c58 ["INT_ADD", "register:40f0:8", ["const:524c58:8", "const:4:8"]]
+ 00547af0 ["INT_ADD", "register:40f0:8", ["const:547af0:8", "const:4:8"]]
- 00524c60 ["COPY", "register:4040:8", ["const:bed000:8"]]
- 00524c64 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 00547af8 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00547afc ["COPY", "tmp:0:8", ["const:2b0:8"]]
~~~


### [`00524c7c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c7c.md) → [`00547b14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b14.md) FUN_00547b14

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
      "definition_site": "00547b1c",
      "incomplete_value": false,
      "site": "00547b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00524c84",
      "incomplete_value": false,
      "site": "00524c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
        "00bed6f0",
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
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00524c80 ["COPY", "register:4048:8", ["const:bed000:8"]]
- 00524c84 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 00547b18 ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00547b1c ["COPY", "tmp:0:8", ["const:2b0:8"]]
~~~


### [`00524cd8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524cd8.md) → [`00547b70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md) FUN_00547b70

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`004dc168`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc168.md) [`00540d3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540d3c.md) [`00562028`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562028.md) · 呼出先 1件 [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 3件 [`004ff000`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff000.md) [`00563bd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563bd4.md) [`00584ec0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md) · 呼出先 1件 [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00547c00",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00524d60",
      "incomplete_value": true,
      "site": "00524d68",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "4",
            [
              [
                "live",
                "register:4000:4"
              ],
              [
                "leaf",
                "const:0:4"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00547cc8",
      "incomplete_value": true,
      "site": "00547cc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00524e30",
      "incomplete_value": true,
      "site": "00524e30",
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
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00547c08",
      "incomplete_value": true,
      "site": "00547c14",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


~~~diff
- 00524cf8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00547b90 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00524d20 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00547bb8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00524d54 ["INT_ADD", "register:40f0:8", ["const:524d54:8", "const:4:8"]]
+ 00547bec ["INT_ADD", "register:40f0:8", ["const:547bec:8", "const:4:8"]]
~~~


### [`00524e98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524e98.md) → [`00547d30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d30.md) FUN_00547d30

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00547d48",
      "incomplete_value": true,
      "site": "00547d4c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  }
]
~~~


~~~diff
- 00524eac ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00547d44 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
- 00524eb4 ["INT_ADD", "register:40f0:8", ["const:524eb4:8", "const:4:8"]]
+ 00547d4c ["INT_ADD", "register:40f0:8", ["const:547d4c:8", "const:4:8"]]
- 00524ebc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00547d54 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
~~~


### [`00524eec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524eec.md) → [`00547d84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d84.md) FUN_00547d84

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`004dc4a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc4a4.md) · 呼出先 2件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`004ff33c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) · 呼出先 2件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_value

優先判定に残った影響 `branch_value` 4件, `return_value_candidate` 1件, `store_condition` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00547db0",
      "incomplete_value": true,
      "site": "00547dbc",
      "value": [
        "LOAD",
        "16",
        [
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
      "site": "00524f24",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00547dc0",
      "incomplete_value": true,
      "site": "00547dc0",
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
      "definition_site": "00524f28",
      "incomplete_value": true,
      "site": "00524f28",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00547de0",
      "value": [
        "live",
        "register:5020:16"
      ]
    },
    "old": {
      "definition_site": "00524f34",
      "incomplete_value": true,
      "site": "00524f48",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:28:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c1afc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c9a9b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00524f08 ["INT_ADD", "register:40f0:8", ["const:524f08:8", "const:4:8"]]
+ 00547da0 ["INT_ADD", "register:40f0:8", ["const:547da0:8", "const:4:8"]]
- 00524f0c ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 00547da4 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00524f14 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f50:8"]]
+ 00547dac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:940:8"]]
~~~


### [`00525054`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525054.md) → [`00547eec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547eec.md) FUN_00547eec

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`004dc4a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc4a4.md) · 呼出先 5件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0047c554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`004ff33c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) · 呼出先 5件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0049f3ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00547f28",
      "incomplete_value": true,
      "site": "00547f2c",
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00525094",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00547f80",
      "incomplete_value": true,
      "site": "00547f80",
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
      "definition_site": "005250e8",
      "incomplete_value": true,
      "site": "005250e8",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00547f30",
      "incomplete_value": true,
      "site": "00547f34",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "old": {
      "definition_site": "00525098",
      "incomplete_value": true,
      "site": "0052509c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4048:8"
              ],
              [
                "live",
                "register:40b0:8"
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
      44,
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      132,
      "READ",
      [
        "storage",
        "00c1afc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      44,
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      132,
      "READ",
      [
        "storage",
        "00c9a9b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00525074 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00547f0c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00525080 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 00547f18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 0052509c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00547f34 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
~~~


### [`005251c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005251c0.md) → [`00548058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md) FUN_00548058

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 7件 [`004dc6d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc6d0.md) [`004dc84c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc84c.md) [`004dcbd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcbd4.md) [`004e12e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e12e8.md) [`005001f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/005001f4.md) · 呼出先 1件 [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 7件 [`004ff568`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff568.md) [`004ff6e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff6e4.md) [`004ffa6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) [`00504180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504180.md) [`0052308c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/0052308c.md) · 呼出先 1件 [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 11件, `call_argument_candidate` 1件, `store_destination` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00548060",
      "incomplete_value": true,
      "site": "00548060",
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
                "const:ffffffffffffffb0:8"
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
      "definition_site": "005251c8",
      "incomplete_value": true,
      "site": "005251c8",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00548060",
      "incomplete_value": true,
      "site": "00548060",
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
      "definition_site": "005251c8",
      "incomplete_value": true,
      "site": "005251c8",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00548064",
      "incomplete_value": true,
      "site": "00548064",
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
                "const:ffffffffffffffb0:8"
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
      "definition_site": "005251cc",
      "incomplete_value": true,
      "site": "005251cc",
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
    "ordinal": 6,
    "slot": 1
  }
]
~~~


~~~diff
- 005251e0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00548078 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00525208 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 005480a0 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 0052523c ["INT_ADD", "register:40f0:8", ["const:52523c:8", "const:4:8"]]
+ 005480d4 ["INT_ADD", "register:40f0:8", ["const:5480d4:8", "const:4:8"]]
~~~


### [`00525380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md) → [`00548218`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md) FUN_00548218

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`004e56e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e56e4.md) [`004f7f54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7f54.md) [`0053d168`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d168.md) [`00b88310`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md) · 呼出先 1件 [`00bdd170`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd170.md)
- 新版 呼出元 4件 [`0050857c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md) [`0051adec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051adec.md) [`00560000`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md) [`00c04d58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04d58.md) · 呼出先 1件 [`00c59bc0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59bc0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

~~~diff
- 005253c8 ["CBRANCH", null, ["local:b9:8", "tmp:3:1"]]
+ 00548260 ["CBRANCH", null, ["local:b10:8", "tmp:3:1"]]
- 005253f0 ["INT_ADD", "register:40f0:8", ["const:5253f0:8", "const:4:8"]]
+ 00548288 ["INT_ADD", "register:40f0:8", ["const:548288:8", "const:4:8"]]
- 0052541c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 005482b4 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
~~~


### [`005254e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005254e0.md) → [`00548378`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md) FUN_00548378

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 3件 [`004de4b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de4b0.md) [`004dfd64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfd64.md) [`00508860`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) · 呼出先 6件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005256ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256ac.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`00501348`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md) [`00502bfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md) [`0052b6f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) · 呼出先 6件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548544`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `branch_value` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00548414",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00525574",
      "incomplete_value": true,
      "site": "0052557c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40c8:8"
              ],
              [
                "live",
                "register:40a8:8"
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "005255f8",
      "incomplete_value": true,
      "site": "00525610",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


~~~diff
- 00525510 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 005483a8 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 0052553c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 005483d4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00525544 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
+ 005483dc ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
~~~


### [`00525620`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525620.md) → [`005484b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005484b8.md) FUN_005484b8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0052565c",
      "incomplete_value": false,
      "site": "00525660",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
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
      "definition_site": "00525658",
      "incomplete_value": true,
      "site": "00525660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


~~~diff
- 00525644 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 005484dc ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00525660 ["INT_ADD", "register:40f0:8", ["const:525660:8", "const:4:8"]]
+ 005484f8 ["INT_ADD", "register:40f0:8", ["const:5484f8:8", "const:4:8"]]
- 00525674 ["INT_ADD", "register:40f0:8", ["const:525674:8", "const:4:8"]]
+ 0054850c ["INT_ADD", "register:40f0:8", ["const:54850c:8", "const:4:8"]]
~~~


### [`005256ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256ac.md) → [`00548544`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) FUN_00548544

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 8件 [`00506ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) [`00508860`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) [`0050947c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050947c.md) [`00509f18`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md) [`005254e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005254e0.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`00529d78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) [`0052b6f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) [`0052c314`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md) [`0052cdb0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) [`00548378`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00548554",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005256bc",
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
      "definition_site": "00548550",
      "incomplete_value": false,
      "site": "00548554",
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
      "definition_site": "005256b8",
      "incomplete_value": false,
      "site": "005256bc",
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
- 005256b4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 005256b8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0054854c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00548550 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005256bc ["INT_ADD", "register:40f0:8", ["const:5256bc:8", "const:4:8"]]
- 005256bc ["CALL", null, ["ram:418c38:8"]]
+ 00548554 ["INT_ADD", "register:40f0:8", ["const:548554:8", "const:4:8"]]
+ 00548554 ["CALL", null, ["ram:43b738:8"]]
~~~


### [`005256c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256c0.md) → [`00548558`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548558.md) FUN_00548558

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 4件 [`004de768`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de768.md) [`004ded14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004ded14.md) [`0050645c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/0050645c.md) [`00506ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) · 呼出先 7件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005256ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256ac.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 4件 [`00501600`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501600.md) [`00501bac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501bac.md) [`005292f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md) [`00529d78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 7件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548544`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_destination, store_value

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_destination` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00548564",
      "incomplete_value": true,
      "site": "00548564",
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
                "const:ffffffffffffffb0:8"
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
      "definition_site": "005256cc",
      "incomplete_value": true,
      "site": "005256cc",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00548564",
      "incomplete_value": true,
      "site": "00548564",
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
      "definition_site": "005256cc",
      "incomplete_value": true,
      "site": "005256cc",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00548568",
      "incomplete_value": true,
      "site": "00548568",
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
                "const:ffffffffffffffb0:8"
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
    "old": {
      "definition_site": "005256d0",
      "incomplete_value": true,
      "site": "005256d0",
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
    "ordinal": 7,
    "slot": 1
  }
]
~~~


~~~diff
- 005256f0 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
+ 00548588 ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 0052571c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 005485b4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00525724 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
+ 005485bc ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
~~~


### [`0052581c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/0052581c.md) → [`005486b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) FUN_005486b4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`004de868`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de868.md) · 呼出先 8件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004df920`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df920.md) [`005180b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`005259e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005259e4.md) [`00525b94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525b94.md)
- 新版 呼出元 1件 [`00501700`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501700.md) · 呼出先 8件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005027b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) [`0053af50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0054887c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/0054887c.md) [`00548a2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a2c.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_condition` 1件, `store_destination` 8件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005486b8",
      "incomplete_value": true,
      "site": "005486b8",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00525820",
      "incomplete_value": true,
      "site": "00525820",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005486b8",
      "incomplete_value": true,
      "site": "005486b8",
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
      "definition_site": "00525820",
      "incomplete_value": true,
      "site": "00525820",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005486bc",
      "incomplete_value": true,
      "site": "005486bc",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00525824",
      "incomplete_value": true,
      "site": "00525824",
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
    "ordinal": 2,
    "slot": 1
  }
]
~~~


~~~diff
- 0052587c ["CBRANCH", null, ["local:b21:8", "tmp:1:1"]]
+ 00548714 ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
- 005258bc ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00548754 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 005258c4 ["CBRANCH", null, ["local:b24:8", "tmp:1:1"]]
+ 0054875c ["CBRANCH", null, ["local:b18:8", "tmp:1:1"]]
~~~


### [`005259e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005259e4.md) → [`0054887c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/0054887c.md) FUN_0054887c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`0052581c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/0052581c.md) · 呼出先 2件 [`005180b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005486b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) · 呼出先 2件 [`0053af50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 2件, `store_destination` 8件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005488dc",
      "incomplete_value": true,
      "site": "005488dc",
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
                "register:40b8:8"
              ],
              [
                "live",
                "register:4040:8"
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
      "definition_site": "00525a44",
      "incomplete_value": true,
      "site": "00525a44",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005488dc",
      "incomplete_value": true,
      "site": "005488dc",
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
      "definition_site": "00525a44",
      "incomplete_value": true,
      "site": "00525a44",
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
                "register:4050:8"
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
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005488e0",
      "incomplete_value": true,
      "site": "005488e0",
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
                "register:40b8:8"
              ],
              [
                "live",
                "register:4040:8"
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
      "definition_site": "00525a48",
      "incomplete_value": true,
      "site": "00525a48",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
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
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      156,
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      60,
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      156,
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00525a14 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00525a18 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 005488ac ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 005488b0 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00525a20 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2e0:8"]]
+ 005488b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cd0:8"]]
- 00525a28 ["BRANCH", null, ["local:b7:8"]]
+ 005488c0 ["BRANCH", null, ["local:b4:8"]]
~~~


### [`00525b1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525b1c.md) → [`005489b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005489b4.md) FUN_005489b4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005180b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053af50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005489bc",
      "incomplete_value": true,
      "site": "005489bc",
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
                "const:ffffffffffffffd0:8"
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
      "definition_site": "00525b24",
      "incomplete_value": true,
      "site": "00525b24",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005489bc",
      "incomplete_value": true,
      "site": "005489bc",
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
      "definition_site": "00525b24",
      "incomplete_value": true,
      "site": "00525b24",
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
    "ordinal": 4,
    "slot": 1
  }
]
~~~


~~~diff
- 00525b34 ["BRANCH", null, ["local:b6:8"]]
+ 005489cc ["BRANCH", null, ["local:b2:8"]]
- 00525b40 ["INT_ADD", "register:40f0:8", ["const:525b40:8", "const:4:8"]]
+ 005489d8 ["INT_ADD", "register:40f0:8", ["const:5489d8:8", "const:4:8"]]
- 00525b4c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 005489e4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
~~~


### [`00525b94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525b94.md) → [`00548a2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a2c.md) FUN_00548a2c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0052581c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/0052581c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005486b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00548a3c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00525ba4",
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
      "definition_site": "00548a38",
      "incomplete_value": false,
      "site": "00548a3c",
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
      "definition_site": "00525ba0",
      "incomplete_value": true,
      "site": "00525ba4",
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
- 00525b9c ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00525ba0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00548a34 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00548a38 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00525ba4 ["INT_ADD", "register:40f0:8", ["const:525ba4:8", "const:4:8"]]
- 00525ba4 ["CALL", null, ["ram:418c38:8"]]
+ 00548a3c ["INT_ADD", "register:40f0:8", ["const:548a3c:8", "const:4:8"]]
+ 00548a3c ["CALL", null, ["ram:43b738:8"]]
~~~


### [`00525bf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525bf0.md) → [`00548a88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a88.md) FUN_00548a88

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`004df5b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df5b0.md) · 呼出先 2件 [`00525c44`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525c44.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00502448`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502448.md) · 呼出先 2件 [`00548adc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548adc.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00548a90",
      "incomplete_value": true,
      "site": "00548a90",
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
      "definition_site": "00525bf8",
      "incomplete_value": true,
      "site": "00525bf8",
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
                "const:30:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00548aac",
      "incomplete_value": true,
      "site": "00548aac",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00525c14",
      "incomplete_value": true,
      "site": "00525c14",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00548aa0",
      "incomplete_value": true,
      "site": "00548ab0",
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
            "const:7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00525c08",
      "incomplete_value": true,
      "site": "00525c18",
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
                "const:30:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:7:8"
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
- 00525c18 ["INT_ADD", "register:40f0:8", ["const:525c18:8", "const:4:8"]]
+ 00548ab0 ["INT_ADD", "register:40f0:8", ["const:548ab0:8", "const:4:8"]]
- 00525c28 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00548ac0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00525c3c ["INT_ADD", "register:40f0:8", ["const:525c3c:8", "const:4:8"]]
+ 00548ad4 ["INT_ADD", "register:40f0:8", ["const:548ad4:8", "const:4:8"]]
~~~


### [`00525ce8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525ce8.md) → [`00548b80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548b80.md) FUN_00548b80

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`004df724`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df724.md) · 呼出先 7件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00525e44`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525e44.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`005025bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005025bc.md) · 呼出先 7件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548cdc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548cdc.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00548c08",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "old": {
      "definition_site": "00525d64",
      "incomplete_value": true,
      "site": "00525d70",
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
            "register:40b0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00548bb0",
      "incomplete_value": true,
      "site": "00548bb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "INT_RIGHT",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:3c:8"
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
      "definition_site": "00525d18",
      "incomplete_value": true,
      "site": "00525d18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "INT_RIGHT",
            "8",
            [
              [
                "live",
                "register:4040:8"
              ],
              [
                "leaf",
                "const:3c:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00525ddc",
      "incomplete_value": false,
      "site": "00525de0",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


~~~diff
- 00525d18 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00548bb0 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00525d44 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00548bdc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00525d4c ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
+ 00548be4 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
~~~


### [`00525e44`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525e44.md) → [`00548cdc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548cdc.md) FUN_00548cdc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 2件 [`005060a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/005060a8.md) [`00525ce8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525ce8.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00528f40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528f40.md) [`00548b80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548b80.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, cfg_edge_inventory, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00548cec",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00525e54",
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
    "new": null,
    "old": {
      "definition_site": "00525e50",
      "incomplete_value": false,
      "site": "00525e54",
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
- 00525e4c ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00525e50 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00548ce4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00548ce8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00525e54 ["INT_ADD", "register:40f0:8", ["const:525e54:8", "const:4:8"]]
- 00525e54 ["CALL", null, ["ram:418c38:8"]]
+ 00548cec ["INT_ADD", "register:40f0:8", ["const:548cec:8", "const:4:8"]]
+ 00548cec ["CALL", null, ["ram:43b738:8"]]
~~~


### [`00525ea0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525ea0.md) → [`00548d38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d38.md) FUN_00548d38

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`004dfd64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfd64.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00502bfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

### [`00525efc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525efc.md) → [`00548d94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d94.md) FUN_00548d94

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`004e0894`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0894.md) [`00525ed4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525ed4.md) · 呼出先 2件 [`0051854c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0050372c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md) [`00548d6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d6c.md) · 呼出先 2件 [`0053b3e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00548dbc",
      "incomplete_value": true,
      "site": "00548dbc",
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
      "definition_site": "00525f24",
      "incomplete_value": true,
      "site": "00525f24",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:40a0:8"
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
      "definition_site": "00548dcc",
      "incomplete_value": true,
      "site": "00548dcc",
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
      "definition_site": "00525f34",
      "incomplete_value": true,
      "site": "00525f34",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00548db0",
      "incomplete_value": true,
      "site": "00548db4",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00525f18",
      "incomplete_value": true,
      "site": "00525f1c",
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
            "const:68:8"
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
- 00525efc ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00548d94 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00525f1c ["INT_ADD", "register:40f0:8", ["const:525f1c:8", "const:4:8"]]
+ 00548db4 ["INT_ADD", "register:40f0:8", ["const:548db4:8", "const:4:8"]]
- 00525f24 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00548dbc ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
~~~


### [`00525f90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) → [`00548e28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) FUN_00548e28

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 10件 [`004c15a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c15a4.md) [`004e0038`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0038.md) [`004e40b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e40b8.md) [`004e7c0c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7c0c.md) [`004efe30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efe30.md) · 呼出先 5件 [`0047c554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 10件 [`004e443c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e443c.md) [`00502ed0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ed0.md) [`00506f50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md) [`0050aaa4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050aaa4.md) [`00512cc8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md) · 呼出先 5件 [`0049f3ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00548e2c",
      "incomplete_value": true,
      "site": "00548e2c",
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
      "definition_site": "00525f94",
      "incomplete_value": true,
      "site": "00525f94",
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
                "const:ffffffffffffffc0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00548f28",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "0052608c",
      "incomplete_value": true,
      "site": "00526090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "live",
            "register:40a0:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00548f14",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00526078",
      "incomplete_value": true,
      "site": "0052607c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
              ],
              [
                "live",
                "register:4008:8"
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
    "ordinal": 9,
    "slot": 0
  }
]
~~~


~~~diff
- 00525fd4 ["INT_ADD", "register:40f0:8", ["const:525fd4:8", "const:4:8"]]
+ 00548e6c ["INT_ADD", "register:40f0:8", ["const:548e6c:8", "const:4:8"]]
- 00525fe8 ["CBRANCH", null, ["local:b19:8", "tmp:3:1"]]
+ 00548e80 ["CBRANCH", null, ["local:b27:8", "tmp:3:1"]]
- 0052600c ["INT_ADD", "register:40f0:8", ["const:52600c:8", "const:4:8"]]
+ 00548ea4 ["INT_ADD", "register:40f0:8", ["const:548ea4:8", "const:4:8"]]
~~~


### [`005260b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005260b0.md) → [`00548f48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548f48.md) FUN_00548f48

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`004e0ec0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0ec0.md) · 呼出先 1件 [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00503d58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503d58.md) · 呼出先 1件 [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition

優先判定に残った影響 `branch_value` 3件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00548f6c",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "005260d0",
      "incomplete_value": true,
      "site": "005260d4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_AND",
            "4",
            [
              [
                "live",
                "register:4040:4"
              ],
              [
                "leaf",
                "const:1:4"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:4"
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
      "definition_site": "00548f74",
      "incomplete_value": true,
      "site": "00548f74",
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
      "definition_site": "005260dc",
      "incomplete_value": true,
      "site": "005260dc",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00549088",
      "incomplete_value": true,
      "site": "00549088",
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
      "definition_site": "005261f0",
      "incomplete_value": true,
      "site": "005261f0",
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
    "ordinal": 15,
    "slot": 0
  }
]
~~~


~~~diff
- 005260dc ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00548f74 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 005260f8 ["CBRANCH", null, ["local:b10:8", "tmp:3:1"]]
+ 00548f90 ["CBRANCH", null, ["local:b16:8", "tmp:3:1"]]
- 00526100 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00548f98 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
~~~


### [`005261fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005261fc.md) → [`00549094`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) FUN_00549094

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 5件 [`004dc2c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`004e105c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e105c.md) [`00540c2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540c2c.md) [`00560834`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560834.md) [`00562028`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562028.md) · 呼出先 3件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 5件 [`004ff160`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00503ef4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503ef4.md) [`00563ac4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md) [`005836cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005836cc.md) [`00584ec0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md) · 呼出先 3件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005490b8",
      "incomplete_value": true,
      "site": "005490e0",
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
            "register:40a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00526248",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005490c4",
      "incomplete_value": true,
      "site": "005490e4",
      "value": [
        "LOAD",
        "8",
        [
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
      "site": "0052624c",
      "value": [
        "live",
        "register:4048:8"
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005490c8",
      "incomplete_value": true,
      "site": "005490e8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00526250",
      "value": [
        "live",
        "register:5020:16"
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


~~~diff
- 0052621c ["INT_ADD", "register:40f0:8", ["const:52621c:8", "const:4:8"]]
+ 005490b4 ["INT_ADD", "register:40f0:8", ["const:5490b4:8", "const:4:8"]]
- 00526258 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 005490f0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00526278 ["BRANCH", null, ["local:b5:8"]]
+ 00549110 ["BRANCH", null, ["local:b3:8"]]
~~~


### [`00526340`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526340.md) → [`005491d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005491d8.md) FUN_005491d8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005491ec",
      "incomplete_value": false,
      "site": "005491f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00526354",
      "incomplete_value": false,
      "site": "00526358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
        "00bed8c0",
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
        "00c6a480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052634c ["INT_ADD", "register:40f0:8", ["const:52634c:8", "const:4:8"]]
+ 005491e4 ["INT_ADD", "register:40f0:8", ["const:5491e4:8", "const:4:8"]]
- 00526350 ["COPY", "register:4040:8", ["const:bed000:8"]]
- 00526354 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 005491e8 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 005491ec ["COPY", "tmp:0:8", ["const:480:8"]]
~~~


### [`00526364`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526364.md) → [`005491fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005491fc.md) FUN_005491fc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00549204",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "00526368",
      "incomplete_value": true,
      "site": "0052636c",
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
            "const:8c0:8"
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
        "00bed8c0",
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
        "00c6a480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00526364 ["COPY", "register:4040:8", ["const:bed000:8"]]
- 00526368 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 005491fc ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00549200 ["COPY", "tmp:0:8", ["const:480:8"]]
~~~


### [`0052637c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/0052637c.md) → [`00549214`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549214.md) FUN_00549214

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57bd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `branch_value` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00549288",
      "incomplete_value": true,
      "site": "00549288",
      "value": [
        "BOOL_AND",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ],
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SLESS",
              "INT_SBORROW"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005263f0",
      "incomplete_value": true,
      "site": "005263f0",
      "value": [
        "BOOL_AND",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ],
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SLESS",
              "INT_SBORROW"
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0054929c",
      "incomplete_value": true,
      "site": "005492ac",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 0
  }
]
~~~


~~~diff
- 005263ac ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00549244 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005263c8 ["INT_ADD", "register:40f0:8", ["const:5263c8:8", "const:4:8"]]
+ 00549260 ["INT_ADD", "register:40f0:8", ["const:549260:8", "const:4:8"]]
- 005263cc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00549264 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
~~~


### [`00526448`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526448.md) → [`005492e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005492e0.md) FUN_005492e0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005492f4",
      "incomplete_value": false,
      "site": "005492f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052645c",
      "incomplete_value": false,
      "site": "00526460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
    "new": null,
    "old": {
      "definition_site": "00526450",
      "incomplete_value": false,
      "site": "00526454",
      "value": [
        "leaf",
        "const:10:8"
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
      24,
      "DATA",
      [
        "storage",
        "00bed950",
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
        "00c6a510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00526454 ["INT_ADD", "register:40f0:8", ["const:526454:8", "const:4:8"]]
+ 005492ec ["INT_ADD", "register:40f0:8", ["const:5492ec:8", "const:4:8"]]
- 00526458 ["COPY", "register:4040:8", ["const:bed000:8"]]
- 0052645c ["COPY", "tmp:0:8", ["const:950:8"]]
+ 005492f0 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 005492f4 ["COPY", "tmp:0:8", ["const:510:8"]]
~~~


### [`0052646c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/0052646c.md) → [`00549304`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549304.md) FUN_00549304

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
      "definition_site": "00549308",
      "incomplete_value": true,
      "site": "0054930c",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00526474",
      "value": [
        "live",
        "register:4040:8"
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
        "00bed950",
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
        "00c6a510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052646c ["COPY", "register:4040:8", ["const:bed000:8"]]
- 00526470 ["COPY", "tmp:0:8", ["const:950:8"]]
+ 00549304 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00549308 ["COPY", "tmp:0:8", ["const:510:8"]]
~~~


### [`00526484`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526484.md) → [`0054931c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/0054931c.md) FUN_0054931c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `branch_value` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00549358",
      "incomplete_value": true,
      "site": "00549358",
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
      "definition_site": "005264c0",
      "incomplete_value": true,
      "site": "005264c0",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_AND",
              [
                "leaf",
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00526540",
      "incomplete_value": false,
      "site": "00526544",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


~~~diff
- 0052649c ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 00549334 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 005264a4 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 0054933c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 005264ac ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00549344 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
~~~


### [`005265bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005265bc.md) → [`00549454`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549454.md) FUN_00549454

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_value

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00549460",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "005265c4",
      "incomplete_value": true,
      "site": "005265c8",
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
      4,
      "READ",
      [
        "storage",
        "00c1b340",
        null,
        "pointer"
      ]
    ],
    [
      12,
      "DATA",
      [
        "storage",
        "00bed9d0",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      4,
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ],
    [
      12,
      "DATA",
      [
        "storage",
        "00c6a590",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005265bc ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 005265c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:340:8"]]
+ 00549454 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00549458 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d30:8"]]
~~~


### [`005265e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005265e0.md) → [`00549478`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549478.md) FUN_00549478

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, local_def_use, operands_and_dependencies

~~~diff
- 005265f0 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
+ 00549488 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
~~~


### [`00526628`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526628.md) → [`005494c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005494c0.md) FUN_005494c0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`004e4494`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md) · 呼出先 1件 [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0050732c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) · 呼出先 1件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 7件, `call_target` 5件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005494cc",
      "incomplete_value": true,
      "site": "005494cc",
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
      "definition_site": "00526634",
      "incomplete_value": true,
      "site": "00526634",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005494cc",
      "incomplete_value": true,
      "site": "005494cc",
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
      "definition_site": "00526634",
      "incomplete_value": true,
      "site": "00526634",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005494e0",
      "incomplete_value": true,
      "site": "005494e0",
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
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00526648",
      "incomplete_value": true,
      "site": "00526648",
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


~~~diff
- 0052664c ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 005494e4 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00526664 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00526668 ["INT_LESSEQUAL", "register:105:1", ["register:4098:8", "register:4048:8"]]
- 00526668 ["INT_SBORROW", "register:106:1", ["register:4048:8", "register:4098:8"]]
- 00526668 ["INT_SUB", "tmp:0:8", ["register:4048:8", "register:4098:8"]]
+ 005494fc ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00549508 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:20:8"]]
+ 00549508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0054950c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:20:8"]]
+ 0054950c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
~~~


### [`00526790`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526790.md) → [`00549628`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) FUN_00549628

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`004deb5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deb5c.md) [`004e50d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md) [`004f1c30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1c30.md) [`004f1ecc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1ecc.md) [`00503af8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md) · 呼出先 2件 [`00526790`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526790.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 6件 [`005019f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005019f4.md) [`00507f68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md) [`00514ac8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514ac8.md) [`00514d64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md) [`00526990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md) · 呼出先 2件 [`00549628`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005267a4",
      "incomplete_value": true,
      "site": "005267ac",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 0,
    "slot": 2
  }
]
~~~


~~~diff
- 00526790 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00549628 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 005267ac ["INT_ADD", "register:40f0:8", ["const:5267ac:8", "const:4:8"]]
+ 00549644 ["INT_ADD", "register:40f0:8", ["const:549644:8", "const:4:8"]]
- 005267b8 ["INT_ADD", "register:40f0:8", ["const:5267b8:8", "const:4:8"]]
+ 00549650 ["INT_ADD", "register:40f0:8", ["const:549650:8", "const:4:8"]]
~~~


### [`005267f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005267f0.md) → [`00549688`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549688.md) FUN_00549688

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`004e50d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00507f68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00549690",
      "incomplete_value": true,
      "site": "00549690",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4068:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005267f8",
      "incomplete_value": true,
      "site": "005267f8",
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
      "definition_site": "005496b0",
      "incomplete_value": true,
      "site": "005496b0",
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
                "register:4068:8"
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
      "definition_site": "00526818",
      "incomplete_value": true,
      "site": "00526818",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4068:8"
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
      "definition_site": "00549700",
      "incomplete_value": true,
      "site": "00549700",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              [
                "live",
                "register:102:1"
              ]
            ]
          ],
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00526868",
      "incomplete_value": true,
      "site": "00526868",
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
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


~~~diff
- 005267f8 ["CBRANCH", null, ["local:b47:8", "tmp:0:1"]]
+ 00549690 ["CBRANCH", null, ["local:b62:8", "tmp:0:1"]]
- 0052680c ["BRANCH", null, ["local:b5:8"]]
+ 005496a4 ["BRANCH", null, ["local:b4:8"]]
- 00526818 ["CBRANCH", null, ["local:b47:8", "tmp:0:1"]]
+ 005496b0 ["CBRANCH", null, ["local:b62:8", "tmp:0:1"]]
~~~


### [`005269b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005269b0.md) → [`00549848`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md) FUN_00549848

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`004e7fa0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7fa0.md) · 呼出先 8件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0051d764`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d764.md) [`00526bb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526bb4.md) [`00526cf8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526cf8.md) [`00526ee4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526ee4.md)
- 新版 呼出元 1件 [`0050ae38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md) · 呼出先 8件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005405fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005405fc.md) [`00549a4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md) [`00549b90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549b90.md) [`00549d7c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d7c.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_destination, store_value

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00549878",
      "incomplete_value": true,
      "site": "00549878",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005269e0",
      "incomplete_value": true,
      "site": "005269e0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0054992c",
      "incomplete_value": true,
      "site": "0054992c",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": {
      "definition_site": "00526a94",
      "incomplete_value": true,
      "site": "00526a94",
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:f8:8"
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
      "definition_site": "0054992c",
      "incomplete_value": true,
      "site": "0054992c",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": {
      "definition_site": "00526a94",
      "incomplete_value": true,
      "site": "00526a94",
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:f8:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      212,
      "READ",
      [
        "storage",
        "00c1b370",
        null,
        "pointer"
      ]
    ],
    [
      240,
      "DATA",
      [
        "storage",
        "00becac0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      272,
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      212,
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ],
    [
      240,
      "DATA",
      [
        "storage",
        "00c69680",
        null,
        "undefined1[48]"
      ]
    ],
    [
      272,
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00526a10 ["CBRANCH", null, ["local:b20:8", "tmp:1:1"]]
+ 005498a8 ["CBRANCH", null, ["local:b17:8", "tmp:1:1"]]
- 00526a54 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 005498ec ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00526a5c ["CBRANCH", null, ["local:b22:8", "tmp:1:1"]]
+ 005498f4 ["CBRANCH", null, ["local:b19:8", "tmp:1:1"]]
~~~


### [`00526bb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526bb4.md) → [`00549a4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md) FUN_00549a4c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 3件 [`004e7fa0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7fa0.md) [`005269b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005269b0.md) [`00526cf8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526cf8.md) · 呼出先 5件 [`0047c554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`005137dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005137dc.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdbcf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md)
- 新版 呼出元 3件 [`0050ae38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md) [`00549848`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md) [`00549b90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549b90.md) · 呼出先 5件 [`0049f3ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00536674`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536674.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c58740`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 9件, `call_target` 1件, `store_destination` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00549a80",
      "incomplete_value": true,
      "site": "00549a80",
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
      "definition_site": "00526be8",
      "incomplete_value": true,
      "site": "00526be8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00549a94",
      "incomplete_value": true,
      "site": "00549a94",
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "00526bfc",
      "incomplete_value": true,
      "site": "00526bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "00549ab0",
      "incomplete_value": true,
      "site": "00549ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "live",
            "register:40c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00526c28",
      "value": [
        "live",
        "register:40c8:8"
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
        "00c1b378",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00bea858",
        null,
        "undefined1[48]"
      ]
    ],
    [
      200,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "00c9ad68",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00c67418",
        null,
        "undefined1[48]"
      ]
    ],
    [
      200,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ]
  ]
}
~~~


~~~diff
- 00526bcc ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00549a64 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00526bd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
+ 00549a70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d68:8"]]
- 00526bf0 ["INT_ADD", "register:40f0:8", ["const:526bf0:8", "const:4:8"]]
+ 00549a88 ["INT_ADD", "register:40f0:8", ["const:549a88:8", "const:4:8"]]
~~~


### [`00526cf8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526cf8.md) → [`00549b90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549b90.md) FUN_00549b90

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`005269b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005269b0.md) · 呼出先 3件 [`0051d764`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d764.md) [`00526bb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526bb4.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00549848`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md) · 呼出先 3件 [`005405fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005405fc.md) [`00549a4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00549bc8",
      "incomplete_value": true,
      "site": "00549bc8",
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
      "definition_site": "00526d30",
      "incomplete_value": true,
      "site": "00526d30",
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
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00549bc8",
      "incomplete_value": true,
      "site": "00549bc8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00526d30",
      "incomplete_value": true,
      "site": "00526d30",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00549bd8",
      "incomplete_value": true,
      "site": "00549bd8",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00526d40",
      "incomplete_value": true,
      "site": "00526d40",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "READ",
      [
        "storage",
        "00c1b370",
        null,
        "pointer"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      140,
      "DATA",
      [
        "storage",
        "00becac0",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      112,
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ],
    [
      140,
      "DATA",
      [
        "storage",
        "00c69680",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00526d58 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
+ 00549bf0 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00526d60 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 00526d64 ["COPY", "register:4048:8", ["const:c1a000:8"]]
- 00526d68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 00549bf8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00549bfc ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00549c00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
- 00526d6c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
+ 00549c04 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b0:8"]]
~~~


### [`00526e8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526e8c.md) → [`00549d24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d24.md) FUN_00549d24

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d764`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d764.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005405fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005405fc.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00549d3c",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00526ea0",
      "incomplete_value": true,
      "site": "00526ea4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00526ea8",
      "incomplete_value": true,
      "site": "00526eb4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:20:8"
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
    "new": null,
    "old": {
      "definition_site": "00526eac",
      "incomplete_value": true,
      "site": "00526eb4",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


~~~diff
- 00526ea4 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00549d3c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00526eb4 ["INT_ADD", "register:40f0:8", ["const:526eb4:8", "const:4:8"]]
+ 00549d4c ["INT_ADD", "register:40f0:8", ["const:549d4c:8", "const:4:8"]]
- 00526ec0 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
+ 00549d58 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
~~~


### [`00526ee4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526ee4.md) → [`00549d7c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d7c.md) FUN_00549d7c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005269b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005269b0.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00549848`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00549d8c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00526ef4",
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
      "definition_site": "00549d88",
      "incomplete_value": false,
      "site": "00549d8c",
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
      "definition_site": "00526ef0",
      "incomplete_value": false,
      "site": "00526ef4",
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
- 00526eec ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00526ef0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00549d84 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00549d88 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00526ef4 ["INT_ADD", "register:40f0:8", ["const:526ef4:8", "const:4:8"]]
- 00526ef4 ["CALL", null, ["ram:418c38:8"]]
+ 00549d8c ["INT_ADD", "register:40f0:8", ["const:549d8c:8", "const:4:8"]]
+ 00549d8c ["CALL", null, ["ram:43b738:8"]]
~~~


### [`00526ef8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526ef8.md) → [`00549d90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d90.md) FUN_00549d90

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0051d764`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d764.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005405fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005405fc.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00549dbc",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00526f20",
      "incomplete_value": true,
      "site": "00526f24",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 1,
    "slot": 0
  }
]
~~~


~~~diff
- 00526f24 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00549dbc ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00526f38 ["INT_ADD", "register:40f0:8", ["const:526f38:8", "const:4:8"]]
+ 00549dd0 ["INT_ADD", "register:40f0:8", ["const:549dd0:8", "const:4:8"]]
- 00526f40 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00549dd8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
~~~


### [`00526f54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526f54.md) → [`00549dec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md) FUN_00549dec

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`004e82ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e82ac.md) · 呼出先 5件 [`0051854c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`005271dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005271dc.md) [`00527320`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527320.md) [`005273ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005273ec.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0050b144`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b144.md) · 呼出先 5件 [`0053b3e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`0054a074`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a074.md) [`0054a1b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a1b8.md) [`0054a284`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a284.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 2件, `store_condition` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00549e18",
      "incomplete_value": true,
      "site": "00549e18",
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
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00526f80",
      "incomplete_value": true,
      "site": "00526f80",
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
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00549e68",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00526fcc",
      "incomplete_value": true,
      "site": "00526fd0",
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
                "register:4008:8"
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00549f20",
      "incomplete_value": true,
      "site": "00549f20",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00527088",
      "incomplete_value": true,
      "site": "00527088",
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
    "ordinal": 17,
    "slot": 0
  }
]
~~~


~~~diff
- 00526f88 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
+ 00549e20 ["CBRANCH", null, ["local:b46:8", "tmp:0:1"]]
- 00526fbc ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00549e54 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00526fc4 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00549e5c ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
~~~


### [`005271dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005271dc.md) → [`0054a074`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a074.md) FUN_0054a074

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00526f54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526f54.md) · 呼出先 1件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md)
- 新版 呼出元 1件 [`00549dec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md) · 呼出先 1件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md)

変更の種類 branch_condition_or_target, branch_value, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_value

優先判定に残った影響 `branch_value` 3件, `return_value_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054a14c",
      "incomplete_value": true,
      "site": "0054a150",
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
      "definition_site": "005272b4",
      "incomplete_value": true,
      "site": "005272b8",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054a0b0",
      "incomplete_value": true,
      "site": "0054a0b0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4068:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00527218",
      "incomplete_value": true,
      "site": "00527218",
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
                "register:4040:8"
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
      "definition_site": "0054a0c8",
      "incomplete_value": true,
      "site": "0054a0c8",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              [
                "live",
                "register:4070:8"
              ],
              [
                "live",
                "register:4058:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00527230",
      "incomplete_value": true,
      "site": "00527230",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              "INT_SRIGHT",
              [
                "live",
                "register:4058:8"
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


~~~diff
- 005271f8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 0054a090 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 0052720c ["BRANCH", null, ["local:b3:8"]]
+ 0054a0a4 ["BRANCH", null, ["local:b4:8"]]
- 00527218 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 0054a0b0 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
~~~


### [`005272c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005272c8.md) → [`0054a160`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a160.md) FUN_0054a160

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0051854c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0053b3e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005272d8",
      "incomplete_value": true,
      "site": "005272e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4000:8"
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
      "definition_site": "0054a174",
      "incomplete_value": true,
      "site": "0054a178",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005272dc",
      "incomplete_value": true,
      "site": "005272e0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


~~~diff
- 005272e0 ["INT_ADD", "register:40f0:8", ["const:5272e0:8", "const:4:8"]]
+ 0054a178 ["INT_ADD", "register:40f0:8", ["const:54a178:8", "const:4:8"]]
- 005272e8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0054a180 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 005272f0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0054a188 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
~~~


### [`00527320`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527320.md) → [`0054a1b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a1b8.md) FUN_0054a1b8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00526f54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526f54.md) · 呼出先 5件 [`005192a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/005192a0.md) [`00525f90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00549dec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md) · 呼出先 5件 [`0053c138`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md) [`00548e28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 6件, `store_destination` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054a1bc",
      "incomplete_value": true,
      "site": "0054a1bc",
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
      "definition_site": "00527324",
      "incomplete_value": true,
      "site": "00527324",
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
                "const:ffffffffffffffb0:8"
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
      "definition_site": "0054a1c0",
      "incomplete_value": true,
      "site": "0054a1c0",
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
      "definition_site": "00527328",
      "incomplete_value": true,
      "site": "00527328",
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
                "const:ffffffffffffffb0:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054a1c0",
      "incomplete_value": true,
      "site": "0054a1c0",
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
      "definition_site": "00527328",
      "incomplete_value": true,
      "site": "00527328",
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
    "ordinal": 4,
    "slot": 1
  }
]
~~~


~~~diff
- 00527348 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 0054a1e0 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 0052735c ["INT_ADD", "register:40f0:8", ["const:52735c:8", "const:4:8"]]
+ 0054a1f4 ["INT_ADD", "register:40f0:8", ["const:54a1f4:8", "const:4:8"]]
- 0052736c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0054a204 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
~~~


### [`005273ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005273ec.md) → [`0054a284`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a284.md) FUN_0054a284

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00526f54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526f54.md) · 呼出先 4件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004f45b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f45b0.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00549dec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md) · 呼出先 4件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00517448`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517448.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054a2fc",
      "incomplete_value": true,
      "site": "0054a2fc",
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
                "register:40b8:8"
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
      "definition_site": "00527464",
      "incomplete_value": true,
      "site": "00527464",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4060:8"
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
      "definition_site": "0054a314",
      "incomplete_value": true,
      "site": "0054a314",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              "INT_SRIGHT",
              [
                "live",
                "register:4050:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052747c",
      "incomplete_value": true,
      "site": "0052747c",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              "INT_SRIGHT",
              [
                "live",
                "register:4050:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0054a370",
      "incomplete_value": true,
      "site": "0054a370",
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
    "old": {
      "definition_site": "005274d8",
      "incomplete_value": true,
      "site": "005274d8",
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
                "register:4040:8"
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
    "ordinal": 9,
    "slot": 0
  }
]
~~~


~~~diff
- 00527420 ["INT_ADD", "register:40f0:8", ["const:527420:8", "const:4:8"]]
+ 0054a2b8 ["INT_ADD", "register:40f0:8", ["const:54a2b8:8", "const:4:8"]]
- 00527438 ["INT_ADD", "register:40f0:8", ["const:527438:8", "const:4:8"]]
+ 0054a2d0 ["INT_ADD", "register:40f0:8", ["const:54a2d0:8", "const:4:8"]]
- 00527444 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 0054a2dc ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
~~~


### [`00527554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527554.md) → [`0054a3ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a3ec.md) FUN_0054a3ec

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`004eb16c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb16c.md) [`004ec194`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec194.md) [`005278b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005278b4.md) · 呼出先 4件 [`0044a5b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`0051854c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0050e004`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) [`0050f02c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f02c.md) [`0054a74c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a74c.md) · 呼出先 4件 [`0046d450`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053b3e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054a3f4",
      "incomplete_value": true,
      "site": "0054a3f4",
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
                "const:ffffffffffffffd0:8"
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
      "definition_site": "0052755c",
      "incomplete_value": true,
      "site": "0052755c",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054a3f4",
      "incomplete_value": true,
      "site": "0054a3f4",
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
      "definition_site": "0052755c",
      "incomplete_value": true,
      "site": "0052755c",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054a438",
      "incomplete_value": true,
      "site": "0054a438",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005275a0",
      "incomplete_value": true,
      "site": "005275a0",
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
    "ordinal": 3,
    "slot": 0
  }
]
~~~


~~~diff
- 00527570 ["INT_ADD", "register:40f0:8", ["const:527570:8", "const:4:8"]]
+ 0054a408 ["INT_ADD", "register:40f0:8", ["const:54a408:8", "const:4:8"]]
- 00527578 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 0054a410 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00527588 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0052758c ["BRANCH", null, ["local:b10:8"]]
+ 0054a420 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0054a424 ["BRANCH", null, ["local:b8:8"]]
~~~


### [`0052761c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052761c.md) → [`0054a4b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a4b4.md) FUN_0054a4b4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`004eb16c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb16c.md) [`0050645c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/0050645c.md) [`00506ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) [`00b58dc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58dc4.md) · 呼出先 5件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0052773c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052773c.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`0050e004`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) [`005292f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md) [`00529d78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) [`00bc82c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc82c4.md) · 呼出先 5件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054a5d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054a520",
      "incomplete_value": true,
      "site": "0054a528",
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
            "register:40a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00527690",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054a52c",
      "incomplete_value": true,
      "site": "0054a52c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00527694",
      "incomplete_value": true,
      "site": "00527694",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054a540",
      "incomplete_value": true,
      "site": "0054a54c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:8:8"
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
      "site": "005276b4",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


~~~diff
- 00527650 ["INT_ADD", "register:40f0:8", ["const:527650:8", "const:4:8"]]
+ 0054a4e8 ["INT_ADD", "register:40f0:8", ["const:54a4e8:8", "const:4:8"]]
- 00527660 ["BRANCH", null, ["local:b22:8"]]
+ 0054a4f8 ["BRANCH", null, ["local:b9:8"]]
- 00527670 ["INT_ADD", "register:40f0:8", ["const:527670:8", "const:4:8"]]
+ 0054a508 ["INT_ADD", "register:40f0:8", ["const:54a508:8", "const:4:8"]]
~~~


### [`0052773c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052773c.md) → [`0054a5d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) FUN_0054a5d4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 5件 [`00509ac0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509ac0.md) [`0050a3ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a3ac.md) [`0052761c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052761c.md) [`00b26b28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26b28.md) [`00b284c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b284c4.md) · 呼出先 1件 [`00bdb200`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 9件 [`0052c958`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c958.md) [`0052d244`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d244.md) [`0054a4b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a4b4.md) [`00b6eebc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eebc.md) [`00b82890`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82890.md) · 呼出先 1件 [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054a5dc",
      "incomplete_value": true,
      "site": "0054a5dc",
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
      "definition_site": "00527744",
      "incomplete_value": true,
      "site": "00527744",
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
                "const:ffffffffffffffb0:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054a5dc",
      "incomplete_value": true,
      "site": "0054a5dc",
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
      "definition_site": "00527744",
      "incomplete_value": true,
      "site": "00527744",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054a5e0",
      "incomplete_value": true,
      "site": "0054a5e0",
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
      "definition_site": "00527748",
      "incomplete_value": true,
      "site": "00527748",
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
                "const:ffffffffffffffb0:8"
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
    "ordinal": 6,
    "slot": 1
  }
]
~~~


~~~diff
- 00527760 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 0054a5f8 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 0052777c ["BRANCH", null, ["local:b4:8"]]
+ 0054a614 ["BRANCH", null, ["local:b5:8"]]
- 00527788 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 0054a620 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
~~~


### [`00527840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527840.md) → [`0054a6d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a6d8.md) FUN_0054a6d8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054a6e4",
      "incomplete_value": true,
      "site": "0054a6e4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052784c",
      "incomplete_value": true,
      "site": "0052784c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00527874",
      "incomplete_value": true,
      "site": "00527878",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:30:8"
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
- 0052784c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0054a6e4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00527854 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0054a6ec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0052785c ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
+ 0054a6f4 ["CBRANCH", null, ["local:b7:8", "tmp:3:1"]]
~~~


### [`0052790c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052790c.md) → [`0054a7a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a7a4.md) FUN_0054a7a4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`004ecb70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ecb70.md) · 呼出先 5件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a6d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0050fa08`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md) · 呼出先 5件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d568`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 2件, `store_condition` 4件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054a7ac",
      "incomplete_value": true,
      "site": "0054a7ac",
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
      "definition_site": "00527914",
      "incomplete_value": true,
      "site": "00527914",
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
            "const:40:8"
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
      "definition_site": "0054a7ac",
      "incomplete_value": true,
      "site": "0054a7ac",
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
      "definition_site": "00527914",
      "incomplete_value": true,
      "site": "00527914",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054a7b0",
      "incomplete_value": true,
      "site": "0054a7b0",
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
      "definition_site": "00527918",
      "incomplete_value": true,
      "site": "00527918",
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
    "ordinal": 4,
    "slot": 1
  }
]
~~~


~~~diff
- 00527940 ["INT_ADD", "register:40f0:8", ["const:527940:8", "const:4:8"]]
+ 0054a7d8 ["INT_ADD", "register:40f0:8", ["const:54a7d8:8", "const:4:8"]]
- 00527948 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0054a7e0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00527950 ["BRANCH", null, ["local:b10:8"]]
+ 0054a7e8 ["BRANCH", null, ["local:b14:8"]]
~~~


### [`00527a44`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527a44.md) → [`0054a8dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a8dc.md) FUN_0054a8dc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`004eef84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eef84.md) · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00511e1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511e1c.md) · 呼出先 3件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054a928",
      "incomplete_value": true,
      "site": "0054a928",
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
      "definition_site": "00527a90",
      "incomplete_value": true,
      "site": "00527a90",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054a934",
      "incomplete_value": true,
      "site": "0054a938",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_SUB",
              [
                "live",
                "register:40b0:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00527aa0",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


~~~diff
- 00527a5c ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
+ 0054a8f4 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
- 00527a90 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00527a94 ["BRANCH", null, ["local:b13:8"]]
+ 0054a928 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 0054a92c ["BRANCH", null, ["local:b12:8"]]
- 00527aa0 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 0054a938 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
~~~


### [`00527b1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527b1c.md) → [`0054a9b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a9b4.md) FUN_0054a9b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00527b74`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527b74.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054aa0c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054aa0c.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00527b30",
      "incomplete_value": true,
      "site": "00527b34",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


~~~diff
- 00527b2c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0054a9c4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00527b34 ["INT_ADD", "register:40f0:8", ["const:527b34:8", "const:4:8"]]
+ 0054a9cc ["INT_ADD", "register:40f0:8", ["const:54a9cc:8", "const:4:8"]]
~~~


### [`00527b74`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527b74.md) → [`0054aa0c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054aa0c.md) FUN_0054aa0c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 3件 [`004f03d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md) [`004f0f3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f0f3c.md) [`00527b1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527b1c.md) · 呼出先 5件 [`005180b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`0051854c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00513270`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md) [`00513dd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513dd4.md) [`0054a9b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a9b4.md) · 呼出先 5件 [`0053af50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053b3e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054aa14",
      "incomplete_value": true,
      "site": "0054aa14",
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
      "definition_site": "00527b7c",
      "incomplete_value": true,
      "site": "00527b7c",
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
                "const:ffffffffffffffd0:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054aa14",
      "incomplete_value": true,
      "site": "0054aa14",
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
      "definition_site": "00527b7c",
      "incomplete_value": true,
      "site": "00527b7c",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054aaa8",
      "incomplete_value": true,
      "site": "0054aaa8",
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
      "definition_site": "00527c10",
      "incomplete_value": true,
      "site": "00527c10",
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
    "ordinal": 7,
    "slot": 0
  }
]
~~~


~~~diff
- 00527b8c ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
+ 0054aa24 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
- 00527b94 ["INT_ADD", "register:40f0:8", ["const:527b94:8", "const:4:8"]]
+ 0054aa2c ["INT_ADD", "register:40f0:8", ["const:54aa2c:8", "const:4:8"]]
- 00527b9c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0054aa34 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
~~~


### [`00527c8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527c8c.md) → [`0054ab24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054ab24.md) FUN_0054ab24

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`004efe30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efe30.md) · 呼出先 6件 [`0051a4c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a4c0.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00512cc8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md) · 呼出先 6件 [`0053d358`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d358.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 7件, `call_argument_candidate` 4件, `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054ad38",
      "incomplete_value": true,
      "site": "0054ad40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "live",
            "register:40b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00527ea8",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054ad6c",
      "incomplete_value": true,
      "site": "0054ad6c",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "00527ed4",
      "incomplete_value": true,
      "site": "00527ed4",
      "value": [
        "live",
        "register:4048:8"
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054ad68",
      "incomplete_value": true,
      "site": "0054ad70",
      "value": [
        "LOAD",
        "8",
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
      "site": "00527ed8",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      552,
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      584,
      "DATA",
      [
        "storage",
        "00bea828",
        null,
        "undefined1[48]"
      ]
    ],
    [
      648,
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      552,
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      584,
      "DATA",
      [
        "storage",
        "00c673e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      648,
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00527cd4 ["CBRANCH", null, ["local:b11:8", "register:102:1"]]
+ 0054ab6c ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
- 00527cd8 ["CBRANCH", null, ["local:b35:8", "tmp:0:1"]]
+ 0054ab70 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 00527cec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00527cf0 ["BRANCH", null, ["local:b34:8"]]
+ 0054ab84 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0054ab88 ["BRANCH", null, ["local:b27:8"]]
~~~


### [`00527fd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527fd4.md) → [`0054ae6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054ae6c.md) FUN_0054ae6c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`004f11e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f11e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00514078`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514078.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054aee4",
      "incomplete_value": true,
      "site": "0054aee4",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              [
                "live",
                "register:102:1"
              ]
            ]
          ],
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052804c",
      "incomplete_value": true,
      "site": "0052804c",
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
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054afd0",
      "incomplete_value": true,
      "site": "0054afd0",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              "INT_SRIGHT",
              [
                "live",
                "register:4058:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528138",
      "incomplete_value": true,
      "site": "00528138",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:102:1"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 0
  }
]
~~~


~~~diff
- 00528018 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 0054aeb0 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00528020 ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
+ 0054aeb8 ["CBRANCH", null, ["local:b11:8", "tmp:1:1"]]
- 00528040 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 0054aed8 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
~~~


### [`00528194`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528194.md) → [`0054b02c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b02c.md) FUN_0054b02c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`004e5c34`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5c34.md) · 呼出先 2件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00508acc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508acc.md) · 呼出先 2件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `return_value_candidate` 1件, `store_condition` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054b07c",
      "incomplete_value": true,
      "site": "0054b07c",
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
      "definition_site": "005281e4",
      "incomplete_value": true,
      "site": "005281e4",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054b07c",
      "incomplete_value": true,
      "site": "0054b07c",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "005281e4",
      "incomplete_value": true,
      "site": "005281e4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054b148",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "005282ac",
      "incomplete_value": true,
      "site": "005282b0",
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
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005281b0 ["INT_ADD", "register:40f0:8", ["const:5281b0:8", "const:4:8"]]
+ 0054b048 ["INT_ADD", "register:40f0:8", ["const:54b048:8", "const:4:8"]]
- 005281c0 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 0054b058 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 005281cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f50:8"]]
+ 0054b064 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:940:8"]]
~~~


### [`005282c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005282c4.md) → [`0054b15c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b15c.md) FUN_0054b15c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`004e5c34`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5c34.md) · 呼出先 6件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00508acc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508acc.md) · 呼出先 6件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054b194",
      "incomplete_value": true,
      "site": "0054b198",
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
      "definition_site": "005282fc",
      "incomplete_value": true,
      "site": "00528300",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054b19c",
      "incomplete_value": true,
      "site": "0054b1a0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4048:8"
              ],
              [
                "live",
                "register:40b0:8"
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
      "definition_site": "00528304",
      "incomplete_value": true,
      "site": "00528308",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      40,
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005282e0 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0054b178 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005282ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 0054b184 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 00528308 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 0054b1a0 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
~~~


### [`0052839c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/0052839c.md) → [`0054b234`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b234.md) FUN_0054b234

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`004e4f2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4f2c.md) [`004f1650`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1650.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00507dc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507dc4.md) [`005144e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005144e8.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054b25c",
      "incomplete_value": true,
      "site": "0054b25c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4068:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005283c4",
      "incomplete_value": true,
      "site": "005283c4",
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
                "register:4068:8"
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
      "definition_site": "0054b2ac",
      "incomplete_value": true,
      "site": "0054b2ac",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              [
                "live",
                "register:102:1"
              ]
            ]
          ],
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528414",
      "incomplete_value": true,
      "site": "00528414",
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
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054b330",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00528494",
      "incomplete_value": true,
      "site": "00528498",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4088:8"
              ],
              [
                "live",
                "register:4078:8"
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
    "ordinal": 17,
    "slot": 0
  }
]
~~~


~~~diff
- 005283a4 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
+ 0054b23c ["CBRANCH", null, ["local:b44:8", "tmp:0:1"]]
- 005283b8 ["BRANCH", null, ["local:b3:8"]]
+ 0054b250 ["BRANCH", null, ["local:b4:8"]]
- 005283c4 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
+ 0054b25c ["CBRANCH", null, ["local:b44:8", "tmp:0:1"]]
~~~


### [`0052855c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/0052855c.md) → [`0054b3f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b3f4.md) FUN_0054b3f4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`004f25dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f25dc.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00515474`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `branch_value` 4件, `return_value_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054b4e4",
      "incomplete_value": true,
      "site": "0054b4e8",
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
                "const:2:8"
              ]
            ]
          ],
          [
            "INT_SRIGHT",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052864c",
      "incomplete_value": true,
      "site": "00528650",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
          [
            "INT_SRIGHT",
            "8",
            [
              [
                "live",
                "register:4088:8"
              ],
              [
                "leaf",
                "const:2:8"
              ]
            ]
          ],
          [
            "live",
            "register:4078:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054b5a8",
      "incomplete_value": true,
      "site": "0054b5a8",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              [
                "live",
                "register:102:1"
              ]
            ]
          ],
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528710",
      "incomplete_value": true,
      "site": "00528710",
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
    "ordinal": 29,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054b5e8",
      "incomplete_value": true,
      "site": "0054b5e8",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              [
                "live",
                "register:102:1"
              ]
            ]
          ],
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528750",
      "incomplete_value": true,
      "site": "00528750",
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
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 0
  }
]
~~~


~~~diff
- 005285f0 ["CBRANCH", null, ["local:b53:8", "tmp:1:1"]]
+ 0054b488 ["CBRANCH", null, ["local:b52:8", "tmp:1:1"]]
- 005285fc ["CBRANCH", null, ["local:b59:8", "tmp:0:1"]]
+ 0054b494 ["CBRANCH", null, ["local:b60:8", "tmp:0:1"]]
- 00528618 ["BRANCH", null, ["local:b23:8"]]
+ 0054b4b0 ["BRANCH", null, ["local:b22:8"]]
~~~


### [`005288f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005288f8.md) → [`0054b790`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b790.md) FUN_0054b790

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f25dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f25dc.md) · 呼出先 6件 [`00512c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`005289d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005289d0.md) [`00bd70ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00515474`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md) · 呼出先 6件 [`00535b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0054b868`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b868.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054b7d4",
      "incomplete_value": true,
      "site": "0054b7e0",
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
      "definition_site": "0052893c",
      "incomplete_value": true,
      "site": "00528948",
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
      52,
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      52,
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052891c ["INT_ADD", "register:40f0:8", ["const:52891c:8", "const:4:8"]]
+ 0054b7b4 ["INT_ADD", "register:40f0:8", ["const:54b7b4:8", "const:4:8"]]
- 00528924 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0054b7bc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0052892c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 0054b7c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
~~~


### [`005289d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005289d0.md) → [`0054b868`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b868.md) FUN_0054b868

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`005288f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005288f8.md) · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054b790`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b790.md) · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

~~~diff
- 005289e4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0054b87c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 005289fc ["INT_ADD", "register:40f0:8", ["const:5289fc:8", "const:4:8"]]
+ 0054b894 ["INT_ADD", "register:40f0:8", ["const:54b894:8", "const:4:8"]]
~~~


### [`00528a1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a1c.md) → [`0054b8b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b8b4.md) FUN_0054b8b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`004f26f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f26f8.md) [`00528a1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a1c.md) · 呼出先 2件 [`00528a1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a1c.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00515590`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515590.md) [`0054b8b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b8b4.md) · 呼出先 2件 [`0054b8b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b8b4.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054b8d8",
      "incomplete_value": true,
      "site": "0054b8dc",
      "value": [
        "live",
        "register:40a0:8"
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
      "definition_site": "0054b8d4",
      "incomplete_value": true,
      "site": "0054b8dc",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


~~~diff
- 00528a1c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0054b8b4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00528a38 ["INT_ADD", "register:40f0:8", ["const:528a38:8", "const:4:8"]]
+ 0054b8d0 ["INT_ADD", "register:40f0:8", ["const:54b8d0:8", "const:4:8"]]
- 00528a44 ["INT_ADD", "register:40f0:8", ["const:528a44:8", "const:4:8"]]
+ 0054b8dc ["INT_ADD", "register:40f0:8", ["const:54b8dc:8", "const:4:8"]]
~~~


### [`00528a6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a6c.md) → [`0054b904`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md) FUN_0054b904

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 6件 [`004e01ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e01ec.md) [`004ee4f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md) [`004f4778`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4778.md) [`004f6f28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6f28.md) [`004f9190`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9190.md) · 呼出先 9件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00512c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0051c12c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`00528cb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528cb4.md) [`00bd70ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 6件 [`00503084`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md) [`0051138c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) [`00517610`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md) [`00519dc0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519dc0.md) [`0051c028`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c028.md) · 呼出先 9件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0053efc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`0054bb4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bb4c.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 6件, `store_condition` 3件, `store_destination` 9件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054b918",
      "incomplete_value": true,
      "site": "0054b918",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528a80",
      "incomplete_value": true,
      "site": "00528a80",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054b918",
      "incomplete_value": true,
      "site": "0054b918",
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
                "const:80:8"
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
      "definition_site": "00528a80",
      "incomplete_value": true,
      "site": "00528a80",
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
                "const:80:8"
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
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054b91c",
      "incomplete_value": true,
      "site": "0054b91c",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528a84",
      "incomplete_value": true,
      "site": "00528a84",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      168,
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      192,
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      284,
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      168,
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      192,
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      284,
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00528ab0 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
+ 0054b948 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
- 00528ae8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 0054b980 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00528af0 ["CBRANCH", null, ["local:b30:8", "tmp:0:1"]]
+ 0054b988 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
~~~


### [`00528cb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528cb4.md) → [`0054bb4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bb4c.md) FUN_0054bb4c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00528a6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a6c.md) · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054b904`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md) · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054bba0",
      "incomplete_value": true,
      "site": "0054bba0",
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
                "register:4098:8"
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
      "definition_site": "00528d08",
      "incomplete_value": true,
      "site": "00528d08",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4000:8"
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


~~~diff
- 00528cd8 ["INT_ADD", "register:40f0:8", ["const:528cd8:8", "const:4:8"]]
+ 0054bb70 ["INT_ADD", "register:40f0:8", ["const:54bb70:8", "const:4:8"]]
- 00528d08 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 0054bba0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
~~~


### [`00528d24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528d24.md) → [`0054bbbc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bbbc.md) FUN_0054bbbc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`004e01ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e01ec.md) [`004ee4f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md) · 呼出先 4件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00528ef0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528ef0.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00503084`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md) [`0051138c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) · 呼出先 4件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054bd88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bd88.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054bbf0",
      "incomplete_value": true,
      "site": "0054bbf0",
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
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528d58",
      "incomplete_value": true,
      "site": "00528d58",
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054bbf0",
      "incomplete_value": true,
      "site": "0054bbf0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00528d58",
      "incomplete_value": true,
      "site": "00528d58",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054bd24",
      "incomplete_value": true,
      "site": "0054bd28",
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
      "definition_site": "00528e8c",
      "incomplete_value": true,
      "site": "00528e90",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  }
]
~~~


~~~diff
- 00528d68 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
+ 0054bc00 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00528d7c ["BRANCH", null, ["local:b5:8"]]
+ 0054bc14 ["BRANCH", null, ["local:b4:8"]]
- 00528d88 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
+ 0054bc20 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
~~~


### [`00528ef0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528ef0.md) → [`0054bd88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bd88.md) FUN_0054bd88

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00528d24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528d24.md) · 呼出先 5件 [`0047c554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0054bbbc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bbbc.md) · 呼出先 5件 [`0049f3ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 8件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054bd8c",
      "incomplete_value": true,
      "site": "0054bd8c",
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
      "definition_site": "00528ef4",
      "incomplete_value": true,
      "site": "00528ef4",
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
                "const:ffffffffffffffb0:8"
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
      "definition_site": "0054bd90",
      "incomplete_value": true,
      "site": "0054bd90",
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
      "definition_site": "00528ef8",
      "incomplete_value": true,
      "site": "00528ef8",
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
                "const:ffffffffffffffb0:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054bd90",
      "incomplete_value": true,
      "site": "0054bd90",
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
      "definition_site": "00528ef8",
      "incomplete_value": true,
      "site": "00528ef8",
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
      44,
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      44,
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00528f10 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0054bda8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00528f1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 0054bdb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 00528f38 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 0054bdd0 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
~~~


### [`0052903c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052903c.md) → [`0054bed4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bed4.md) FUN_0054bed4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`004ee4f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md) · 呼出先 1件 [`0052913c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052913c.md)
- 新版 呼出元 1件 [`0051138c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) · 呼出先 1件 [`0054bfd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bfd4.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `branch_value` 4件, `return_value_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054bf18",
      "incomplete_value": true,
      "site": "0054bf18",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:102:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00529080",
      "incomplete_value": true,
      "site": "00529080",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              [
                "live",
                "register:4048:8"
              ],
              "INT_SRIGHT"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0054bf50",
      "incomplete_value": true,
      "site": "0054bf50",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              [
                "live",
                "register:102:1"
              ]
            ]
          ],
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005290b8",
      "incomplete_value": true,
      "site": "005290b8",
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
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054bf74",
      "incomplete_value": true,
      "site": "0054bf78",
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
                "const:2:8"
              ]
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005290dc",
      "incomplete_value": true,
      "site": "005290e0",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
          [
            "live",
            "register:4060:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


~~~diff
- 00529044 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 0054bedc ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00529060 ["BRANCH", null, ["local:b4:8"]]
+ 0054bef8 ["BRANCH", null, ["local:b3:8"]]
- 00529080 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0054bf18 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
~~~


### [`0052913c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052913c.md) → [`0054bfd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bfd4.md) FUN_0054bfd4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0052903c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052903c.md) · 呼出先 4件 [`00471738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054bed4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bed4.md) · 呼出先 4件 [`004945d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054c030",
      "incomplete_value": true,
      "site": "0054c034",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00529198",
      "incomplete_value": true,
      "site": "0052919c",
      "value": [
        "INT_SUB",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054bfec",
      "incomplete_value": true,
      "site": "0054bfec",
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
      "definition_site": "00529154",
      "incomplete_value": true,
      "site": "00529154",
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
      "definition_site": "0054c014",
      "incomplete_value": true,
      "site": "0054c014",
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
      "definition_site": "0052917c",
      "incomplete_value": true,
      "site": "0052917c",
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
    "ordinal": 2,
    "slot": 0
  }
]
~~~


~~~diff
- 00529164 ["BRANCH", null, ["local:b7:8"]]
+ 0054bffc ["BRANCH", null, ["local:b6:8"]]
- 00529188 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 0054c020 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 005291a4 ["INT_ADD", "register:40f0:8", ["const:5291a4:8", "const:4:8"]]
+ 0054c03c ["INT_ADD", "register:40f0:8", ["const:54c03c:8", "const:4:8"]]
~~~


### [`00529214`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529214.md) → [`0054c0ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c0ac.md) FUN_0054c0ac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`004f4030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4030.md) · 呼出先 4件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0052934c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052934c.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00516ec8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ec8.md) · 呼出先 4件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0054c1e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1e4.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054c0f4",
      "incomplete_value": true,
      "site": "0054c0f4",
      "value": [
        "BOOL_AND",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              [
                "live",
                "register:4040:8"
              ],
              "INT_SRIGHT"
            ]
          ],
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052925c",
      "incomplete_value": true,
      "site": "0052925c",
      "value": [
        "BOOL_AND",
        "1",
        [
          [
            "live",
            "register:102:1"
          ],
          [
            "BOOL_NEGATE",
            "1",
            [
              [
                "live",
                "register:101:1"
              ]
            ]
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054c14c",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "005292a8",
      "incomplete_value": true,
      "site": "005292b4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054c184",
      "incomplete_value": true,
      "site": "0054c188",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
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
    "old": {
      "definition_site": "005292ec",
      "incomplete_value": true,
      "site": "005292f0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40c0:8"
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
    "ordinal": 7,
    "slot": 0
  }
]
~~~


~~~diff
- 00529240 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
+ 0054c0d8 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00529274 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 0054c10c ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 0052927c ["INT_ADD", "register:40f0:8", ["const:52927c:8", "const:4:8"]]
+ 0054c114 ["INT_ADD", "register:40f0:8", ["const:54c114:8", "const:4:8"]]
~~~


### [`0052934c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052934c.md) → [`0054c1e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1e4.md) FUN_0054c1e4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00529214`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529214.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0054c0ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c0ac.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0054c1f4",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052935c",
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
      "definition_site": "0054c1f0",
      "incomplete_value": false,
      "site": "0054c1f4",
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
      "definition_site": "00529358",
      "incomplete_value": false,
      "site": "0052935c",
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
- 00529354 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00529358 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0054c1ec ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0054c1f0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0052935c ["INT_ADD", "register:40f0:8", ["const:52935c:8", "const:4:8"]]
- 0052935c ["CALL", null, ["ram:418c38:8"]]
+ 0054c1f4 ["INT_ADD", "register:40f0:8", ["const:54c1f4:8", "const:4:8"]]
+ 0054c1f4 ["CALL", null, ["ram:43b738:8"]]
~~~


### [`00529858`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529858.md) → [`0054c6f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c6f0.md) FUN_0054c6f0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`0052968c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052968c.md) · 呼出先 5件 [`0047c554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0054c524`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c524.md) · 呼出先 5件 [`0049f3ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054c72c",
      "incomplete_value": true,
      "site": "0054c730",
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
      "definition_site": "00529894",
      "incomplete_value": true,
      "site": "00529898",
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
      44,
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      44,
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00529878 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0054c710 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00529884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 0054c71c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 005298a4 ["CBRANCH", null, ["local:b14:8", "tmp:3:1"]]
+ 0054c73c ["CBRANCH", null, ["local:b15:8", "tmp:3:1"]]
~~~


### [`005299a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/005299a4.md) → [`0054c83c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c83c.md) FUN_0054c83c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`004f78a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f78a4.md) · 呼出先 6件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0051a920`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a920.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0051a73c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a73c.md) · 呼出先 6件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0053d7b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7b8.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 9件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054c844",
      "incomplete_value": true,
      "site": "0054c844",
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
      "definition_site": "005299ac",
      "incomplete_value": true,
      "site": "005299ac",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054c844",
      "incomplete_value": true,
      "site": "0054c844",
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
      "definition_site": "005299ac",
      "incomplete_value": true,
      "site": "005299ac",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054c848",
      "incomplete_value": true,
      "site": "0054c848",
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
      "definition_site": "005299b0",
      "incomplete_value": true,
      "site": "005299b0",
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
      192,
      "READ",
      [
        "storage",
        "00c1b360",
        null,
        "pointer"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ],
    [
      216,
      "DATA",
      [
        "storage",
        "00beb158",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      192,
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      216,
      "DATA",
      [
        "storage",
        "00c67d18",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005299f8 ["CBRANCH", null, ["local:b35:8", "tmp:1:1"]]
+ 0054c890 ["CBRANCH", null, ["local:b34:8", "tmp:1:1"]]
- 00529a34 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 0054c8cc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00529a3c ["CBRANCH", null, ["local:b37:8", "tmp:1:1"]]
+ 0054c8d4 ["CBRANCH", null, ["local:b36:8", "tmp:1:1"]]
~~~


### [`00529c48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529c48.md) → [`0054cae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cae0.md) FUN_0054cae0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, constant, control_flow, local_def_use, operands_and_dependencies, store_condition

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054cb04",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00529c68",
      "incomplete_value": true,
      "site": "00529c6c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00529c6c"
      ],
      [
        "FALL_THROUGH",
        "0054cb04"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054cb0c",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00529c68",
      "incomplete_value": true,
      "site": "00529c74",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
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
    "ordinal": 5,
    "slot": 0
  }
]
~~~


~~~diff
- 00529c60 ["BRANCH", null, ["local:b3:8"]]
+ 0054caf8 ["BRANCH", null, ["local:b2:8"]]
- 00529c6c ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
+ 0054cb04 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00529c84 ["INT_ADD", "register:40f0:8", ["const:529c84:8", "const:4:8"]]
+ 0054cb1c ["INT_ADD", "register:40f0:8", ["const:54cb1c:8", "const:4:8"]]
~~~


### [`00529cc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529cc4.md) → [`0054cb5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb5c.md) FUN_0054cb5c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004f8244`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8244.md) [`00504f50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504f50.md) [`005054cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00505/005054cc.md) · 呼出先 1件 [`0041fdf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`0051b0dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b0dc.md) [`00527de8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) [`00528364`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md) · 呼出先 1件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "0054cb6c",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00529cd4",
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
      "definition_site": "0054cb68",
      "incomplete_value": true,
      "site": "0054cb6c",
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
            "const:f0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00529cd0",
      "incomplete_value": true,
      "site": "00529cd4",
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
- 00529ccc ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00529cd0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0054cb64 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0054cb68 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00529cd4 ["INT_ADD", "register:40f0:8", ["const:529cd4:8", "const:4:8"]]
- 00529cd4 ["CALL", null, ["ram:41fdf0:8"]]
+ 0054cb6c ["INT_ADD", "register:40f0:8", ["const:54cb6c:8", "const:4:8"]]
+ 0054cb6c ["CALL", null, ["ram:4428f0:8"]]
~~~


### [`00529d48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d48.md) → [`0054cbe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbe0.md) FUN_0054cbe0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004f8c10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8c10.md) [`004f9190`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9190.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0051baa8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051baa8.md) [`0051c028`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c028.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054cbf0",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00529d58",
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
      "definition_site": "0054cbec",
      "incomplete_value": true,
      "site": "0054cbf0",
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
            "const:f0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00529d54",
      "incomplete_value": false,
      "site": "00529d58",
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
- 00529d50 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00529d54 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0054cbe8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0054cbec ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00529d58 ["INT_ADD", "register:40f0:8", ["const:529d58:8", "const:4:8"]]
- 00529d58 ["CALL", null, ["ram:418c38:8"]]
+ 0054cbf0 ["INT_ADD", "register:40f0:8", ["const:54cbf0:8", "const:4:8"]]
+ 0054cbf0 ["CALL", null, ["ram:43b738:8"]]
~~~


### [`00529d5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d5c.md) → [`0054cbf4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbf4.md) FUN_0054cbf4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`004f9abc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9abc.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0051c954`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `branch_value` 14件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054cc18",
      "incomplete_value": true,
      "site": "0054cc1c",
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
                "const:2:8"
              ]
            ]
          ],
          [
            "INT_SRIGHT",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00529d84",
      "value": [
        "live",
        "register:102:1"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054cc2c",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00529d90",
      "incomplete_value": true,
      "site": "00529d94",
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
                "register:4008:8"
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054cc4c",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00529db0",
      "incomplete_value": true,
      "site": "00529db4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4048:8"
              ],
              [
                "live",
                "register:4050:8"
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
    "ordinal": 5,
    "slot": 0
  }
]
~~~


~~~diff
- 00529d64 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 0054cbfc ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00529d84 ["CBRANCH", null, ["local:b9:8", "register:102:1"]]
+ 0054cc1c ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
- 00529dd8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0054cc70 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
~~~


### [`0052a0f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a0f8.md) → [`0054cf90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cf90.md) FUN_0054cf90

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`004f9abc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9abc.md) · 呼出先 6件 [`00512c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0052a1c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a1c8.md) [`00bd70ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0051c954`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md) · 呼出先 6件 [`00535b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0054d060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d060.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054cfd0",
      "incomplete_value": true,
      "site": "0054cfd8",
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
      "definition_site": "0052a138",
      "incomplete_value": true,
      "site": "0052a140",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054cfdc",
      "incomplete_value": true,
      "site": "0054cfe4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4048:8"
              ],
              [
                "live",
                "register:40b0:8"
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
      "definition_site": "0052a144",
      "incomplete_value": true,
      "site": "0052a14c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0052a168",
      "incomplete_value": true,
      "site": "0052a174",
      "value": [
        "live",
        "register:40b8:8"
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      48,
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052a11c ["INT_ADD", "register:40f0:8", ["const:52a11c:8", "const:4:8"]]
+ 0054cfb4 ["INT_ADD", "register:40f0:8", ["const:54cfb4:8", "const:4:8"]]
- 0052a124 ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 0052a128 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 0054cfbc ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0054cfc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 0052a14c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 0054cfe4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
~~~


### [`0052a1c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a1c8.md) → [`0054d060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d060.md) FUN_0054d060

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0052a0f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a0f8.md) · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054cf90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cf90.md) · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054d064",
      "incomplete_value": true,
      "site": "0054d064",
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
      "definition_site": "0052a1cc",
      "incomplete_value": true,
      "site": "0052a1cc",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0054d074",
      "incomplete_value": true,
      "site": "0054d074",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052a1dc",
      "incomplete_value": true,
      "site": "0052a1dc",
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
    "ordinal": 0,
    "slot": 0
  }
]
~~~


~~~diff
- 0052a1e4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0054d07c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0052a1ec ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0054d084 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0052a1f4 ["INT_ADD", "register:40f0:8", ["const:52a1f4:8", "const:4:8"]]
+ 0054d08c ["INT_ADD", "register:40f0:8", ["const:54d08c:8", "const:4:8"]]
~~~


### [`0052a264`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a264.md) → [`0054d0fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0fc.md) FUN_0054d0fc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`004fb4c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fb4c0.md) · 呼出先 9件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a5b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00519a68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`0051cdc8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cdc8.md)
- 新版 呼出元 1件 [`0051e358`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e358.md) · 呼出先 9件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d450`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053c900`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`0053fc60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fc60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_condition` 1件, `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054d120",
      "incomplete_value": true,
      "site": "0054d120",
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
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052a288",
      "incomplete_value": true,
      "site": "0052a288",
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054d120",
      "incomplete_value": true,
      "site": "0054d120",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052a288",
      "incomplete_value": true,
      "site": "0052a288",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0054d148",
      "incomplete_value": true,
      "site": "0054d14c",
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
    "old": {
      "definition_site": "0052a2b0",
      "incomplete_value": true,
      "site": "0052a2b4",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      152,
      "READ",
      [
        "storage",
        "00c1b3f8",
        null,
        "pointer"
      ]
    ],
    [
      172,
      "DATA",
      [
        "storage",
        "00bebe68",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      152,
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      172,
      "DATA",
      [
        "storage",
        "00c68a28",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052a2a0 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 0054d138 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 0052a2e4 ["INT_ADD", "register:40f0:8", ["const:52a2e4:8", "const:4:8"]]
+ 0054d17c ["INT_ADD", "register:40f0:8", ["const:54d17c:8", "const:4:8"]]
- 0052a2f4 ["COPY", "register:4050:8", ["const:c1b000:8"]]
+ 0054d18c ["COPY", "register:4050:8", ["const:c9a000:8"]]
~~~


### [`0052a400`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a400.md) → [`0054d298`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d298.md) FUN_0054d298

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`0052a264`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a264.md) · 呼出先 2件 [`0044a5b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md)
- 新版 呼出元 1件 [`0054d0fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0fc.md) · 呼出先 2件 [`0046d450`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 1件, `store_condition` 10件, `store_destination` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054d2a4",
      "incomplete_value": true,
      "site": "0054d2a4",
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
                "const:ffffffffffffffc0:8"
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
      "definition_site": "0052a40c",
      "incomplete_value": true,
      "site": "0052a40c",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054d2a4",
      "incomplete_value": true,
      "site": "0054d2a4",
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
      "definition_site": "0052a40c",
      "incomplete_value": true,
      "site": "0052a40c",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054d330",
      "incomplete_value": true,
      "site": "0054d330",
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
                "register:40b8:8"
              ],
              [
                "live",
                "register:4040:8"
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
      "definition_site": "0052a498",
      "incomplete_value": true,
      "site": "0052a498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      64,
      "READ",
      [
        "storage",
        "00c1b3f8",
        null,
        "pointer"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c1b2d8",
        null,
        "pointer"
      ]
    ],
    [
      124,
      "DATA",
      [
        "storage",
        "00bebe68",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      64,
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c9acc8",
        null,
        "pointer"
      ]
    ],
    [
      124,
      "DATA",
      [
        "storage",
        "00c68a28",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052a434 ["COPY", "register:4048:8", ["const:c1b000:8"]]
- 0052a438 ["COPY", "register:4050:8", ["const:c1b000:8"]]
+ 0054d2cc ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 0054d2d0 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 0052a440 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3f8:8"]]
+ 0054d2d8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de8:8"]]
- 0052a444 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:2d8:8"]]
+ 0054d2dc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:cc8:8"]]
~~~


### [`0052a558`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a558.md) → [`0054d3f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d3f0.md) FUN_0054d3f0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044a5b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d450`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054d41c",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "0052a57c",
      "incomplete_value": true,
      "site": "0052a584",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:40:8"
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
    "new": null,
    "old": {
      "definition_site": "0052a580",
      "incomplete_value": true,
      "site": "0052a588",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:18:8"
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
    "new": null,
    "old": {
      "definition_site": "0052a578",
      "incomplete_value": true,
      "site": "0052a588",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:fffffffffffffff0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


~~~diff
- 0052a574 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 0054d40c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 0052a588 ["INT_ADD", "register:40f0:8", ["const:52a588:8", "const:4:8"]]
+ 0054d420 ["INT_ADD", "register:40f0:8", ["const:54d420:8", "const:4:8"]]
- 0052a594 ["INT_ADD", "register:40f0:8", ["const:52a594:8", "const:4:8"]]
+ 0054d42c ["INT_ADD", "register:40f0:8", ["const:54d42c:8", "const:4:8"]]
~~~


### [`0052a5cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a5cc.md) → [`0054d464`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md) FUN_0054d464

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`004fdfd8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdfd8.md) [`004ff950`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ff950.md) [`0052a914`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a914.md) · 呼出先 5件 [`0044a5b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004f7dec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7dec.md) [`005180b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`0051854c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00520e70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) [`005227e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005227e8.md) [`0054d7ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d7ac.md) · 呼出先 5件 [`0046d450`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0051ac84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md) [`0053af50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053b3e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054d46c",
      "incomplete_value": true,
      "site": "0054d46c",
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
      "definition_site": "0052a5d4",
      "incomplete_value": true,
      "site": "0052a5d4",
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
                "const:ffffffffffffffd0:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0054d46c",
      "incomplete_value": true,
      "site": "0054d46c",
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
      "definition_site": "0052a5d4",
      "incomplete_value": true,
      "site": "0052a5d4",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0054d534",
      "incomplete_value": true,
      "site": "0054d538",
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
    "old": {
      "definition_site": "0052a69c",
      "incomplete_value": true,
      "site": "0052a6a0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4040:8"
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


~~~diff
- 0052a5e8 ["INT_ADD", "register:40f0:8", ["const:52a5e8:8", "const:4:8"]]
+ 0054d480 ["INT_ADD", "register:40f0:8", ["const:54d480:8", "const:4:8"]]
- 0052a5f4 ["INT_ADD", "register:40f0:8", ["const:52a5f4:8", "const:4:8"]]
+ 0054d48c ["INT_ADD", "register:40f0:8", ["const:54d48c:8", "const:4:8"]]
- 0052a5fc ["INT_ADD", "register:40f0:8", ["const:52a5fc:8", "const:4:8"]]
+ 0054d494 ["INT_ADD", "register:40f0:8", ["const:54d494:8", "const:4:8"]]
~~~


### [`0052ab40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ab40.md) → [`0054d9d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9d8.md) FUN_0054d9d8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00504f50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504f50.md) · 呼出先 1件 [`0041fdf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00527de8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) · 呼出先 1件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "0054d9e8",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052ab50",
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
      "definition_site": "0054d9e4",
      "incomplete_value": false,
      "site": "0054d9e8",
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
      "definition_site": "0052ab4c",
      "incomplete_value": false,
      "site": "0052ab50",
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
- 0052ab48 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 0052ab4c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0054d9e0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0054d9e4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0052ab50 ["INT_ADD", "register:40f0:8", ["const:52ab50:8", "const:4:8"]]
- 0052ab50 ["CALL", null, ["ram:41fdf0:8"]]
+ 0054d9e8 ["INT_ADD", "register:40f0:8", ["const:54d9e8:8", "const:4:8"]]
+ 0054d9e8 ["CALL", null, ["ram:4428f0:8"]]
~~~


### [`0052acbc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acbc.md) → [`0054db54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db54.md) FUN_0054db54

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052b868`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b868.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0054e700`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0054db64",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052accc",
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
      "definition_site": "0054db60",
      "incomplete_value": false,
      "site": "0054db64",
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
      "definition_site": "0052acc8",
      "incomplete_value": false,
      "site": "0052accc",
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
- 0052acc4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 0052acc8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0054db5c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0054db60 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0052accc ["INT_ADD", "register:40f0:8", ["const:52accc:8", "const:4:8"]]
- 0052accc ["CALL", null, ["ram:418c38:8"]]
+ 0054db64 ["INT_ADD", "register:40f0:8", ["const:54db64:8", "const:4:8"]]
+ 0054db64 ["CALL", null, ["ram:43b738:8"]]
~~~


### [`0052ae7c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae7c.md) → [`0054dd14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd14.md) FUN_0054dd14

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00506ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00529d78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0054dd24",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052ae8c",
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
      "definition_site": "0054dd20",
      "incomplete_value": false,
      "site": "0054dd24",
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
      "definition_site": "0052ae88",
      "incomplete_value": false,
      "site": "0052ae8c",
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
- 0052ae84 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 0052ae88 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0054dd1c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0054dd20 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0052ae8c ["INT_ADD", "register:40f0:8", ["const:52ae8c:8", "const:4:8"]]
- 0052ae8c ["CALL", null, ["ram:418c38:8"]]
+ 0054dd24 ["INT_ADD", "register:40f0:8", ["const:54dd24:8", "const:4:8"]]
+ 0054dd24 ["CALL", null, ["ram:43b738:8"]]
~~~


### [`0052b348`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b348.md) → [`0054e1e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1e0.md) FUN_0054e1e0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052ae90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae90.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0054dd28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0054e1f0",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052b358",
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
      "definition_site": "0054e1ec",
      "incomplete_value": false,
      "site": "0054e1f0",
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
      "definition_site": "0052b354",
      "incomplete_value": false,
      "site": "0052b358",
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
- 0052b350 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 0052b354 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0054e1e8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0054e1ec ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0052b358 ["INT_ADD", "register:40f0:8", ["const:52b358:8", "const:4:8"]]
- 0052b358 ["CALL", null, ["ram:418c38:8"]]
+ 0054e1f0 ["INT_ADD", "register:40f0:8", ["const:54e1f0:8", "const:4:8"]]
+ 0054e1f0 ["CALL", null, ["ram:43b738:8"]]
~~~


### [`0052c024`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c024.md) → [`0054eebc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eebc.md) FUN_0054eebc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052be2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052be2c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0054ecc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0054eecc",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052c034",
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
      "definition_site": "0054eec8",
      "incomplete_value": false,
      "site": "0054eecc",
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
      "definition_site": "0052c030",
      "incomplete_value": false,
      "site": "0052c034",
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
- 0052c02c ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 0052c030 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0054eec4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0054eec8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0052c034 ["INT_ADD", "register:40f0:8", ["const:52c034:8", "const:4:8"]]
- 0052c034 ["CALL", null, ["ram:418c38:8"]]
+ 0054eecc ["INT_ADD", "register:40f0:8", ["const:54eecc:8", "const:4:8"]]
+ 0054eecc ["CALL", null, ["ram:43b738:8"]]
~~~


### [`0052c558`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c558.md) → [`0054f3f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md) _INIT_25

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004c45bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c45bc.md) [`004c4764`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4764.md) [`004f25dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f25dc.md) [`004f26f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f26f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00473500`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004e7454`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md) [`004e75fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e75fc.md) [`00515474`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md) [`00515590`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515590.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054f714",
      "incomplete_value": false,
      "site": "0054f728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052c87c",
      "incomplete_value": false,
      "site": "0052c890",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054fa04",
      "incomplete_value": false,
      "site": "0054fa18",
      "value": [
        "leaf",
        "const:4e75fc:8"
      ]
    },
    "old": {
      "definition_site": "0052cb6c",
      "incomplete_value": false,
      "site": "0052cb80",
      "value": [
        "leaf",
        "const:4c4764:8"
      ]
    },
    "ordinal": 35,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054fa0c",
      "incomplete_value": false,
      "site": "0054fa18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052cb74",
      "incomplete_value": false,
      "site": "0052cb80",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      660,
      "DATA",
      [
        "storage",
        "0030312e",
        null,
        "fde_table_entry"
      ]
    ],
    [
      776,
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "byte[43]"
      ]
    ],
    [
      804,
      "PARAM",
      [
        "storage",
        "00c253a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      660,
      "DATA",
      [
        "storage",
        "0030312e",
        null,
        "string"
      ]
    ],
    [
      776,
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "qword"
      ]
    ],
    [
      804,
      "PARAM",
      [
        "storage",
        "00ca4e68",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0052c5b4 ["INT_ADD", "register:40f0:8", ["const:52c5b4:8", "const:4:8"]]
+ 0054f44c ["INT_ADD", "register:40f0:8", ["const:54f44c:8", "const:4:8"]]
- 0052c5f8 ["INT_ADD", "register:40f0:8", ["const:52c5f8:8", "const:4:8"]]
+ 0054f490 ["INT_ADD", "register:40f0:8", ["const:54f490:8", "const:4:8"]]
- 0052c62c ["INT_ADD", "register:40f0:8", ["const:52c62c:8", "const:4:8"]]
+ 0054f4c4 ["INT_ADD", "register:40f0:8", ["const:54f4c4:8", "const:4:8"]]
~~~


### [`0052daf4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052daf4.md) → [`0055098c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055098c.md) FUN_0055098c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006fd020`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd020.md) [`006fd460`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd460.md) · 呼出先 1件 [`00553568`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553568.md)
- 新版 呼出元 2件 [`00727120`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727120.md) [`00727560`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727560.md) · 呼出先 1件 [`00576400`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576400.md)

変更の種類 branch_value, constant, operands_and_dependencies

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005509a8",
      "incomplete_value": true,
      "site": "005509a8",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "FLOAT_NAN",
            "1",
            [
              [
                "live",
                "register:5020:8"
              ]
            ]
          ],
          [
            "FLOAT_NAN",
            "1",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052db10",
      "incomplete_value": true,
      "site": "0052db10",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "FLOAT_NAN",
            "1",
            [
              [
                "live",
                "register:5020:8"
              ]
            ]
          ],
          [
            "FLOAT_NAN",
            "1",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005509a8",
      "incomplete_value": true,
      "site": "005509ac",
      "value": [
        "FLOAT_LESS",
        "1",
        [
          [
            "live",
            "register:5020:8"
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
      "definition_site": "0052db10",
      "incomplete_value": true,
      "site": "0052db14",
      "value": [
        "FLOAT_LESS",
        "1",
        [
          [
            "live",
            "register:5020:8"
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
    "ordinal": 5,
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
      "READ",
      [
        "storage",
        "002b2578",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      24,
      "READ",
      [
        "storage",
        "002c3c48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052db00 ["COPY", "register:4040:8", ["const:2b2000:8"]]
+ 00550998 ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 0052db0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
+ 005509a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c48:8"]]
~~~


### [`0052db94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db94.md) → [`00550a2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a2c.md) FUN_00550a2c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052db88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db88.md) · 呼出先 12件 [`004377f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377f0.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb4a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`00550a20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a20.md) · 呼出先 12件 [`0045a688`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00550ad0",
      "incomplete_value": true,
      "site": "00550ad4",
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
      "definition_site": "0052dc38",
      "incomplete_value": true,
      "site": "0052dc3c",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00550a6c",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052dbd4",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00550aac",
      "incomplete_value": true,
      "site": "00550ab4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052dc14",
      "incomplete_value": true,
      "site": "0052dc1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ],
    [
      124,
      "PARAM",
      [
        "storage",
        "004377f0",
        null,
        null
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "00c1ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ],
    [
      124,
      "PARAM",
      [
        "storage",
        "0045a688",
        null,
        null
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "00c9a858",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052dbd4 ["INT_ADD", "register:40f0:8", ["const:52dbd4:8", "const:4:8"]]
- 0052dbd4 ["CALL", null, ["ram:bdb4a0:8"]]
+ 00550a6c ["INT_ADD", "register:40f0:8", ["const:550a6c:8", "const:4:8"]]
+ 00550a6c ["CALL", null, ["ram:c57ef0:8"]]
- 0052dbec ["INT_ADD", "register:40f0:8", ["const:52dbec:8", "const:4:8"]]
+ 00550a84 ["INT_ADD", "register:40f0:8", ["const:550a84:8", "const:4:8"]]
- 0052dbfc ["INT_ADD", "register:40f0:8", ["const:52dbfc:8", "const:4:8"]]
+ 00550a94 ["INT_ADD", "register:40f0:8", ["const:550a94:8", "const:4:8"]]
~~~


### [`0052e05c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e05c.md) → [`00550ef4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md) FUN_00550ef4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005321d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005321d8.md) · 呼出先 5件 [`0053b668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b668.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00555070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md) · 呼出先 5件 [`0055e500`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e500.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00550f38",
      "incomplete_value": false,
      "site": "00550f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e0a0",
      "incomplete_value": false,
      "site": "0052e0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      72,
      "DATA",
      [
        "storage",
        "00bedc20",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      72,
      "DATA",
      [
        "storage",
        "00c6a7e0",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "DATA",
      [
        "storage",
        "00c6a848",
        null,
        "undefined *"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052e094 ["INT_ADD", "register:40f0:8", ["const:52e094:8", "const:4:8"]]
+ 00550f2c ["INT_ADD", "register:40f0:8", ["const:550f2c:8", "const:4:8"]]
- 0052e09c ["COPY", "register:4040:8", ["const:bed000:8"]]
- 0052e0a0 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 00550f34 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00550f38 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 0052e0b8 ["COPY", "register:40c8:8", ["const:c1b000:8"]]
+ 00550f50 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
~~~


### [`0052e39c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e39c.md) → [`00551234`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md) FUN_00551234

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005f2980`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2980.md) [`00877a44`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md) [`00878b14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md) [`008a4e38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md) · 呼出先 6件 [`0052f11c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md) [`0053980c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md) [`00574ff4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`006181c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md) [`008aabe4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008aa/008aabe4.md) [`008abcb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008abcb4.md) [`008d8cd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) · 呼出先 6件 [`00551fb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md) [`0055c6a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md) [`00597e8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055128c",
      "incomplete_value": true,
      "site": "00551294",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e3f4",
      "incomplete_value": true,
      "site": "0052e3fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:500:8"
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
      "definition_site": "00551288",
      "incomplete_value": true,
      "site": "00551298",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1a3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9aa:8"
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
      "definition_site": "00551288",
      "incomplete_value": true,
      "site": "00551298",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
      "value": [
        "LOAD",
        "16",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      84,
      "READ",
      [
        "storage",
        "002939aa",
        null,
        "string"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "002939ba",
        null,
        "string"
      ]
    ],
    [
      88,
      "READ",
      [
        "storage",
        "002b1500",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      84,
      "READ",
      [
        "storage",
        "002a31a3",
        null,
        "string"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "002a31b3",
        null,
        "string"
      ]
    ],
    [
      88,
      "READ",
      [
        "storage",
        "002c2b50",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0052e3e0 ["INT_ADD", "register:40f0:8", ["const:52e3e0:8", "const:4:8"]]
+ 00551278 ["INT_ADD", "register:40f0:8", ["const:551278:8", "const:4:8"]]
- 0052e3e4 ["COPY", "register:4040:8", ["const:293000:8"]]
- 0052e3e8 ["COPY", "tmp:0:8", ["const:9aa:8"]]
+ 0055127c ["COPY", "register:4040:8", ["const:2a3000:8"]]
+ 00551280 ["COPY", "tmp:0:8", ["const:1a3:8"]]
- 0052e3ec ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00551284 ["COPY", "register:4048:8", ["const:2c2000:8"]]
~~~


### [`0052eee8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052eee8.md) → [`00551d80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551d80.md) FUN_00551d80

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0053b74c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b74c.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0055e5e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5e4.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00551dd0",
      "incomplete_value": true,
      "site": "00551dd0",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "0052ef38",
      "incomplete_value": true,
      "site": "0052ef38",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00551dc0",
      "incomplete_value": true,
      "site": "00551dd0",
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
      "definition_site": "0052ef28",
      "incomplete_value": true,
      "site": "0052ef38",
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
    "ordinal": 1,
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
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00c26650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00ca6110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052ef0c ["INT_ADD", "register:40f0:8", ["const:52ef0c:8", "const:4:8"]]
+ 00551da4 ["INT_ADD", "register:40f0:8", ["const:551da4:8", "const:4:8"]]
- 0052ef14 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00551dac ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0052ef20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 00551db8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e40:8"]]
~~~


### [`0052f034`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f034.md) → [`00551ecc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md) FUN_00551ecc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0055e56c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00551edc",
      "incomplete_value": true,
      "site": "00551ee8",
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
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f044",
      "incomplete_value": true,
      "site": "0052f050",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00551eec",
      "incomplete_value": true,
      "site": "00551ef0",
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
                "const:7e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f054",
      "incomplete_value": true,
      "site": "0052f058",
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
                "const:c20:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
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
      28,
      "DATA",
      [
        "storage",
        "00bedc20",
        null,
        "undefined *"
      ]
    ],
    [
      36,
      "DATA",
      [
        "storage",
        "00bedc88",
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
        "00c6a7e0",
        null,
        "undefined *"
      ]
    ],
    [
      36,
      "DATA",
      [
        "storage",
        "00c6a848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0052f040 ["COPY", "register:4040:8", ["const:bed000:8"]]
- 0052f044 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 00551ed8 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00551edc ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 0052f068 ["INT_ADD", "register:40f0:8", ["const:52f068:8", "const:4:8"]]
+ 00551f00 ["INT_ADD", "register:40f0:8", ["const:551f00:8", "const:4:8"]]
- 0052f07c ["INT_ADD", "register:40f0:8", ["const:52f07c:8", "const:4:8"]]
+ 00551f14 ["INT_ADD", "register:40f0:8", ["const:551f14:8", "const:4:8"]]
~~~


