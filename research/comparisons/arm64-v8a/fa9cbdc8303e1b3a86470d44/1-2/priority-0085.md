# v15.7.4 → v16.0.0 · 最優先の変更候補 (85)

[一覧の目次](README.md)

### [`00b65a20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a20.md) → [`00bd4f20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f20.md) _ZN8firebase4auth9emailcred12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd4f5c",
      "incomplete_value": true,
      "site": "00bd4f5c",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65a5c",
      "incomplete_value": true,
      "site": "00b65a5c",
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
            "const:768:8"
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
      "definition_site": "00bd4f7c",
      "incomplete_value": true,
      "site": "00bd4f7c",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65a7c",
      "incomplete_value": true,
      "site": "00b65a7c",
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
            "const:760:8"
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
      "definition_site": "00bd4f38",
      "incomplete_value": true,
      "site": "00bd4f38",
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
      "definition_site": "00b65a38",
      "incomplete_value": true,
      "site": "00b65a38",
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
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a1768",
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
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65a30 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
- 00b65a34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
+ 00bd4f30 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd4f34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00b65a3c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b65a40 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:768:8"]]
+ 00bd4f3c ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd4f40 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:670:8"]]
- 00b65a58 ["INT_ADD", "register:40f0:8", ["const:b65a58:8", "const:4:8"]]
+ 00bd4f58 ["INT_ADD", "register:40f0:8", ["const:bd4f58:8", "const:4:8"]]
~~~


### [`00b65a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a90.md) → [`00bd4f90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f90.md) _ZN8firebase4auth9emailcred14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd4fd0",
      "incomplete_value": true,
      "site": "00bd4fd0",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ad0",
      "incomplete_value": true,
      "site": "00b65ad0",
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
            "const:760:8"
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
      "definition_site": "00bd4fac",
      "incomplete_value": true,
      "site": "00bd4fac",
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
      "definition_site": "00b65aac",
      "incomplete_value": true,
      "site": "00b65aac",
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
      "definition_site": "00bd4fb4",
      "incomplete_value": false,
      "site": "00bd4fc8",
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
            "const:3b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ab4",
      "incomplete_value": false,
      "site": "00b65ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:18d:8"
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
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1760",
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
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65a9c ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd4f9c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b65aa4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
+ 00bd4fa4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00b65aac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b65ab0 ["COPY", "register:4018:8", ["const:29c000:8"]]
- 00b65ab4 ["COPY", "tmp:0:8", ["const:18d:8"]]
+ 00bd4fac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd4fb0 ["COPY", "register:4018:8", ["const:2ac000:8"]]
+ 00bd4fb4 ["COPY", "tmp:0:8", ["const:3b3:8"]]
~~~


### [`00b65b00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b00.md) → [`00bd5000`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5000.md) _ZN8firebase4auth9emailcred11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd501c",
      "incomplete_value": false,
      "site": "00bd5020",
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
      "definition_site": "00b65b1c",
      "incomplete_value": false,
      "site": "00b65b20",
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
      "definition_site": "00bd502c",
      "incomplete_value": true,
      "site": "00bd5038",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65b2c",
      "incomplete_value": true,
      "site": "00b65b38",
      "value": [
        "LOAD",
        "8",
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
        "010a1770",
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
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65b18 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00b65b1c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00bd5018 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00bd501c ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b65b20 ["INT_ADD", "register:40f0:8", ["const:b65b20:8", "const:4:8"]]
+ 00bd5020 ["INT_ADD", "register:40f0:8", ["const:bd5020:8", "const:4:8"]]
- 00b65b24 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b65b28 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00bd5024 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd5028 ["COPY", "tmp:0:8", ["const:678:8"]]
~~~


### [`00b65b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b3c.md) → [`00bd503c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd503c.md) _ZN8firebase4auth9emailcred13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd507c",
      "incomplete_value": true,
      "site": "00bd507c",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b7c",
      "incomplete_value": true,
      "site": "00b65b7c",
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
            "const:760:8"
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
      "definition_site": "00bd5058",
      "incomplete_value": true,
      "site": "00bd5058",
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
      "definition_site": "00b65b58",
      "incomplete_value": true,
      "site": "00b65b58",
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
      "definition_site": "00bd5060",
      "incomplete_value": false,
      "site": "00bd5074",
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
            "const:3b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b60",
      "incomplete_value": false,
      "site": "00b65b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:18d:8"
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
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1760",
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
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65b48 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd5048 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b65b50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
+ 00bd5050 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00b65b5c ["COPY", "register:4018:8", ["const:29c000:8"]]
- 00b65b60 ["COPY", "tmp:0:8", ["const:18d:8"]]
+ 00bd505c ["COPY", "register:4018:8", ["const:2ac000:8"]]
+ 00bd5060 ["COPY", "tmp:0:8", ["const:3b3:8"]]
~~~


### [`00b65bac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65bac.md) → [`00bd50ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50ac.md) _ZN8firebase4auth9emailcred10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd50c8",
      "incomplete_value": false,
      "site": "00bd50cc",
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
      "definition_site": "00b65bc8",
      "incomplete_value": false,
      "site": "00b65bcc",
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
      "definition_site": "00bd50d8",
      "incomplete_value": true,
      "site": "00bd50e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65bd8",
      "incomplete_value": true,
      "site": "00b65be4",
      "value": [
        "LOAD",
        "8",
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
        "010a1778",
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
        "01126680",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65bc4 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00b65bc8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00bd50c4 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bd50c8 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b65bcc ["INT_ADD", "register:40f0:8", ["const:b65bcc:8", "const:4:8"]]
+ 00bd50cc ["INT_ADD", "register:40f0:8", ["const:bd50cc:8", "const:4:8"]]
- 00b65bd0 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b65bd4 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00bd50d0 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd50d4 ["COPY", "tmp:0:8", ["const:680:8"]]
~~~


### [`00b65be8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65be8.md) → [`00bd50e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50e8.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00bd5114",
      "incomplete_value": true,
      "site": "00bd5114",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c14",
      "incomplete_value": true,
      "site": "00b65c14",
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
            "const:780:8"
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
      "definition_site": "00bd50fc",
      "incomplete_value": true,
      "site": "00bd50fc",
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
      "definition_site": "00b65bfc",
      "incomplete_value": true,
      "site": "00b65bfc",
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
      "definition_site": "00bd5108",
      "incomplete_value": false,
      "site": "00bd510c",
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
            "const:459:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c08",
      "incomplete_value": false,
      "site": "00b65c0c",
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
            "const:3e1:8"
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
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a1780",
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
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65bf4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b65bf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00bd50f4 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd50f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:688:8"]]
- 00b65c04 ["COPY", "register:4018:8", ["const:2ac000:8"]]
- 00b65c08 ["COPY", "tmp:0:8", ["const:3e1:8"]]
+ 00bd5104 ["COPY", "register:4018:8", ["const:2bd000:8"]]
+ 00bd5108 ["COPY", "tmp:0:8", ["const:459:8"]]
- 00b65c0c ["INT_ADD", "register:40f0:8", ["const:b65c0c:8", "const:4:8"]]
+ 00bd510c ["INT_ADD", "register:40f0:8", ["const:bd510c:8", "const:4:8"]]
~~~


### [`00b65c28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65c28.md) → [`00bd5128`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5128.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00bd5154",
      "incomplete_value": true,
      "site": "00bd5154",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c54",
      "incomplete_value": true,
      "site": "00b65c54",
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
            "const:780:8"
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
      "definition_site": "00bd513c",
      "incomplete_value": true,
      "site": "00bd513c",
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
      "definition_site": "00b65c3c",
      "incomplete_value": true,
      "site": "00b65c3c",
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
      "definition_site": "00bd5144",
      "incomplete_value": true,
      "site": "00bd514c",
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
            "const:459:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c44",
      "incomplete_value": false,
      "site": "00b65c4c",
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
            "const:3e1:8"
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
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a1780",
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
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65c34 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b65c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00bd5134 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5138 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:688:8"]]
- 00b65c3c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65c40 ["COPY", "register:4018:8", ["const:2ac000:8"]]
- 00b65c44 ["COPY", "tmp:0:8", ["const:3e1:8"]]
+ 00bd513c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd5140 ["COPY", "register:4018:8", ["const:2bd000:8"]]
+ 00bd5144 ["COPY", "tmp:0:8", ["const:459:8"]]
- 00b65c4c ["INT_ADD", "register:40f0:8", ["const:b65c4c:8", "const:4:8"]]
+ 00bd514c ["INT_ADD", "register:40f0:8", ["const:bd514c:8", "const:4:8"]]
~~~


### [`00b65c68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65c68.md) → [`00bd5168`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5168.md) _ZN8firebase4auth12facebookcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd5198",
      "incomplete_value": true,
      "site": "00bd5198",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c98",
      "incomplete_value": true,
      "site": "00b65c98",
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
            "const:780:8"
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
      "definition_site": "00bd517c",
      "incomplete_value": true,
      "site": "00bd517c",
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
      "definition_site": "00b65c7c",
      "incomplete_value": true,
      "site": "00b65c7c",
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
      "definition_site": "00bd5188",
      "incomplete_value": false,
      "site": "00bd5190",
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
            "const:459:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c88",
      "incomplete_value": false,
      "site": "00b65c90",
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
            "const:3e1:8"
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
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a1780",
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
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65c74 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b65c78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00bd5174 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5178 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:688:8"]]
- 00b65c7c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65c80 ["COPY", "register:4018:8", ["const:2ac000:8"]]
+ 00bd517c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd5180 ["COPY", "register:4018:8", ["const:2bd000:8"]]
- 00b65c88 ["COPY", "tmp:0:8", ["const:3e1:8"]]
+ 00bd5188 ["COPY", "tmp:0:8", ["const:459:8"]]
~~~


### [`00b65cac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65cac.md) → [`00bd51ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51ac.md) _ZN8firebase4auth12facebookcred10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd51dc",
      "incomplete_value": true,
      "site": "00bd51dc",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65cdc",
      "incomplete_value": true,
      "site": "00b65cdc",
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
            "const:780:8"
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
      "definition_site": "00bd51c0",
      "incomplete_value": true,
      "site": "00bd51c0",
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
      "definition_site": "00b65cc0",
      "incomplete_value": true,
      "site": "00b65cc0",
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
      "definition_site": "00b65ccc",
      "incomplete_value": false,
      "site": "00b65cd4",
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
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a1780",
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
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65cb8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b65cbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00bd51b8 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd51bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:688:8"]]
- 00b65cc0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65cc4 ["COPY", "register:4018:8", ["const:2ac000:8"]]
- 00b65cc8 ["COPY", "tmp:0:8", ["const:3e1:8"]]
+ 00bd51c0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd51c4 ["COPY", "register:4018:8", ["const:2bd000:8"]]
+ 00bd51c8 ["COPY", "tmp:0:8", ["const:459:8"]]
- 00b65cd4 ["INT_ADD", "register:40f0:8", ["const:b65cd4:8", "const:4:8"]]
+ 00bd51d4 ["INT_ADD", "register:40f0:8", ["const:bd51d4:8", "const:4:8"]]
~~~


### [`00b65cfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65cfc.md) → [`00bd51fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51fc.md) _ZN8firebase4auth12facebookcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5254",
      "incomplete_value": true,
      "site": "00bd5254",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d54",
      "incomplete_value": true,
      "site": "00b65d54",
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
            "const:788:8"
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
      "definition_site": "00bd523c",
      "incomplete_value": true,
      "site": "00bd523c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:6b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d3c",
      "incomplete_value": true,
      "site": "00b65d3c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b65d30",
      "incomplete_value": true,
      "site": "00b65d3c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:780:8"
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
        "010a1788",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "010a1788",
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
        "01126690",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126690",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65d0c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b65d10 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:788:8"]]
+ 00bd520c ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd5210 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:690:8"]]
- 00b65d1c ["BRANCH", null, ["local:b3:8"]]
+ 00bd521c ["BRANCH", null, ["local:b4:8"]]
- 00b65d24 ["COPY", "register:4048:8", ["const:10a1000:8"]]
+ 00bd5224 ["COPY", "register:4048:8", ["const:1126000:8"]]
~~~


### [`00b65d68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65d68.md) → [`00bd5268`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5268.md) _ZN8firebase4auth12facebookcred12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd52a4",
      "incomplete_value": true,
      "site": "00bd52a4",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65da4",
      "incomplete_value": true,
      "site": "00b65da4",
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
            "const:788:8"
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
      "definition_site": "00bd52c4",
      "incomplete_value": true,
      "site": "00bd52c4",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65dc4",
      "incomplete_value": true,
      "site": "00b65dc4",
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
            "const:780:8"
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
      "definition_site": "00bd5280",
      "incomplete_value": true,
      "site": "00bd5280",
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
      "definition_site": "00b65d80",
      "incomplete_value": true,
      "site": "00b65d80",
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
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a1788",
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
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126690",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126690",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65d78 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
- 00b65d7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00bd5278 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd527c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:688:8"]]
- 00b65d80 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b65d84 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b65d88 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:788:8"]]
+ 00bd5280 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd5284 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd5288 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:690:8"]]
- 00b65d90 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd5290 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
~~~


### [`00b65dd8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65dd8.md) → [`00bd52d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd52d8.md) _ZN8firebase4auth12facebookcred14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd5318",
      "incomplete_value": true,
      "site": "00bd5318",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e18",
      "incomplete_value": true,
      "site": "00b65e18",
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
            "const:780:8"
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
      "definition_site": "00bd52f4",
      "incomplete_value": true,
      "site": "00bd52f4",
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
      "definition_site": "00b65df4",
      "incomplete_value": true,
      "site": "00b65df4",
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
      "definition_site": "00b65e00",
      "incomplete_value": true,
      "site": "00b65e10",
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
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1780",
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
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65de4 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd52e4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b65dec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00bd52ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:688:8"]]
- 00b65df4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65df8 ["COPY", "register:4018:8", ["const:2ac000:8"]]
- 00b65dfc ["COPY", "tmp:0:8", ["const:3e1:8"]]
+ 00bd52f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd52f8 ["COPY", "register:4018:8", ["const:2bd000:8"]]
+ 00bd52fc ["COPY", "tmp:0:8", ["const:459:8"]]
~~~


