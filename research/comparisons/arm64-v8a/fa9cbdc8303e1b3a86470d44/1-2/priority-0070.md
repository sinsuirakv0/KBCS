# v15.7.4 → v16.0.0 · 最優先の変更候補 (70)

[一覧の目次](README.md)

### [`00ae5e00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5e00.md) → [`00b45b84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45b84.md) _ZN8firebase4util3log12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45bc0",
      "incomplete_value": true,
      "site": "00b45bc0",
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
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5e3c",
      "incomplete_value": true,
      "site": "00ae5e3c",
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
            "const:420:8"
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
      "definition_site": "00b45c10",
      "incomplete_value": true,
      "site": "00b45c10",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5e8c",
      "incomplete_value": true,
      "site": "00ae5e8c",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45b9c",
      "incomplete_value": true,
      "site": "00b45b9c",
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
      "definition_site": "00ae5e18",
      "incomplete_value": true,
      "site": "00ae5e18",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0420",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0420",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011252e0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011252e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae5e10 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae5e14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00b45b94 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b45b98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d8:8"]]
- 00ae5e18 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae5e1c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae5e20 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:420:8"]]
+ 00b45b9c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00b45ba0 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b45ba4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2e0:8"]]
- 00ae5e38 ["INT_ADD", "register:40f0:8", ["const:ae5e38:8", "const:4:8"]]
+ 00b45bbc ["INT_ADD", "register:40f0:8", ["const:b45bbc:8", "const:4:8"]]
~~~