### [`00b65e48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65e48.md) → [`00bd5348`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5348.md) _ZN8firebase4auth12facebookcred11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd535c",
      "incomplete_value": true,
      "site": "00bd535c",
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
      "definition_site": "00b65e5c",
      "incomplete_value": true,
      "site": "00b65e5c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b65e64",
      "incomplete_value": false,
      "site": "00b65e68",
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
      "definition_site": "00bd5374",
      "incomplete_value": true,
      "site": "00bd5380",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65e74",
      "incomplete_value": true,
      "site": "00b65e80",
      "value": [
        "LOAD",
        "8",
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
        "010a1790",
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
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65e5c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65e60 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00b65e64 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00bd535c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd5360 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00bd5364 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b65e68 ["INT_ADD", "register:40f0:8", ["const:b65e68:8", "const:4:8"]]
+ 00bd5368 ["INT_ADD", "register:40f0:8", ["const:bd5368:8", "const:4:8"]]
- 00b65e6c ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b65e70 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00bd536c ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd5370 ["COPY", "tmp:0:8", ["const:698:8"]]
~~~


### [`00b65e84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65e84.md) → [`00bd5384`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5384.md) _ZN8firebase4auth12facebookcred13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd53c4",
      "incomplete_value": true,
      "site": "00bd53c4",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ec4",
      "incomplete_value": true,
      "site": "00b65ec4",
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
            "const:780:8"
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
      "definition_site": "00bd53a0",
      "incomplete_value": true,
      "site": "00bd53a0",
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
      "definition_site": "00b65ea0",
      "incomplete_value": true,
      "site": "00b65ea0",
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
      "definition_site": "00b65eac",
      "incomplete_value": true,
      "site": "00b65ebc",
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
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1780",
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
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65e90 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd5390 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b65e98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00bd5398 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:688:8"]]
- 00b65ea0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65ea4 ["COPY", "register:4018:8", ["const:2ac000:8"]]
- 00b65ea8 ["COPY", "tmp:0:8", ["const:3e1:8"]]
+ 00bd53a0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd53a4 ["COPY", "register:4018:8", ["const:2bd000:8"]]
+ 00bd53a8 ["COPY", "tmp:0:8", ["const:459:8"]]
~~~


### [`00b65ef4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65ef4.md) → [`00bd53f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd53f4.md) _ZN8firebase4auth12facebookcred10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd5410",
      "incomplete_value": false,
      "site": "00bd5414",
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
      "definition_site": "00b65f10",
      "incomplete_value": false,
      "site": "00b65f14",
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
    "new": null,
    "old": {
      "definition_site": "00b65f20",
      "incomplete_value": true,
      "site": "00b65f2c",
      "value": [
        "LOAD",
        "8",
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
        "010a1798",
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
        "011266a0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65f0c ["COPY", "register:4000:8", ["const:299000:8"]]
- 00b65f10 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00bd540c ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bd5410 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b65f14 ["INT_ADD", "register:40f0:8", ["const:b65f14:8", "const:4:8"]]
+ 00bd5414 ["INT_ADD", "register:40f0:8", ["const:bd5414:8", "const:4:8"]]
- 00b65f18 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b65f1c ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00bd5418 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd541c ["COPY", "tmp:0:8", ["const:6a0:8"]]
~~~


### [`00b65f30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65f30.md) → [`00bd5430`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5430.md) _ZN8firebase4auth10githubcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5434",
      "incomplete_value": true,
      "site": "00bd5434",
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
      "definition_site": "00b65f34",
      "incomplete_value": true,
      "site": "00b65f34",
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
      "definition_site": "00bd5434",
      "incomplete_value": true,
      "site": "00bd5434",
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
      "definition_site": "00b65f34",
      "incomplete_value": true,
      "site": "00b65f34",
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
      "definition_site": "00bd545c",
      "incomplete_value": true,
      "site": "00bd545c",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f5c",
      "incomplete_value": true,
      "site": "00b65f5c",
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
            "const:7a0:8"
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
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a17a0",
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
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65f3c ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b65f40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00bd543c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5440 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00b65f44 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd5444 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b65f4c ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00b65f50 ["COPY", "tmp:0:8", ["const:7f9:8"]]
+ 00bd544c ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00bd5450 ["COPY", "tmp:0:8", ["const:da2:8"]]
~~~


### [`00b65f70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65f70.md) → [`00bd5470`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5470.md) _ZN8firebase4auth10githubcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd549c",
      "incomplete_value": true,
      "site": "00bd549c",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f9c",
      "incomplete_value": true,
      "site": "00b65f9c",
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
            "const:7a0:8"
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
      "definition_site": "00bd5484",
      "incomplete_value": true,
      "site": "00bd5484",
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
      "definition_site": "00b65f84",
      "incomplete_value": true,
      "site": "00b65f84",
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
      "definition_site": "00bd548c",
      "incomplete_value": false,
      "site": "00bd5494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:da2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f8c",
      "incomplete_value": false,
      "site": "00b65f94",
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
            "const:7f9:8"
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
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a17a0",
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
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65f7c ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b65f80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00bd547c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5480 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00b65f88 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00b65f8c ["COPY", "tmp:0:8", ["const:7f9:8"]]
+ 00bd5488 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00bd548c ["COPY", "tmp:0:8", ["const:da2:8"]]
- 00b65f94 ["INT_ADD", "register:40f0:8", ["const:b65f94:8", "const:4:8"]]
+ 00bd5494 ["INT_ADD", "register:40f0:8", ["const:bd5494:8", "const:4:8"]]
~~~


### [`00b65fb0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65fb0.md) → [`00bd54b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54b0.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd54e0",
      "incomplete_value": true,
      "site": "00bd54e0",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65fe0",
      "incomplete_value": true,
      "site": "00b65fe0",
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
            "const:7a0:8"
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
      "definition_site": "00bd54c4",
      "incomplete_value": true,
      "site": "00bd54c4",
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
      "definition_site": "00b65fc4",
      "incomplete_value": true,
      "site": "00b65fc4",
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
      "definition_site": "00bd54d0",
      "incomplete_value": false,
      "site": "00bd54d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:da2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65fd0",
      "incomplete_value": false,
      "site": "00b65fd8",
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
            "const:7f9:8"
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
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a17a0",
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
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b65fbc ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b65fc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00bd54bc ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd54c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00b65fc8 ["COPY", "register:4018:8", ["const:2b0000:8"]]
+ 00bd54c8 ["COPY", "register:4018:8", ["const:2c1000:8"]]
- 00b65fd0 ["COPY", "tmp:0:8", ["const:7f9:8"]]
+ 00bd54d0 ["COPY", "tmp:0:8", ["const:da2:8"]]
~~~


### [`00b65ff4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65ff4.md) → [`00bd54f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54f4.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5524",
      "incomplete_value": true,
      "site": "00bd5524",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66024",
      "incomplete_value": true,
      "site": "00b66024",
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
            "const:7a0:8"
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
      "definition_site": "00bd5508",
      "incomplete_value": true,
      "site": "00bd5508",
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
      "definition_site": "00b66008",
      "incomplete_value": true,
      "site": "00b66008",
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
      "definition_site": "00b66014",
      "incomplete_value": false,
      "site": "00b6601c",
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
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a17a0",
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
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66000 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66004 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00bd5500 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00b66008 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6600c ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00b66010 ["COPY", "tmp:0:8", ["const:7f9:8"]]
+ 00bd5508 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd550c ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00bd5510 ["COPY", "tmp:0:8", ["const:da2:8"]]
- 00b6601c ["INT_ADD", "register:40f0:8", ["const:b6601c:8", "const:4:8"]]
+ 00bd551c ["INT_ADD", "register:40f0:8", ["const:bd551c:8", "const:4:8"]]
~~~


### [`00b66038`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66038.md) → [`00bd5538`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5538.md) _ZN8firebase4auth10githubcred8GetClassEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd553c",
      "incomplete_value": true,
      "site": "00bd5540",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:6a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6603c",
      "incomplete_value": true,
      "site": "00b66040",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7a0:8"
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
      4,
      "READ",
      [
        "storage",
        "010a17a0",
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
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66038 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b6603c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7a0:8"]]
+ 00bd5538 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd553c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6a8:8"]]
~~~


### [`00b66044`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66044.md) → [`00bd5544`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5544.md) _ZN8firebase4auth10githubcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd554c",
      "incomplete_value": true,
      "site": "00bd554c",
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
      "definition_site": "00b6604c",
      "incomplete_value": true,
      "site": "00b6604c",
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
      "definition_site": "00bd554c",
      "incomplete_value": true,
      "site": "00bd554c",
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
      "definition_site": "00b6604c",
      "incomplete_value": true,
      "site": "00b6604c",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd559c",
      "incomplete_value": true,
      "site": "00bd559c",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6609c",
      "incomplete_value": true,
      "site": "00b6609c",
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
            "const:7a8:8"
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
      20,
      "READ",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "010a17a8",
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
        "011266b0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "011266b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66054 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b66058 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7a8:8"]]
+ 00bd5554 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd5558 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6b0:8"]]
- 00b6605c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd555c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b66064 ["BRANCH", null, ["local:b3:8"]]
+ 00bd5564 ["BRANCH", null, ["local:b5:8"]]
~~~


### [`00b660b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b660b0.md) → [`00bd55b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd55b0.md) _ZN8firebase4auth10githubcred12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd55ec",
      "incomplete_value": true,
      "site": "00bd55ec",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b660ec",
      "incomplete_value": true,
      "site": "00b660ec",
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
            "const:7a8:8"
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
      "definition_site": "00bd560c",
      "incomplete_value": true,
      "site": "00bd560c",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6610c",
      "incomplete_value": true,
      "site": "00b6610c",
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
            "const:7a0:8"
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
      "definition_site": "00bd55c8",
      "incomplete_value": true,
      "site": "00bd55c8",
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
      "definition_site": "00b660c8",
      "incomplete_value": true,
      "site": "00b660c8",
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
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a17a8",
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
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011266b0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011266b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b660c0 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
- 00b660c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00bd55c0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd55c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00b660c8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b660cc ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b660d0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7a8:8"]]
+ 00bd55c8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd55cc ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd55d0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6b0:8"]]
- 00b660e8 ["INT_ADD", "register:40f0:8", ["const:b660e8:8", "const:4:8"]]
+ 00bd55e8 ["INT_ADD", "register:40f0:8", ["const:bd55e8:8", "const:4:8"]]
~~~


### [`00b66120`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66120.md) → [`00bd5620`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5620.md) _ZN8firebase4auth10githubcred14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd5660",
      "incomplete_value": true,
      "site": "00bd5660",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66160",
      "incomplete_value": true,
      "site": "00b66160",
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
            "const:7a0:8"
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
      "definition_site": "00bd563c",
      "incomplete_value": true,
      "site": "00bd563c",
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
      "definition_site": "00b6613c",
      "incomplete_value": true,
      "site": "00b6613c",
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
      "definition_site": "00bd5644",
      "incomplete_value": false,
      "site": "00bd5658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:da2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66144",
      "incomplete_value": false,
      "site": "00b66158",
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
            "const:7f9:8"
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
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a17a0",
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
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b6612c ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd562c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b66134 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00bd5634 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00b66140 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00b66144 ["COPY", "tmp:0:8", ["const:7f9:8"]]
+ 00bd5640 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00bd5644 ["COPY", "tmp:0:8", ["const:da2:8"]]
~~~


### [`00b66190`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66190.md) → [`00bd5690`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5690.md) _ZN8firebase4auth10githubcred11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd56ac",
      "incomplete_value": false,
      "site": "00bd56b0",
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
      "definition_site": "00b661ac",
      "incomplete_value": false,
      "site": "00b661b0",
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
      "definition_site": "00b661bc",
      "incomplete_value": true,
      "site": "00b661c8",
      "value": [
        "LOAD",
        "8",
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
        "010a17b0",
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
        "011266b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b661a8 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00b661ac ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00bd56a8 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00bd56ac ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b661b0 ["INT_ADD", "register:40f0:8", ["const:b661b0:8", "const:4:8"]]
+ 00bd56b0 ["INT_ADD", "register:40f0:8", ["const:bd56b0:8", "const:4:8"]]
- 00b661b4 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b661b8 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 00bd56b4 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd56b8 ["COPY", "tmp:0:8", ["const:6b8:8"]]
~~~


### [`00b661cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b661cc.md) → [`00bd56cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd56cc.md) _ZN8firebase4auth10githubcred13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd570c",
      "incomplete_value": true,
      "site": "00bd570c",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6620c",
      "incomplete_value": true,
      "site": "00b6620c",
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
            "const:7a0:8"
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
      "definition_site": "00bd56e8",
      "incomplete_value": true,
      "site": "00bd56e8",
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
      "definition_site": "00b661e8",
      "incomplete_value": true,
      "site": "00b661e8",
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
      "definition_site": "00bd56f0",
      "incomplete_value": false,
      "site": "00bd5704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:da2:8"
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
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a17a0",
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
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b661d8 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd56d8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b661e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00bd56e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
- 00b661e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b661ec ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00b661f0 ["COPY", "tmp:0:8", ["const:7f9:8"]]
+ 00bd56e8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd56ec ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00bd56f0 ["COPY", "tmp:0:8", ["const:da2:8"]]
~~~


### [`00b6623c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6623c.md) → [`00bd573c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd573c.md) _ZN8firebase4auth10githubcred10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd5758",
      "incomplete_value": false,
      "site": "00bd575c",
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
      "definition_site": "00b66258",
      "incomplete_value": false,
      "site": "00b6625c",
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
    "new": null,
    "old": {
      "definition_site": "00b66268",
      "incomplete_value": true,
      "site": "00b66274",
      "value": [
        "LOAD",
        "8",
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
        "010a17b8",
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
        "011266c0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66254 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00b66258 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00bd5754 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bd5758 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b6625c ["INT_ADD", "register:40f0:8", ["const:b6625c:8", "const:4:8"]]
+ 00bd575c ["INT_ADD", "register:40f0:8", ["const:bd575c:8", "const:4:8"]]
- 00b66260 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b66264 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 00bd5760 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd5764 ["COPY", "tmp:0:8", ["const:6c0:8"]]
~~~


### [`00b66278`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66278.md) → [`00bd5778`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5778.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00bd57a4",
      "incomplete_value": true,
      "site": "00bd57a4",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662a4",
      "incomplete_value": true,
      "site": "00b662a4",
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
            "const:7c0:8"
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
      "definition_site": "00bd578c",
      "incomplete_value": true,
      "site": "00bd578c",
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
      "definition_site": "00b6628c",
      "incomplete_value": true,
      "site": "00b6628c",
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
      "definition_site": "00bd5798",
      "incomplete_value": false,
      "site": "00bd579c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66298",
      "incomplete_value": false,
      "site": "00b6629c",
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
            "const:829:8"
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
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a17c0",
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
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66284 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66288 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00bd5784 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5788 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c8:8"]]
- 00b66294 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00b66298 ["COPY", "tmp:0:8", ["const:829:8"]]
+ 00bd5794 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00bd5798 ["COPY", "tmp:0:8", ["const:dd2:8"]]
- 00b6629c ["INT_ADD", "register:40f0:8", ["const:b6629c:8", "const:4:8"]]
+ 00bd579c ["INT_ADD", "register:40f0:8", ["const:bd579c:8", "const:4:8"]]
~~~


### [`00b662b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662b8.md) → [`00bd57b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57b8.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd57e4",
      "incomplete_value": true,
      "site": "00bd57e4",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662e4",
      "incomplete_value": true,
      "site": "00b662e4",
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
            "const:7c0:8"
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
      "definition_site": "00bd57cc",
      "incomplete_value": true,
      "site": "00bd57cc",
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
      "definition_site": "00b662cc",
      "incomplete_value": true,
      "site": "00b662cc",
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
      "definition_site": "00bd57d4",
      "incomplete_value": false,
      "site": "00bd57dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662d4",
      "incomplete_value": false,
      "site": "00b662dc",
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
            "const:829:8"
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
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a17c0",
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
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b662c4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b662c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00bd57c4 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd57c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c8:8"]]
- 00b662d0 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00b662d4 ["COPY", "tmp:0:8", ["const:829:8"]]
+ 00bd57d0 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00bd57d4 ["COPY", "tmp:0:8", ["const:dd2:8"]]
- 00b662dc ["INT_ADD", "register:40f0:8", ["const:b662dc:8", "const:4:8"]]
+ 00bd57dc ["INT_ADD", "register:40f0:8", ["const:bd57dc:8", "const:4:8"]]
~~~


### [`00b662f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662f8.md) → [`00bd57f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57f8.md) _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd5828",
      "incomplete_value": true,
      "site": "00bd5828",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66328",
      "incomplete_value": true,
      "site": "00b66328",
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
            "const:7c0:8"
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
      "definition_site": "00bd580c",
      "incomplete_value": true,
      "site": "00bd580c",
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
      "definition_site": "00b6630c",
      "incomplete_value": true,
      "site": "00b6630c",
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
      "definition_site": "00bd5818",
      "incomplete_value": false,
      "site": "00bd5820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66318",
      "incomplete_value": false,
      "site": "00b66320",
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
            "const:829:8"
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
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a17c0",
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
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66304 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66308 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00bd5804 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5808 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c8:8"]]
- 00b66310 ["COPY", "register:4018:8", ["const:2b0000:8"]]
+ 00bd5810 ["COPY", "register:4018:8", ["const:2c1000:8"]]
- 00b66318 ["COPY", "tmp:0:8", ["const:829:8"]]
+ 00bd5818 ["COPY", "tmp:0:8", ["const:dd2:8"]]
~~~


### [`00b6633c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6633c.md) → [`00bd583c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd583c.md) _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd586c",
      "incomplete_value": true,
      "site": "00bd586c",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6636c",
      "incomplete_value": true,
      "site": "00b6636c",
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
            "const:7c0:8"
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
      "definition_site": "00bd5850",
      "incomplete_value": true,
      "site": "00bd5850",
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
      "definition_site": "00b66350",
      "incomplete_value": true,
      "site": "00b66350",
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
      "definition_site": "00bd5858",
      "incomplete_value": false,
      "site": "00bd5864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66358",
      "incomplete_value": false,
      "site": "00b66364",
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
            "const:829:8"
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
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a17c0",
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
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66348 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b6634c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00bd5848 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd584c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c8:8"]]
- 00b66350 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66354 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00b66358 ["COPY", "tmp:0:8", ["const:829:8"]]
+ 00bd5850 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd5854 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00bd5858 ["COPY", "tmp:0:8", ["const:dd2:8"]]
- 00b66364 ["INT_ADD", "register:40f0:8", ["const:b66364:8", "const:4:8"]]
+ 00bd5864 ["INT_ADD", "register:40f0:8", ["const:bd5864:8", "const:4:8"]]
~~~


### [`00b66380`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66380.md) → [`00bd5880`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5880.md) _ZN8firebase4auth10googlecred8GetClassEv

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
      "definition_site": "00bd5884",
      "incomplete_value": true,
      "site": "00bd5888",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:6c8:8"
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
        "010a17c0",
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
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66380 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b66384 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7c0:8"]]
+ 00bd5880 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd5884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6c8:8"]]
~~~


### [`00b6638c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6638c.md) → [`00bd588c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd588c.md) _ZN8firebase4auth10googlecred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd58e4",
      "incomplete_value": true,
      "site": "00bd58e4",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b663e4",
      "incomplete_value": true,
      "site": "00b663e4",
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
            "const:7c8:8"
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
      "definition_site": "00bd58c0",
      "incomplete_value": true,
      "site": "00bd58cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:6c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b663c0",
      "incomplete_value": true,
      "site": "00b663cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:7c0:8"
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
        "010a17c8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "010a17c8",
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
        "011266d0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "011266d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b6639c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b663a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7c8:8"]]
+ 00bd589c ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd58a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6d0:8"]]
- 00b663b4 ["COPY", "register:4048:8", ["const:10a1000:8"]]
+ 00bd58b4 ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00b663c0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
+ 00bd58c0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6c8:8"]]
~~~


### [`00b663f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b663f8.md) → [`00bd58f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd58f8.md) _ZN8firebase4auth10googlecred12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5900",
      "incomplete_value": true,
      "site": "00bd5900",
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
      "definition_site": "00b66400",
      "incomplete_value": true,
      "site": "00b66400",
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
      "definition_site": "00bd5900",
      "incomplete_value": true,
      "site": "00bd5900",
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
      "definition_site": "00b66400",
      "incomplete_value": true,
      "site": "00b66400",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5934",
      "incomplete_value": true,
      "site": "00bd5934",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66434",
      "incomplete_value": true,
      "site": "00b66434",
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
            "const:7c8:8"
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
      20,
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a17c8",
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
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011266d0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011266d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66408 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
- 00b6640c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00bd5908 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd590c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c8:8"]]
- 00b66410 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b66414 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b66418 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7c8:8"]]
+ 00bd5910 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd5914 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd5918 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6d0:8"]]
- 00b66420 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd5920 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
~~~


### [`00b66468`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66468.md) → [`00bd5968`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5968.md) _ZN8firebase4auth10googlecred14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd59a8",
      "incomplete_value": true,
      "site": "00bd59a8",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b664a8",
      "incomplete_value": true,
      "site": "00b664a8",
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
            "const:7c0:8"
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
      "definition_site": "00bd5984",
      "incomplete_value": true,
      "site": "00bd5984",
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
      "definition_site": "00b66484",
      "incomplete_value": true,
      "site": "00b66484",
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
      "definition_site": "00bd598c",
      "incomplete_value": false,
      "site": "00bd59a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6648c",
      "incomplete_value": false,
      "site": "00b664a0",
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
            "const:829:8"
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
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a17c0",
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
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66474 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd5974 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b6647c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00bd597c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c8:8"]]
- 00b66488 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00b6648c ["COPY", "tmp:0:8", ["const:829:8"]]
+ 00bd5988 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00bd598c ["COPY", "tmp:0:8", ["const:dd2:8"]]
~~~


### [`00b664d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b664d8.md) → [`00bd59d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd59d8.md) _ZN8firebase4auth10googlecred11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd59f4",
      "incomplete_value": false,
      "site": "00bd59f8",
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
      "definition_site": "00b664f4",
      "incomplete_value": false,
      "site": "00b664f8",
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
      "definition_site": "00bd5a04",
      "incomplete_value": true,
      "site": "00bd5a10",
      "value": [
        "LOAD",
        "8",
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
        "010a17d0",
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
        "011266d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b664ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b664f0 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00b664f4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00bd59ec ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd59f0 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00bd59f4 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b664f8 ["INT_ADD", "register:40f0:8", ["const:b664f8:8", "const:4:8"]]
+ 00bd59f8 ["INT_ADD", "register:40f0:8", ["const:bd59f8:8", "const:4:8"]]
- 00b664fc ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b66500 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 00bd59fc ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd5a00 ["COPY", "tmp:0:8", ["const:6d8:8"]]
~~~


### [`00b66514`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66514.md) → [`00bd5a14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a14.md) _ZN8firebase4auth10googlecred13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd5a54",
      "incomplete_value": true,
      "site": "00bd5a54",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66554",
      "incomplete_value": true,
      "site": "00b66554",
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
            "const:7c0:8"
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
      "definition_site": "00bd5a30",
      "incomplete_value": true,
      "site": "00bd5a30",
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
    "old": {
      "definition_site": "00b66530",
      "incomplete_value": true,
      "site": "00b66530",
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
      "definition_site": "00bd5a38",
      "incomplete_value": false,
      "site": "00bd5a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66538",
      "incomplete_value": false,
      "site": "00b6654c",
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
            "const:829:8"
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
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a17c0",
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
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66520 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd5a20 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b66528 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00bd5a28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c8:8"]]
- 00b66530 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66534 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00b66538 ["COPY", "tmp:0:8", ["const:829:8"]]
+ 00bd5a30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd5a34 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00bd5a38 ["COPY", "tmp:0:8", ["const:dd2:8"]]
~~~


### [`00b66584`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66584.md) → [`00bd5a84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a84.md) _ZN8firebase4auth10googlecred10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd5aa0",
      "incomplete_value": false,
      "site": "00bd5aa4",
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
      "definition_site": "00b665a0",
      "incomplete_value": false,
      "site": "00b665a4",
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
      "definition_site": "00bd5ab0",
      "incomplete_value": true,
      "site": "00bd5abc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b665b0",
      "incomplete_value": true,
      "site": "00b665bc",
      "value": [
        "LOAD",
        "8",
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
        "010a17d8",
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
        "011266e0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00b6659c ["COPY", "register:4000:8", ["const:299000:8"]]
- 00b665a0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00bd5a9c ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bd5aa0 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b665a4 ["INT_ADD", "register:40f0:8", ["const:b665a4:8", "const:4:8"]]
+ 00bd5aa4 ["INT_ADD", "register:40f0:8", ["const:bd5aa4:8", "const:4:8"]]
- 00b665a8 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b665ac ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00bd5aa8 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd5aac ["COPY", "tmp:0:8", ["const:6e0:8"]]
~~~


### [`00b665c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b665c0.md) → [`00bd5ac0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ac0.md) _ZN8firebase4auth13playgamescred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00bd5ac4",
      "incomplete_value": true,
      "site": "00bd5ac4",
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
      "definition_site": "00b665c4",
      "incomplete_value": true,
      "site": "00b665c4",
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
      "definition_site": "00bd5ac4",
      "incomplete_value": true,
      "site": "00bd5ac4",
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
      "definition_site": "00b665c4",
      "incomplete_value": true,
      "site": "00b665c4",
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
      "definition_site": "00bd5aec",
      "incomplete_value": true,
      "site": "00bd5aec",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b665ec",
      "incomplete_value": true,
      "site": "00b665ec",
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
            "const:7e0:8"
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
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a17e0",
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
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b665cc ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b665d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00bd5acc ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5ad0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b665d4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd5ad4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b665dc ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b665e0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00bd5adc ["COPY", "register:4018:8", ["const:2b3000:8"]]
+ 00bd5ae0 ["COPY", "tmp:0:8", ["const:757:8"]]
~~~


### [`00b66600`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66600.md) → [`00bd5b00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b00.md) _ZN8firebase4auth13playgamescred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00bd5b2c",
      "incomplete_value": true,
      "site": "00bd5b2c",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6662c",
      "incomplete_value": true,
      "site": "00b6662c",
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
            "const:7e0:8"
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
      "definition_site": "00bd5b14",
      "incomplete_value": true,
      "site": "00bd5b14",
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
      "definition_site": "00b66614",
      "incomplete_value": true,
      "site": "00b66614",
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
      "definition_site": "00bd5b1c",
      "incomplete_value": false,
      "site": "00bd5b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:757:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6661c",
      "incomplete_value": false,
      "site": "00b66624",
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
            "const:78:8"
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
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a17e0",
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
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b6660c ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66610 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00bd5b0c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5b10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b66618 ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b6661c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00bd5b18 ["COPY", "register:4018:8", ["const:2b3000:8"]]
+ 00bd5b1c ["COPY", "tmp:0:8", ["const:757:8"]]
- 00b66624 ["INT_ADD", "register:40f0:8", ["const:b66624:8", "const:4:8"]]
+ 00bd5b24 ["INT_ADD", "register:40f0:8", ["const:bd5b24:8", "const:4:8"]]
~~~


### [`00b66640`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66640.md) → [`00bd5b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b40.md) _ZN8firebase4auth13playgamescred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd5b70",
      "incomplete_value": true,
      "site": "00bd5b70",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66670",
      "incomplete_value": true,
      "site": "00b66670",
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
            "const:7e0:8"
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
      "definition_site": "00bd5b54",
      "incomplete_value": true,
      "site": "00bd5b54",
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
      "definition_site": "00b66654",
      "incomplete_value": true,
      "site": "00b66654",
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
      "definition_site": "00bd5b60",
      "incomplete_value": false,
      "site": "00bd5b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:757:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66660",
      "incomplete_value": false,
      "site": "00b66668",
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
            "const:78:8"
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
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a17e0",
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
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b6664c ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66650 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00bd5b4c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5b50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b66658 ["COPY", "register:4018:8", ["const:2a3000:8"]]
+ 00bd5b58 ["COPY", "register:4018:8", ["const:2b3000:8"]]
- 00b66660 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00bd5b60 ["COPY", "tmp:0:8", ["const:757:8"]]
~~~


### [`00b66684`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66684.md) → [`00bd5b84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b84.md) _ZN8firebase4auth13playgamescred10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5bb4",
      "incomplete_value": true,
      "site": "00bd5bb4",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b666b4",
      "incomplete_value": true,
      "site": "00b666b4",
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
            "const:7e0:8"
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
      "definition_site": "00bd5b98",
      "incomplete_value": true,
      "site": "00bd5b98",
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
      "definition_site": "00b66698",
      "incomplete_value": true,
      "site": "00b66698",
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
      "definition_site": "00bd5ba4",
      "incomplete_value": false,
      "site": "00bd5bac",
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
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a17e0",
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
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66690 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66694 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00bd5b90 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b66698 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6669c ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b666a0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00bd5b98 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd5b9c ["COPY", "register:4018:8", ["const:2b3000:8"]]
+ 00bd5ba0 ["COPY", "tmp:0:8", ["const:757:8"]]
- 00b666ac ["INT_ADD", "register:40f0:8", ["const:b666ac:8", "const:4:8"]]
+ 00bd5bac ["INT_ADD", "register:40f0:8", ["const:bd5bac:8", "const:4:8"]]
~~~


### [`00b666d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b666d4.md) → [`00bd5bd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5bd4.md) _ZN8firebase4auth13playgamescred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5bd8",
      "incomplete_value": true,
      "site": "00bd5bd8",
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
      "definition_site": "00b666d8",
      "incomplete_value": true,
      "site": "00b666d8",
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
      "definition_site": "00bd5bd8",
      "incomplete_value": true,
      "site": "00bd5bd8",
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
      "definition_site": "00b666d8",
      "incomplete_value": true,
      "site": "00b666d8",
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
      "definition_site": "00bd5bdc",
      "incomplete_value": true,
      "site": "00bd5bdc",
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
      "definition_site": "00b666dc",
      "incomplete_value": true,
      "site": "00b666dc",
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
        "010a17e8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "010a17e8",
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
        "011266f0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b666e4 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b666e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7e8:8"]]
+ 00bd5be4 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd5be8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6f0:8"]]
- 00b666ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd5bec ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b666f4 ["BRANCH", null, ["local:b3:8"]]
+ 00bd5bf4 ["BRANCH", null, ["local:b4:8"]]
~~~


### [`00b66740`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66740.md) → [`00bd5c40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5c40.md) _ZN8firebase4auth13playgamescred12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5c7c",
      "incomplete_value": true,
      "site": "00bd5c7c",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6677c",
      "incomplete_value": true,
      "site": "00b6677c",
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
            "const:7e8:8"
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
      "definition_site": "00bd5c9c",
      "incomplete_value": true,
      "site": "00bd5c9c",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6679c",
      "incomplete_value": true,
      "site": "00b6679c",
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
            "const:7e0:8"
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
      "definition_site": "00bd5c58",
      "incomplete_value": true,
      "site": "00bd5c58",
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
      "definition_site": "00b66758",
      "incomplete_value": true,
      "site": "00b66758",
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
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a17e8",
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
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66750 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
- 00b66754 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00bd5c50 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd5c54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00b6675c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b66760 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7e8:8"]]
+ 00bd5c5c ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd5c60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6f0:8"]]
- 00b66778 ["INT_ADD", "register:40f0:8", ["const:b66778:8", "const:4:8"]]
+ 00bd5c78 ["INT_ADD", "register:40f0:8", ["const:bd5c78:8", "const:4:8"]]
~~~


### [`00b667b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b667b0.md) → [`00bd5cb0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5cb0.md) _ZN8firebase4auth13playgamescred14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd5cf0",
      "incomplete_value": true,
      "site": "00bd5cf0",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b667f0",
      "incomplete_value": true,
      "site": "00b667f0",
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
            "const:7e0:8"
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
      "definition_site": "00bd5ccc",
      "incomplete_value": true,
      "site": "00bd5ccc",
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
      "definition_site": "00b667cc",
      "incomplete_value": true,
      "site": "00b667cc",
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
      "definition_site": "00bd5cd4",
      "incomplete_value": false,
      "site": "00bd5ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:757:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b667d4",
      "incomplete_value": false,
      "site": "00b667e8",
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
            "const:78:8"
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
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a17e0",
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
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b667bc ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd5cbc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b667c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00bd5cc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00b667d0 ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b667d4 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00bd5cd0 ["COPY", "register:4018:8", ["const:2b3000:8"]]
+ 00bd5cd4 ["COPY", "tmp:0:8", ["const:757:8"]]
~~~


### [`00b66820`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66820.md) → [`00bd5d20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d20.md) _ZN8firebase4auth13playgamescred11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd5d34",
      "incomplete_value": true,
      "site": "00bd5d34",
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
      "definition_site": "00b66834",
      "incomplete_value": true,
      "site": "00b66834",
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
      "definition_site": "00bd5d3c",
      "incomplete_value": false,
      "site": "00bd5d40",
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
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd5d4c",
      "incomplete_value": true,
      "site": "00bd5d58",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6684c",
      "incomplete_value": true,
      "site": "00b66858",
      "value": [
        "LOAD",
        "8",
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
        "010a17f0",
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
        "011266f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66834 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b66838 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00b6683c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00bd5d34 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd5d38 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00bd5d3c ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b66840 ["INT_ADD", "register:40f0:8", ["const:b66840:8", "const:4:8"]]
+ 00bd5d40 ["INT_ADD", "register:40f0:8", ["const:bd5d40:8", "const:4:8"]]
- 00b66844 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b66848 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 00bd5d44 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd5d48 ["COPY", "tmp:0:8", ["const:6f8:8"]]
~~~


### [`00b6685c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6685c.md) → [`00bd5d5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d5c.md) _ZN8firebase4auth13playgamescred13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd5d9c",
      "incomplete_value": true,
      "site": "00bd5d9c",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6689c",
      "incomplete_value": true,
      "site": "00b6689c",
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
            "const:7e0:8"
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
      "definition_site": "00bd5d78",
      "incomplete_value": true,
      "site": "00bd5d78",
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
      "definition_site": "00b66878",
      "incomplete_value": true,
      "site": "00b66878",
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
      "definition_site": "00bd5d80",
      "incomplete_value": false,
      "site": "00bd5d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:757:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66880",
      "incomplete_value": false,
      "site": "00b66894",
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
            "const:78:8"
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
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a3078",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a17e0",
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
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66868 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd5d68 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b66870 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00bd5d70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00b6687c ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b66880 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00bd5d7c ["COPY", "register:4018:8", ["const:2b3000:8"]]
+ 00bd5d80 ["COPY", "tmp:0:8", ["const:757:8"]]
~~~


### [`00b668cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b668cc.md) → [`00bd5dcc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5dcc.md) _ZN8firebase4auth13playgamescred10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd5de8",
      "incomplete_value": false,
      "site": "00bd5dec",
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
      "definition_site": "00b668e8",
      "incomplete_value": false,
      "site": "00b668ec",
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
      "definition_site": "00bd5df8",
      "incomplete_value": true,
      "site": "00bd5e04",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b668f8",
      "incomplete_value": true,
      "site": "00b66904",
      "value": [
        "LOAD",
        "8",
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
        "010a17f8",
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
        "01126700",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00b668e4 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00b668e8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00bd5de4 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bd5de8 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b668ec ["INT_ADD", "register:40f0:8", ["const:b668ec:8", "const:4:8"]]
+ 00bd5dec ["INT_ADD", "register:40f0:8", ["const:bd5dec:8", "const:4:8"]]
- 00b668f0 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b668f4 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 00bd5df0 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd5df4 ["COPY", "tmp:0:8", ["const:700:8"]]
~~~


### [`00b66908`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66908.md) → [`00bd5e08`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e08.md) _ZN8firebase4auth11twittercred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd5e34",
      "incomplete_value": true,
      "site": "00bd5e34",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66934",
      "incomplete_value": true,
      "site": "00b66934",
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
            "const:800:8"
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
      "definition_site": "00bd5e1c",
      "incomplete_value": true,
      "site": "00bd5e1c",
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
      "definition_site": "00b6691c",
      "incomplete_value": true,
      "site": "00b6691c",
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
      "definition_site": "00bd5e28",
      "incomplete_value": false,
      "site": "00bd5e2c",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66928",
      "incomplete_value": false,
      "site": "00b6692c",
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
            "const:53b:8"
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
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a1800",
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
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66914 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66918 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00bd5e14 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5e18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00b66924 ["COPY", "register:4018:8", ["const:292000:8"]]
- 00b66928 ["COPY", "tmp:0:8", ["const:53b:8"]]
+ 00bd5e24 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00bd5e28 ["COPY", "tmp:0:8", ["const:c4b:8"]]
- 00b6692c ["INT_ADD", "register:40f0:8", ["const:b6692c:8", "const:4:8"]]
+ 00bd5e2c ["INT_ADD", "register:40f0:8", ["const:bd5e2c:8", "const:4:8"]]
~~~


### [`00b66948`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66948.md) → [`00bd5e48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e48.md) _ZN8firebase4auth11twittercred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd5e74",
      "incomplete_value": true,
      "site": "00bd5e74",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66974",
      "incomplete_value": true,
      "site": "00b66974",
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
            "const:800:8"
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
      "definition_site": "00bd5e5c",
      "incomplete_value": true,
      "site": "00bd5e5c",
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
      "definition_site": "00b6695c",
      "incomplete_value": true,
      "site": "00b6695c",
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
      "definition_site": "00bd5e64",
      "incomplete_value": false,
      "site": "00bd5e6c",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66964",
      "incomplete_value": false,
      "site": "00b6696c",
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
            "const:53b:8"
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
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a1800",
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
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66954 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66958 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00bd5e54 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5e58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00b66960 ["COPY", "register:4018:8", ["const:292000:8"]]
- 00b66964 ["COPY", "tmp:0:8", ["const:53b:8"]]
+ 00bd5e60 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00bd5e64 ["COPY", "tmp:0:8", ["const:c4b:8"]]
- 00b6696c ["INT_ADD", "register:40f0:8", ["const:b6696c:8", "const:4:8"]]
+ 00bd5e6c ["INT_ADD", "register:40f0:8", ["const:bd5e6c:8", "const:4:8"]]
~~~


### [`00b66988`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66988.md) → [`00bd5e88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e88.md) _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd5eb8",
      "incomplete_value": true,
      "site": "00bd5eb8",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669b8",
      "incomplete_value": true,
      "site": "00b669b8",
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
            "const:800:8"
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
      "definition_site": "00bd5e9c",
      "incomplete_value": true,
      "site": "00bd5e9c",
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
      "definition_site": "00b6699c",
      "incomplete_value": true,
      "site": "00b6699c",
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
      "definition_site": "00bd5ea8",
      "incomplete_value": false,
      "site": "00bd5eb0",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669a8",
      "incomplete_value": false,
      "site": "00b669b0",
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
            "const:53b:8"
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
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a1800",
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
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66994 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66998 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00bd5e94 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5e98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00b669a0 ["COPY", "register:4018:8", ["const:292000:8"]]
+ 00bd5ea0 ["COPY", "register:4018:8", ["const:2a1000:8"]]
- 00b669a8 ["COPY", "tmp:0:8", ["const:53b:8"]]
+ 00bd5ea8 ["COPY", "tmp:0:8", ["const:c4b:8"]]
~~~


### [`00b669cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b669cc.md) → [`00bd5ecc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ecc.md) _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd5efc",
      "incomplete_value": true,
      "site": "00bd5efc",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669fc",
      "incomplete_value": true,
      "site": "00b669fc",
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
            "const:800:8"
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
      "definition_site": "00bd5ee0",
      "incomplete_value": true,
      "site": "00bd5ee0",
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
      "definition_site": "00b669e0",
      "incomplete_value": true,
      "site": "00b669e0",
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
      "definition_site": "00bd5ee8",
      "incomplete_value": false,
      "site": "00bd5ef4",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669e8",
      "incomplete_value": false,
      "site": "00b669f4",
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
            "const:53b:8"
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
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a1800",
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
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b669d8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b669dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
+ 00bd5ed8 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd5edc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00b669e4 ["COPY", "register:4018:8", ["const:292000:8"]]
- 00b669e8 ["COPY", "tmp:0:8", ["const:53b:8"]]
+ 00bd5ee4 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00bd5ee8 ["COPY", "tmp:0:8", ["const:c4b:8"]]
- 00b669f4 ["INT_ADD", "register:40f0:8", ["const:b669f4:8", "const:4:8"]]
+ 00bd5ef4 ["INT_ADD", "register:40f0:8", ["const:bd5ef4:8", "const:4:8"]]
~~~


### [`00b66a1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a1c.md) → [`00bd5f1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f1c.md) _ZN8firebase4auth11twittercred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5f74",
      "incomplete_value": true,
      "site": "00bd5f74",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66a74",
      "incomplete_value": true,
      "site": "00b66a74",
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
            "const:808:8"
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
      "definition_site": "00bd5f50",
      "incomplete_value": true,
      "site": "00bd5f5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00b66a50",
      "incomplete_value": true,
      "site": "00b66a5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:800:8"
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
        "010a1808",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "010a1808",
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
        "01126710",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66a2c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b66a30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00bd5f2c ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd5f30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:710:8"]]
- 00b66a44 ["COPY", "register:4048:8", ["const:10a1000:8"]]
+ 00bd5f44 ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00b66a50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:800:8"]]
+ 00bd5f50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:708:8"]]
~~~


### [`00b66a88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66a88.md) → [`00bd5f88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5f88.md) _ZN8firebase4auth11twittercred12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5fc4",
      "incomplete_value": true,
      "site": "00bd5fc4",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ac4",
      "incomplete_value": true,
      "site": "00b66ac4",
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
            "const:808:8"
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
      "definition_site": "00bd5fe4",
      "incomplete_value": true,
      "site": "00bd5fe4",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ae4",
      "incomplete_value": true,
      "site": "00b66ae4",
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
            "const:800:8"
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
      "definition_site": "00bd5fa0",
      "incomplete_value": true,
      "site": "00bd5fa0",
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
      "definition_site": "00b66aa0",
      "incomplete_value": true,
      "site": "00b66aa0",
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
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a1808",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a1808",
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
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126710",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66a98 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
- 00b66a9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00bd5f98 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd5f9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:708:8"]]
- 00b66aa4 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b66aa8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00bd5fa4 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd5fa8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:710:8"]]
- 00b66ac0 ["INT_ADD", "register:40f0:8", ["const:b66ac0:8", "const:4:8"]]
+ 00bd5fc0 ["INT_ADD", "register:40f0:8", ["const:bd5fc0:8", "const:4:8"]]
~~~


### [`00b66af8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66af8.md) → [`00bd5ff8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ff8.md) _ZN8firebase4auth11twittercred14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6038",
      "incomplete_value": true,
      "site": "00bd6038",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66b38",
      "incomplete_value": true,
      "site": "00b66b38",
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
            "const:800:8"
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
      "definition_site": "00bd6014",
      "incomplete_value": true,
      "site": "00bd6014",
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
      "definition_site": "00b66b14",
      "incomplete_value": true,
      "site": "00b66b14",
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
      "definition_site": "00bd601c",
      "incomplete_value": false,
      "site": "00bd6030",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66b1c",
      "incomplete_value": false,
      "site": "00b66b30",
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
            "const:53b:8"
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
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1800",
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
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66b04 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd6004 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b66b0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00bd600c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:708:8"]]
- 00b66b18 ["COPY", "register:4018:8", ["const:292000:8"]]
- 00b66b1c ["COPY", "tmp:0:8", ["const:53b:8"]]
+ 00bd6018 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00bd601c ["COPY", "tmp:0:8", ["const:c4b:8"]]
~~~


### [`00b66b68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66b68.md) → [`00bd6068`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6068.md) _ZN8firebase4auth11twittercred11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd6084",
      "incomplete_value": false,
      "site": "00bd6088",
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
      "definition_site": "00b66b84",
      "incomplete_value": false,
      "site": "00b66b88",
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
      "definition_site": "00bd6094",
      "incomplete_value": true,
      "site": "00bd60a0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66b94",
      "incomplete_value": true,
      "site": "00b66ba0",
      "value": [
        "LOAD",
        "8",
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
        "010a1810",
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
        "01126718",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66b80 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00b66b84 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00bd6080 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00bd6084 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b66b88 ["INT_ADD", "register:40f0:8", ["const:b66b88:8", "const:4:8"]]
+ 00bd6088 ["INT_ADD", "register:40f0:8", ["const:bd6088:8", "const:4:8"]]
- 00b66b8c ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b66b90 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 00bd608c ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd6090 ["COPY", "tmp:0:8", ["const:718:8"]]
~~~


### [`00b66ba4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66ba4.md) → [`00bd60a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd60a4.md) _ZN8firebase4auth11twittercred13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd60e4",
      "incomplete_value": true,
      "site": "00bd60e4",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66be4",
      "incomplete_value": true,
      "site": "00b66be4",
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
            "const:800:8"
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
      "definition_site": "00bd60c0",
      "incomplete_value": true,
      "site": "00bd60c0",
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
      "definition_site": "00b66bc0",
      "incomplete_value": true,
      "site": "00b66bc0",
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
      "definition_site": "00bd60c8",
      "incomplete_value": false,
      "site": "00bd60dc",
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
            "const:c4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66bc8",
      "incomplete_value": false,
      "site": "00b66bdc",
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
            "const:53b:8"
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
        "010a1800",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1800",
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
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66bb0 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd60b0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b66bb8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:800:8"]]
+ 00bd60b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:708:8"]]
- 00b66bc4 ["COPY", "register:4018:8", ["const:292000:8"]]
- 00b66bc8 ["COPY", "tmp:0:8", ["const:53b:8"]]
+ 00bd60c4 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00bd60c8 ["COPY", "tmp:0:8", ["const:c4b:8"]]
~~~


### [`00b66c14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c14.md) → [`00bd6114`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6114.md) _ZN8firebase4auth11twittercred10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd6130",
      "incomplete_value": false,
      "site": "00bd6134",
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
      "definition_site": "00b66c30",
      "incomplete_value": false,
      "site": "00b66c34",
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
      "definition_site": "00bd6140",
      "incomplete_value": true,
      "site": "00bd614c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66c40",
      "incomplete_value": true,
      "site": "00b66c4c",
      "value": [
        "LOAD",
        "8",
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
        "010a1818",
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
        "01126720",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66c2c ["COPY", "register:4000:8", ["const:299000:8"]]
- 00b66c30 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00bd612c ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bd6130 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b66c34 ["INT_ADD", "register:40f0:8", ["const:b66c34:8", "const:4:8"]]
+ 00bd6134 ["INT_ADD", "register:40f0:8", ["const:bd6134:8", "const:4:8"]]
- 00b66c38 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b66c3c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00bd6138 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd613c ["COPY", "tmp:0:8", ["const:720:8"]]
~~~


### [`00b66c50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c50.md) → [`00bd6150`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6150.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00bd617c",
      "incomplete_value": true,
      "site": "00bd617c",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66c7c",
      "incomplete_value": true,
      "site": "00b66c7c",
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
            "const:820:8"
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
      "definition_site": "00bd6164",
      "incomplete_value": true,
      "site": "00bd6164",
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
      "definition_site": "00b66c64",
      "incomplete_value": true,
      "site": "00b66c64",
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
      "definition_site": "00bd6170",
      "incomplete_value": false,
      "site": "00bd6174",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66c70",
      "incomplete_value": false,
      "site": "00b66c74",
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
            "const:71:8"
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
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a1820",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66c5c ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66c60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00bd615c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6160 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b66c6c ["COPY", "register:4018:8", ["const:2a9000:8"]]
- 00b66c70 ["COPY", "tmp:0:8", ["const:71:8"]]
+ 00bd616c ["COPY", "register:4018:8", ["const:2b9000:8"]]
+ 00bd6170 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00b66c74 ["INT_ADD", "register:40f0:8", ["const:b66c74:8", "const:4:8"]]
+ 00bd6174 ["INT_ADD", "register:40f0:8", ["const:bd6174:8", "const:4:8"]]
~~~


### [`00b66c90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66c90.md) → [`00bd6190`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6190.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00bd61bc",
      "incomplete_value": true,
      "site": "00bd61bc",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66cbc",
      "incomplete_value": true,
      "site": "00b66cbc",
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
            "const:820:8"
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
      "definition_site": "00bd61a4",
      "incomplete_value": true,
      "site": "00bd61a4",
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
      "definition_site": "00b66ca4",
      "incomplete_value": true,
      "site": "00b66ca4",
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
      "definition_site": "00bd61ac",
      "incomplete_value": false,
      "site": "00bd61b4",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66cac",
      "incomplete_value": false,
      "site": "00b66cb4",
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
            "const:71:8"
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
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a1820",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66c9c ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66ca0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00bd619c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd61a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b66ca8 ["COPY", "register:4018:8", ["const:2a9000:8"]]
- 00b66cac ["COPY", "tmp:0:8", ["const:71:8"]]
+ 00bd61a8 ["COPY", "register:4018:8", ["const:2b9000:8"]]
+ 00bd61ac ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00b66cb4 ["INT_ADD", "register:40f0:8", ["const:b66cb4:8", "const:4:8"]]
+ 00bd61b4 ["INT_ADD", "register:40f0:8", ["const:bd61b4:8", "const:4:8"]]
~~~


### [`00b66cd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66cd0.md) → [`00bd61d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd61d0.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd6200",
      "incomplete_value": true,
      "site": "00bd6200",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d00",
      "incomplete_value": true,
      "site": "00b66d00",
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
            "const:820:8"
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
      "definition_site": "00bd61e4",
      "incomplete_value": true,
      "site": "00bd61e4",
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
      "definition_site": "00b66ce4",
      "incomplete_value": true,
      "site": "00b66ce4",
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
      "definition_site": "00bd61f0",
      "incomplete_value": false,
      "site": "00bd61f8",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66cf0",
      "incomplete_value": false,
      "site": "00b66cf8",
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
            "const:71:8"
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
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a1820",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66cdc ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66ce0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00bd61dc ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd61e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b66ce8 ["COPY", "register:4018:8", ["const:2a9000:8"]]
+ 00bd61e8 ["COPY", "register:4018:8", ["const:2b9000:8"]]
- 00b66cf0 ["COPY", "tmp:0:8", ["const:71:8"]]
+ 00bd61f0 ["COPY", "tmp:0:8", ["const:d08:8"]]
~~~


### [`00b66d14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d14.md) → [`00bd6214`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6214.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6244",
      "incomplete_value": true,
      "site": "00bd6244",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d44",
      "incomplete_value": true,
      "site": "00b66d44",
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
            "const:820:8"
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
      "definition_site": "00bd6228",
      "incomplete_value": true,
      "site": "00bd6228",
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
      "definition_site": "00b66d28",
      "incomplete_value": true,
      "site": "00b66d28",
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
      "definition_site": "00bd6230",
      "incomplete_value": false,
      "site": "00bd623c",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d30",
      "incomplete_value": false,
      "site": "00b66d3c",
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
            "const:71:8"
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
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a1820",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66d20 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66d24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:820:8"]]
+ 00bd6220 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6224 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b66d2c ["COPY", "register:4018:8", ["const:2a9000:8"]]
- 00b66d30 ["COPY", "tmp:0:8", ["const:71:8"]]
+ 00bd622c ["COPY", "register:4018:8", ["const:2b9000:8"]]
+ 00bd6230 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00b66d3c ["INT_ADD", "register:40f0:8", ["const:b66d3c:8", "const:4:8"]]
+ 00bd623c ["INT_ADD", "register:40f0:8", ["const:bd623c:8", "const:4:8"]]
~~~


### [`00b66d64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66d64.md) → [`00bd6264`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6264.md) _ZN8firebase4auth13oauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd62bc",
      "incomplete_value": true,
      "site": "00bd62bc",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66dbc",
      "incomplete_value": true,
      "site": "00b66dbc",
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
            "const:828:8"
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
      "definition_site": "00bd6298",
      "incomplete_value": true,
      "site": "00bd62a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00b66d98",
      "incomplete_value": true,
      "site": "00b66da4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:820:8"
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
        "010a1828",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "010a1828",
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
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66d74 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b66d78 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:828:8"]]
+ 00bd6274 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd6278 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:730:8"]]
- 00b66d8c ["COPY", "register:4048:8", ["const:10a1000:8"]]
+ 00bd628c ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00b66d98 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:820:8"]]
+ 00bd6298 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
~~~


### [`00b66dd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66dd0.md) → [`00bd62d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd62d0.md) _ZN8firebase4auth13oauthprovider12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd62d4",
      "incomplete_value": true,
      "site": "00bd62d4",
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
      "definition_site": "00b66dd4",
      "incomplete_value": true,
      "site": "00b66dd4",
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
      "definition_site": "00bd62d4",
      "incomplete_value": true,
      "site": "00bd62d4",
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
      "definition_site": "00b66dd4",
      "incomplete_value": true,
      "site": "00b66dd4",
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
      "definition_site": "00bd62d8",
      "incomplete_value": true,
      "site": "00bd62d8",
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
      "definition_site": "00b66dd8",
      "incomplete_value": true,
      "site": "00b66dd8",
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
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a1828",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66de0 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
- 00b66de4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
+ 00bd62e0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd62e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00b66de8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b66dec ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b66df0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:828:8"]]
+ 00bd62e8 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00bd62ec ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd62f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:730:8"]]
- 00b66df8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd62f8 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
~~~


### [`00b66e40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66e40.md) → [`00bd6340`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6340.md) _ZN8firebase4auth13oauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6380",
      "incomplete_value": true,
      "site": "00bd6380",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66e80",
      "incomplete_value": true,
      "site": "00b66e80",
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
            "const:820:8"
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
      "definition_site": "00bd635c",
      "incomplete_value": true,
      "site": "00bd635c",
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
      "definition_site": "00b66e5c",
      "incomplete_value": true,
      "site": "00b66e5c",
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
      "definition_site": "00b66e68",
      "incomplete_value": true,
      "site": "00b66e78",
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
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1820",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66e4c ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd634c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b66e54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
+ 00bd6354 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00b66e5c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66e60 ["COPY", "register:4018:8", ["const:2a9000:8"]]
- 00b66e64 ["COPY", "tmp:0:8", ["const:71:8"]]
+ 00bd635c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00bd6360 ["COPY", "register:4018:8", ["const:2b9000:8"]]
+ 00bd6364 ["COPY", "tmp:0:8", ["const:d08:8"]]
~~~


### [`00b66eb0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66eb0.md) → [`00bd63b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63b0.md) _ZN8firebase4auth13oauthprovider11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd63cc",
      "incomplete_value": true,
      "site": "00bd63d0",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ecc",
      "incomplete_value": false,
      "site": "00b66ed0",
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
      "definition_site": "00b66edc",
      "incomplete_value": true,
      "site": "00b66ee8",
      "value": [
        "LOAD",
        "8",
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
        "010a1830",
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
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66ec4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66ec8 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00b66ecc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00bd63c4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd63c8 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00bd63cc ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b66ed0 ["INT_ADD", "register:40f0:8", ["const:b66ed0:8", "const:4:8"]]
+ 00bd63d0 ["INT_ADD", "register:40f0:8", ["const:bd63d0:8", "const:4:8"]]
- 00b66ed4 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b66ed8 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00bd63d4 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd63d8 ["COPY", "tmp:0:8", ["const:738:8"]]
~~~


### [`00b66eec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66eec.md) → [`00bd63ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63ec.md) _ZN8firebase4auth13oauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd642c",
      "incomplete_value": true,
      "site": "00bd642c",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66f2c",
      "incomplete_value": true,
      "site": "00b66f2c",
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
            "const:820:8"
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
      "definition_site": "00bd6408",
      "incomplete_value": true,
      "site": "00bd6408",
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
    "old": {
      "definition_site": "00b66f08",
      "incomplete_value": true,
      "site": "00b66f08",
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
      "definition_site": "00bd6414",
      "incomplete_value": true,
      "site": "00bd6424",
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
        "010a1820",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a9071",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1820",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b9d08",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66ef8 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd63f8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b66f00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
+ 00bd6400 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00b66f08 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b66f0c ["COPY", "register:4018:8", ["const:2a9000:8"]]
- 00b66f10 ["COPY", "tmp:0:8", ["const:71:8"]]
+ 00bd6408 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd640c ["COPY", "register:4018:8", ["const:2b9000:8"]]
+ 00bd6410 ["COPY", "tmp:0:8", ["const:d08:8"]]
~~~


### [`00b66f5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66f5c.md) → [`00bd645c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd645c.md) _ZN8firebase4auth13oauthprovider10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd6460",
      "incomplete_value": true,
      "site": "00bd6460",
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
      "definition_site": "00b66f60",
      "incomplete_value": true,
      "site": "00b66f60",
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
      "definition_site": "00bd6460",
      "incomplete_value": true,
      "site": "00bd6460",
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
      "definition_site": "00b66f60",
      "incomplete_value": true,
      "site": "00b66f60",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6478",
      "incomplete_value": false,
      "site": "00bd647c",
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
      "definition_site": "00b66f78",
      "incomplete_value": false,
      "site": "00b66f7c",
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
        "010a1848",
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
        "01126750",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66f70 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66f74 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00b66f78 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00bd6470 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd6474 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bd6478 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b66f7c ["INT_ADD", "register:40f0:8", ["const:b66f7c:8", "const:4:8"]]
+ 00bd647c ["INT_ADD", "register:40f0:8", ["const:bd647c:8", "const:4:8"]]
- 00b66f80 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b66f84 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bd6480 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd6484 ["COPY", "tmp:0:8", ["const:750:8"]]
~~~


### [`00b66f98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66f98.md) → [`00bd6498`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6498.md) _ZN8firebase4auth8timeunit19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd64c4",
      "incomplete_value": true,
      "site": "00bd64c4",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66fc4",
      "incomplete_value": true,
      "site": "00b66fc4",
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
            "const:850:8"
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
      "definition_site": "00bd64ac",
      "incomplete_value": true,
      "site": "00bd64ac",
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
      "definition_site": "00b66fac",
      "incomplete_value": true,
      "site": "00b66fac",
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
      "definition_site": "00bd64b8",
      "incomplete_value": false,
      "site": "00bd64bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:78a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66fb8",
      "incomplete_value": false,
      "site": "00b66fbc",
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
            "const:ab:8"
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
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a1850",
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
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b378a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66fa4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66fa8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00bd64a4 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd64a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b66fac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd64ac ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b66fb4 ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b66fb8 ["COPY", "tmp:0:8", ["const:ab:8"]]
+ 00bd64b4 ["COPY", "register:4018:8", ["const:2b3000:8"]]
+ 00bd64b8 ["COPY", "tmp:0:8", ["const:78a:8"]]
~~~


### [`00b66fd8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66fd8.md) → [`00bd64d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd64d8.md) _ZN8firebase4auth8timeunit19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd6504",
      "incomplete_value": true,
      "site": "00bd6504",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67004",
      "incomplete_value": true,
      "site": "00b67004",
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
            "const:850:8"
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
      "definition_site": "00bd64ec",
      "incomplete_value": true,
      "site": "00bd64ec",
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
      "definition_site": "00b66fec",
      "incomplete_value": true,
      "site": "00b66fec",
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
      "definition_site": "00b66ff4",
      "incomplete_value": false,
      "site": "00b66ffc",
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
            "const:ab:8"
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
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a1850",
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
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b378a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b66fe4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b66fe8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00bd64e4 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd64e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b66fec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66ff0 ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b66ff4 ["COPY", "tmp:0:8", ["const:ab:8"]]
+ 00bd64ec ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bd64f0 ["COPY", "register:4018:8", ["const:2b3000:8"]]
+ 00bd64f4 ["COPY", "tmp:0:8", ["const:78a:8"]]
- 00b66ffc ["INT_ADD", "register:40f0:8", ["const:b66ffc:8", "const:4:8"]]
+ 00bd64fc ["INT_ADD", "register:40f0:8", ["const:bd64fc:8", "const:4:8"]]
~~~


### [`00b67018`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67018.md) → [`00bd6518`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6518.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd6548",
      "incomplete_value": true,
      "site": "00bd6548",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67048",
      "incomplete_value": true,
      "site": "00b67048",
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
            "const:850:8"
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
      "definition_site": "00bd652c",
      "incomplete_value": true,
      "site": "00bd652c",
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
      "definition_site": "00b6702c",
      "incomplete_value": true,
      "site": "00b6702c",
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
      "definition_site": "00b67038",
      "incomplete_value": false,
      "site": "00b67040",
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
            "const:ab:8"
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
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a1850",
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
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b378a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67024 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b67028 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00bd6524 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6528 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b6702c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b67030 ["COPY", "register:4018:8", ["const:2a3000:8"]]
+ 00bd652c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bd6530 ["COPY", "register:4018:8", ["const:2b3000:8"]]
- 00b67038 ["COPY", "tmp:0:8", ["const:ab:8"]]
+ 00bd6538 ["COPY", "tmp:0:8", ["const:78a:8"]]
~~~


### [`00b6705c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6705c.md) → [`00bd655c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd655c.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd658c",
      "incomplete_value": true,
      "site": "00bd658c",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6708c",
      "incomplete_value": true,
      "site": "00b6708c",
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
            "const:850:8"
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
      "definition_site": "00bd6570",
      "incomplete_value": true,
      "site": "00bd6570",
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
      "definition_site": "00b67070",
      "incomplete_value": true,
      "site": "00b67070",
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
      "definition_site": "00bd6578",
      "incomplete_value": true,
      "site": "00bd6584",
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
            "const:78a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67078",
      "incomplete_value": false,
      "site": "00b67084",
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
            "const:ab:8"
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
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a1850",
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
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b378a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67068 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b6706c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00bd6568 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd656c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b67070 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b67074 ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b67078 ["COPY", "tmp:0:8", ["const:ab:8"]]
+ 00bd6570 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd6574 ["COPY", "register:4018:8", ["const:2b3000:8"]]
+ 00bd6578 ["COPY", "tmp:0:8", ["const:78a:8"]]
- 00b67084 ["INT_ADD", "register:40f0:8", ["const:b67084:8", "const:4:8"]]
+ 00bd6584 ["INT_ADD", "register:40f0:8", ["const:bd6584:8", "const:4:8"]]
~~~


### [`00b670ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b670ac.md) → [`00bd65ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd65ac.md) _ZN8firebase4auth8timeunit15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_destination` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd65b0",
      "incomplete_value": true,
      "site": "00bd65b0",
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
      "definition_site": "00b670b0",
      "incomplete_value": true,
      "site": "00b670b0",
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
      "definition_site": "00bd65b0",
      "incomplete_value": true,
      "site": "00bd65b0",
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
      "definition_site": "00b670b0",
      "incomplete_value": true,
      "site": "00b670b0",
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
      "definition_site": "00bd65b4",
      "incomplete_value": true,
      "site": "00bd65b4",
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
      "definition_site": "00b670b4",
      "incomplete_value": true,
      "site": "00b670b4",
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
        "010a1858",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "010a1858",
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
        "01126760",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126760",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b670bc ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b670c0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:858:8"]]
+ 00bd65bc ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd65c0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:760:8"]]
- 00b670c4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd65c4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b670cc ["BRANCH", null, ["local:b4:8"]]
+ 00bd65cc ["BRANCH", null, ["local:b8:8"]]
~~~


### [`00b67118`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67118.md) → [`00bd6618`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6618.md) _ZN8firebase4auth8timeunit12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd6654",
      "incomplete_value": true,
      "site": "00bd6654",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67154",
      "incomplete_value": true,
      "site": "00b67154",
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
            "const:858:8"
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
      "definition_site": "00bd6674",
      "incomplete_value": true,
      "site": "00bd6674",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67174",
      "incomplete_value": true,
      "site": "00b67174",
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
            "const:850:8"
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
      "definition_site": "00bd6630",
      "incomplete_value": true,
      "site": "00bd6630",
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
      "definition_site": "00b67130",
      "incomplete_value": true,
      "site": "00b67130",
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
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a1858",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a1858",
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
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126760",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126760",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67128 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
- 00b6712c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00bd6628 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd662c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
- 00b67134 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b67138 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:858:8"]]
+ 00bd6634 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd6638 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:760:8"]]
- 00b67150 ["INT_ADD", "register:40f0:8", ["const:b67150:8", "const:4:8"]]
+ 00bd6650 ["INT_ADD", "register:40f0:8", ["const:bd6650:8", "const:4:8"]]
~~~


### [`00b67188`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67188.md) → [`00bd6688`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6688.md) _ZN8firebase4auth8timeunit14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd66c8",
      "incomplete_value": true,
      "site": "00bd66c8",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b671c8",
      "incomplete_value": true,
      "site": "00b671c8",
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
            "const:850:8"
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
      "definition_site": "00bd66a4",
      "incomplete_value": true,
      "site": "00bd66a4",
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
      "definition_site": "00b671a4",
      "incomplete_value": true,
      "site": "00b671a4",
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
      "definition_site": "00b671b4",
      "incomplete_value": true,
      "site": "00b671c0",
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
      20,
      "READ",
      [
        "storage",
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1850",
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
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b378a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67194 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd6694 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b6719c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00bd669c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
- 00b671a4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b671a8 ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b671ac ["COPY", "tmp:0:8", ["const:ab:8"]]
+ 00bd66a4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd66a8 ["COPY", "register:4018:8", ["const:2b3000:8"]]
+ 00bd66ac ["COPY", "tmp:0:8", ["const:78a:8"]]
~~~


### [`00b671f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b671f8.md) → [`00bd66f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd66f8.md) _ZN8firebase4auth8timeunit11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd6714",
      "incomplete_value": false,
      "site": "00bd6718",
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
      "definition_site": "00b67214",
      "incomplete_value": false,
      "site": "00b67218",
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
      "definition_site": "00bd6724",
      "incomplete_value": true,
      "site": "00bd6730",
      "value": [
        "LOAD",
        "8",
        [
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
        "010a1860",
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
        "01126768",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67210 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00b67214 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00bd6710 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00bd6714 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b67218 ["INT_ADD", "register:40f0:8", ["const:b67218:8", "const:4:8"]]
+ 00bd6718 ["INT_ADD", "register:40f0:8", ["const:bd6718:8", "const:4:8"]]
- 00b6721c ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b67220 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00bd671c ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd6720 ["COPY", "tmp:0:8", ["const:768:8"]]
~~~


### [`00b67234`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67234.md) → [`00bd6734`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6734.md) _ZN8firebase4auth8timeunit13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6774",
      "incomplete_value": true,
      "site": "00bd6774",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67274",
      "incomplete_value": true,
      "site": "00b67274",
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
            "const:850:8"
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
      "definition_site": "00bd6750",
      "incomplete_value": true,
      "site": "00bd6750",
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
      "definition_site": "00b67250",
      "incomplete_value": true,
      "site": "00b67250",
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
      "definition_site": "00bd6758",
      "incomplete_value": false,
      "site": "00bd676c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:78a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67258",
      "incomplete_value": false,
      "site": "00b6726c",
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
            "const:ab:8"
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
        "010a1850",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a30ab",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1850",
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
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b378a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67240 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd6740 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b67248 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00bd6748 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
- 00b67250 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b67254 ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00b67258 ["COPY", "tmp:0:8", ["const:ab:8"]]
+ 00bd6750 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd6754 ["COPY", "register:4018:8", ["const:2b3000:8"]]
+ 00bd6758 ["COPY", "tmp:0:8", ["const:78a:8"]]
~~~


### [`00b672a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b672a4.md) → [`00bd67a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67a4.md) _ZN8firebase4auth8timeunit10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd67b8",
      "incomplete_value": true,
      "site": "00bd67b8",
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
      "definition_site": "00b672b8",
      "incomplete_value": true,
      "site": "00b672b8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd67c0",
      "incomplete_value": true,
      "site": "00bd67c4",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b672c0",
      "incomplete_value": false,
      "site": "00b672c4",
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
    "new": null,
    "old": {
      "definition_site": "00b672d0",
      "incomplete_value": true,
      "site": "00b672dc",
      "value": [
        "LOAD",
        "8",
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
        "010a1868",
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
        "01126770",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b672b8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b672bc ["COPY", "register:4000:8", ["const:299000:8"]]
- 00b672c0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00bd67b8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bd67bc ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bd67c0 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b672c4 ["INT_ADD", "register:40f0:8", ["const:b672c4:8", "const:4:8"]]
+ 00bd67c4 ["INT_ADD", "register:40f0:8", ["const:bd67c4:8", "const:4:8"]]
- 00b672c8 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b672cc ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00bd67c8 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd67cc ["COPY", "tmp:0:8", ["const:770:8"]]
~~~


### [`00b672e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b672e0.md) → [`00bd67e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67e0.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd67e4",
      "incomplete_value": true,
      "site": "00bd67e4",
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
      "definition_site": "00b672e4",
      "incomplete_value": true,
      "site": "00b672e4",
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
      "definition_site": "00bd67e4",
      "incomplete_value": true,
      "site": "00bd67e4",
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
      "definition_site": "00b672e4",
      "incomplete_value": true,
      "site": "00b672e4",
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
      "definition_site": "00bd680c",
      "incomplete_value": true,
      "site": "00bd680c",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6730c",
      "incomplete_value": true,
      "site": "00b6730c",
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
            "const:870:8"
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
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00290722",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a1870",
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
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b672ec ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b672f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00bd67ec ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd67f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00b672f4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd67f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b672fc ["COPY", "register:4018:8", ["const:290000:8"]]
- 00b67300 ["COPY", "tmp:0:8", ["const:722:8"]]
+ 00bd67fc ["COPY", "register:4018:8", ["const:29f000:8"]]
+ 00bd6800 ["COPY", "tmp:0:8", ["const:c64:8"]]
~~~


### [`00b67320`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67320.md) → [`00bd6820`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6820.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00bd6824",
      "incomplete_value": true,
      "site": "00bd6824",
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
      "definition_site": "00b67324",
      "incomplete_value": true,
      "site": "00b67324",
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
      "definition_site": "00bd6824",
      "incomplete_value": true,
      "site": "00bd6824",
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
      "definition_site": "00b67324",
      "incomplete_value": true,
      "site": "00b67324",
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
      "definition_site": "00bd684c",
      "incomplete_value": true,
      "site": "00bd684c",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6734c",
      "incomplete_value": true,
      "site": "00b6734c",
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
            "const:870:8"
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
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00290722",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a1870",
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
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b6732c ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b67330 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00bd682c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6830 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00b67334 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b67338 ["COPY", "register:4018:8", ["const:290000:8"]]
- 00b6733c ["COPY", "tmp:0:8", ["const:722:8"]]
+ 00bd6834 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd6838 ["COPY", "register:4018:8", ["const:29f000:8"]]
+ 00bd683c ["COPY", "tmp:0:8", ["const:c64:8"]]
- 00b67344 ["INT_ADD", "register:40f0:8", ["const:b67344:8", "const:4:8"]]
+ 00bd6844 ["INT_ADD", "register:40f0:8", ["const:bd6844:8", "const:4:8"]]
~~~


### [`00b67360`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67360.md) → [`00bd6860`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6860.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd6890",
      "incomplete_value": true,
      "site": "00bd6890",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67390",
      "incomplete_value": true,
      "site": "00b67390",
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
            "const:870:8"
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
      "definition_site": "00bd6874",
      "incomplete_value": true,
      "site": "00bd6874",
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
      "definition_site": "00b67374",
      "incomplete_value": true,
      "site": "00b67374",
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
      "definition_site": "00bd6880",
      "incomplete_value": false,
      "site": "00bd6888",
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
            "const:c64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67380",
      "incomplete_value": false,
      "site": "00b67388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:722:8"
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
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00290722",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a1870",
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
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b6736c ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b67370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00bd686c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6870 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00b67378 ["COPY", "register:4018:8", ["const:290000:8"]]
+ 00bd6878 ["COPY", "register:4018:8", ["const:29f000:8"]]
- 00b67380 ["COPY", "tmp:0:8", ["const:722:8"]]
+ 00bd6880 ["COPY", "tmp:0:8", ["const:c64:8"]]
~~~


### [`00b673a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673a4.md) → [`00bd68a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68a4.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd68d4",
      "incomplete_value": true,
      "site": "00bd68d4",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b673d4",
      "incomplete_value": true,
      "site": "00b673d4",
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
            "const:870:8"
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
      "definition_site": "00bd68b8",
      "incomplete_value": true,
      "site": "00bd68b8",
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
      "definition_site": "00b673b8",
      "incomplete_value": true,
      "site": "00b673b8",
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
      "definition_site": "00bd68c0",
      "incomplete_value": false,
      "site": "00bd68cc",
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
            "const:c64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b673c0",
      "incomplete_value": false,
      "site": "00b673cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:722:8"
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
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00290722",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a1870",
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
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b673b0 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b673b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00bd68b0 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd68b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00b673bc ["COPY", "register:4018:8", ["const:290000:8"]]
- 00b673c0 ["COPY", "tmp:0:8", ["const:722:8"]]
+ 00bd68bc ["COPY", "register:4018:8", ["const:29f000:8"]]
+ 00bd68c0 ["COPY", "tmp:0:8", ["const:c64:8"]]
- 00b673cc ["INT_ADD", "register:40f0:8", ["const:b673cc:8", "const:4:8"]]
+ 00bd68cc ["INT_ADD", "register:40f0:8", ["const:bd68cc:8", "const:4:8"]]
~~~


### [`00b673f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b673f4.md) → [`00bd68f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd68f4.md) _ZN8firebase4auth26phone_auth_options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd694c",
      "incomplete_value": true,
      "site": "00bd694c",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6744c",
      "incomplete_value": true,
      "site": "00b6744c",
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
            "const:878:8"
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
      "definition_site": "00bd6928",
      "incomplete_value": true,
      "site": "00bd6934",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "definition_site": "00b67428",
      "incomplete_value": true,
      "site": "00b67434",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:870:8"
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
        "010a1878",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "010a1878",
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
        "01126780",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67404 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b67408 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:878:8"]]
+ 00bd6904 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd6908 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:780:8"]]
- 00b6741c ["COPY", "register:4048:8", ["const:10a1000:8"]]
+ 00bd691c ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00b67428 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:870:8"]]
+ 00bd6928 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
~~~


### [`00b67460`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67460.md) → [`00bd6960`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6960.md) _ZN8firebase4auth26phone_auth_options_builder12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd699c",
      "incomplete_value": true,
      "site": "00bd699c",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6749c",
      "incomplete_value": true,
      "site": "00b6749c",
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
            "const:878:8"
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
      "definition_site": "00bd69bc",
      "incomplete_value": true,
      "site": "00bd69bc",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b674bc",
      "incomplete_value": true,
      "site": "00b674bc",
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
            "const:870:8"
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
      "definition_site": "00bd6978",
      "incomplete_value": true,
      "site": "00bd6978",
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
      "definition_site": "00b67478",
      "incomplete_value": true,
      "site": "00b67478",
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
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a1878",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a1878",
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
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126780",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67470 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
- 00b67474 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00bd6970 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd6974 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00b6747c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b67480 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:878:8"]]
+ 00bd697c ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd6980 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:780:8"]]
- 00b67498 ["INT_ADD", "register:40f0:8", ["const:b67498:8", "const:4:8"]]
+ 00bd6998 ["INT_ADD", "register:40f0:8", ["const:bd6998:8", "const:4:8"]]
~~~


### [`00b674d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b674d0.md) → [`00bd69d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd69d0.md) _ZN8firebase4auth26phone_auth_options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6a10",
      "incomplete_value": true,
      "site": "00bd6a10",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67510",
      "incomplete_value": true,
      "site": "00b67510",
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
            "const:870:8"
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
      "definition_site": "00bd69ec",
      "incomplete_value": true,
      "site": "00bd69ec",
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
      "definition_site": "00b674ec",
      "incomplete_value": true,
      "site": "00b674ec",
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
      "definition_site": "00bd69f4",
      "incomplete_value": false,
      "site": "00bd6a08",
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
            "const:c64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b674f4",
      "incomplete_value": false,
      "site": "00b67508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:722:8"
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
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00290722",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1870",
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
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b674dc ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd69dc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b674e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00bd69e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00b674f0 ["COPY", "register:4018:8", ["const:290000:8"]]
- 00b674f4 ["COPY", "tmp:0:8", ["const:722:8"]]
+ 00bd69f0 ["COPY", "register:4018:8", ["const:29f000:8"]]
+ 00bd69f4 ["COPY", "tmp:0:8", ["const:c64:8"]]
~~~


### [`00b67540`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67540.md) → [`00bd6a40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a40.md) _ZN8firebase4auth26phone_auth_options_builder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd6a5c",
      "incomplete_value": false,
      "site": "00bd6a60",
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
      "definition_site": "00b6755c",
      "incomplete_value": false,
      "site": "00b67560",
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
      "definition_site": "00bd6a6c",
      "incomplete_value": true,
      "site": "00bd6a78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6756c",
      "incomplete_value": true,
      "site": "00b67578",
      "value": [
        "LOAD",
        "8",
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
        "010a1880",
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
        "01126788",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67558 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00b6755c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00bd6a58 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00bd6a5c ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b67560 ["INT_ADD", "register:40f0:8", ["const:b67560:8", "const:4:8"]]
+ 00bd6a60 ["INT_ADD", "register:40f0:8", ["const:bd6a60:8", "const:4:8"]]
- 00b67564 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b67568 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00bd6a64 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd6a68 ["COPY", "tmp:0:8", ["const:788:8"]]
~~~


### [`00b6757c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6757c.md) → [`00bd6a7c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6a7c.md) _ZN8firebase4auth26phone_auth_options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6abc",
      "incomplete_value": true,
      "site": "00bd6abc",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b675bc",
      "incomplete_value": true,
      "site": "00b675bc",
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
            "const:870:8"
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
      "definition_site": "00bd6a98",
      "incomplete_value": true,
      "site": "00bd6a98",
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
      "definition_site": "00b67598",
      "incomplete_value": true,
      "site": "00b67598",
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
      "definition_site": "00bd6aa0",
      "incomplete_value": false,
      "site": "00bd6ab4",
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
            "const:c64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b675a0",
      "incomplete_value": false,
      "site": "00b675b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:722:8"
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
        "010a1870",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00290722",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a1870",
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
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029fc64",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67588 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd6a88 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b67590 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00bd6a90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
- 00b6759c ["COPY", "register:4018:8", ["const:290000:8"]]
- 00b675a0 ["COPY", "tmp:0:8", ["const:722:8"]]
+ 00bd6a9c ["COPY", "register:4018:8", ["const:29f000:8"]]
+ 00bd6aa0 ["COPY", "tmp:0:8", ["const:c64:8"]]
~~~


### [`00b675ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b675ec.md) → [`00bd6aec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6aec.md) _ZN8firebase4auth26phone_auth_options_builder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd6b08",
      "incomplete_value": false,
      "site": "00bd6b0c",
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
      "definition_site": "00b67608",
      "incomplete_value": false,
      "site": "00b6760c",
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
      "definition_site": "00bd6b18",
      "incomplete_value": true,
      "site": "00bd6b24",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67618",
      "incomplete_value": true,
      "site": "00b67624",
      "value": [
        "LOAD",
        "8",
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
        "010a18c0",
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
        "011267c8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67604 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00b67608 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00bd6b04 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bd6b08 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b6760c ["INT_ADD", "register:40f0:8", ["const:b6760c:8", "const:4:8"]]
+ 00bd6b0c ["INT_ADD", "register:40f0:8", ["const:bd6b0c:8", "const:4:8"]]
- 00b67610 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b67614 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00bd6b10 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd6b14 ["COPY", "tmp:0:8", ["const:7c8:8"]]
~~~


### [`00b67628`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67628.md) → [`00bd6b28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b28.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00bd6b54",
      "incomplete_value": true,
      "site": "00bd6b54",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67654",
      "incomplete_value": true,
      "site": "00b67654",
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
            "const:8c8:8"
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
      "definition_site": "00bd6b3c",
      "incomplete_value": true,
      "site": "00bd6b3c",
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
      "definition_site": "00b6763c",
      "incomplete_value": true,
      "site": "00b6763c",
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
      "definition_site": "00bd6b48",
      "incomplete_value": false,
      "site": "00bd6b4c",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67648",
      "incomplete_value": false,
      "site": "00b6764c",
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
            "const:56c:8"
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
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a18c8",
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
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67634 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b67638 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00bd6b34 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6b38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00b67644 ["COPY", "register:4018:8", ["const:292000:8"]]
- 00b67648 ["COPY", "tmp:0:8", ["const:56c:8"]]
+ 00bd6b44 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00bd6b48 ["COPY", "tmp:0:8", ["const:c7c:8"]]
- 00b6764c ["INT_ADD", "register:40f0:8", ["const:b6764c:8", "const:4:8"]]
+ 00bd6b4c ["INT_ADD", "register:40f0:8", ["const:bd6b4c:8", "const:4:8"]]
~~~


### [`00b67668`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67668.md) → [`00bd6b68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6b68.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00bd6b94",
      "incomplete_value": true,
      "site": "00bd6b94",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67694",
      "incomplete_value": true,
      "site": "00b67694",
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
            "const:8c8:8"
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
      "definition_site": "00bd6b7c",
      "incomplete_value": true,
      "site": "00bd6b7c",
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
      "definition_site": "00b6767c",
      "incomplete_value": true,
      "site": "00b6767c",
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
      "definition_site": "00bd6b84",
      "incomplete_value": false,
      "site": "00bd6b8c",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67684",
      "incomplete_value": false,
      "site": "00b6768c",
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
            "const:56c:8"
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
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a18c8",
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
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67674 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b67678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00bd6b74 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6b78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00b67680 ["COPY", "register:4018:8", ["const:292000:8"]]
- 00b67684 ["COPY", "tmp:0:8", ["const:56c:8"]]
+ 00bd6b80 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00bd6b84 ["COPY", "tmp:0:8", ["const:c7c:8"]]
- 00b6768c ["INT_ADD", "register:40f0:8", ["const:b6768c:8", "const:4:8"]]
+ 00bd6b8c ["INT_ADD", "register:40f0:8", ["const:bd6b8c:8", "const:4:8"]]
~~~


### [`00b676a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676a8.md) → [`00bd6ba8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ba8.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd6bd8",
      "incomplete_value": true,
      "site": "00bd6bd8",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b676d8",
      "incomplete_value": true,
      "site": "00b676d8",
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
            "const:8c8:8"
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
      "definition_site": "00bd6bbc",
      "incomplete_value": true,
      "site": "00bd6bbc",
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
      "definition_site": "00b676bc",
      "incomplete_value": true,
      "site": "00b676bc",
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
      "definition_site": "00bd6bc8",
      "incomplete_value": false,
      "site": "00bd6bd0",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b676c8",
      "incomplete_value": false,
      "site": "00b676d0",
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
            "const:56c:8"
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
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a18c8",
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
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b676b4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b676b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00bd6bb4 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6bb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00b676c0 ["COPY", "register:4018:8", ["const:292000:8"]]
+ 00bd6bc0 ["COPY", "register:4018:8", ["const:2a1000:8"]]
- 00b676c8 ["COPY", "tmp:0:8", ["const:56c:8"]]
+ 00bd6bc8 ["COPY", "tmp:0:8", ["const:c7c:8"]]
~~~


### [`00b676ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b676ec.md) → [`00bd6bec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6bec.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6c1c",
      "incomplete_value": true,
      "site": "00bd6c1c",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6771c",
      "incomplete_value": true,
      "site": "00b6771c",
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
            "const:8c8:8"
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
      "definition_site": "00bd6c00",
      "incomplete_value": true,
      "site": "00bd6c00",
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
      "definition_site": "00b67700",
      "incomplete_value": true,
      "site": "00b67700",
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
      "definition_site": "00bd6c08",
      "incomplete_value": false,
      "site": "00bd6c14",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67708",
      "incomplete_value": false,
      "site": "00b67714",
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
            "const:56c:8"
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
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a18c8",
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
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b676f8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b676fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00bd6bf8 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6bfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00b67704 ["COPY", "register:4018:8", ["const:292000:8"]]
- 00b67708 ["COPY", "tmp:0:8", ["const:56c:8"]]
+ 00bd6c04 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00bd6c08 ["COPY", "tmp:0:8", ["const:c7c:8"]]
- 00b67714 ["INT_ADD", "register:40f0:8", ["const:b67714:8", "const:4:8"]]
+ 00bd6c14 ["INT_ADD", "register:40f0:8", ["const:bd6c14:8", "const:4:8"]]
~~~


### [`00b6773c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b6773c.md) → [`00bd6c3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6c3c.md) _ZN8firebase4auth17phoneauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd6c94",
      "incomplete_value": true,
      "site": "00bd6c94",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67794",
      "incomplete_value": true,
      "site": "00b67794",
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
            "const:8d0:8"
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
      "definition_site": "00bd6c70",
      "incomplete_value": true,
      "site": "00bd6c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67770",
      "incomplete_value": true,
      "site": "00b6777c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:8c8:8"
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
        "010a18d0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "010a18d0",
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
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b6774c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b67750 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8d0:8"]]
+ 00bd6c4c ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd6c50 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7d8:8"]]
- 00b67764 ["COPY", "register:4048:8", ["const:10a1000:8"]]
+ 00bd6c64 ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00b67770 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8c8:8"]]
+ 00bd6c70 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7d0:8"]]
~~~


### [`00b677a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b677a8.md) → [`00bd6ca8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ca8.md) _ZN8firebase4auth17phoneauthprovider12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd6ce4",
      "incomplete_value": true,
      "site": "00bd6ce4",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b677e4",
      "incomplete_value": true,
      "site": "00b677e4",
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
            "const:8d0:8"
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
      "definition_site": "00bd6d04",
      "incomplete_value": true,
      "site": "00bd6d04",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67804",
      "incomplete_value": true,
      "site": "00b67804",
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
            "const:8c8:8"
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
      "definition_site": "00bd6cc0",
      "incomplete_value": true,
      "site": "00bd6cc0",
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
      "definition_site": "00b677c0",
      "incomplete_value": true,
      "site": "00b677c0",
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
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a18d0",
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
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b677b8 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
- 00b677bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00bd6cb8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd6cbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00b677c4 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b677c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8d0:8"]]
+ 00bd6cc4 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd6cc8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7d8:8"]]
- 00b677e0 ["INT_ADD", "register:40f0:8", ["const:b677e0:8", "const:4:8"]]
+ 00bd6ce0 ["INT_ADD", "register:40f0:8", ["const:bd6ce0:8", "const:4:8"]]
~~~


### [`00b67818`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67818.md) → [`00bd6d18`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d18.md) _ZN8firebase4auth17phoneauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd6d58",
      "incomplete_value": true,
      "site": "00bd6d58",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67858",
      "incomplete_value": true,
      "site": "00b67858",
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
            "const:8c8:8"
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
      "definition_site": "00bd6d34",
      "incomplete_value": true,
      "site": "00bd6d34",
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
      "definition_site": "00b67834",
      "incomplete_value": true,
      "site": "00b67834",
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
      "definition_site": "00b67840",
      "incomplete_value": true,
      "site": "00b67850",
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
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a18c8",
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
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b67824 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd6d24 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b6782c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00bd6d2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00b67834 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b67838 ["COPY", "register:4018:8", ["const:292000:8"]]
- 00b6783c ["COPY", "tmp:0:8", ["const:56c:8"]]
+ 00bd6d34 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd6d38 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00bd6d3c ["COPY", "tmp:0:8", ["const:c7c:8"]]
~~~


### [`00b67888`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67888.md) → [`00bd6d88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6d88.md) _ZN8firebase4auth17phoneauthprovider11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd6da4",
      "incomplete_value": false,
      "site": "00bd6da8",
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
      "definition_site": "00b678a4",
      "incomplete_value": false,
      "site": "00b678a8",
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
      "definition_site": "00bd6db4",
      "incomplete_value": true,
      "site": "00bd6dc0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b678b4",
      "incomplete_value": true,
      "site": "00b678c0",
      "value": [
        "LOAD",
        "8",
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
        "010a18d8",
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
        "011267e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b678a0 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00b678a4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00bd6da0 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00bd6da4 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b678a8 ["INT_ADD", "register:40f0:8", ["const:b678a8:8", "const:4:8"]]
+ 00bd6da8 ["INT_ADD", "register:40f0:8", ["const:bd6da8:8", "const:4:8"]]
- 00b678ac ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b678b0 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00bd6dac ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd6db0 ["COPY", "tmp:0:8", ["const:7e0:8"]]
~~~


### [`00b678c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b678c4.md) → [`00bd6dc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6dc4.md) _ZN8firebase4auth17phoneauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6e04",
      "incomplete_value": true,
      "site": "00bd6e04",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67904",
      "incomplete_value": true,
      "site": "00b67904",
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
            "const:8c8:8"
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
      "definition_site": "00bd6de0",
      "incomplete_value": true,
      "site": "00bd6de0",
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
      "definition_site": "00b678e0",
      "incomplete_value": true,
      "site": "00b678e0",
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
      "definition_site": "00bd6de8",
      "incomplete_value": false,
      "site": "00bd6dfc",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b678e8",
      "incomplete_value": false,
      "site": "00b678fc",
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
            "const:56c:8"
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
        "010a18c8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a18c8",
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
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a1c7c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b678d0 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd6dd0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b678d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00bd6dd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00b678e4 ["COPY", "register:4018:8", ["const:292000:8"]]
- 00b678e8 ["COPY", "tmp:0:8", ["const:56c:8"]]
+ 00bd6de4 ["COPY", "register:4018:8", ["const:2a1000:8"]]
+ 00bd6de8 ["COPY", "tmp:0:8", ["const:c7c:8"]]
~~~


### [`00b67934`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67934.md) → [`00bd6e34`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e34.md) _ZN8firebase4auth17phoneauthprovider10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd6e50",
      "incomplete_value": false,
      "site": "00bd6e54",
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
      "definition_site": "00b67950",
      "incomplete_value": false,
      "site": "00b67954",
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
      "definition_site": "00bd6e60",
      "incomplete_value": true,
      "site": "00bd6e6c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b67960",
      "incomplete_value": true,
      "site": "00b6796c",
      "value": [
        "LOAD",
        "8",
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
        "010a18f0",
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
        "011267f8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00b6794c ["COPY", "register:4000:8", ["const:299000:8"]]
- 00b67950 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00bd6e4c ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bd6e50 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b67954 ["INT_ADD", "register:40f0:8", ["const:b67954:8", "const:4:8"]]
+ 00bd6e54 ["INT_ADD", "register:40f0:8", ["const:bd6e54:8", "const:4:8"]]
- 00b67958 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b6795c ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00bd6e58 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bd6e5c ["COPY", "tmp:0:8", ["const:7f8:8"]]
~~~


### [`00b67970`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b67970.md) → [`00bd6e70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6e70.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00bd6e9c",
      "incomplete_value": true,
      "site": "00bd6e9c",
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
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6799c",
      "incomplete_value": true,
      "site": "00b6799c",
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
            "const:8f8:8"
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
      "definition_site": "00bd6e84",
      "incomplete_value": true,
      "site": "00bd6e84",
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
      "definition_site": "00b67984",
      "incomplete_value": true,
      "site": "00b67984",
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
      "definition_site": "00bd6e90",
      "incomplete_value": false,
      "site": "00bd6e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:cda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67990",
      "incomplete_value": false,
      "site": "00b67994",
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
            "const:6b6:8"
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
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a18f8",
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
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b6797c ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b67980 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00bd6e7c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00b6798c ["COPY", "register:4018:8", ["const:2af000:8"]]
- 00b67990 ["COPY", "tmp:0:8", ["const:6b6:8"]]
+ 00bd6e8c ["COPY", "register:4018:8", ["const:2c0000:8"]]
+ 00bd6e90 ["COPY", "tmp:0:8", ["const:cda:8"]]
- 00b67994 ["INT_ADD", "register:40f0:8", ["const:b67994:8", "const:4:8"]]
+ 00bd6e94 ["INT_ADD", "register:40f0:8", ["const:bd6e94:8", "const:4:8"]]
~~~


### [`00b679b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679b0.md) → [`00bd6eb0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6eb0.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00bd6edc",
      "incomplete_value": true,
      "site": "00bd6edc",
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
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b679dc",
      "incomplete_value": true,
      "site": "00b679dc",
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
            "const:8f8:8"
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
      "definition_site": "00bd6ec4",
      "incomplete_value": true,
      "site": "00bd6ec4",
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
      "definition_site": "00b679c4",
      "incomplete_value": true,
      "site": "00b679c4",
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
      "definition_site": "00bd6ecc",
      "incomplete_value": false,
      "site": "00bd6ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:cda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b679cc",
      "incomplete_value": false,
      "site": "00b679d4",
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
            "const:6b6:8"
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
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a18f8",
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
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b679bc ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b679c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00bd6ebc ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00b679c8 ["COPY", "register:4018:8", ["const:2af000:8"]]
- 00b679cc ["COPY", "tmp:0:8", ["const:6b6:8"]]
+ 00bd6ec8 ["COPY", "register:4018:8", ["const:2c0000:8"]]
+ 00bd6ecc ["COPY", "tmp:0:8", ["const:cda:8"]]
- 00b679d4 ["INT_ADD", "register:40f0:8", ["const:b679d4:8", "const:4:8"]]
+ 00bd6ed4 ["INT_ADD", "register:40f0:8", ["const:bd6ed4:8", "const:4:8"]]
~~~


### [`00b679f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b67/00b679f0.md) → [`00bd6ef0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6ef0.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd6f20",
      "incomplete_value": true,
      "site": "00bd6f20",
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
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a20",
      "incomplete_value": true,
      "site": "00b67a20",
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
            "const:8f8:8"
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
      "definition_site": "00bd6f04",
      "incomplete_value": true,
      "site": "00bd6f04",
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
      "definition_site": "00b67a04",
      "incomplete_value": true,
      "site": "00b67a04",
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
      "definition_site": "00bd6f10",
      "incomplete_value": false,
      "site": "00bd6f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:cda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a10",
      "incomplete_value": false,
      "site": "00b67a18",
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
            "const:6b6:8"
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
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002af6b6",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a18f8",
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
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c0cda",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00b679fc ["COPY", "register:4098:8", ["const:10a1000:8"]]
- 00b67a00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00bd6efc ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bd6f00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:800:8"]]
- 00b67a08 ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00bd6f08 ["COPY", "register:4018:8", ["const:2c0000:8"]]
- 00b67a10 ["COPY", "tmp:0:8", ["const:6b6:8"]]
+ 00bd6f10 ["COPY", "tmp:0:8", ["const:cda:8"]]
~~~