### [`00ae5ea0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ea0.md) → [`00b45c24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c24.md) _ZN8firebase4util3log14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45c64",
      "incomplete_value": true,
      "site": "00b45c64",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ee0",
      "incomplete_value": true,
      "site": "00ae5ee0",
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
            "const:418:8"
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
      "definition_site": "00b45c40",
      "incomplete_value": true,
      "site": "00b45c40",
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
    "old": {
      "definition_site": "00ae5ebc",
      "incomplete_value": true,
      "site": "00ae5ebc",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae5ec8",
      "incomplete_value": true,
      "site": "00ae5ed8",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002aafae",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bbd77",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae5eac ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b45c30 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae5eb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00b45c38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d8:8"]]
- 00ae5ebc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5ec0 ["COPY", "register:4018:8", ["const:2aa000:8"]]
- 00ae5ec4 ["COPY", "tmp:0:8", ["const:fae:8"]]
+ 00b45c40 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b45c44 ["COPY", "register:4018:8", ["const:2bb000:8"]]
+ 00b45c48 ["COPY", "tmp:0:8", ["const:d77:8"]]
~~~


### [`00ae5f10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f10.md) → [`00b45c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c94.md) _ZN8firebase4util3log11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45c98",
      "incomplete_value": true,
      "site": "00b45c98",
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
      "definition_site": "00ae5f14",
      "incomplete_value": true,
      "site": "00ae5f14",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45c98",
      "incomplete_value": true,
      "site": "00b45c98",
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
      "definition_site": "00ae5f14",
      "incomplete_value": true,
      "site": "00ae5f14",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45ca8",
      "incomplete_value": true,
      "site": "00b45ca8",
      "value": [
        "INT_NOTEQUAL",
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
    "old": {
      "definition_site": "00ae5f24",
      "incomplete_value": true,
      "site": "00ae5f24",
      "value": [
        "INT_NOTEQUAL",
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
                "register:4000:4"
              ],
              [
                "leaf",
                "const:1:4"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011252e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae5f24 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae5f28 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae5f2c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b45ca8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b45cac ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b45cb0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae5f30 ["INT_ADD", "register:40f0:8", ["const:ae5f30:8", "const:4:8"]]
+ 00b45cb4 ["INT_ADD", "register:40f0:8", ["const:b45cb4:8", "const:4:8"]]
- 00ae5f34 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae5f38 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 00b45cb8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b45cbc ["COPY", "tmp:0:8", ["const:2e8:8"]]
~~~


### [`00ae5f4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f4c.md) → [`00b45cd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45cd0.md) _ZN8firebase4util3log13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45d10",
      "incomplete_value": true,
      "site": "00b45d10",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5f8c",
      "incomplete_value": true,
      "site": "00ae5f8c",
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
            "const:418:8"
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
      "definition_site": "00b45cec",
      "incomplete_value": true,
      "site": "00b45cec",
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
    "old": {
      "definition_site": "00ae5f68",
      "incomplete_value": true,
      "site": "00ae5f68",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45cf4",
      "incomplete_value": true,
      "site": "00b45d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:d77:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5f70",
      "incomplete_value": false,
      "site": "00ae5f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:fae:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002aafae",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bbd77",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae5f58 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b45cdc ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae5f60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00b45ce4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d8:8"]]
- 00ae5f68 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5f6c ["COPY", "register:4018:8", ["const:2aa000:8"]]
- 00ae5f70 ["COPY", "tmp:0:8", ["const:fae:8"]]
+ 00b45cec ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b45cf0 ["COPY", "register:4018:8", ["const:2bb000:8"]]
+ 00b45cf4 ["COPY", "tmp:0:8", ["const:d77:8"]]
~~~


### [`00ae5fbc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5fbc.md) → [`00b45d40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d40.md) _ZN8firebase4util3log10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45d5c",
      "incomplete_value": false,
      "site": "00b45d60",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5fd8",
      "incomplete_value": false,
      "site": "00ae5fdc",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b45d6c",
      "incomplete_value": true,
      "site": "00b45d78",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5fe8",
      "incomplete_value": true,
      "site": "00ae5ff4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0430",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011252f0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae5fd0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5fd4 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae5fd8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b45d54 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b45d58 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b45d5c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae5fdc ["INT_ADD", "register:40f0:8", ["const:ae5fdc:8", "const:4:8"]]
+ 00b45d60 ["INT_ADD", "register:40f0:8", ["const:b45d60:8", "const:4:8"]]
- 00ae5fe0 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae5fe4 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 00b45d64 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b45d68 ["COPY", "tmp:0:8", ["const:2f0:8"]]
~~~


### [`00ae5ff8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ff8.md) → [`00b45d7c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d7c.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45da8",
      "incomplete_value": true,
      "site": "00b45da8",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6024",
      "incomplete_value": true,
      "site": "00ae6024",
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
            "const:438:8"
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
      "definition_site": "00b45d90",
      "incomplete_value": true,
      "site": "00b45d90",
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
    "old": {
      "definition_site": "00ae600c",
      "incomplete_value": true,
      "site": "00ae600c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45d9c",
      "incomplete_value": false,
      "site": "00b45da0",
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
            "const:2cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6018",
      "incomplete_value": false,
      "site": "00ae601c",
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
            "const:eaa:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6004 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6008 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00b45d88 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b45d8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00ae600c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b45d90 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae6014 ["COPY", "register:4018:8", ["const:29e000:8"]]
- 00ae6018 ["COPY", "tmp:0:8", ["const:eaa:8"]]
+ 00b45d98 ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00b45d9c ["COPY", "tmp:0:8", ["const:2cd:8"]]
~~~


### [`00ae6038`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6038.md) → [`00b45dbc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dbc.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45de8",
      "incomplete_value": true,
      "site": "00b45de8",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6064",
      "incomplete_value": true,
      "site": "00ae6064",
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
            "const:438:8"
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
      "definition_site": "00b45dd0",
      "incomplete_value": true,
      "site": "00b45dd0",
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
    "old": {
      "definition_site": "00ae604c",
      "incomplete_value": true,
      "site": "00ae604c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae6054",
      "incomplete_value": false,
      "site": "00ae605c",
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
            "const:eaa:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6044 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6048 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00b45dc8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b45dcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00ae604c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6050 ["COPY", "register:4018:8", ["const:29e000:8"]]
- 00ae6054 ["COPY", "tmp:0:8", ["const:eaa:8"]]
+ 00b45dd0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b45dd4 ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00b45dd8 ["COPY", "tmp:0:8", ["const:2cd:8"]]
- 00ae605c ["INT_ADD", "register:40f0:8", ["const:ae605c:8", "const:4:8"]]
+ 00b45de0 ["INT_ADD", "register:40f0:8", ["const:b45de0:8", "const:4:8"]]
~~~


### [`00ae6078`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6078.md) → [`00b45dfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dfc.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45e2c",
      "incomplete_value": true,
      "site": "00b45e2c",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae60a8",
      "incomplete_value": true,
      "site": "00ae60a8",
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
            "const:438:8"
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
      "definition_site": "00b45e10",
      "incomplete_value": true,
      "site": "00b45e10",
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
      "definition_site": "00ae608c",
      "incomplete_value": true,
      "site": "00ae608c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae6098",
      "incomplete_value": false,
      "site": "00ae60a0",
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
            "const:eaa:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6084 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6088 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00b45e08 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b45e0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00ae608c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6090 ["COPY", "register:4018:8", ["const:29e000:8"]]
+ 00b45e10 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b45e14 ["COPY", "register:4018:8", ["const:2af000:8"]]
- 00ae6098 ["COPY", "tmp:0:8", ["const:eaa:8"]]
+ 00b45e1c ["COPY", "tmp:0:8", ["const:2cd:8"]]
~~~


### [`00ae60bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae60bc.md) → [`00b45e40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e40.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45e70",
      "incomplete_value": true,
      "site": "00b45e70",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae60ec",
      "incomplete_value": true,
      "site": "00ae60ec",
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
            "const:438:8"
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
      "definition_site": "00b45e54",
      "incomplete_value": true,
      "site": "00b45e54",
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
      "definition_site": "00ae60d0",
      "incomplete_value": true,
      "site": "00ae60d0",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45e60",
      "incomplete_value": false,
      "site": "00b45e68",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae60c8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae60cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00b45e4c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b45e50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00ae60d4 ["COPY", "register:4018:8", ["const:29e000:8"]]
- 00ae60d8 ["COPY", "tmp:0:8", ["const:eaa:8"]]
+ 00b45e58 ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00b45e5c ["COPY", "tmp:0:8", ["const:2cd:8"]]
- 00ae60e4 ["INT_ADD", "register:40f0:8", ["const:ae60e4:8", "const:4:8"]]
+ 00b45e68 ["INT_ADD", "register:40f0:8", ["const:b45e68:8", "const:4:8"]]
~~~


### [`00ae610c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae610c.md) → [`00b45e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e90.md) _ZN8firebase4util10uribuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45f18",
      "incomplete_value": true,
      "site": "00b45f18",
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
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6194",
      "incomplete_value": true,
      "site": "00ae6194",
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
            "const:440:8"
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
      "definition_site": "00b45ee8",
      "incomplete_value": true,
      "site": "00b45eec",
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
                "register:4000:4"
              ],
              [
                "leaf",
                "const:ff:4"
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
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ae6168",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45ec4",
      "incomplete_value": true,
      "site": "00b45ed0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:2f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6140",
      "incomplete_value": true,
      "site": "00ae614c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:438:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0440",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0440",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125300",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125300",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae611c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae6120 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:440:8"]]
+ 00b45ea0 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b45ea4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:300:8"]]
- 00ae6124 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b45ea8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae612c ["BRANCH", null, ["local:b9:8"]]
+ 00b45eb0 ["BRANCH", null, ["local:b7:8"]]
~~~


### [`00ae61a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae61a8.md) → [`00b45f2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45f2c.md) _ZN8firebase4util10uribuilder12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45f30",
      "incomplete_value": true,
      "site": "00b45f30",
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
      "definition_site": "00ae61ac",
      "incomplete_value": true,
      "site": "00ae61ac",
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
            "const:10:8"
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
      "definition_site": "00b45f30",
      "incomplete_value": true,
      "site": "00b45f30",
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
      "definition_site": "00ae61ac",
      "incomplete_value": true,
      "site": "00ae61ac",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45f34",
      "incomplete_value": true,
      "site": "00b45f34",
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
      "definition_site": "00ae61b0",
      "incomplete_value": true,
      "site": "00ae61b0",
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
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0440",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0440",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125300",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125300",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae61b8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae61bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00b45f3c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b45f40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
- 00ae61c0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae61c4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae61c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:440:8"]]
+ 00b45f44 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00b45f48 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b45f4c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:300:8"]]
- 00ae61d0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b45f54 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
~~~


### [`00ae6248`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6248.md) → [`00b45fcc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45fcc.md) _ZN8firebase4util10uribuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4600c",
      "incomplete_value": true,
      "site": "00b4600c",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6288",
      "incomplete_value": true,
      "site": "00ae6288",
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
            "const:438:8"
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
      "definition_site": "00b45fe8",
      "incomplete_value": true,
      "site": "00b45fe8",
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
    "old": {
      "definition_site": "00ae6264",
      "incomplete_value": true,
      "site": "00ae6264",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b45ff0",
      "incomplete_value": false,
      "site": "00b46004",
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
            "const:2cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae626c",
      "incomplete_value": false,
      "site": "00ae6280",
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
            "const:eaa:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6254 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b45fd8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae625c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00b45fe0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
- 00ae6268 ["COPY", "register:4018:8", ["const:29e000:8"]]
- 00ae626c ["COPY", "tmp:0:8", ["const:eaa:8"]]
+ 00b45fec ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00b45ff0 ["COPY", "tmp:0:8", ["const:2cd:8"]]
~~~


### [`00ae62b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62b8.md) → [`00b4603c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4603c.md) _ZN8firebase4util10uribuilder11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46058",
      "incomplete_value": false,
      "site": "00b4605c",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae62d4",
      "incomplete_value": false,
      "site": "00ae62d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae62e4",
      "incomplete_value": true,
      "site": "00ae62f0",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0448",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125308",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae62d0 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae62d4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b46054 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b46058 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae62d8 ["INT_ADD", "register:40f0:8", ["const:ae62d8:8", "const:4:8"]]
+ 00b4605c ["INT_ADD", "register:40f0:8", ["const:b4605c:8", "const:4:8"]]
- 00ae62dc ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae62e0 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 00b46060 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46064 ["COPY", "tmp:0:8", ["const:308:8"]]
~~~


### [`00ae62f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62f4.md) → [`00b46078`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46078.md) _ZN8firebase4util10uribuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b460b8",
      "incomplete_value": true,
      "site": "00b460b8",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6334",
      "incomplete_value": true,
      "site": "00ae6334",
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
            "const:438:8"
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
      "definition_site": "00b46094",
      "incomplete_value": true,
      "site": "00b46094",
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
    "old": {
      "definition_site": "00ae6310",
      "incomplete_value": true,
      "site": "00ae6310",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b460a0",
      "incomplete_value": true,
      "site": "00b460b0",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      20,
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6300 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b46084 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae6308 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00b4608c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
- 00ae6310 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6314 ["COPY", "register:4018:8", ["const:29e000:8"]]
- 00ae6318 ["COPY", "tmp:0:8", ["const:eaa:8"]]
+ 00b46094 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46098 ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00b4609c ["COPY", "tmp:0:8", ["const:2cd:8"]]
~~~


### [`00ae6364`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6364.md) → [`00b460e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b460e8.md) _ZN8firebase4util10uribuilder10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46104",
      "incomplete_value": false,
      "site": "00b46108",
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
            "const:451:8"
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
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b46114",
      "incomplete_value": true,
      "site": "00b46120",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6390",
      "incomplete_value": true,
      "site": "00ae639c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0460",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125320",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6378 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae637c ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae6380 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b460fc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46100 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b46104 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae6384 ["INT_ADD", "register:40f0:8", ["const:ae6384:8", "const:4:8"]]
+ 00b46108 ["INT_ADD", "register:40f0:8", ["const:b46108:8", "const:4:8"]]
- 00ae6388 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae638c ["COPY", "tmp:0:8", ["const:460:8"]]
+ 00b4610c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46110 ["COPY", "tmp:0:8", ["const:320:8"]]
~~~


### [`00ae63a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63a0.md) → [`00b46124`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46124.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46150",
      "incomplete_value": true,
      "site": "00b46150",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae63cc",
      "incomplete_value": true,
      "site": "00ae63cc",
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
            "const:468:8"
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
      "definition_site": "00b46138",
      "incomplete_value": true,
      "site": "00b46138",
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
    "old": {
      "definition_site": "00ae63b4",
      "incomplete_value": true,
      "site": "00ae63b4",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46144",
      "incomplete_value": false,
      "site": "00b46148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae63c0",
      "incomplete_value": true,
      "site": "00ae63c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:156:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae63ac ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae63b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00b46130 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46134 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae63b4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b46138 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae63bc ["COPY", "register:4018:8", ["const:2ac000:8"]]
- 00ae63c0 ["COPY", "tmp:0:8", ["const:156:8"]]
+ 00b46140 ["COPY", "register:4018:8", ["const:2bd000:8"]]
+ 00b46144 ["COPY", "tmp:0:8", ["const:e1:8"]]
~~~


### [`00ae63e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63e0.md) → [`00b46164`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46164.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46190",
      "incomplete_value": true,
      "site": "00b46190",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae640c",
      "incomplete_value": true,
      "site": "00ae640c",
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
            "const:468:8"
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
      "definition_site": "00b46178",
      "incomplete_value": true,
      "site": "00b46178",
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
    "old": {
      "definition_site": "00ae63f4",
      "incomplete_value": true,
      "site": "00ae63f4",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46180",
      "incomplete_value": false,
      "site": "00b46188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae63fc",
      "incomplete_value": false,
      "site": "00ae6404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:156:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae63ec ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae63f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00b46170 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46174 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae63f8 ["COPY", "register:4018:8", ["const:2ac000:8"]]
- 00ae63fc ["COPY", "tmp:0:8", ["const:156:8"]]
+ 00b4617c ["COPY", "register:4018:8", ["const:2bd000:8"]]
+ 00b46180 ["COPY", "tmp:0:8", ["const:e1:8"]]
- 00ae6404 ["INT_ADD", "register:40f0:8", ["const:ae6404:8", "const:4:8"]]
+ 00b46188 ["INT_ADD", "register:40f0:8", ["const:b46188:8", "const:4:8"]]
~~~


### [`00ae6420`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6420.md) → [`00b461a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461a4.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b461d4",
      "incomplete_value": true,
      "site": "00b461d4",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6450",
      "incomplete_value": true,
      "site": "00ae6450",
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
            "const:468:8"
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
      "definition_site": "00b461b8",
      "incomplete_value": true,
      "site": "00b461b8",
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
    "old": {
      "definition_site": "00ae6434",
      "incomplete_value": true,
      "site": "00ae6434",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae6440",
      "incomplete_value": false,
      "site": "00ae6448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:156:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae642c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6430 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00b461b0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b461b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae6434 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6438 ["COPY", "register:4018:8", ["const:2ac000:8"]]
+ 00b461b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b461bc ["COPY", "register:4018:8", ["const:2bd000:8"]]
- 00ae6440 ["COPY", "tmp:0:8", ["const:156:8"]]
+ 00b461c4 ["COPY", "tmp:0:8", ["const:e1:8"]]
~~~


### [`00ae6464`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6464.md) → [`00b461e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461e8.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46218",
      "incomplete_value": true,
      "site": "00b46218",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6494",
      "incomplete_value": true,
      "site": "00ae6494",
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
            "const:468:8"
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
      "definition_site": "00b461fc",
      "incomplete_value": true,
      "site": "00b461fc",
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
    "old": {
      "definition_site": "00ae6478",
      "incomplete_value": true,
      "site": "00ae6478",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46204",
      "incomplete_value": false,
      "site": "00b46210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6480",
      "incomplete_value": false,
      "site": "00ae648c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:156:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6470 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6474 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00b461f4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b461f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae6478 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae647c ["COPY", "register:4018:8", ["const:2ac000:8"]]
- 00ae6480 ["COPY", "tmp:0:8", ["const:156:8"]]
+ 00b461fc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46200 ["COPY", "register:4018:8", ["const:2bd000:8"]]
+ 00b46204 ["COPY", "tmp:0:8", ["const:e1:8"]]
- 00ae648c ["INT_ADD", "register:40f0:8", ["const:ae648c:8", "const:4:8"]]
+ 00b46210 ["INT_ADD", "register:40f0:8", ["const:b46210:8", "const:4:8"]]
~~~


### [`00ae64a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae64a8.md) → [`00b4622c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4622c.md) _ZN8firebase4util3url8GetClassEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b46230",
      "incomplete_value": true,
      "site": "00b46234",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:328:8"
              ]
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      4,
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      4,
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae64a8 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae64ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:468:8"]]
+ 00b4622c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46230 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
~~~


### [`00ae64b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae64b4.md) → [`00b46238`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46238.md) _ZN8firebase4util3url15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4623c",
      "incomplete_value": true,
      "site": "00b4623c",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae64b8",
      "incomplete_value": true,
      "site": "00ae64b8",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4623c",
      "incomplete_value": true,
      "site": "00b4623c",
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
      "definition_site": "00ae64b8",
      "incomplete_value": true,
      "site": "00ae64b8",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46240",
      "incomplete_value": true,
      "site": "00b46240",
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
      "definition_site": "00ae64bc",
      "incomplete_value": true,
      "site": "00ae64bc",
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
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0470",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125330",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae64c4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae64c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:470:8"]]
+ 00b46248 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4624c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:330:8"]]
- 00ae64cc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b46250 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae64d4 ["BRANCH", null, ["local:b8:8"]]
+ 00b46258 ["BRANCH", null, ["local:b6:8"]]
~~~


### [`00ae6550`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6550.md) → [`00b462d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b462d4.md) _ZN8firebase4util3url12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46310",
      "incomplete_value": true,
      "site": "00b46310",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae658c",
      "incomplete_value": true,
      "site": "00ae658c",
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
            "const:470:8"
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
      "definition_site": "00b46360",
      "incomplete_value": true,
      "site": "00b46360",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae65dc",
      "incomplete_value": true,
      "site": "00ae65dc",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b462ec",
      "incomplete_value": true,
      "site": "00b462ec",
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
      "definition_site": "00ae6568",
      "incomplete_value": true,
      "site": "00ae6568",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4008:8"
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
      20,
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0470",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125330",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6560 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae6564 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:468:8"]]
+ 00b462e4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b462e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00ae6568 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ae656c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae6570 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:470:8"]]
+ 00b462ec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b462f0 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b462f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:330:8"]]
- 00ae6578 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b462fc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`00ae65f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae65f0.md) → [`00b46374`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46374.md) _ZN8firebase4util3url14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b463b4",
      "incomplete_value": true,
      "site": "00b463b4",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6630",
      "incomplete_value": true,
      "site": "00ae6630",
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
            "const:468:8"
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
      "definition_site": "00b46390",
      "incomplete_value": true,
      "site": "00b46390",
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
    "old": {
      "definition_site": "00ae660c",
      "incomplete_value": true,
      "site": "00ae660c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "live",
            "register:4008:8"
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
      "definition_site": "00b46398",
      "incomplete_value": false,
      "site": "00b463ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6614",
      "incomplete_value": false,
      "site": "00ae6628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:156:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae65fc ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b46380 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae6604 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:468:8"]]
+ 00b46388 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00ae660c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae6610 ["COPY", "register:4018:8", ["const:2ac000:8"]]
- 00ae6614 ["COPY", "tmp:0:8", ["const:156:8"]]
+ 00b46390 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46394 ["COPY", "register:4018:8", ["const:2bd000:8"]]
+ 00b46398 ["COPY", "tmp:0:8", ["const:e1:8"]]
~~~


### [`00ae6660`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6660.md) → [`00b463e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b463e4.md) _ZN8firebase4util3url11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b463e8",
      "incomplete_value": true,
      "site": "00b463e8",
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
    "old": {
      "definition_site": "00ae6664",
      "incomplete_value": true,
      "site": "00ae6664",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b463e8",
      "incomplete_value": true,
      "site": "00b463e8",
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
      "definition_site": "00ae6664",
      "incomplete_value": true,
      "site": "00ae6664",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46400",
      "incomplete_value": false,
      "site": "00b46404",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae667c",
      "incomplete_value": false,
      "site": "00ae6680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      28,
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125338",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6674 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae6678 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae667c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b463f8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b463fc ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b46400 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae6680 ["INT_ADD", "register:40f0:8", ["const:ae6680:8", "const:4:8"]]
+ 00b46404 ["INT_ADD", "register:40f0:8", ["const:b46404:8", "const:4:8"]]
- 00ae6684 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae6688 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00b46408 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4640c ["COPY", "tmp:0:8", ["const:338:8"]]
~~~


### [`00ae669c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae669c.md) → [`00b46420`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46420.md) _ZN8firebase4util3url13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46460",
      "incomplete_value": true,
      "site": "00b46460",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae66dc",
      "incomplete_value": true,
      "site": "00ae66dc",
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
            "const:468:8"
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
      "definition_site": "00b4643c",
      "incomplete_value": true,
      "site": "00b4643c",
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
    "old": {
      "definition_site": "00ae66b8",
      "incomplete_value": true,
      "site": "00ae66b8",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae66cc",
      "incomplete_value": false,
      "site": "00ae66d4",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae66a8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4642c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae66b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:468:8"]]
+ 00b46434 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00ae66bc ["COPY", "register:4018:8", ["const:2ac000:8"]]
- 00ae66c0 ["COPY", "tmp:0:8", ["const:156:8"]]
+ 00b46440 ["COPY", "register:4018:8", ["const:2bd000:8"]]
+ 00b46444 ["COPY", "tmp:0:8", ["const:e1:8"]]
~~~


### [`00ae670c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae670c.md) → [`00b46490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46490.md) _ZN8firebase4util3url10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b464ac",
      "incomplete_value": false,
      "site": "00b464b0",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6728",
      "incomplete_value": false,
      "site": "00ae672c",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b464bc",
      "incomplete_value": true,
      "site": "00b464c8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0488",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125348",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6724 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae6728 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b464a8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b464ac ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae672c ["INT_ADD", "register:40f0:8", ["const:ae672c:8", "const:4:8"]]
+ 00b464b0 ["INT_ADD", "register:40f0:8", ["const:b464b0:8", "const:4:8"]]
- 00ae6730 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae6734 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00b464b4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b464b8 ["COPY", "tmp:0:8", ["const:348:8"]]
~~~


### [`00ae6748`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6748.md) → [`00b464cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b464cc.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b464f8",
      "incomplete_value": true,
      "site": "00b464f8",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6774",
      "incomplete_value": true,
      "site": "00ae6774",
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
            "const:490:8"
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
      "definition_site": "00b464e0",
      "incomplete_value": true,
      "site": "00b464e0",
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
    "old": {
      "definition_site": "00ae675c",
      "incomplete_value": true,
      "site": "00ae675c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b464ec",
      "incomplete_value": false,
      "site": "00b464f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6768",
      "incomplete_value": false,
      "site": "00ae676c",
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
            "const:ff7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6754 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6758 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00b464d8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b464dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae675c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b464e0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6764 ["COPY", "register:4018:8", ["const:29f000:8"]]
- 00ae6768 ["COPY", "tmp:0:8", ["const:ff7:8"]]
+ 00b464e8 ["COPY", "register:4018:8", ["const:2b0000:8"]]
+ 00b464ec ["COPY", "tmp:0:8", ["const:4f4:8"]]
~~~


### [`00ae6788`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6788.md) → [`00b4650c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4650c.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46538",
      "incomplete_value": true,
      "site": "00b46538",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae67b4",
      "incomplete_value": true,
      "site": "00ae67b4",
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
            "const:490:8"
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
      "definition_site": "00b46520",
      "incomplete_value": true,
      "site": "00b46520",
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
    "old": {
      "definition_site": "00ae679c",
      "incomplete_value": true,
      "site": "00ae679c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae67a4",
      "incomplete_value": true,
      "site": "00ae67ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:ff7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6794 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6798 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00b46518 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4651c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae679c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae67a0 ["COPY", "register:4018:8", ["const:29f000:8"]]
- 00ae67a4 ["COPY", "tmp:0:8", ["const:ff7:8"]]
+ 00b46520 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b46524 ["COPY", "register:4018:8", ["const:2b0000:8"]]
+ 00b46528 ["COPY", "tmp:0:8", ["const:4f4:8"]]
- 00ae67ac ["INT_ADD", "register:40f0:8", ["const:ae67ac:8", "const:4:8"]]
+ 00b46530 ["INT_ADD", "register:40f0:8", ["const:b46530:8", "const:4:8"]]
~~~


### [`00ae67c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae67c8.md) → [`00b4654c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4654c.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4657c",
      "incomplete_value": true,
      "site": "00b4657c",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae67f8",
      "incomplete_value": true,
      "site": "00ae67f8",
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
            "const:490:8"
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
      "definition_site": "00b46560",
      "incomplete_value": true,
      "site": "00b46560",
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
    "old": {
      "definition_site": "00ae67dc",
      "incomplete_value": true,
      "site": "00ae67dc",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae67e8",
      "incomplete_value": false,
      "site": "00ae67f0",
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
            "const:ff7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae67d4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae67d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00b46558 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4655c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae67dc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae67e0 ["COPY", "register:4018:8", ["const:29f000:8"]]
+ 00b46560 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b46564 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00ae67e8 ["COPY", "tmp:0:8", ["const:ff7:8"]]
+ 00b4656c ["COPY", "tmp:0:8", ["const:4f4:8"]]
~~~


### [`00ae680c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae680c.md) → [`00b46590`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46590.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b465c0",
      "incomplete_value": true,
      "site": "00b465c0",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae683c",
      "incomplete_value": true,
      "site": "00ae683c",
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
            "const:490:8"
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
      "definition_site": "00b465a4",
      "incomplete_value": true,
      "site": "00b465a4",
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
    "old": {
      "definition_site": "00ae6820",
      "incomplete_value": true,
      "site": "00ae6820",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b465ac",
      "incomplete_value": false,
      "site": "00b465b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6828",
      "incomplete_value": true,
      "site": "00ae6834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:ff7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6818 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae681c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00b4659c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b465a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae6820 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6824 ["COPY", "register:4018:8", ["const:29f000:8"]]
- 00ae6828 ["COPY", "tmp:0:8", ["const:ff7:8"]]
+ 00b465a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b465a8 ["COPY", "register:4018:8", ["const:2b0000:8"]]
+ 00b465ac ["COPY", "tmp:0:8", ["const:4f4:8"]]
- 00ae6834 ["INT_ADD", "register:40f0:8", ["const:ae6834:8", "const:4:8"]]
+ 00b465b8 ["INT_ADD", "register:40f0:8", ["const:b465b8:8", "const:4:8"]]
~~~


### [`00ae685c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae685c.md) → [`00b465e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b465e0.md) _ZN8firebase4util18file_output_stream15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b465e4",
      "incomplete_value": true,
      "site": "00b465e4",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6860",
      "incomplete_value": true,
      "site": "00ae6860",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b465e4",
      "incomplete_value": true,
      "site": "00b465e4",
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
      "definition_site": "00ae6860",
      "incomplete_value": true,
      "site": "00ae6860",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b465e8",
      "incomplete_value": true,
      "site": "00b465e8",
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
      "definition_site": "00ae6864",
      "incomplete_value": true,
      "site": "00ae6864",
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
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0498",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0498",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125358",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125358",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae686c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae6870 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:498:8"]]
+ 00b465f0 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b465f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:358:8"]]
- 00ae6874 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b465f8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae687c ["BRANCH", null, ["local:b9:8"]]
+ 00b46600 ["BRANCH", null, ["local:b5:8"]]
~~~


### [`00ae68f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae68f8.md) → [`00b4667c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4667c.md) _ZN8firebase4util18file_output_stream12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b466b8",
      "incomplete_value": true,
      "site": "00b466b8",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6934",
      "incomplete_value": true,
      "site": "00ae6934",
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
            "const:498:8"
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
      "definition_site": "00b46708",
      "incomplete_value": true,
      "site": "00b46708",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6984",
      "incomplete_value": true,
      "site": "00ae6984",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46694",
      "incomplete_value": true,
      "site": "00b46694",
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
      "definition_site": "00ae6910",
      "incomplete_value": true,
      "site": "00ae6910",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0498",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0498",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125358",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125358",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6908 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae690c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:490:8"]]
+ 00b4668c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b46690 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00ae6914 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae6918 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:498:8"]]
+ 00b46698 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4669c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:358:8"]]
- 00ae6930 ["INT_ADD", "register:40f0:8", ["const:ae6930:8", "const:4:8"]]
+ 00b466b4 ["INT_ADD", "register:40f0:8", ["const:b466b4:8", "const:4:8"]]
~~~


### [`00ae6998`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6998.md) → [`00b4671c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4671c.md) _ZN8firebase4util18file_output_stream14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46720",
      "incomplete_value": true,
      "site": "00b46720",
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
    "old": {
      "definition_site": "00ae699c",
      "incomplete_value": true,
      "site": "00ae699c",
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
      "definition_site": "00b46720",
      "incomplete_value": true,
      "site": "00b46720",
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
      "definition_site": "00ae699c",
      "incomplete_value": true,
      "site": "00ae699c",
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
      "definition_site": "00b4675c",
      "incomplete_value": true,
      "site": "00b4675c",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae69d8",
      "incomplete_value": true,
      "site": "00ae69d8",
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
            "const:490:8"
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
      20,
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae69a4 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b46728 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae69ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:490:8"]]
+ 00b46730 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00ae69b4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae69b8 ["COPY", "register:4018:8", ["const:29f000:8"]]
- 00ae69bc ["COPY", "tmp:0:8", ["const:ff7:8"]]
+ 00b46738 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4673c ["COPY", "register:4018:8", ["const:2b0000:8"]]
+ 00b46740 ["COPY", "tmp:0:8", ["const:4f4:8"]]
~~~


### [`00ae6a08`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a08.md) → [`00b4678c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4678c.md) _ZN8firebase4util18file_output_stream11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b467a8",
      "incomplete_value": false,
      "site": "00b467ac",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6a24",
      "incomplete_value": false,
      "site": "00ae6a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b467b8",
      "incomplete_value": true,
      "site": "00b467c4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6a34",
      "incomplete_value": true,
      "site": "00ae6a40",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125360",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6a1c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6a20 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae6a24 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b467a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b467a4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b467a8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae6a28 ["INT_ADD", "register:40f0:8", ["const:ae6a28:8", "const:4:8"]]
+ 00b467ac ["INT_ADD", "register:40f0:8", ["const:b467ac:8", "const:4:8"]]
- 00ae6a2c ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae6a30 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 00b467b0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b467b4 ["COPY", "tmp:0:8", ["const:360:8"]]
~~~


### [`00ae6a44`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a44.md) → [`00b467c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b467c8.md) _ZN8firebase4util18file_output_stream13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46808",
      "incomplete_value": true,
      "site": "00b46808",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6a84",
      "incomplete_value": true,
      "site": "00ae6a84",
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
            "const:490:8"
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
      "definition_site": "00b467e4",
      "incomplete_value": true,
      "site": "00b467e4",
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
    "old": {
      "definition_site": "00ae6a60",
      "incomplete_value": true,
      "site": "00ae6a60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "live",
            "register:4008:8"
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
      "definition_site": "00b467f0",
      "incomplete_value": true,
      "site": "00b46800",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      20,
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6a50 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b467d4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae6a58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:490:8"]]
+ 00b467dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00ae6a60 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae6a64 ["COPY", "register:4018:8", ["const:29f000:8"]]
- 00ae6a68 ["COPY", "tmp:0:8", ["const:ff7:8"]]
+ 00b467e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b467e8 ["COPY", "register:4018:8", ["const:2b0000:8"]]
+ 00b467ec ["COPY", "tmp:0:8", ["const:4f4:8"]]
~~~


### [`00ae6ab4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ab4.md) → [`00b46838`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46838.md) _ZN8firebase4util18file_output_stream10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4684c",
      "incomplete_value": true,
      "site": "00b4684c",
      "value": [
        "INT_NOTEQUAL",
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
                "register:4000:4"
              ],
              [
                "leaf",
                "const:1:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ac8",
      "incomplete_value": true,
      "site": "00ae6ac8",
      "value": [
        "INT_NOTEQUAL",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46854",
      "incomplete_value": false,
      "site": "00b46858",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ad0",
      "incomplete_value": false,
      "site": "00ae6ad4",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b46864",
      "incomplete_value": true,
      "site": "00b46870",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ae0",
      "incomplete_value": true,
      "site": "00ae6aec",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a04b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125378",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6ac8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6acc ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae6ad0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b4684c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46850 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b46854 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae6ad4 ["INT_ADD", "register:40f0:8", ["const:ae6ad4:8", "const:4:8"]]
+ 00b46858 ["INT_ADD", "register:40f0:8", ["const:b46858:8", "const:4:8"]]
- 00ae6ad8 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae6adc ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 00b4685c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46860 ["COPY", "tmp:0:8", ["const:378:8"]]
~~~


### [`00ae6af0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6af0.md) → [`00b46874`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46874.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b468a0",
      "incomplete_value": true,
      "site": "00b468a0",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b1c",
      "incomplete_value": true,
      "site": "00ae6b1c",
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
            "const:4c0:8"
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
      "definition_site": "00b46888",
      "incomplete_value": true,
      "site": "00b46888",
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
      "definition_site": "00ae6b04",
      "incomplete_value": true,
      "site": "00ae6b04",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46894",
      "incomplete_value": false,
      "site": "00b46898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b10",
      "incomplete_value": false,
      "site": "00ae6b14",
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
            "const:d9a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6afc ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6b00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00b46880 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46884 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:380:8"]]
- 00ae6b04 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46888 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6b0c ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00ae6b10 ["COPY", "tmp:0:8", ["const:d9a:8"]]
+ 00b46890 ["COPY", "register:4018:8", ["const:2b8000:8"]]
+ 00b46894 ["COPY", "tmp:0:8", ["const:a16:8"]]
~~~


### [`00ae6b30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b30.md) → [`00b468b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468b4.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b468e0",
      "incomplete_value": true,
      "site": "00b468e0",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b5c",
      "incomplete_value": true,
      "site": "00ae6b5c",
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
            "const:4c0:8"
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
      "definition_site": "00b468c8",
      "incomplete_value": true,
      "site": "00b468c8",
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
    "old": {
      "definition_site": "00ae6b44",
      "incomplete_value": true,
      "site": "00ae6b44",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b468d0",
      "incomplete_value": false,
      "site": "00b468d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b4c",
      "incomplete_value": false,
      "site": "00ae6b54",
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
            "const:d9a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6b3c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6b40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00b468c0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b468c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:380:8"]]
- 00ae6b44 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6b48 ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00ae6b4c ["COPY", "tmp:0:8", ["const:d9a:8"]]
+ 00b468c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b468cc ["COPY", "register:4018:8", ["const:2b8000:8"]]
+ 00b468d0 ["COPY", "tmp:0:8", ["const:a16:8"]]
- 00ae6b54 ["INT_ADD", "register:40f0:8", ["const:ae6b54:8", "const:4:8"]]
+ 00b468d8 ["INT_ADD", "register:40f0:8", ["const:b468d8:8", "const:4:8"]]
~~~


### [`00ae6b70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b70.md) → [`00b468f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468f4.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46924",
      "incomplete_value": true,
      "site": "00b46924",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ba0",
      "incomplete_value": true,
      "site": "00ae6ba0",
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
            "const:4c0:8"
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
      "definition_site": "00b46908",
      "incomplete_value": true,
      "site": "00b46908",
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
      "definition_site": "00ae6b84",
      "incomplete_value": true,
      "site": "00ae6b84",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae6b94",
      "incomplete_value": false,
      "site": "00ae6b98",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6b7c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6b80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00b46900 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46904 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:380:8"]]
- 00ae6b84 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae6b88 ["COPY", "register:4018:8", ["const:2a7000:8"]]
+ 00b46908 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b4690c ["COPY", "register:4018:8", ["const:2b8000:8"]]
- 00ae6b90 ["COPY", "tmp:0:8", ["const:d9a:8"]]
+ 00b46914 ["COPY", "tmp:0:8", ["const:a16:8"]]
~~~


### [`00ae6bb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6bb4.md) → [`00b46938`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46938.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4693c",
      "incomplete_value": true,
      "site": "00b4693c",
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
    "old": {
      "definition_site": "00ae6bb8",
      "incomplete_value": true,
      "site": "00ae6bb8",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4693c",
      "incomplete_value": true,
      "site": "00b4693c",
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
      "definition_site": "00ae6bb8",
      "incomplete_value": true,
      "site": "00ae6bb8",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46968",
      "incomplete_value": true,
      "site": "00b46968",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6be4",
      "incomplete_value": true,
      "site": "00ae6be4",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6bc0 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6bc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00b46944 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46948 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:380:8"]]
- 00ae6bc8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6bcc ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00ae6bd0 ["COPY", "tmp:0:8", ["const:d9a:8"]]
+ 00b4694c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46950 ["COPY", "register:4018:8", ["const:2b8000:8"]]
+ 00b46954 ["COPY", "tmp:0:8", ["const:a16:8"]]
- 00ae6bdc ["INT_ADD", "register:40f0:8", ["const:ae6bdc:8", "const:4:8"]]
+ 00b46960 ["INT_ADD", "register:40f0:8", ["const:b46960:8", "const:4:8"]]
~~~


### [`00ae6bf8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6bf8.md) → [`00b4697c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4697c.md) _ZN8firebase4util16dex_class_loader8GetClassEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b46980",
      "incomplete_value": true,
      "site": "00b46984",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:380:8"
              ]
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      4,
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      4,
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6bf8 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae6bfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
+ 00b4697c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46980 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:380:8"]]
~~~


### [`00ae6c04`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6c04.md) → [`00b46988`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46988.md) _ZN8firebase4util16dex_class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46a10",
      "incomplete_value": true,
      "site": "00b46a10",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6c8c",
      "incomplete_value": true,
      "site": "00ae6c8c",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00b469c8",
      "incomplete_value": true,
      "site": "00b469c8",
      "value": [
        "LOAD",
        "8",
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
                "const:6b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6c44",
      "incomplete_value": true,
      "site": "00ae6c44",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b469bc",
      "incomplete_value": true,
      "site": "00b469c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:380:8"
              ]
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
      20,
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125388",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125388",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6c14 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae6c18 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4c8:8"]]
+ 00b46998 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4699c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:388:8"]]
- 00ae6c24 ["BRANCH", null, ["local:b8:8"]]
+ 00b469a8 ["BRANCH", null, ["local:b5:8"]]
- 00ae6c2c ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b469b0 ["COPY", "register:4048:8", ["const:1125000:8"]]
~~~


### [`00ae6ca0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ca0.md) → [`00b46a24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46a24.md) _ZN8firebase4util16dex_class_loader12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46a60",
      "incomplete_value": true,
      "site": "00b46a60",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6cdc",
      "incomplete_value": true,
      "site": "00ae6cdc",
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
            "const:4c8:8"
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
      "definition_site": "00b46ab0",
      "incomplete_value": true,
      "site": "00b46ab0",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6d2c",
      "incomplete_value": true,
      "site": "00ae6d2c",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46a3c",
      "incomplete_value": true,
      "site": "00b46a3c",
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
      "definition_site": "00ae6cb8",
      "incomplete_value": true,
      "site": "00ae6cb8",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125388",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125388",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6cb0 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae6cb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
+ 00b46a34 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b46a38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:380:8"]]
- 00ae6cbc ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae6cc0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4c8:8"]]
+ 00b46a40 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b46a44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:388:8"]]
- 00ae6cd8 ["INT_ADD", "register:40f0:8", ["const:ae6cd8:8", "const:4:8"]]
+ 00b46a5c ["INT_ADD", "register:40f0:8", ["const:b46a5c:8", "const:4:8"]]
~~~


### [`00ae6d40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6d40.md) → [`00b46ac4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ac4.md) _ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46b04",
      "incomplete_value": true,
      "site": "00b46b04",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6d80",
      "incomplete_value": true,
      "site": "00ae6d80",
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
            "const:4c0:8"
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
      "definition_site": "00b46ae0",
      "incomplete_value": true,
      "site": "00b46ae0",
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
    "old": {
      "definition_site": "00ae6d5c",
      "incomplete_value": true,
      "site": "00ae6d5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "live",
            "register:4008:8"
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
      "definition_site": "00b46ae8",
      "incomplete_value": false,
      "site": "00b46afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6d64",
      "incomplete_value": false,
      "site": "00ae6d78",
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
            "const:d9a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6d4c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b46ad0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae6d54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
+ 00b46ad8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:380:8"]]
- 00ae6d5c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae6d60 ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00ae6d64 ["COPY", "tmp:0:8", ["const:d9a:8"]]
+ 00b46ae0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b46ae4 ["COPY", "register:4018:8", ["const:2b8000:8"]]
+ 00b46ae8 ["COPY", "tmp:0:8", ["const:a16:8"]]
~~~


### [`00ae6db0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6db0.md) → [`00b46b34`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b34.md) _ZN8firebase4util16dex_class_loader11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46b50",
      "incomplete_value": false,
      "site": "00b46b54",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6dcc",
      "incomplete_value": false,
      "site": "00ae6dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b46b60",
      "incomplete_value": true,
      "site": "00b46b6c",
      "value": [
        "LOAD",
        "8",
        [
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ddc",
      "incomplete_value": true,
      "site": "00ae6de8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a04d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6dc4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6dc8 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae6dcc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b46b48 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46b4c ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b46b50 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae6dd0 ["INT_ADD", "register:40f0:8", ["const:ae6dd0:8", "const:4:8"]]
+ 00b46b54 ["INT_ADD", "register:40f0:8", ["const:b46b54:8", "const:4:8"]]
- 00ae6dd4 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae6dd8 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 00b46b58 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46b5c ["COPY", "tmp:0:8", ["const:390:8"]]
~~~


### [`00ae6dec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6dec.md) → [`00b46b70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b70.md) _ZN8firebase4util16dex_class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46bb0",
      "incomplete_value": true,
      "site": "00b46bb0",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6e2c",
      "incomplete_value": true,
      "site": "00ae6e2c",
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
            "const:4c0:8"
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
      "definition_site": "00b46b8c",
      "incomplete_value": true,
      "site": "00b46b8c",
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
    "old": {
      "definition_site": "00ae6e08",
      "incomplete_value": true,
      "site": "00ae6e08",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae6e14",
      "incomplete_value": true,
      "site": "00ae6e24",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6df8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b46b7c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae6e00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
+ 00b46b84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:380:8"]]
- 00ae6e08 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6e0c ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00ae6e10 ["COPY", "tmp:0:8", ["const:d9a:8"]]
+ 00b46b8c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b46b90 ["COPY", "register:4018:8", ["const:2b8000:8"]]
+ 00b46b94 ["COPY", "tmp:0:8", ["const:a16:8"]]
~~~


### [`00ae6e5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e5c.md) → [`00b46be0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46be0.md) _ZN8firebase4util16dex_class_loader10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46bfc",
      "incomplete_value": false,
      "site": "00b46c00",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6e78",
      "incomplete_value": false,
      "site": "00ae6e7c",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b46c0c",
      "incomplete_value": true,
      "site": "00b46c18",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6e88",
      "incomplete_value": true,
      "site": "00ae6e94",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a04e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011253a0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6e74 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae6e78 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b46bf8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b46bfc ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae6e7c ["INT_ADD", "register:40f0:8", ["const:ae6e7c:8", "const:4:8"]]
+ 00b46c00 ["INT_ADD", "register:40f0:8", ["const:b46c00:8", "const:4:8"]]
- 00ae6e80 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae6e84 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00b46c04 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46c08 ["COPY", "tmp:0:8", ["const:3a0:8"]]
~~~


### [`00ae6e98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e98.md) → [`00b46c1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c1c.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46c48",
      "incomplete_value": true,
      "site": "00b46c48",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ec4",
      "incomplete_value": true,
      "site": "00ae6ec4",
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
            "const:4e8:8"
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
      "definition_site": "00b46c30",
      "incomplete_value": true,
      "site": "00b46c30",
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
    "old": {
      "definition_site": "00ae6eac",
      "incomplete_value": true,
      "site": "00ae6eac",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46c3c",
      "incomplete_value": false,
      "site": "00b46c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6eb8",
      "incomplete_value": false,
      "site": "00ae6ebc",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6ea4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6ea8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b46c28 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46c2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00ae6eb4 ["COPY", "register:4018:8", ["const:2a4000:8"]]
- 00ae6eb8 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b46c38 ["COPY", "register:4018:8", ["const:2b5000:8"]]
+ 00b46c3c ["COPY", "tmp:0:8", ["const:87d:8"]]
- 00ae6ebc ["INT_ADD", "register:40f0:8", ["const:ae6ebc:8", "const:4:8"]]
+ 00b46c40 ["INT_ADD", "register:40f0:8", ["const:b46c40:8", "const:4:8"]]
~~~


### [`00ae6ed8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ed8.md) → [`00b46c5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c5c.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46c88",
      "incomplete_value": true,
      "site": "00b46c88",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f04",
      "incomplete_value": true,
      "site": "00ae6f04",
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
            "const:4e8:8"
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
      "definition_site": "00b46c70",
      "incomplete_value": true,
      "site": "00b46c70",
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
    "old": {
      "definition_site": "00ae6eec",
      "incomplete_value": true,
      "site": "00ae6eec",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46c78",
      "incomplete_value": false,
      "site": "00b46c80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ef4",
      "incomplete_value": false,
      "site": "00ae6efc",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6ee4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6ee8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b46c68 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46c6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00ae6ef0 ["COPY", "register:4018:8", ["const:2a4000:8"]]
- 00ae6ef4 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b46c74 ["COPY", "register:4018:8", ["const:2b5000:8"]]
+ 00b46c78 ["COPY", "tmp:0:8", ["const:87d:8"]]
- 00ae6efc ["INT_ADD", "register:40f0:8", ["const:ae6efc:8", "const:4:8"]]
+ 00b46c80 ["INT_ADD", "register:40f0:8", ["const:b46c80:8", "const:4:8"]]
~~~


### [`00ae6f18`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f18.md) → [`00b46c9c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c9c.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46ccc",
      "incomplete_value": true,
      "site": "00b46ccc",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f48",
      "incomplete_value": true,
      "site": "00ae6f48",
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
            "const:4e8:8"
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
      "definition_site": "00b46cb0",
      "incomplete_value": true,
      "site": "00b46cb0",
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
    "old": {
      "definition_site": "00ae6f2c",
      "incomplete_value": true,
      "site": "00ae6f2c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46cbc",
      "incomplete_value": false,
      "site": "00b46cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f38",
      "incomplete_value": false,
      "site": "00ae6f40",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6f24 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6f28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b46ca8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46cac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00ae6f30 ["COPY", "register:4018:8", ["const:2a4000:8"]]
+ 00b46cb4 ["COPY", "register:4018:8", ["const:2b5000:8"]]
- 00ae6f38 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b46cbc ["COPY", "tmp:0:8", ["const:87d:8"]]
~~~


### [`00ae6f5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f5c.md) → [`00b46ce0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ce0.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46d10",
      "incomplete_value": true,
      "site": "00b46d10",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f8c",
      "incomplete_value": true,
      "site": "00ae6f8c",
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
            "const:4e8:8"
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
      "definition_site": "00b46cf4",
      "incomplete_value": true,
      "site": "00b46cf4",
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
    "old": {
      "definition_site": "00ae6f70",
      "incomplete_value": true,
      "site": "00ae6f70",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46cfc",
      "incomplete_value": false,
      "site": "00b46d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f78",
      "incomplete_value": false,
      "site": "00ae6f84",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6f68 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae6f6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b46cec ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46cf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00ae6f74 ["COPY", "register:4018:8", ["const:2a4000:8"]]
- 00ae6f78 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b46cf8 ["COPY", "register:4018:8", ["const:2b5000:8"]]
+ 00b46cfc ["COPY", "tmp:0:8", ["const:87d:8"]]
- 00ae6f84 ["INT_ADD", "register:40f0:8", ["const:ae6f84:8", "const:4:8"]]
+ 00b46d08 ["INT_ADD", "register:40f0:8", ["const:b46d08:8", "const:4:8"]]
~~~


### [`00ae6fac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6fac.md) → [`00b46d30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46d30.md) _ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46db8",
      "incomplete_value": true,
      "site": "00b46db8",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7034",
      "incomplete_value": true,
      "site": "00ae7034",
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
            "const:4f0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46d64",
      "incomplete_value": true,
      "site": "00b46d70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:3a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6fe0",
      "incomplete_value": true,
      "site": "00ae6fec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:4e8:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00b46dac",
      "incomplete_value": true,
      "site": "00b46dac",
      "value": [
        "LOAD",
        "8",
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
                "const:88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7028",
      "incomplete_value": true,
      "site": "00ae7028",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:88:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011253b0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "011253b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae6fbc ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae6fc0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4f0:8"]]
+ 00b46d40 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b46d44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3b0:8"]]
- 00ae6fcc ["BRANCH", null, ["local:b7:8"]]
+ 00b46d50 ["BRANCH", null, ["local:b5:8"]]
- 00ae6fd4 ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b46d58 ["COPY", "register:4048:8", ["const:1125000:8"]]
~~~


### [`00ae7048`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7048.md) → [`00b46dcc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46dcc.md) _ZN8firebase4util9resources12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46e08",
      "incomplete_value": true,
      "site": "00b46e08",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7084",
      "incomplete_value": true,
      "site": "00ae7084",
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
            "const:4f0:8"
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
      "definition_site": "00b46e58",
      "incomplete_value": true,
      "site": "00b46e58",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae70d4",
      "incomplete_value": true,
      "site": "00ae70d4",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46de4",
      "incomplete_value": true,
      "site": "00b46de4",
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
      "definition_site": "00ae7060",
      "incomplete_value": true,
      "site": "00ae7060",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011253b0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011253b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7058 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae705c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00b46ddc ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b46de0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
- 00ae7060 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae7064 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae7068 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4f0:8"]]
+ 00b46de4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b46de8 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b46dec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3b0:8"]]
- 00ae7080 ["INT_ADD", "register:40f0:8", ["const:ae7080:8", "const:4:8"]]
+ 00b46e04 ["INT_ADD", "register:40f0:8", ["const:b46e04:8", "const:4:8"]]
~~~


### [`00ae70e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae70e8.md) → [`00b46e6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46e6c.md) _ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46eac",
      "incomplete_value": true,
      "site": "00b46eac",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7128",
      "incomplete_value": true,
      "site": "00ae7128",
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
            "const:4e8:8"
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
      "definition_site": "00b46e88",
      "incomplete_value": true,
      "site": "00b46e88",
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
    "old": {
      "definition_site": "00ae7104",
      "incomplete_value": true,
      "site": "00ae7104",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46e94",
      "incomplete_value": true,
      "site": "00b46ea4",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      20,
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae70f4 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b46e78 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae70fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00b46e80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
- 00ae7104 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae7108 ["COPY", "register:4018:8", ["const:2a4000:8"]]
- 00ae710c ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b46e88 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b46e8c ["COPY", "register:4018:8", ["const:2b5000:8"]]
+ 00b46e90 ["COPY", "tmp:0:8", ["const:87d:8"]]
~~~


### [`00ae7158`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7158.md) → [`00b46edc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46edc.md) _ZN8firebase4util9resources11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46ef8",
      "incomplete_value": false,
      "site": "00b46efc",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7174",
      "incomplete_value": false,
      "site": "00ae7178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b46f08",
      "incomplete_value": true,
      "site": "00b46f14",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7184",
      "incomplete_value": true,
      "site": "00ae7190",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a04f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011253b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7170 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae7174 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b46ef4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b46ef8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae7178 ["INT_ADD", "register:40f0:8", ["const:ae7178:8", "const:4:8"]]
+ 00b46efc ["INT_ADD", "register:40f0:8", ["const:b46efc:8", "const:4:8"]]
- 00ae717c ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae7180 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00b46f00 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46f04 ["COPY", "tmp:0:8", ["const:3b8:8"]]
~~~


### [`00ae7194`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7194.md) → [`00b46f18`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f18.md) _ZN8firebase4util9resources13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46f58",
      "incomplete_value": true,
      "site": "00b46f58",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae71d4",
      "incomplete_value": true,
      "site": "00ae71d4",
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
            "const:4e8:8"
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
      "definition_site": "00b46f34",
      "incomplete_value": true,
      "site": "00b46f34",
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
    "old": {
      "definition_site": "00ae71b0",
      "incomplete_value": true,
      "site": "00ae71b0",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46f3c",
      "incomplete_value": false,
      "site": "00b46f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae71b8",
      "incomplete_value": false,
      "site": "00ae71cc",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae71a0 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b46f24 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae71a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00b46f2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
- 00ae71b0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae71b4 ["COPY", "register:4018:8", ["const:2a4000:8"]]
- 00ae71b8 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b46f34 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46f38 ["COPY", "register:4018:8", ["const:2b5000:8"]]
+ 00b46f3c ["COPY", "tmp:0:8", ["const:87d:8"]]
~~~


### [`00ae7204`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7204.md) → [`00b46f88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f88.md) _ZN8firebase4util9resources10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46fa4",
      "incomplete_value": false,
      "site": "00b46fa8",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7220",
      "incomplete_value": false,
      "site": "00ae7224",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b46fb4",
      "incomplete_value": true,
      "site": "00b46fc0",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7230",
      "incomplete_value": true,
      "site": "00ae723c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0500",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011253c0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae721c ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae7220 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b46fa0 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b46fa4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae7224 ["INT_ADD", "register:40f0:8", ["const:ae7224:8", "const:4:8"]]
+ 00b46fa8 ["INT_ADD", "register:40f0:8", ["const:b46fa8:8", "const:4:8"]]
- 00ae7228 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae722c ["COPY", "tmp:0:8", ["const:500:8"]]
+ 00b46fac ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b46fb0 ["COPY", "tmp:0:8", ["const:3c0:8"]]
~~~


### [`00ae7240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7240.md) → [`00b46fc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46fc4.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46ff0",
      "incomplete_value": true,
      "site": "00b46ff0",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae726c",
      "incomplete_value": true,
      "site": "00ae726c",
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
            "const:508:8"
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
      "definition_site": "00b46fd8",
      "incomplete_value": true,
      "site": "00b46fd8",
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
    "old": {
      "definition_site": "00ae7254",
      "incomplete_value": true,
      "site": "00ae7254",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46fe4",
      "incomplete_value": false,
      "site": "00b46fe8",
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
            "const:591:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7260",
      "incomplete_value": false,
      "site": "00ae7264",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae724c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7250 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00b46fd0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b46fd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00ae725c ["COPY", "register:4018:8", ["const:2ad000:8"]]
- 00ae7260 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b46fe0 ["COPY", "register:4018:8", ["const:2be000:8"]]
+ 00b46fe4 ["COPY", "tmp:0:8", ["const:591:8"]]
- 00ae7264 ["INT_ADD", "register:40f0:8", ["const:ae7264:8", "const:4:8"]]
+ 00b46fe8 ["INT_ADD", "register:40f0:8", ["const:b46fe8:8", "const:4:8"]]
~~~


### [`00ae7280`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7280.md) → [`00b47004`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47004.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47030",
      "incomplete_value": true,
      "site": "00b47030",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae72ac",
      "incomplete_value": true,
      "site": "00ae72ac",
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
            "const:508:8"
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
      "definition_site": "00b47018",
      "incomplete_value": true,
      "site": "00b47018",
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
    "old": {
      "definition_site": "00ae7294",
      "incomplete_value": true,
      "site": "00ae7294",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47020",
      "incomplete_value": false,
      "site": "00b47028",
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
            "const:591:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae729c",
      "incomplete_value": false,
      "site": "00ae72a4",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae728c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7290 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00b47010 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47014 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00ae7294 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae7298 ["COPY", "register:4018:8", ["const:2ad000:8"]]
- 00ae729c ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b47018 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4701c ["COPY", "register:4018:8", ["const:2be000:8"]]
+ 00b47020 ["COPY", "tmp:0:8", ["const:591:8"]]
- 00ae72a4 ["INT_ADD", "register:40f0:8", ["const:ae72a4:8", "const:4:8"]]
+ 00b47028 ["INT_ADD", "register:40f0:8", ["const:b47028:8", "const:4:8"]]
~~~


### [`00ae72c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae72c0.md) → [`00b47044`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47044.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47074",
      "incomplete_value": true,
      "site": "00b47074",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae72f0",
      "incomplete_value": true,
      "site": "00ae72f0",
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
            "const:508:8"
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
      "definition_site": "00b47058",
      "incomplete_value": true,
      "site": "00b47058",
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
    "old": {
      "definition_site": "00ae72d4",
      "incomplete_value": true,
      "site": "00ae72d4",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47064",
      "incomplete_value": false,
      "site": "00b4706c",
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
            "const:591:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae72e0",
      "incomplete_value": false,
      "site": "00ae72e8",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae72cc ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae72d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00b47050 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00ae72d8 ["COPY", "register:4018:8", ["const:2ad000:8"]]
+ 00b4705c ["COPY", "register:4018:8", ["const:2be000:8"]]
- 00ae72e0 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b47064 ["COPY", "tmp:0:8", ["const:591:8"]]
~~~


### [`00ae7304`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7304.md) → [`00b47088`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47088.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b470b8",
      "incomplete_value": true,
      "site": "00b470b8",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7334",
      "incomplete_value": true,
      "site": "00ae7334",
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
            "const:508:8"
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
      "definition_site": "00b4709c",
      "incomplete_value": true,
      "site": "00b4709c",
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
    "old": {
      "definition_site": "00ae7318",
      "incomplete_value": true,
      "site": "00ae7318",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b470a4",
      "incomplete_value": false,
      "site": "00b470b0",
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
            "const:591:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7320",
      "incomplete_value": false,
      "site": "00ae732c",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7310 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00b47094 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47098 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00ae731c ["COPY", "register:4018:8", ["const:2ad000:8"]]
- 00ae7320 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b470a0 ["COPY", "register:4018:8", ["const:2be000:8"]]
+ 00b470a4 ["COPY", "tmp:0:8", ["const:591:8"]]
- 00ae732c ["INT_ADD", "register:40f0:8", ["const:ae732c:8", "const:4:8"]]
+ 00b470b0 ["INT_ADD", "register:40f0:8", ["const:b470b0:8", "const:4:8"]]
~~~


### [`00ae7354`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7354.md) → [`00b470d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b470d8.md) _ZN8firebase4util8activity15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47160",
      "incomplete_value": true,
      "site": "00b47160",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae73dc",
      "incomplete_value": true,
      "site": "00ae73dc",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4710c",
      "incomplete_value": true,
      "site": "00b47118",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:3c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7388",
      "incomplete_value": true,
      "site": "00ae7394",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
      20,
      "READ",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7364 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae7368 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:510:8"]]
+ 00b470e8 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b470ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3d0:8"]]
- 00ae737c ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b47100 ["COPY", "register:4048:8", ["const:1125000:8"]]
- 00ae7388 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:508:8"]]
+ 00b4710c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3c8:8"]]
~~~


### [`00ae73f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae73f0.md) → [`00b47174`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47174.md) _ZN8firebase4util8activity12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b471b0",
      "incomplete_value": true,
      "site": "00b471b0",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae742c",
      "incomplete_value": true,
      "site": "00ae742c",
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
            "const:510:8"
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
      "definition_site": "00b47200",
      "incomplete_value": true,
      "site": "00b47200",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae747c",
      "incomplete_value": true,
      "site": "00ae747c",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4718c",
      "incomplete_value": true,
      "site": "00b4718c",
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
      "definition_site": "00ae7408",
      "incomplete_value": true,
      "site": "00ae7408",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7400 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae7404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00b47184 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b47188 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00ae7408 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ae740c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae7410 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:510:8"]]
+ 00b4718c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b47190 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b47194 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3d0:8"]]
- 00ae7418 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b4719c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`00ae7490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7490.md) → [`00b47214`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47214.md) _ZN8firebase4util8activity14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47254",
      "incomplete_value": true,
      "site": "00b47254",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae74d0",
      "incomplete_value": true,
      "site": "00ae74d0",
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
            "const:508:8"
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
      "definition_site": "00b47230",
      "incomplete_value": true,
      "site": "00b47230",
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
    "old": {
      "definition_site": "00ae74ac",
      "incomplete_value": true,
      "site": "00ae74ac",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47238",
      "incomplete_value": false,
      "site": "00b4724c",
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
            "const:591:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae749c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b47220 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae74a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00b47228 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00ae74ac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae74b0 ["COPY", "register:4018:8", ["const:2ad000:8"]]
- 00ae74b4 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b47230 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47234 ["COPY", "register:4018:8", ["const:2be000:8"]]
+ 00b47238 ["COPY", "tmp:0:8", ["const:591:8"]]
~~~


### [`00ae7500`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7500.md) → [`00b47284`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47284.md) _ZN8firebase4util8activity11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00bde6d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6d0.md) · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b150.md) · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b472a0",
      "incomplete_value": false,
      "site": "00b472a4",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae751c",
      "incomplete_value": false,
      "site": "00ae7520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b472b0",
      "incomplete_value": true,
      "site": "00b472bc",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae752c",
      "incomplete_value": true,
      "site": "00ae7538",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0518",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011253d8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7518 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae751c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b4729c ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b472a0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae7520 ["INT_ADD", "register:40f0:8", ["const:ae7520:8", "const:4:8"]]
+ 00b472a4 ["INT_ADD", "register:40f0:8", ["const:b472a4:8", "const:4:8"]]
- 00ae7524 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae7528 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00b472a8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b472ac ["COPY", "tmp:0:8", ["const:3d8:8"]]
~~~


### [`00ae753c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae753c.md) → [`00b472c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b472c0.md) _ZN8firebase4util8activity13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47300",
      "incomplete_value": true,
      "site": "00b47300",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae757c",
      "incomplete_value": true,
      "site": "00ae757c",
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
            "const:508:8"
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
      "definition_site": "00b472dc",
      "incomplete_value": true,
      "site": "00b472dc",
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
    "old": {
      "definition_site": "00ae7558",
      "incomplete_value": true,
      "site": "00ae7558",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b472e8",
      "incomplete_value": true,
      "site": "00b472f8",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      20,
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7548 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b472cc ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae7550 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00b472d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00ae7558 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae755c ["COPY", "register:4018:8", ["const:2ad000:8"]]
- 00ae7560 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b472dc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b472e0 ["COPY", "register:4018:8", ["const:2be000:8"]]
+ 00b472e4 ["COPY", "tmp:0:8", ["const:591:8"]]
~~~


### [`00ae75ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75ac.md) → [`00b47330`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47330.md) _ZN8firebase4util8activity10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4734c",
      "incomplete_value": false,
      "site": "00b47350",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae75c8",
      "incomplete_value": false,
      "site": "00ae75cc",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4735c",
      "incomplete_value": true,
      "site": "00b47368",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae75d8",
      "incomplete_value": true,
      "site": "00ae75e4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0568",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125428",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae75c4 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae75c8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b47348 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b4734c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae75cc ["INT_ADD", "register:40f0:8", ["const:ae75cc:8", "const:4:8"]]
+ 00b47350 ["INT_ADD", "register:40f0:8", ["const:b47350:8", "const:4:8"]]
- 00ae75d0 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae75d4 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00b47354 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47358 ["COPY", "tmp:0:8", ["const:428:8"]]
~~~


### [`00ae75e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75e8.md) → [`00b4736c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4736c.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47398",
      "incomplete_value": true,
      "site": "00b47398",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7614",
      "incomplete_value": true,
      "site": "00ae7614",
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
            "const:570:8"
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
      "definition_site": "00b47380",
      "incomplete_value": true,
      "site": "00b47380",
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
    "old": {
      "definition_site": "00ae75fc",
      "incomplete_value": true,
      "site": "00ae75fc",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4738c",
      "incomplete_value": false,
      "site": "00b47390",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7608",
      "incomplete_value": false,
      "site": "00ae760c",
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
            "const:497:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae75f4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae75f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b47378 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4737c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00ae75fc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47380 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7604 ["COPY", "register:4018:8", ["const:297000:8"]]
- 00ae7608 ["COPY", "tmp:0:8", ["const:497:8"]]
+ 00b47388 ["COPY", "register:4018:8", ["const:2a7000:8"]]
+ 00b4738c ["COPY", "tmp:0:8", ["const:38:8"]]
~~~


### [`00ae7628`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7628.md) → [`00b473ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ac.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b473b0",
      "incomplete_value": true,
      "site": "00b473b0",
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
    "old": {
      "definition_site": "00ae762c",
      "incomplete_value": true,
      "site": "00ae762c",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b473b0",
      "incomplete_value": true,
      "site": "00b473b0",
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
      "definition_site": "00ae762c",
      "incomplete_value": true,
      "site": "00ae762c",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b473d8",
      "incomplete_value": true,
      "site": "00b473d8",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7654",
      "incomplete_value": true,
      "site": "00ae7654",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7634 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7638 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b473b8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b473bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00ae763c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae7640 ["COPY", "register:4018:8", ["const:297000:8"]]
- 00ae7644 ["COPY", "tmp:0:8", ["const:497:8"]]
+ 00b473c0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b473c4 ["COPY", "register:4018:8", ["const:2a7000:8"]]
+ 00b473c8 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00ae764c ["INT_ADD", "register:40f0:8", ["const:ae764c:8", "const:4:8"]]
+ 00b473d0 ["INT_ADD", "register:40f0:8", ["const:b473d0:8", "const:4:8"]]
~~~


### [`00ae7668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7668.md) → [`00b473ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ec.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4741c",
      "incomplete_value": true,
      "site": "00b4741c",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7698",
      "incomplete_value": true,
      "site": "00ae7698",
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
            "const:570:8"
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
      "definition_site": "00b47400",
      "incomplete_value": true,
      "site": "00b47400",
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
    "old": {
      "definition_site": "00ae767c",
      "incomplete_value": true,
      "site": "00ae767c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4740c",
      "incomplete_value": false,
      "site": "00b47414",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7688",
      "incomplete_value": true,
      "site": "00ae7690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:497:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7674 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b473f8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b473fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00ae767c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7680 ["COPY", "register:4018:8", ["const:297000:8"]]
+ 00b47400 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47404 ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00ae7688 ["COPY", "tmp:0:8", ["const:497:8"]]
+ 00b4740c ["COPY", "tmp:0:8", ["const:38:8"]]
~~~


### [`00ae76ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76ac.md) → [`00b47430`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47430.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47460",
      "incomplete_value": true,
      "site": "00b47460",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae76dc",
      "incomplete_value": true,
      "site": "00ae76dc",
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
            "const:570:8"
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
      "definition_site": "00b47444",
      "incomplete_value": true,
      "site": "00b47444",
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
    "old": {
      "definition_site": "00ae76c0",
      "incomplete_value": true,
      "site": "00ae76c0",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4744c",
      "incomplete_value": false,
      "site": "00b47458",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae76c8",
      "incomplete_value": false,
      "site": "00ae76d4",
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
            "const:497:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae76b8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae76bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b4743c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47440 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00ae76c4 ["COPY", "register:4018:8", ["const:297000:8"]]
- 00ae76c8 ["COPY", "tmp:0:8", ["const:497:8"]]
+ 00b47448 ["COPY", "register:4018:8", ["const:2a7000:8"]]
+ 00b4744c ["COPY", "tmp:0:8", ["const:38:8"]]
- 00ae76d4 ["INT_ADD", "register:40f0:8", ["const:ae76d4:8", "const:4:8"]]
+ 00b47458 ["INT_ADD", "register:40f0:8", ["const:b47458:8", "const:4:8"]]
~~~


### [`00ae76f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76f0.md) → [`00b47474`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47474.md) _ZN8firebase4util10array_list8GetClassEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde040.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5aac0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aac0.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b47478",
      "incomplete_value": true,
      "site": "00b4747c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:430:8"
              ]
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      4,
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      4,
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae76f0 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae76f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 00b47474 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47478 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
~~~


### [`00ae76fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76fc.md) → [`00b47480`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47480.md) _ZN8firebase4util10array_list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47508",
      "incomplete_value": true,
      "site": "00b47508",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7784",
      "incomplete_value": true,
      "site": "00ae7784",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b474b4",
      "incomplete_value": true,
      "site": "00b474c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7730",
      "incomplete_value": true,
      "site": "00ae773c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
      20,
      "READ",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae770c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae7710 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
+ 00b47490 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b47494 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:438:8"]]
- 00ae7724 ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b474a8 ["COPY", "register:4048:8", ["const:1125000:8"]]
- 00ae7730 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:570:8"]]
+ 00b474b4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:430:8"]]
~~~


### [`00ae7798`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7798.md) → [`00b4751c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4751c.md) _ZN8firebase4util10array_list12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47558",
      "incomplete_value": true,
      "site": "00b47558",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae77d4",
      "incomplete_value": true,
      "site": "00ae77d4",
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
            "const:578:8"
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
      "definition_site": "00b475a8",
      "incomplete_value": true,
      "site": "00b475a8",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7824",
      "incomplete_value": true,
      "site": "00ae7824",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47534",
      "incomplete_value": true,
      "site": "00b47534",
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
      "definition_site": "00ae77b0",
      "incomplete_value": true,
      "site": "00ae77b0",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae77a8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae77ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00b4752c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b47530 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:430:8"]]
- 00ae77b0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae77b4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae77b8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
+ 00b47534 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b47538 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4753c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:438:8"]]
- 00ae77d0 ["INT_ADD", "register:40f0:8", ["const:ae77d0:8", "const:4:8"]]
+ 00b47554 ["INT_ADD", "register:40f0:8", ["const:b47554:8", "const:4:8"]]
~~~


### [`00ae7838`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7838.md) → [`00b475bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b475bc.md) _ZN8firebase4util10array_list14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b475fc",
      "incomplete_value": true,
      "site": "00b475fc",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7878",
      "incomplete_value": true,
      "site": "00ae7878",
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
            "const:570:8"
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
      "definition_site": "00b475d8",
      "incomplete_value": true,
      "site": "00b475d8",
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
    "old": {
      "definition_site": "00ae7854",
      "incomplete_value": true,
      "site": "00ae7854",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b475e0",
      "incomplete_value": false,
      "site": "00b475f4",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae785c",
      "incomplete_value": false,
      "site": "00ae7870",
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
            "const:497:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7844 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b475c8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae784c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00b475d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:430:8"]]
- 00ae7854 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7858 ["COPY", "register:4018:8", ["const:297000:8"]]
- 00ae785c ["COPY", "tmp:0:8", ["const:497:8"]]
+ 00b475d8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b475dc ["COPY", "register:4018:8", ["const:2a7000:8"]]
+ 00b475e0 ["COPY", "tmp:0:8", ["const:38:8"]]
~~~


### [`00ae78a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78a8.md) → [`00b4762c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4762c.md) _ZN8firebase4util10array_list11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde030.md) · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5aab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aab0.md) · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47648",
      "incomplete_value": false,
      "site": "00b4764c",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae78c4",
      "incomplete_value": false,
      "site": "00ae78c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b47658",
      "incomplete_value": true,
      "site": "00b47664",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae78d4",
      "incomplete_value": true,
      "site": "00ae78e0",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125440",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae78c0 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae78c4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b47644 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b47648 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae78c8 ["INT_ADD", "register:40f0:8", ["const:ae78c8:8", "const:4:8"]]
+ 00b4764c ["INT_ADD", "register:40f0:8", ["const:b4764c:8", "const:4:8"]]
- 00ae78cc ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae78d0 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00b47650 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47654 ["COPY", "tmp:0:8", ["const:440:8"]]
~~~


### [`00ae78e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78e4.md) → [`00b47668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47668.md) _ZN8firebase4util10array_list13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b476a8",
      "incomplete_value": true,
      "site": "00b476a8",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7924",
      "incomplete_value": true,
      "site": "00ae7924",
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
            "const:570:8"
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
      "definition_site": "00b47684",
      "incomplete_value": true,
      "site": "00b47684",
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
    "old": {
      "definition_site": "00ae7900",
      "incomplete_value": true,
      "site": "00ae7900",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4768c",
      "incomplete_value": false,
      "site": "00b476a0",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7908",
      "incomplete_value": false,
      "site": "00ae791c",
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
            "const:497:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae78f0 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b47674 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae78f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00b4767c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:430:8"]]
- 00ae7904 ["COPY", "register:4018:8", ["const:297000:8"]]
- 00ae7908 ["COPY", "tmp:0:8", ["const:497:8"]]
+ 00b47688 ["COPY", "register:4018:8", ["const:2a7000:8"]]
+ 00b4768c ["COPY", "tmp:0:8", ["const:38:8"]]
~~~


### [`00ae7954`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7954.md) → [`00b476d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b476d8.md) _ZN8firebase4util10array_list10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b476f4",
      "incomplete_value": false,
      "site": "00b476f8",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7970",
      "incomplete_value": false,
      "site": "00ae7974",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b47704",
      "incomplete_value": true,
      "site": "00b47710",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7980",
      "incomplete_value": true,
      "site": "00ae798c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0598",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125458",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae796c ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae7970 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b476f0 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b476f4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae7974 ["INT_ADD", "register:40f0:8", ["const:ae7974:8", "const:4:8"]]
+ 00b476f8 ["INT_ADD", "register:40f0:8", ["const:b476f8:8", "const:4:8"]]
- 00ae7978 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae797c ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00b476fc ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47700 ["COPY", "tmp:0:8", ["const:458:8"]]
~~~


### [`00ae7990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7990.md) → [`00b47714`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47714.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47740",
      "incomplete_value": true,
      "site": "00b47740",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79bc",
      "incomplete_value": true,
      "site": "00ae79bc",
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
            "const:5a0:8"
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
      "definition_site": "00b47728",
      "incomplete_value": true,
      "site": "00b47728",
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
    "old": {
      "definition_site": "00ae79a4",
      "incomplete_value": true,
      "site": "00ae79a4",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47734",
      "incomplete_value": false,
      "site": "00b47738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:77e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79b0",
      "incomplete_value": false,
      "site": "00ae79b4",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae799c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae79a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b47720 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47724 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00ae79ac ["COPY", "register:4018:8", ["const:2ae000:8"]]
- 00ae79b0 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b47730 ["COPY", "register:4018:8", ["const:2bf000:8"]]
+ 00b47734 ["COPY", "tmp:0:8", ["const:77e:8"]]
- 00ae79b4 ["INT_ADD", "register:40f0:8", ["const:ae79b4:8", "const:4:8"]]
+ 00b47738 ["INT_ADD", "register:40f0:8", ["const:b47738:8", "const:4:8"]]
~~~


### [`00ae79d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae79d0.md) → [`00b47754`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47754.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47780",
      "incomplete_value": true,
      "site": "00b47780",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79fc",
      "incomplete_value": true,
      "site": "00ae79fc",
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
            "const:5a0:8"
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
      "definition_site": "00b47768",
      "incomplete_value": true,
      "site": "00b47768",
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
    "old": {
      "definition_site": "00ae79e4",
      "incomplete_value": true,
      "site": "00ae79e4",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47770",
      "incomplete_value": false,
      "site": "00b47778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:77e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79ec",
      "incomplete_value": true,
      "site": "00ae79f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:339:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae79dc ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae79e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b47760 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47764 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00ae79e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae79e8 ["COPY", "register:4018:8", ["const:2ae000:8"]]
- 00ae79ec ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b47768 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4776c ["COPY", "register:4018:8", ["const:2bf000:8"]]
+ 00b47770 ["COPY", "tmp:0:8", ["const:77e:8"]]
- 00ae79f4 ["INT_ADD", "register:40f0:8", ["const:ae79f4:8", "const:4:8"]]
+ 00b47778 ["INT_ADD", "register:40f0:8", ["const:b47778:8", "const:4:8"]]
~~~


### [`00ae7a10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a10.md) → [`00b47794`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47794.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b477c4",
      "incomplete_value": true,
      "site": "00b477c4",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7a40",
      "incomplete_value": true,
      "site": "00ae7a40",
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
            "const:5a0:8"
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
      "definition_site": "00b477a8",
      "incomplete_value": true,
      "site": "00b477a8",
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
    "old": {
      "definition_site": "00ae7a24",
      "incomplete_value": true,
      "site": "00ae7a24",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b477b4",
      "incomplete_value": false,
      "site": "00b477bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:77e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7a30",
      "incomplete_value": true,
      "site": "00ae7a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:339:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7a1c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7a20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b477a0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b477a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00ae7a24 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae7a28 ["COPY", "register:4018:8", ["const:2ae000:8"]]
+ 00b477a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b477ac ["COPY", "register:4018:8", ["const:2bf000:8"]]
- 00ae7a30 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b477b4 ["COPY", "tmp:0:8", ["const:77e:8"]]
~~~


### [`00ae7a54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a54.md) → [`00b477d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b477d8.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47808",
      "incomplete_value": true,
      "site": "00b47808",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7a84",
      "incomplete_value": true,
      "site": "00ae7a84",
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
            "const:5a0:8"
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
      "definition_site": "00b477ec",
      "incomplete_value": true,
      "site": "00b477ec",
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
    "old": {
      "definition_site": "00ae7a68",
      "incomplete_value": true,
      "site": "00ae7a68",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b477f4",
      "incomplete_value": false,
      "site": "00b47800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:77e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7a70",
      "incomplete_value": false,
      "site": "00ae7a7c",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7a60 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7a64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b477e4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b477e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00ae7a68 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7a6c ["COPY", "register:4018:8", ["const:2ae000:8"]]
- 00ae7a70 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b477ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b477f0 ["COPY", "register:4018:8", ["const:2bf000:8"]]
+ 00b477f4 ["COPY", "tmp:0:8", ["const:77e:8"]]
- 00ae7a7c ["INT_ADD", "register:40f0:8", ["const:ae7a7c:8", "const:4:8"]]
+ 00b47800 ["INT_ADD", "register:40f0:8", ["const:b47800:8", "const:4:8"]]
~~~


### [`00ae7aa4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7aa4.md) → [`00b47828`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47828.md) _ZN8firebase4util21asset_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b478b0",
      "incomplete_value": true,
      "site": "00b478b0",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7b2c",
      "incomplete_value": true,
      "site": "00ae7b2c",
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
            "const:5a8:8"
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
      "definition_site": "00b47880",
      "incomplete_value": true,
      "site": "00b47884",
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
                "register:4000:4"
              ],
              [
                "leaf",
                "const:ff:4"
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
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ae7b00",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4785c",
      "incomplete_value": true,
      "site": "00b47868",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:460:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7ad8",
      "incomplete_value": true,
      "site": "00ae7ae4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:5a0:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7ab4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae7ab8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a8:8"]]
+ 00b47838 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4783c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:468:8"]]
- 00ae7ac4 ["BRANCH", null, ["local:b7:8"]]
+ 00b47848 ["BRANCH", null, ["local:b5:8"]]
- 00ae7acc ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b47850 ["COPY", "register:4048:8", ["const:1125000:8"]]
~~~


### [`00ae7b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md) → [`00b478c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b478c4.md) _ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47900",
      "incomplete_value": true,
      "site": "00b47900",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7b7c",
      "incomplete_value": true,
      "site": "00ae7b7c",
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
            "const:5a8:8"
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
      "definition_site": "00b47950",
      "incomplete_value": true,
      "site": "00b47950",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7bcc",
      "incomplete_value": true,
      "site": "00ae7bcc",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b478dc",
      "incomplete_value": true,
      "site": "00b478dc",
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
      "definition_site": "00ae7b58",
      "incomplete_value": true,
      "site": "00ae7b58",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7b50 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae7b54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00b478d4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b478d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
- 00ae7b58 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae7b5c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae7b60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a8:8"]]
+ 00b478dc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b478e0 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b478e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:468:8"]]
- 00ae7b78 ["INT_ADD", "register:40f0:8", ["const:ae7b78:8", "const:4:8"]]
+ 00b478fc ["INT_ADD", "register:40f0:8", ["const:b478fc:8", "const:4:8"]]
~~~


### [`00ae7be0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7be0.md) → [`00b47964`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47964.md) _ZN8firebase4util21asset_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b479a4",
      "incomplete_value": true,
      "site": "00b479a4",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7c20",
      "incomplete_value": true,
      "site": "00ae7c20",
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
            "const:5a0:8"
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
      "definition_site": "00b47980",
      "incomplete_value": true,
      "site": "00b47980",
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
    "old": {
      "definition_site": "00ae7bfc",
      "incomplete_value": true,
      "site": "00ae7bfc",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47988",
      "incomplete_value": false,
      "site": "00b4799c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:77e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7c04",
      "incomplete_value": false,
      "site": "00ae7c18",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7bec ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b47970 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae7bf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00b47978 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
- 00ae7bfc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7c00 ["COPY", "register:4018:8", ["const:2ae000:8"]]
- 00ae7c04 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b47980 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47984 ["COPY", "register:4018:8", ["const:2bf000:8"]]
+ 00b47988 ["COPY", "tmp:0:8", ["const:77e:8"]]
~~~


### [`00ae7c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c50.md) → [`00b479d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b479d4.md) _ZN8firebase4util21asset_file_descriptor11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b479f0",
      "incomplete_value": false,
      "site": "00b479f4",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7c6c",
      "incomplete_value": false,
      "site": "00ae7c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b47a00",
      "incomplete_value": true,
      "site": "00b47a0c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7c7c",
      "incomplete_value": true,
      "site": "00ae7c88",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a05b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125470",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7c68 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae7c6c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b479ec ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b479f0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae7c70 ["INT_ADD", "register:40f0:8", ["const:ae7c70:8", "const:4:8"]]
+ 00b479f4 ["INT_ADD", "register:40f0:8", ["const:b479f4:8", "const:4:8"]]
- 00ae7c74 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae7c78 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 00b479f8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b479fc ["COPY", "tmp:0:8", ["const:470:8"]]
~~~


### [`00ae7c8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c8c.md) → [`00b47a10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a10.md) _ZN8firebase4util21asset_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47a50",
      "incomplete_value": true,
      "site": "00b47a50",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7ccc",
      "incomplete_value": true,
      "site": "00ae7ccc",
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
            "const:5a0:8"
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
      "definition_site": "00b47a2c",
      "incomplete_value": true,
      "site": "00b47a2c",
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
    "old": {
      "definition_site": "00ae7ca8",
      "incomplete_value": true,
      "site": "00ae7ca8",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47a34",
      "incomplete_value": false,
      "site": "00b47a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:77e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7cb0",
      "incomplete_value": false,
      "site": "00ae7cc4",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7c98 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b47a1c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae7ca0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00b47a24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
- 00ae7cac ["COPY", "register:4018:8", ["const:2ae000:8"]]
- 00ae7cb0 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00b47a30 ["COPY", "register:4018:8", ["const:2bf000:8"]]
+ 00b47a34 ["COPY", "tmp:0:8", ["const:77e:8"]]
~~~


### [`00ae7cfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7cfc.md) → [`00b47a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a80.md) _ZN8firebase4util21asset_file_descriptor10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47a9c",
      "incomplete_value": false,
      "site": "00b47aa0",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d18",
      "incomplete_value": false,
      "site": "00ae7d1c",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b47aac",
      "incomplete_value": true,
      "site": "00b47ab8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d28",
      "incomplete_value": true,
      "site": "00ae7d34",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a05b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125478",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7d14 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae7d18 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b47a98 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b47a9c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae7d1c ["INT_ADD", "register:40f0:8", ["const:ae7d1c:8", "const:4:8"]]
+ 00b47aa0 ["INT_ADD", "register:40f0:8", ["const:b47aa0:8", "const:4:8"]]
- 00ae7d20 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae7d24 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00b47aa4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47aa8 ["COPY", "tmp:0:8", ["const:478:8"]]
~~~


### [`00ae7d38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d38.md) → [`00b47abc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47abc.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47ae8",
      "incomplete_value": true,
      "site": "00b47ae8",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d64",
      "incomplete_value": true,
      "site": "00ae7d64",
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
            "const:5c0:8"
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
      "definition_site": "00b47ad0",
      "incomplete_value": true,
      "site": "00b47ad0",
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
    "old": {
      "definition_site": "00ae7d4c",
      "incomplete_value": true,
      "site": "00ae7d4c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47adc",
      "incomplete_value": false,
      "site": "00b47ae0",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d58",
      "incomplete_value": false,
      "site": "00ae7d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:5dc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7d44 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7d48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b47ac8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47acc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae7d4c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47ad0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7d54 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae7d58 ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 00b47ad8 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b47adc ["COPY", "tmp:0:8", ["const:32f:8"]]
~~~


### [`00ae7d78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d78.md) → [`00b47afc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47afc.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47b28",
      "incomplete_value": true,
      "site": "00b47b28",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7da4",
      "incomplete_value": true,
      "site": "00ae7da4",
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
            "const:5c0:8"
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
      "definition_site": "00b47b10",
      "incomplete_value": true,
      "site": "00b47b10",
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
    "old": {
      "definition_site": "00ae7d8c",
      "incomplete_value": true,
      "site": "00ae7d8c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47b18",
      "incomplete_value": false,
      "site": "00b47b20",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d94",
      "incomplete_value": true,
      "site": "00ae7d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:5dc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7d84 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7d88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b47b08 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47b0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae7d8c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae7d90 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae7d94 ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 00b47b10 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47b14 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b47b18 ["COPY", "tmp:0:8", ["const:32f:8"]]
- 00ae7d9c ["INT_ADD", "register:40f0:8", ["const:ae7d9c:8", "const:4:8"]]
+ 00b47b20 ["INT_ADD", "register:40f0:8", ["const:b47b20:8", "const:4:8"]]
~~~


### [`00ae7db8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7db8.md) → [`00b47b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b3c.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47b6c",
      "incomplete_value": true,
      "site": "00b47b6c",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7de8",
      "incomplete_value": true,
      "site": "00ae7de8",
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
            "const:5c0:8"
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
      "definition_site": "00b47b50",
      "incomplete_value": true,
      "site": "00b47b50",
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
    "old": {
      "definition_site": "00ae7dcc",
      "incomplete_value": true,
      "site": "00ae7dcc",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47b5c",
      "incomplete_value": false,
      "site": "00b47b64",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7dc4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7dc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b47b48 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47b4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae7dcc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7dd0 ["COPY", "register:4018:8", ["const:298000:8"]]
+ 00b47b50 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47b54 ["COPY", "register:4018:8", ["const:2a8000:8"]]
- 00ae7dd8 ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 00b47b5c ["COPY", "tmp:0:8", ["const:32f:8"]]
~~~


### [`00ae7dfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7dfc.md) → [`00b47b80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b80.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47bb0",
      "incomplete_value": true,
      "site": "00b47bb0",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7e2c",
      "incomplete_value": true,
      "site": "00ae7e2c",
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
            "const:5c0:8"
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
      "definition_site": "00b47b94",
      "incomplete_value": true,
      "site": "00b47b94",
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
    "old": {
      "definition_site": "00ae7e10",
      "incomplete_value": true,
      "site": "00ae7e10",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47b9c",
      "incomplete_value": false,
      "site": "00b47ba8",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7e18",
      "incomplete_value": false,
      "site": "00ae7e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:5dc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7e08 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae7e0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b47b8c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47b90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae7e10 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7e14 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae7e18 ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 00b47b94 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47b98 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b47b9c ["COPY", "tmp:0:8", ["const:32f:8"]]
- 00ae7e24 ["INT_ADD", "register:40f0:8", ["const:ae7e24:8", "const:4:8"]]
+ 00b47ba8 ["INT_ADD", "register:40f0:8", ["const:b47ba8:8", "const:4:8"]]
~~~


### [`00ae7e4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7e4c.md) → [`00b47bd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47bd0.md) _ZN8firebase4util13boolean_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47c58",
      "incomplete_value": true,
      "site": "00b47c58",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7ed4",
      "incomplete_value": true,
      "site": "00ae7ed4",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00b47c10",
      "incomplete_value": true,
      "site": "00b47c10",
      "value": [
        "LOAD",
        "8",
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
                "const:6b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7e8c",
      "incomplete_value": true,
      "site": "00ae7e8c",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47c04",
      "incomplete_value": true,
      "site": "00b47c10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
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
      20,
      "READ",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125488",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125488",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7e5c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae7e60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
+ 00b47be0 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b47be4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:488:8"]]
- 00ae7e64 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47be8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7e6c ["BRANCH", null, ["local:b7:8"]]
+ 00b47bf0 ["BRANCH", null, ["local:b6:8"]]
~~~


### [`00ae7ee8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ee8.md) → [`00b47c6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47c6c.md) _ZN8firebase4util13boolean_class12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47ca8",
      "incomplete_value": true,
      "site": "00b47ca8",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7f24",
      "incomplete_value": true,
      "site": "00ae7f24",
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
            "const:5c8:8"
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
      "definition_site": "00b47cf8",
      "incomplete_value": true,
      "site": "00b47cf8",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7f74",
      "incomplete_value": true,
      "site": "00ae7f74",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47c84",
      "incomplete_value": true,
      "site": "00b47c84",
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
      "definition_site": "00ae7f00",
      "incomplete_value": true,
      "site": "00ae7f00",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125488",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125488",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7ef8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae7efc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00b47c7c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b47c80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00ae7f00 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ae7f04 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae7f08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
+ 00b47c84 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b47c88 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b47c8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:488:8"]]
- 00ae7f10 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b47c94 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`00ae7f88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7f88.md) → [`00b47d0c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d0c.md) _ZN8firebase4util13boolean_class14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47d4c",
      "incomplete_value": true,
      "site": "00b47d4c",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7fc8",
      "incomplete_value": true,
      "site": "00ae7fc8",
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
            "const:5c0:8"
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
      "definition_site": "00b47d28",
      "incomplete_value": true,
      "site": "00b47d28",
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
    "old": {
      "definition_site": "00ae7fa4",
      "incomplete_value": true,
      "site": "00ae7fa4",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47d30",
      "incomplete_value": false,
      "site": "00b47d44",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7fac",
      "incomplete_value": false,
      "site": "00ae7fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:5dc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7f94 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b47d18 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae7f9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00b47d20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00ae7fa8 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae7fac ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 00b47d2c ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b47d30 ["COPY", "tmp:0:8", ["const:32f:8"]]
~~~


### [`00ae7ff8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md) → [`00b47d7c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d7c.md) _ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde440`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde440.md) · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5aec0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aec0.md) · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47d98",
      "incomplete_value": false,
      "site": "00b47d9c",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8014",
      "incomplete_value": false,
      "site": "00ae8018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b47da8",
      "incomplete_value": true,
      "site": "00b47db4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8024",
      "incomplete_value": true,
      "site": "00ae8030",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a05d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01125490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8010 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae8014 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b47d94 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b47d98 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae8018 ["INT_ADD", "register:40f0:8", ["const:ae8018:8", "const:4:8"]]
+ 00b47d9c ["INT_ADD", "register:40f0:8", ["const:b47d9c:8", "const:4:8"]]
- 00ae801c ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae8020 ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 00b47da0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47da4 ["COPY", "tmp:0:8", ["const:490:8"]]
~~~


### [`00ae8034`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8034.md) → [`00b47db8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47db8.md) _ZN8firebase4util13boolean_class13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47df8",
      "incomplete_value": true,
      "site": "00b47df8",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8074",
      "incomplete_value": true,
      "site": "00ae8074",
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
            "const:5c0:8"
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
      "definition_site": "00b47dd4",
      "incomplete_value": true,
      "site": "00b47dd4",
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
    "old": {
      "definition_site": "00ae8050",
      "incomplete_value": true,
      "site": "00ae8050",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47ddc",
      "incomplete_value": false,
      "site": "00b47df0",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8058",
      "incomplete_value": false,
      "site": "00ae806c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:5dc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8040 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b47dc4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae8048 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00b47dcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00ae8050 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8054 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae8058 ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 00b47dd4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47dd8 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b47ddc ["COPY", "tmp:0:8", ["const:32f:8"]]
~~~


### [`00ae80a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80a4.md) → [`00b47e28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47e28.md) _ZN8firebase4util13boolean_class10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47e44",
      "incomplete_value": false,
      "site": "00b47e48",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae80c0",
      "incomplete_value": false,
      "site": "00ae80c4",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b47e54",
      "incomplete_value": true,
      "site": "00b47e60",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae80d0",
      "incomplete_value": true,
      "site": "00ae80dc",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a05e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011254a0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae80bc ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae80c0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b47e40 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b47e44 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae80c4 ["INT_ADD", "register:40f0:8", ["const:ae80c4:8", "const:4:8"]]
+ 00b47e48 ["INT_ADD", "register:40f0:8", ["const:b47e48:8", "const:4:8"]]
- 00ae80c8 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae80cc ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 00b47e4c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47e50 ["COPY", "tmp:0:8", ["const:4a0:8"]]
~~~


### [`00ae80e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80e0.md) → [`00b47e64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47e64.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47e90",
      "incomplete_value": true,
      "site": "00b47e90",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae810c",
      "incomplete_value": true,
      "site": "00ae810c",
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
            "const:5e8:8"
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
      "definition_site": "00b47e78",
      "incomplete_value": true,
      "site": "00b47e78",
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
    "old": {
      "definition_site": "00ae80f4",
      "incomplete_value": true,
      "site": "00ae80f4",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47e84",
      "incomplete_value": false,
      "site": "00b47e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:95b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8100",
      "incomplete_value": false,
      "site": "00ae8104",
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
            "const:c92:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae80ec ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae80f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00b47e70 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47e74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae80f4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47e78 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae80fc ["COPY", "register:4018:8", ["const:2a8000:8"]]
- 00ae8100 ["COPY", "tmp:0:8", ["const:c92:8"]]
+ 00b47e80 ["COPY", "register:4018:8", ["const:2b9000:8"]]
+ 00b47e84 ["COPY", "tmp:0:8", ["const:95b:8"]]
~~~


### [`00ae8120`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8120.md) → [`00b47ea4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ea4.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47ed0",
      "incomplete_value": true,
      "site": "00b47ed0",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae814c",
      "incomplete_value": true,
      "site": "00ae814c",
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
            "const:5e8:8"
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
      "definition_site": "00b47eb8",
      "incomplete_value": true,
      "site": "00b47eb8",
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
    "old": {
      "definition_site": "00ae8134",
      "incomplete_value": true,
      "site": "00ae8134",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47ec0",
      "incomplete_value": false,
      "site": "00b47ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:95b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae813c",
      "incomplete_value": false,
      "site": "00ae8144",
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
            "const:c92:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae812c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8130 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00b47eb0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47eb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae8134 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae8138 ["COPY", "register:4018:8", ["const:2a8000:8"]]
- 00ae813c ["COPY", "tmp:0:8", ["const:c92:8"]]
+ 00b47eb8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47ebc ["COPY", "register:4018:8", ["const:2b9000:8"]]
+ 00b47ec0 ["COPY", "tmp:0:8", ["const:95b:8"]]
- 00ae8144 ["INT_ADD", "register:40f0:8", ["const:ae8144:8", "const:4:8"]]
+ 00b47ec8 ["INT_ADD", "register:40f0:8", ["const:b47ec8:8", "const:4:8"]]
~~~


