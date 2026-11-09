# v15.7.4 → v16.0.0 · 最優先の変更候補 (13)

[一覧の目次](README.md)

### [`0050d78c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d78c.md) → [`00530624`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530624.md) FUN_00530624

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530648",
      "incomplete_value": true,
      "site": "0053064c",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d7b0",
      "incomplete_value": true,
      "site": "0050d7b4",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0053066c",
      "incomplete_value": true,
      "site": "0053066c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d7d4",
      "incomplete_value": true,
      "site": "0050d7d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530698",
      "incomplete_value": true,
      "site": "00530698",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d800",
      "incomplete_value": true,
      "site": "0050d800",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      28,
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050d79c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00530634 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050d7a4 ["COPY", "register:40a8:8", ["const:bea000:8"]]
- 0050d7a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 0053063c ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00530640 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
- 0050d7c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0053065c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
~~~


### [`0050d830`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d830.md) → [`005306c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005306c8.md) FUN_005306c8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005306ec",
      "incomplete_value": true,
      "site": "005306f0",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d854",
      "incomplete_value": true,
      "site": "0050d858",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530710",
      "incomplete_value": true,
      "site": "00530710",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d878",
      "incomplete_value": true,
      "site": "0050d878",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0053073c",
      "incomplete_value": true,
      "site": "0053073c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d8a4",
      "incomplete_value": true,
      "site": "0050d8a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      28,
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050d840 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005306d8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050d848 ["COPY", "register:40a8:8", ["const:bea000:8"]]
- 0050d84c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 005306e0 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 005306e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
- 0050d868 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00530700 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
~~~


### [`0050d8f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md) → [`0053078c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) FUN_0053078c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`004a4d4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d4c.md) [`004a4d88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d88.md) [`0050d9e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d9e0.md) [`0050da6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da6c.md) [`0050da74`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da74.md) · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 6件 [`004c7be4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7be4.md) [`004c7c20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7c20.md) [`00530878`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530878.md) [`00530904`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530904.md) [`0053090c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053090c.md) · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005307c4",
      "incomplete_value": true,
      "site": "005307c8",
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
      "definition_site": "0050d92c",
      "incomplete_value": true,
      "site": "0050d930",
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
    "kind": "call_target",
    "new": {
      "definition_site": "005307f8",
      "incomplete_value": true,
      "site": "005307f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d960",
      "incomplete_value": true,
      "site": "0050d960",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0053084c",
      "incomplete_value": true,
      "site": "0053084c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d9b4",
      "incomplete_value": true,
      "site": "0050d9b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      44,
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00bea778",
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
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050d910 ["COPY", "register:40b0:8", ["const:bea000:8"]]
+ 005307a8 ["COPY", "register:40b0:8", ["const:c67000:8"]]
- 0050d91c ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050d920 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 005307b4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005307b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 0050d93c ["INT_ADD", "register:40f0:8", ["const:50d93c:8", "const:4:8"]]
+ 005307d4 ["INT_ADD", "register:40f0:8", ["const:5307d4:8", "const:4:8"]]
~~~


### [`0050da9c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da9c.md) → [`00530934`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md) FUN_00530934

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050db70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050db70.md) · 呼出先 2件 [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00530a08`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a08.md) · 呼出先 2件 [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005309b0",
      "incomplete_value": true,
      "site": "005309b4",
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
      "definition_site": "0050db18",
      "incomplete_value": true,
      "site": "0050db1c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0053096c",
      "incomplete_value": true,
      "site": "0053096c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dad4",
      "incomplete_value": true,
      "site": "0050dad4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530998",
      "incomplete_value": true,
      "site": "00530998",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050db00",
      "incomplete_value": true,
      "site": "0050db00",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "00c1b148",
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
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050dab4 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 0053094c ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050dac4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0053095c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 0050dad4 ["INT_ADD", "register:40f0:8", ["const:50dad4:8", "const:4:8"]]
+ 0053096c ["INT_ADD", "register:40f0:8", ["const:53096c:8", "const:4:8"]]
~~~


### [`0050dbfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dbfc.md) → [`00530a94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a94.md) FUN_00530a94

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530ae4",
      "incomplete_value": true,
      "site": "00530ae8",
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
      "definition_site": "0050dc4c",
      "incomplete_value": true,
      "site": "0050dc50",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530acc",
      "incomplete_value": true,
      "site": "00530acc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dc34",
      "incomplete_value": true,
      "site": "0050dc34",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530b08",
      "incomplete_value": true,
      "site": "00530b08",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dc70",
      "incomplete_value": true,
      "site": "0050dc70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050dc14 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00530aac ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050dc24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00530abc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 0050dc34 ["INT_ADD", "register:40f0:8", ["const:50dc34:8", "const:4:8"]]
+ 00530acc ["INT_ADD", "register:40f0:8", ["const:530acc:8", "const:4:8"]]
~~~


### [`0050dca0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dca0.md) → [`00530b38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530b38.md) FUN_00530b38

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530b88",
      "incomplete_value": true,
      "site": "00530b8c",
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
      "definition_site": "0050dcf0",
      "incomplete_value": true,
      "site": "0050dcf4",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530b70",
      "incomplete_value": true,
      "site": "00530b70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dcd8",
      "incomplete_value": true,
      "site": "0050dcd8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530bac",
      "incomplete_value": true,
      "site": "00530bac",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dd14",
      "incomplete_value": true,
      "site": "0050dd14",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050dcb8 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00530b50 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050dcc8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00530b60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 0050dcd8 ["INT_ADD", "register:40f0:8", ["const:50dcd8:8", "const:4:8"]]
+ 00530b70 ["INT_ADD", "register:40f0:8", ["const:530b70:8", "const:4:8"]]
~~~


### [`0050dd3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dd3c.md) → [`00530bd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530bd4.md) FUN_00530bd4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`004a8a10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8a10.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cb8a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb8a8.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "site": "00530bec",
      "value": [
        "leaf",
        "ram:4cb8a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0050dd54",
      "value": [
        "leaf",
        "ram:4a8a10:8"
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
        "004a8a10"
      ]
    ]
  ],
  "added": [
    [
      24,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004cb8a8"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050dd4c ["INT_ADD", "register:40f0:8", ["const:50dd4c:8", "const:4:8"]]
+ 00530be4 ["INT_ADD", "register:40f0:8", ["const:530be4:8", "const:4:8"]]
- 0050dd54 ["INT_ADD", "register:40f0:8", ["const:50dd54:8", "const:4:8"]]
- 0050dd54 ["CALL", null, ["ram:4a8a10:8"]]
+ 00530bec ["INT_ADD", "register:40f0:8", ["const:530bec:8", "const:4:8"]]
+ 00530bec ["CALL", null, ["ram:4cb8a8:8"]]
~~~


### [`0050dda4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dda4.md) → [`00530c3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530c3c.md) FUN_00530c3c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530c8c",
      "incomplete_value": true,
      "site": "00530c90",
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
      "definition_site": "0050ddf4",
      "incomplete_value": true,
      "site": "0050ddf8",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530c74",
      "incomplete_value": true,
      "site": "00530c74",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dddc",
      "incomplete_value": true,
      "site": "0050dddc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530cb0",
      "incomplete_value": true,
      "site": "00530cb0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050de18",
      "incomplete_value": true,
      "site": "0050de18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050ddbc ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00530c54 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050ddcc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00530c64 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 0050dddc ["INT_ADD", "register:40f0:8", ["const:50dddc:8", "const:4:8"]]
+ 00530c74 ["INT_ADD", "register:40f0:8", ["const:530c74:8", "const:4:8"]]
~~~


### [`0050de48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050de48.md) → [`00530ce0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530ce0.md) FUN_00530ce0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530d30",
      "incomplete_value": true,
      "site": "00530d34",
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
      "definition_site": "0050de98",
      "incomplete_value": true,
      "site": "0050de9c",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530d18",
      "incomplete_value": true,
      "site": "00530d18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050de80",
      "incomplete_value": true,
      "site": "0050de80",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530d54",
      "incomplete_value": true,
      "site": "00530d54",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050debc",
      "incomplete_value": true,
      "site": "0050debc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050de60 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00530cf8 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050de70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00530d08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 0050de80 ["INT_ADD", "register:40f0:8", ["const:50de80:8", "const:4:8"]]
+ 00530d18 ["INT_ADD", "register:40f0:8", ["const:530d18:8", "const:4:8"]]
~~~


### [`0050dfd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dfd4.md) → [`00530e6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e6c.md) FUN_00530e6c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530ea4",
      "incomplete_value": true,
      "site": "00530ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:277:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e00c",
      "incomplete_value": true,
      "site": "0050e00c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:786:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "002a6786",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002b7277",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050dfec ["COPY", "register:4048:8", ["const:2a6000:8"]]
- 0050dff0 ["COPY", "tmp:0:8", ["const:786:8"]]
+ 00530e84 ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 00530e88 ["COPY", "tmp:0:8", ["const:277:8"]]
- 0050e018 ["INT_ADD", "register:40f0:8", ["const:50e018:8", "const:4:8"]]
+ 00530eb0 ["INT_ADD", "register:40f0:8", ["const:530eb0:8", "const:4:8"]]
- 0050e028 ["INT_ADD", "register:40f0:8", ["const:50e028:8", "const:4:8"]]
+ 00530ec0 ["INT_ADD", "register:40f0:8", ["const:530ec0:8", "const:4:8"]]
~~~


### [`0050e0cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e0cc.md) → [`00530f64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530f64.md) FUN_00530f64

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530f90",
      "incomplete_value": true,
      "site": "00530f94",
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
      "definition_site": "0050e0f8",
      "incomplete_value": true,
      "site": "0050e0fc",
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
      "READ",
      [
        "storage",
        "00c1b398",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00bea990",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c67550",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050e0e0 ["INT_ADD", "register:40f0:8", ["const:50e0e0:8", "const:4:8"]]
+ 00530f78 ["INT_ADD", "register:40f0:8", ["const:530f78:8", "const:4:8"]]
- 0050e0e4 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00530f7c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0050e0ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:398:8"]]
+ 00530f84 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d88:8"]]
~~~


### [`0050e114`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e114.md) → [`00530fac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fac.md) FUN_00530fac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530fe4",
      "incomplete_value": true,
      "site": "00530fe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:79d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e14c",
      "incomplete_value": true,
      "site": "0050e14c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:418:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "0029e418",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002ae79d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050e12c ["COPY", "register:4048:8", ["const:29e000:8"]]
- 0050e130 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 00530fc4 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 00530fc8 ["COPY", "tmp:0:8", ["const:79d:8"]]
- 0050e158 ["INT_ADD", "register:40f0:8", ["const:50e158:8", "const:4:8"]]
+ 00530ff0 ["INT_ADD", "register:40f0:8", ["const:530ff0:8", "const:4:8"]]
- 0050e168 ["INT_ADD", "register:40f0:8", ["const:50e168:8", "const:4:8"]]
+ 00531000 ["INT_ADD", "register:40f0:8", ["const:531000:8", "const:4:8"]]
~~~


### [`0050e1bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e1bc.md) → [`00531054`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531054.md) FUN_00531054

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531070",
      "incomplete_value": true,
      "site": "00531070",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e1d8",
      "incomplete_value": true,
      "site": "0050e1d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb4:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00531068",
      "incomplete_value": true,
      "site": "00531074",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050e1d0",
      "incomplete_value": true,
      "site": "0050e1dc",
      "value": [
        "LOAD",
        "8",
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
      12,
      "READ",
      [
        "storage",
        "00299bb4",
        null,
        "string"
      ]
    ],
    [
      20,
      "READ",
      [
        "storage",
        "00299bbb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      12,
      "READ",
      [
        "storage",
        "002a9a8d",
        null,
        "string"
      ]
    ],
    [
      20,
      "READ",
      [
        "storage",
        "002a9a94",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050e1c0 ["COPY", "register:4050:8", ["const:299000:8"]]
- 0050e1c4 ["COPY", "tmp:0:8", ["const:bb4:8"]]
+ 00531058 ["COPY", "register:4050:8", ["const:2a9000:8"]]
+ 0053105c ["COPY", "tmp:0:8", ["const:a8d:8"]]
~~~


### [`0050e234`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e234.md) → [`005310cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310cc.md) FUN_005310cc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531104",
      "incomplete_value": true,
      "site": "00531104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ccb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e26c",
      "incomplete_value": true,
      "site": "0050e26c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:45e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "002a445e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002b4ccb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050e24c ["COPY", "register:4048:8", ["const:2a4000:8"]]
- 0050e250 ["COPY", "tmp:0:8", ["const:45e:8"]]
+ 005310e4 ["COPY", "register:4048:8", ["const:2b4000:8"]]
+ 005310e8 ["COPY", "tmp:0:8", ["const:ccb:8"]]
- 0050e278 ["INT_ADD", "register:40f0:8", ["const:50e278:8", "const:4:8"]]
+ 00531110 ["INT_ADD", "register:40f0:8", ["const:531110:8", "const:4:8"]]
- 0050e288 ["INT_ADD", "register:40f0:8", ["const:50e288:8", "const:4:8"]]
+ 00531120 ["INT_ADD", "register:40f0:8", ["const:531120:8", "const:4:8"]]
~~~


### [`0050e32c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e32c.md) → [`005311c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005311c4.md) FUN_005311c4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047c554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f3ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005311f8",
      "incomplete_value": true,
      "site": "00531204",
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
      "definition_site": "0050e360",
      "incomplete_value": true,
      "site": "0050e36c",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "00c1b3c0",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00beaa68",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00c67628",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050e344 ["INT_ADD", "register:40f0:8", ["const:50e344:8", "const:4:8"]]
+ 005311dc ["INT_ADD", "register:40f0:8", ["const:5311dc:8", "const:4:8"]]
- 0050e348 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005311e0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050e350 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3c0:8"]]
+ 005311e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
~~~


### [`0050e43c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e43c.md) → [`005312d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312d4.md) FUN_005312d4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053130c",
      "incomplete_value": true,
      "site": "0053130c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:36:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e474",
      "incomplete_value": true,
      "site": "0050e474",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:720:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "00294720",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002a4036",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050e454 ["COPY", "register:4048:8", ["const:294000:8"]]
- 0050e458 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 005312ec ["COPY", "register:4048:8", ["const:2a4000:8"]]
+ 005312f0 ["COPY", "tmp:0:8", ["const:36:8"]]
- 0050e480 ["INT_ADD", "register:40f0:8", ["const:50e480:8", "const:4:8"]]
+ 00531318 ["INT_ADD", "register:40f0:8", ["const:531318:8", "const:4:8"]]
- 0050e490 ["INT_ADD", "register:40f0:8", ["const:50e490:8", "const:4:8"]]
+ 00531328 ["INT_ADD", "register:40f0:8", ["const:531328:8", "const:4:8"]]
~~~


### [`0050e534`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e534.md) → [`005313cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005313cc.md) FUN_005313cc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047c554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f3ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531400",
      "incomplete_value": true,
      "site": "0053140c",
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
      "definition_site": "0050e568",
      "incomplete_value": true,
      "site": "0050e574",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "00c1b3a0",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00beba00",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "00c9ad90",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00c685c0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050e54c ["INT_ADD", "register:40f0:8", ["const:50e54c:8", "const:4:8"]]
+ 005313e4 ["INT_ADD", "register:40f0:8", ["const:5313e4:8", "const:4:8"]]
- 0050e550 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005313e8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050e558 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
+ 005313f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d90:8"]]
~~~


### [`0050e67c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e67c.md) → [`00531514`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531514.md) FUN_00531514

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053154c",
      "incomplete_value": true,
      "site": "0053154c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e6b4",
      "incomplete_value": true,
      "site": "0050e6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:564:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "002aa564",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002bb2e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050e694 ["COPY", "register:4048:8", ["const:2aa000:8"]]
- 0050e698 ["COPY", "tmp:0:8", ["const:564:8"]]
+ 0053152c ["COPY", "register:4048:8", ["const:2bb000:8"]]
+ 00531530 ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 0050e6c0 ["INT_ADD", "register:40f0:8", ["const:50e6c0:8", "const:4:8"]]
+ 00531558 ["INT_ADD", "register:40f0:8", ["const:531558:8", "const:4:8"]]
- 0050e6d0 ["INT_ADD", "register:40f0:8", ["const:50e6d0:8", "const:4:8"]]
+ 00531568 ["INT_ADD", "register:40f0:8", ["const:531568:8", "const:4:8"]]
~~~


### [`0050e774`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e774.md) → [`0053160c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053160c.md) FUN_0053160c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c900`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531634",
      "incomplete_value": true,
      "site": "00531634",
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
      "definition_site": "0050e79c",
      "incomplete_value": true,
      "site": "0050e79c",
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
      "READ",
      [
        "storage",
        "00c1b3a8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00beba90",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "00c9ad98",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c68650",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050e788 ["INT_ADD", "register:40f0:8", ["const:50e788:8", "const:4:8"]]
+ 00531620 ["INT_ADD", "register:40f0:8", ["const:531620:8", "const:4:8"]]
- 0050e78c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00531624 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050e794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a8:8"]]
+ 0053162c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
~~~


### [`0050e944`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e944.md) → [`005317dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005317dc.md) FUN_005317dc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c900`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531804",
      "incomplete_value": true,
      "site": "00531804",
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
      "definition_site": "0050e96c",
      "incomplete_value": true,
      "site": "0050e96c",
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
      "READ",
      [
        "storage",
        "00c1b3c8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00bebb08",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c686c8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050e958 ["INT_ADD", "register:40f0:8", ["const:50e958:8", "const:4:8"]]
+ 005317f0 ["INT_ADD", "register:40f0:8", ["const:5317f0:8", "const:4:8"]]
- 0050e95c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005317f4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050e964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3c8:8"]]
+ 005317fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
~~~


### [`0050ea1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ea1c.md) → [`005318b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005318b4.md) FUN_005318b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005318ec",
      "incomplete_value": true,
      "site": "005318ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ea54",
      "incomplete_value": true,
      "site": "0050ea54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:369:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "0029b369",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002ab3d7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050ea34 ["COPY", "register:4048:8", ["const:29b000:8"]]
- 0050ea38 ["COPY", "tmp:0:8", ["const:369:8"]]
+ 005318cc ["COPY", "register:4048:8", ["const:2ab000:8"]]
+ 005318d0 ["COPY", "tmp:0:8", ["const:3d7:8"]]
- 0050ea60 ["INT_ADD", "register:40f0:8", ["const:50ea60:8", "const:4:8"]]
+ 005318f8 ["INT_ADD", "register:40f0:8", ["const:5318f8:8", "const:4:8"]]
- 0050ea70 ["INT_ADD", "register:40f0:8", ["const:50ea70:8", "const:4:8"]]
+ 00531908 ["INT_ADD", "register:40f0:8", ["const:531908:8", "const:4:8"]]
~~~


### [`0050eb14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050eb14.md) → [`005319ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md) FUN_005319ac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0051bf98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md) [`0051c12c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`0051d7fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) [`00bd70ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053ee30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00540694`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005319f8",
      "incomplete_value": true,
      "site": "00531a04",
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
      "definition_site": "0050eb60",
      "incomplete_value": true,
      "site": "0050eb6c",
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
      64,
      "READ",
      [
        "storage",
        "00c1b390",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "00bea930",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      64,
      "READ",
      [
        "storage",
        "00c9ad80",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "00c674f0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050eb44 ["INT_ADD", "register:40f0:8", ["const:50eb44:8", "const:4:8"]]
+ 005319dc ["INT_ADD", "register:40f0:8", ["const:5319dc:8", "const:4:8"]]
- 0050eb48 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005319e0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050eb54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
+ 005319ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
~~~


### [`0050ed2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ed2c.md) → [`00531bc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531bc4.md) FUN_00531bc4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531bfc",
      "incomplete_value": true,
      "site": "00531bfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ed64",
      "incomplete_value": true,
      "site": "0050ed64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "0028fa60",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "0029eea0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050ed44 ["COPY", "register:4048:8", ["const:28f000:8"]]
- 0050ed48 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00531bdc ["COPY", "register:4048:8", ["const:29e000:8"]]
+ 00531be0 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 0050ed70 ["INT_ADD", "register:40f0:8", ["const:50ed70:8", "const:4:8"]]
+ 00531c08 ["INT_ADD", "register:40f0:8", ["const:531c08:8", "const:4:8"]]
- 0050ed80 ["INT_ADD", "register:40f0:8", ["const:50ed80:8", "const:4:8"]]
+ 00531c18 ["INT_ADD", "register:40f0:8", ["const:531c18:8", "const:4:8"]]
~~~


### [`0050edd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edd4.md) → [`00531c6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c6c.md) FUN_00531c6c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531c78",
      "incomplete_value": true,
      "site": "00531c88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ede0",
      "incomplete_value": true,
      "site": "0050edf0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:97a:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00531c8c",
      "incomplete_value": true,
      "site": "00531c8c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050edf4",
      "incomplete_value": true,
      "site": "0050edf4",
      "value": [
        "LOAD",
        "8",
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
      12,
      "READ",
      [
        "storage",
        "0029597a",
        null,
        "string"
      ]
    ],
    [
      20,
      "READ",
      [
        "storage",
        "00295988",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      12,
      "READ",
      [
        "storage",
        "002a53b3",
        null,
        "string"
      ]
    ],
    [
      20,
      "READ",
      [
        "storage",
        "002a53c1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050edd8 ["COPY", "register:4050:8", ["const:295000:8"]]
- 0050eddc ["COPY", "tmp:0:8", ["const:97a:8"]]
+ 00531c70 ["COPY", "register:4050:8", ["const:2a5000:8"]]
+ 00531c74 ["COPY", "tmp:0:8", ["const:3b3:8"]]
~~~


### [`0050edfc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edfc.md) → [`00531c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c94.md) FUN_00531c94

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051ca38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051ca38.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053f8d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531cbc",
      "incomplete_value": true,
      "site": "00531cbc",
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
      "definition_site": "0050ee24",
      "incomplete_value": true,
      "site": "0050ee24",
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
      "READ",
      [
        "storage",
        "00c1b3d0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00bebb98",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "00c9adc0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c68758",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050ee10 ["INT_ADD", "register:40f0:8", ["const:50ee10:8", "const:4:8"]]
+ 00531ca8 ["INT_ADD", "register:40f0:8", ["const:531ca8:8", "const:4:8"]]
- 0050ee14 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00531cac ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050ee1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3d0:8"]]
+ 00531cb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
~~~


### [`0050ee8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee8c.md) → [`00531d24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531d24.md) FUN_00531d24

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531d5c",
      "incomplete_value": true,
      "site": "00531d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:701:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050eec4",
      "incomplete_value": true,
      "site": "0050eec4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:477:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "0029d477",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002ad701",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050eea4 ["COPY", "register:4048:8", ["const:29d000:8"]]
- 0050eea8 ["COPY", "tmp:0:8", ["const:477:8"]]
+ 00531d3c ["COPY", "register:4048:8", ["const:2ad000:8"]]
+ 00531d40 ["COPY", "tmp:0:8", ["const:701:8"]]
- 0050eed0 ["INT_ADD", "register:40f0:8", ["const:50eed0:8", "const:4:8"]]
+ 00531d68 ["INT_ADD", "register:40f0:8", ["const:531d68:8", "const:4:8"]]
- 0050eee0 ["INT_ADD", "register:40f0:8", ["const:50eee0:8", "const:4:8"]]
+ 00531d78 ["INT_ADD", "register:40f0:8", ["const:531d78:8", "const:4:8"]]
~~~


### [`0050ef84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ef84.md) → [`00531e1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md) FUN_00531e1c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0051bf98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md) [`0051c12c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`0051d7fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) [`00bd70ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053ee30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00540694`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531e68",
      "incomplete_value": true,
      "site": "00531e74",
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
      "definition_site": "0050efd0",
      "incomplete_value": true,
      "site": "0050efdc",
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
      64,
      "READ",
      [
        "storage",
        "00c1b3e0",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "00bebc10",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      64,
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "00c687d0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050efb4 ["INT_ADD", "register:40f0:8", ["const:50efb4:8", "const:4:8"]]
+ 00531e4c ["INT_ADD", "register:40f0:8", ["const:531e4c:8", "const:4:8"]]
- 0050efb8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00531e50 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050efc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3e0:8"]]
+ 00531e5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
~~~


### [`0050f19c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f19c.md) → [`00532034`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532034.md) FUN_00532034

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053205c",
      "incomplete_value": true,
      "site": "0053206c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a57:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f1c4",
      "incomplete_value": true,
      "site": "0050f1d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:49d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "002a049d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002b0a57",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050f1b4 ["COPY", "register:4048:8", ["const:2a0000:8"]]
- 0050f1b8 ["COPY", "tmp:0:8", ["const:49d:8"]]
+ 0053204c ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 00532050 ["COPY", "tmp:0:8", ["const:a57:8"]]
- 0050f1e0 ["INT_ADD", "register:40f0:8", ["const:50f1e0:8", "const:4:8"]]
+ 00532078 ["INT_ADD", "register:40f0:8", ["const:532078:8", "const:4:8"]]
- 0050f1f0 ["INT_ADD", "register:40f0:8", ["const:50f1f0:8", "const:4:8"]]
+ 00532088 ["INT_ADD", "register:40f0:8", ["const:532088:8", "const:4:8"]]
~~~


### [`0050f294`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f294.md) → [`0053212c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053212c.md) FUN_0053212c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051d884`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0054071c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532164",
      "incomplete_value": true,
      "site": "00532164",
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
      "definition_site": "0050f2cc",
      "incomplete_value": true,
      "site": "0050f2cc",
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
      40,
      "READ",
      [
        "storage",
        "00c1b3e8",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00bebc88",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00c68848",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050f2ac ["INT_ADD", "register:40f0:8", ["const:50f2ac:8", "const:4:8"]]
+ 00532144 ["INT_ADD", "register:40f0:8", ["const:532144:8", "const:4:8"]]
- 0050f2b0 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00532148 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0050f2bc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3e8:8"]]
+ 00532154 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd8:8"]]
~~~


### [`0050f48c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f48c.md) → [`00532324`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532324.md) FUN_00532324

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053235c",
      "incomplete_value": true,
      "site": "0053235c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:c5e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f4c4",
      "incomplete_value": true,
      "site": "0050f4c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:938:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "002ad938",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002bec5e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050f4a4 ["COPY", "register:4048:8", ["const:2ad000:8"]]
- 0050f4a8 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 0053233c ["COPY", "register:4048:8", ["const:2be000:8"]]
+ 00532340 ["COPY", "tmp:0:8", ["const:c5e:8"]]
- 0050f4d0 ["INT_ADD", "register:40f0:8", ["const:50f4d0:8", "const:4:8"]]
+ 00532368 ["INT_ADD", "register:40f0:8", ["const:532368:8", "const:4:8"]]
- 0050f4e0 ["INT_ADD", "register:40f0:8", ["const:50f4e0:8", "const:4:8"]]
+ 00532378 ["INT_ADD", "register:40f0:8", ["const:532378:8", "const:4:8"]]
~~~


### [`0050f534`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f534.md) → [`005323cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323cc.md) FUN_005323cc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005323d8",
      "incomplete_value": true,
      "site": "005323e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3bc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f540",
      "incomplete_value": true,
      "site": "0050f54c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:34e:8"
              ]
            ]
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
      12,
      "READ",
      [
        "storage",
        "0029b34e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      12,
      "READ",
      [
        "storage",
        "002ab3bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050f534 ["COPY", "register:4050:8", ["const:29b000:8"]]
- 0050f538 ["COPY", "tmp:0:8", ["const:34e:8"]]
+ 005323cc ["COPY", "register:4050:8", ["const:2ab000:8"]]
+ 005323d0 ["COPY", "tmp:0:8", ["const:3bc:8"]]
~~~


### [`0050f560`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f560.md) → [`005323f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323f8.md) FUN_005323f8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532430",
      "incomplete_value": true,
      "site": "00532430",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f598",
      "incomplete_value": true,
      "site": "0050f598",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:963:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "00296963",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002a6498",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050f578 ["COPY", "register:4048:8", ["const:296000:8"]]
- 0050f57c ["COPY", "tmp:0:8", ["const:963:8"]]
+ 00532410 ["COPY", "register:4048:8", ["const:2a6000:8"]]
+ 00532414 ["COPY", "tmp:0:8", ["const:498:8"]]
- 0050f5a4 ["INT_ADD", "register:40f0:8", ["const:50f5a4:8", "const:4:8"]]
+ 0053243c ["INT_ADD", "register:40f0:8", ["const:53243c:8", "const:4:8"]]
- 0050f5b4 ["INT_ADD", "register:40f0:8", ["const:50f5b4:8", "const:4:8"]]
+ 0053244c ["INT_ADD", "register:40f0:8", ["const:53244c:8", "const:4:8"]]
~~~


### [`0050f608`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f608.md) → [`005324a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005324a0.md) FUN_005324a0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005324ac",
      "incomplete_value": true,
      "site": "005324bc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:f0d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f614",
      "incomplete_value": true,
      "site": "0050f624",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:26b:8"
              ]
            ]
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
      12,
      "READ",
      [
        "storage",
        "002a826b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      12,
      "READ",
      [
        "storage",
        "002b8f0d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050f608 ["COPY", "register:4050:8", ["const:2a8000:8"]]
- 0050f60c ["COPY", "tmp:0:8", ["const:26b:8"]]
+ 005324a0 ["COPY", "register:4050:8", ["const:2b8000:8"]]
+ 005324a4 ["COPY", "tmp:0:8", ["const:f0d:8"]]
~~~


### [`0050f680`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f680.md) → [`00532518`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532518.md) FUN_00532518

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532550",
      "incomplete_value": true,
      "site": "00532550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ad:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f6b8",
      "incomplete_value": true,
      "site": "0050f6b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a54:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "00297a54",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002a76ad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050f698 ["COPY", "register:4048:8", ["const:297000:8"]]
- 0050f69c ["COPY", "tmp:0:8", ["const:a54:8"]]
+ 00532530 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00532534 ["COPY", "tmp:0:8", ["const:6ad:8"]]
- 0050f6c4 ["INT_ADD", "register:40f0:8", ["const:50f6c4:8", "const:4:8"]]
+ 0053255c ["INT_ADD", "register:40f0:8", ["const:53255c:8", "const:4:8"]]
- 0050f6d4 ["INT_ADD", "register:40f0:8", ["const:50f6d4:8", "const:4:8"]]
+ 0053256c ["INT_ADD", "register:40f0:8", ["const:53256c:8", "const:4:8"]]
~~~


### [`0050f778`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f778.md) → [`00532610`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532610.md) FUN_00532610

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051cc00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cc00.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053fa98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fa98.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053263c",
      "incomplete_value": true,
      "site": "00532640",
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
      "definition_site": "0050f7a4",
      "incomplete_value": true,
      "site": "0050f7a8",
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
    "ordinal": 6,
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
      "READ",
      [
        "storage",
        "00c1b3d8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00bebdf0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "00c9adc8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c689b0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050f78c ["INT_ADD", "register:40f0:8", ["const:50f78c:8", "const:4:8"]]
+ 00532624 ["INT_ADD", "register:40f0:8", ["const:532624:8", "const:4:8"]]
- 0050f790 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00532628 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050f798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3d8:8"]]
+ 00532630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc8:8"]]
~~~


### [`0050f9f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f9f0.md) → [`00532888`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532888.md) FUN_00532888

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005328c0",
      "incomplete_value": true,
      "site": "005328c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:49d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050fa28",
      "incomplete_value": true,
      "site": "0050fa28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:57a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "002ab57a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "002bc49d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050fa08 ["COPY", "register:4048:8", ["const:2ab000:8"]]
- 0050fa0c ["COPY", "tmp:0:8", ["const:57a:8"]]
+ 005328a0 ["COPY", "register:4048:8", ["const:2bc000:8"]]
+ 005328a4 ["COPY", "tmp:0:8", ["const:49d:8"]]
- 0050fa34 ["INT_ADD", "register:40f0:8", ["const:50fa34:8", "const:4:8"]]
+ 005328cc ["INT_ADD", "register:40f0:8", ["const:5328cc:8", "const:4:8"]]
- 0050fa44 ["INT_ADD", "register:40f0:8", ["const:50fa44:8", "const:4:8"]]
+ 005328dc ["INT_ADD", "register:40f0:8", ["const:5328dc:8", "const:4:8"]]
~~~


### [`0050fae8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fae8.md) → [`00532980`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532980.md) FUN_00532980

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c900`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005329b0",
      "incomplete_value": false,
      "site": "005329b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c68000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050fb18",
      "incomplete_value": false,
      "site": "0050fb18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:beb000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "005329b0",
      "incomplete_value": true,
      "site": "005329b0",
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
      "definition_site": "0050fb18",
      "incomplete_value": true,
      "site": "0050fb18",
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
      40,
      "READ",
      [
        "storage",
        "00c1b3f8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00bebeb0",
        null,
        "undefined *"
      ]
    ],
    [
      48,
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
      40,
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c68a70",
        null,
        "undefined *"
      ]
    ],
    [
      48,
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
- 0050fafc ["INT_ADD", "register:40f0:8", ["const:50fafc:8", "const:4:8"]]
+ 00532994 ["INT_ADD", "register:40f0:8", ["const:532994:8", "const:4:8"]]
- 0050fb00 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00532998 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050fb08 ["COPY", "register:4048:8", ["const:beb000:8"]]
- 0050fb0c ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 005329a0 ["COPY", "register:4048:8", ["const:c68000:8"]]
+ 005329a4 ["COPY", "tmp:0:8", ["const:a70:8"]]
~~~


### [`0050fc5c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fc5c.md) → [`00532af4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532af4.md) FUN_00532af4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532b3c",
      "incomplete_value": true,
      "site": "00532b3c",
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
      "definition_site": "0050fca4",
      "incomplete_value": true,
      "site": "0050fca4",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532b3c",
      "incomplete_value": true,
      "site": "00532b3c",
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
      "definition_site": "0050fca4",
      "incomplete_value": true,
      "site": "0050fca4",
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
        "00c1b3f0",
        null,
        "pointer"
      ]
    ],
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
        "00bebf28",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      44,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
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
        "00c68ae8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050fc78 ["INT_ADD", "register:40f0:8", ["const:50fc78:8", "const:4:8"]]
+ 00532b10 ["INT_ADD", "register:40f0:8", ["const:532b10:8", "const:4:8"]]
- 0050fc7c ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050fc80 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 00532b14 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00532b18 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0050fc88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f0:8"]]
+ 00532b20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
~~~


### [`0050ffa4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050ffa4.md) → [`00532e3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md) FUN_00532e3c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00510074`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510074.md) · 呼出先 4件 [`004bb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00532f0c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f0c.md) · 呼出先 4件 [`004de6a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00532ea4",
      "incomplete_value": true,
      "site": "00532ea4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051000c",
      "incomplete_value": true,
      "site": "0051000c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00532ee0",
      "incomplete_value": true,
      "site": "00532ee0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510048",
      "incomplete_value": true,
      "site": "00510048",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      88,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      88,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0050ffc0 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00532e58 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050fffc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00532e94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 0051000c ["INT_ADD", "register:40f0:8", ["const:51000c:8", "const:4:8"]]
+ 00532ea4 ["INT_ADD", "register:40f0:8", ["const:532ea4:8", "const:4:8"]]
~~~


### [`00510098`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510098.md) → [`00532f30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f30.md) FUN_00532f30

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d0c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d0c8.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053ff60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053ff60.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "site": "00532f50",
      "value": [
        "leaf",
        "ram:53ff60:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005100b8",
      "value": [
        "leaf",
        "ram:51d0c8:8"
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
      32,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0051d0c8"
      ]
    ]
  ],
  "added": [
    [
      32,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0053ff60"
      ]
    ]
  ]
}
~~~


~~~diff
- 005100ac ["INT_ADD", "register:40f0:8", ["const:5100ac:8", "const:4:8"]]
+ 00532f44 ["INT_ADD", "register:40f0:8", ["const:532f44:8", "const:4:8"]]
- 005100b8 ["INT_ADD", "register:40f0:8", ["const:5100b8:8", "const:4:8"]]
- 005100b8 ["CALL", null, ["ram:51d0c8:8"]]
+ 00532f50 ["INT_ADD", "register:40f0:8", ["const:532f50:8", "const:4:8"]]
+ 00532f50 ["CALL", null, ["ram:53ff60:8"]]
~~~


### [`005100e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005100e0.md) → [`00532f78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md) FUN_00532f78

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00510254`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510254.md) · 呼出先 4件 [`004bb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`005330ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005330ec.md) · 呼出先 4件 [`004de6a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00532fe0",
      "incomplete_value": true,
      "site": "00532fe0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510148",
      "incomplete_value": true,
      "site": "00510148",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533024",
      "incomplete_value": true,
      "site": "00533024",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051018c",
      "incomplete_value": true,
      "site": "0051018c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533050",
      "incomplete_value": true,
      "site": "00533050",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005101b8",
      "incomplete_value": true,
      "site": "005101b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      88,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      156,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      200,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      88,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      156,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      200,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 005100fc ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00532f94 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00510138 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00532fd0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00510148 ["INT_ADD", "register:40f0:8", ["const:510148:8", "const:4:8"]]
+ 00532fe0 ["INT_ADD", "register:40f0:8", ["const:532fe0:8", "const:4:8"]]
~~~


### [`00510588`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510588.md) → [`00533420`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533420.md) FUN_00533420

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005334c4",
      "incomplete_value": true,
      "site": "005334c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:caa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051062c",
      "incomplete_value": true,
      "site": "0051062c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eec:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00533460",
      "incomplete_value": false,
      "site": "00533468",
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
            "const:e5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005105c8",
      "incomplete_value": false,
      "site": "005105d0",
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
            "const:977:8"
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
      "definition_site": "00533470",
      "incomplete_value": false,
      "site": "00533478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:265:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005105d8",
      "incomplete_value": false,
      "site": "005105e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:284:8"
          ]
        ]
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
      64,
      "PARAM",
      [
        "storage",
        "002ae977",
        null,
        "string"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00298eec",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      64,
      "PARAM",
      [
        "storage",
        "002bfe5b",
        null,
        "string"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "002ab265",
        null,
        null
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "002a8caa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 005105c4 ["COPY", "register:4000:8", ["const:2ae000:8"]]
- 005105c8 ["COPY", "tmp:0:8", ["const:977:8"]]
+ 0053345c ["COPY", "register:4000:8", ["const:2bf000:8"]]
+ 00533460 ["COPY", "tmp:0:8", ["const:e5b:8"]]
- 005105d0 ["INT_ADD", "register:40f0:8", ["const:5105d0:8", "const:4:8"]]
+ 00533468 ["INT_ADD", "register:40f0:8", ["const:533468:8", "const:4:8"]]
- 005105d4 ["COPY", "register:4008:8", ["const:29b000:8"]]
- 005105d8 ["COPY", "tmp:0:8", ["const:284:8"]]
+ 0053346c ["COPY", "register:4008:8", ["const:2ab000:8"]]
+ 00533470 ["COPY", "tmp:0:8", ["const:265:8"]]
~~~


### [`00510894`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510894.md) → [`0053372c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md) FUN_0053372c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00510960`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510960.md) · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`005337f8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005337f8.md) · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00533794",
      "incomplete_value": true,
      "site": "00533798",
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
      "definition_site": "005108fc",
      "incomplete_value": true,
      "site": "00510900",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0053377c",
      "incomplete_value": true,
      "site": "0053377c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005108e4",
      "incomplete_value": true,
      "site": "005108e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "005337c8",
      "incomplete_value": true,
      "site": "005337c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510930",
      "incomplete_value": true,
      "site": "00510930",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
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
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      108,
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      64,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      108,
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005108bc ["INT_ADD", "register:40f0:8", ["const:5108bc:8", "const:4:8"]]
+ 00533754 ["INT_ADD", "register:40f0:8", ["const:533754:8", "const:4:8"]]
- 005108c4 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 0053375c ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 005108d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0053376c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
~~~


### [`005109d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005109d8.md) → [`00533870`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533870.md) FUN_00533870

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053388c",
      "incomplete_value": true,
      "site": "00533890",
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
      "definition_site": "005109f4",
      "incomplete_value": true,
      "site": "005109f8",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005338c4",
      "incomplete_value": true,
      "site": "005338c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510a2c",
      "incomplete_value": true,
      "site": "00510a2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      20,
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 005109e4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 0053387c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005109ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 00533884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 00510a04 ["INT_ADD", "register:40f0:8", ["const:510a04:8", "const:4:8"]]
+ 0053389c ["INT_ADD", "register:40f0:8", ["const:53389c:8", "const:4:8"]]
~~~


### [`00510a58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510a58.md) → [`005338f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005338f0.md) FUN_005338f0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053390c",
      "incomplete_value": true,
      "site": "00533910",
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
      "definition_site": "00510a74",
      "incomplete_value": true,
      "site": "00510a78",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533944",
      "incomplete_value": true,
      "site": "00533944",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510aac",
      "incomplete_value": true,
      "site": "00510aac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      20,
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00510a64 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005338fc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00510a6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 00533904 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 00510a84 ["INT_ADD", "register:40f0:8", ["const:510a84:8", "const:4:8"]]
+ 0053391c ["INT_ADD", "register:40f0:8", ["const:53391c:8", "const:4:8"]]
~~~


### [`00510acc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510acc.md) → [`00533964`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md) FUN_00533964

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00510be8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510be8.md) [`00510c0c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c0c.md) [`00510c14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c14.md) · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 3件 [`00533a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533a80.md) [`00533aa4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533aa4.md) [`00533aac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533aac.md) · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005339dc",
      "incomplete_value": true,
      "site": "005339e0",
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
      "definition_site": "00510b44",
      "incomplete_value": true,
      "site": "00510b48",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00533a18",
      "incomplete_value": true,
      "site": "00533a1c",
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
      "definition_site": "00510b80",
      "incomplete_value": true,
      "site": "00510b84",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0053399c",
      "incomplete_value": true,
      "site": "0053399c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510b04",
      "incomplete_value": true,
      "site": "00510b04",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      40,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00c1b0b0",
        null,
        "pointer"
      ]
    ],
    [
      124,
      "DATA",
      [
        "storage",
        "00be98e8",
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
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00c9aaa0",
        null,
        "pointer"
      ]
    ],
    [
      124,
      "DATA",
      [
        "storage",
        "00c664a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00510ae4 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 0053397c ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00510af4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0053398c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00510b04 ["INT_ADD", "register:40f0:8", ["const:510b04:8", "const:4:8"]]
+ 0053399c ["INT_ADD", "register:40f0:8", ["const:53399c:8", "const:4:8"]]
~~~


### [`00510c70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c70.md) → [`00533b08`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533b08.md) FUN_00533b08

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533b40",
      "incomplete_value": true,
      "site": "00533b40",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510ca8",
      "incomplete_value": true,
      "site": "00510ca8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533b6c",
      "incomplete_value": true,
      "site": "00533b6c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510cd4",
      "incomplete_value": true,
      "site": "00510cd4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00bea778",
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
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00510c88 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00533b20 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00510c98 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00533b30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00510ca8 ["INT_ADD", "register:40f0:8", ["const:510ca8:8", "const:4:8"]]
+ 00533b40 ["INT_ADD", "register:40f0:8", ["const:533b40:8", "const:4:8"]]
~~~


### [`00510d1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510d1c.md) → [`00533bb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533bb4.md) FUN_00533bb4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533bec",
      "incomplete_value": true,
      "site": "00533bec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510d54",
      "incomplete_value": true,
      "site": "00510d54",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533c18",
      "incomplete_value": true,
      "site": "00533c18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510d80",
      "incomplete_value": true,
      "site": "00510d80",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00bea778",
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
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00510d34 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00533bcc ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00510d44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00533bdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00510d54 ["INT_ADD", "register:40f0:8", ["const:510d54:8", "const:4:8"]]
+ 00533bec ["INT_ADD", "register:40f0:8", ["const:533bec:8", "const:4:8"]]
~~~


### [`00510dc0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510dc0.md) → [`00533c58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533c58.md) FUN_00533c58

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58990.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00533d00",
      "incomplete_value": true,
      "site": "00533d0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510e68",
      "incomplete_value": true,
      "site": "00510e74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
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
      "definition_site": "00533cfc",
      "incomplete_value": false,
      "site": "00533d0c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00510e64",
      "incomplete_value": false,
      "site": "00510e74",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      164,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      168,
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ],
    [
      168,
      "PARAM",
      [
        "storage",
        "00be94f0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      164,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      168,
      "READ",
      [
        "storage",
        "00c9aa40",
        null,
        "pointer"
      ]
    ],
    [
      168,
      "PARAM",
      [
        "storage",
        "00c660b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00510e18 ["INT_ADD", "register:40f0:8", ["const:510e18:8", "const:4:8"]]
+ 00533cb0 ["INT_ADD", "register:40f0:8", ["const:533cb0:8", "const:4:8"]]
- 00510e30 ["INT_ADD", "register:40f0:8", ["const:510e30:8", "const:4:8"]]
+ 00533cc8 ["INT_ADD", "register:40f0:8", ["const:533cc8:8", "const:4:8"]]
- 00510e44 ["INT_ADD", "register:40f0:8", ["const:510e44:8", "const:4:8"]]
+ 00533cdc ["INT_ADD", "register:40f0:8", ["const:533cdc:8", "const:4:8"]]
~~~


### [`00510f14`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510f14.md) → [`00533dac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533dac.md) FUN_00533dac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533de4",
      "incomplete_value": true,
      "site": "00533de4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510f4c",
      "incomplete_value": true,
      "site": "00510f4c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533e10",
      "incomplete_value": true,
      "site": "00533e10",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510f78",
      "incomplete_value": true,
      "site": "00510f78",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00bea778",
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
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00510f2c ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00533dc4 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00510f3c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00533dd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00510f4c ["INT_ADD", "register:40f0:8", ["const:510f4c:8", "const:4:8"]]
+ 00533de4 ["INT_ADD", "register:40f0:8", ["const:533de4:8", "const:4:8"]]
~~~


### [`00510fc0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510fc0.md) → [`00533e58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533e58.md) FUN_00533e58

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533e90",
      "incomplete_value": true,
      "site": "00533e90",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510ff8",
      "incomplete_value": true,
      "site": "00510ff8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533ebc",
      "incomplete_value": true,
      "site": "00533ebc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511024",
      "incomplete_value": true,
      "site": "00511024",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00bea778",
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
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00510fd8 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00533e70 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00510fe8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00533e80 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00510ff8 ["INT_ADD", "register:40f0:8", ["const:510ff8:8", "const:4:8"]]
+ 00533e90 ["INT_ADD", "register:40f0:8", ["const:533e90:8", "const:4:8"]]
~~~


### [`00511164`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511164.md) → [`00533ffc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533ffc.md) FUN_00533ffc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00534014",
      "incomplete_value": false,
      "site": "00534018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051117c",
      "incomplete_value": false,
      "site": "00511180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "DATA",
      [
        "storage",
        "00be9ea8",
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
        "00c66a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00511178 ["COPY", "register:4048:8", ["const:be9000:8"]]
- 0051117c ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00534010 ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 00534014 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 0051118c ["INT_ADD", "register:40f0:8", ["const:51118c:8", "const:4:8"]]
+ 00534024 ["INT_ADD", "register:40f0:8", ["const:534024:8", "const:4:8"]]
~~~


### [`005111c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005111c8.md) → [`00534060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534060.md) FUN_00534060

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb970`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb970.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c583c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005340a8",
      "incomplete_value": true,
      "site": "005340a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511210",
      "incomplete_value": true,
      "site": "00511210",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f1:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005340d4",
      "incomplete_value": true,
      "site": "005340e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051123c",
      "incomplete_value": true,
      "site": "00511248",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f98:8"
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
      "definition_site": "005340d0",
      "incomplete_value": false,
      "site": "005340e0",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00511238",
      "incomplete_value": false,
      "site": "00511248",
      "value": [
        "leaf",
        "const:512990:8"
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
      52,
      "READ",
      [
        "storage",
        "002a68f1",
        null,
        "string"
      ]
    ],
    [
      112,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      52,
      "READ",
      [
        "storage",
        "002b73e2",
        null,
        "string"
      ]
    ],
    [
      112,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "00c9a988",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 005111ec ["INT_ADD", "register:40f0:8", ["const:5111ec:8", "const:4:8"]]
+ 00534084 ["INT_ADD", "register:40f0:8", ["const:534084:8", "const:4:8"]]
- 005111f0 ["COPY", "register:4048:8", ["const:2a6000:8"]]
- 005111f4 ["COPY", "tmp:0:8", ["const:8f1:8"]]
+ 00534088 ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 0053408c ["COPY", "tmp:0:8", ["const:3e2:8"]]
- 0051121c ["INT_ADD", "register:40f0:8", ["const:51121c:8", "const:4:8"]]
+ 005340b4 ["INT_ADD", "register:40f0:8", ["const:5340b4:8", "const:4:8"]]
~~~


### [`00511290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511290.md) → [`00534128`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534128.md) FUN_00534128

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00534140",
      "incomplete_value": false,
      "site": "00534144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005112a8",
      "incomplete_value": false,
      "site": "005112ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      28,
      "DATA",
      [
        "storage",
        "00be9ef8",
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
        "00c66ab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 005112a4 ["COPY", "register:4048:8", ["const:be9000:8"]]
- 005112a8 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 0053413c ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 00534140 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 005112b8 ["INT_ADD", "register:40f0:8", ["const:5112b8:8", "const:4:8"]]
+ 00534150 ["INT_ADD", "register:40f0:8", ["const:534150:8", "const:4:8"]]
~~~


### [`005112f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005112f4.md) → [`0053418c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053418c.md) FUN_0053418c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb970`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb970.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c583c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005341d4",
      "incomplete_value": true,
      "site": "005341d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051133c",
      "incomplete_value": true,
      "site": "0051133c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f1:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00534200",
      "incomplete_value": true,
      "site": "0053420c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511368",
      "incomplete_value": true,
      "site": "00511374",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f98:8"
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
      "definition_site": "005341fc",
      "incomplete_value": false,
      "site": "0053420c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00511364",
      "incomplete_value": false,
      "site": "00511374",
      "value": [
        "leaf",
        "const:512990:8"
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
      52,
      "READ",
      [
        "storage",
        "002a68f1",
        null,
        "string"
      ]
    ],
    [
      112,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      52,
      "READ",
      [
        "storage",
        "002b73e2",
        null,
        "string"
      ]
    ],
    [
      112,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "00c9a988",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00511318 ["INT_ADD", "register:40f0:8", ["const:511318:8", "const:4:8"]]
+ 005341b0 ["INT_ADD", "register:40f0:8", ["const:5341b0:8", "const:4:8"]]
- 0051131c ["COPY", "register:4048:8", ["const:2a6000:8"]]
- 00511320 ["COPY", "tmp:0:8", ["const:8f1:8"]]
+ 005341b4 ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 005341b8 ["COPY", "tmp:0:8", ["const:3e2:8"]]
- 00511348 ["INT_ADD", "register:40f0:8", ["const:511348:8", "const:4:8"]]
+ 005341e0 ["INT_ADD", "register:40f0:8", ["const:5341e0:8", "const:4:8"]]
~~~


### [`005113bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005113bc.md) → [`00534254`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534254.md) FUN_00534254

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534284",
      "incomplete_value": true,
      "site": "00534298",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005113ec",
      "incomplete_value": true,
      "site": "00511400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:744:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00534288",
      "incomplete_value": true,
      "site": "0053429c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005113f0",
      "incomplete_value": true,
      "site": "00511404",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005342a8",
      "incomplete_value": true,
      "site": "005342a8",
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
      "definition_site": "00511410",
      "incomplete_value": true,
      "site": "00511410",
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
        "002a1744",
        null,
        "string"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "002a174d",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "002b1d90",
        null,
        "string"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "002b1d99",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 005113d0 ["INT_ADD", "register:40f0:8", ["const:5113d0:8", "const:4:8"]]
+ 00534268 ["INT_ADD", "register:40f0:8", ["const:534268:8", "const:4:8"]]
- 005113dc ["INT_ADD", "register:40f0:8", ["const:5113dc:8", "const:4:8"]]
+ 00534274 ["INT_ADD", "register:40f0:8", ["const:534274:8", "const:4:8"]]
- 005113e0 ["COPY", "register:4040:8", ["const:2a1000:8"]]
- 005113e4 ["COPY", "tmp:0:8", ["const:744:8"]]
+ 00534278 ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 0053427c ["COPY", "tmp:0:8", ["const:d90:8"]]
~~~


### [`00511488`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511488.md) → [`00534320`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534320.md) FUN_00534320

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534350",
      "incomplete_value": true,
      "site": "00534364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005114b8",
      "incomplete_value": true,
      "site": "005114cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b93:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00534354",
      "incomplete_value": true,
      "site": "00534368",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005114bc",
      "incomplete_value": true,
      "site": "005114d0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534374",
      "incomplete_value": true,
      "site": "00534374",
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
      "definition_site": "005114dc",
      "incomplete_value": true,
      "site": "005114dc",
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
        "00296b93",
        null,
        "string"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00296ba1",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "002a66c8",
        null,
        "string"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "002a66d6",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0051149c ["INT_ADD", "register:40f0:8", ["const:51149c:8", "const:4:8"]]
+ 00534334 ["INT_ADD", "register:40f0:8", ["const:534334:8", "const:4:8"]]
- 005114a8 ["INT_ADD", "register:40f0:8", ["const:5114a8:8", "const:4:8"]]
+ 00534340 ["INT_ADD", "register:40f0:8", ["const:534340:8", "const:4:8"]]
- 005114ac ["COPY", "register:4040:8", ["const:296000:8"]]
- 005114b0 ["COPY", "tmp:0:8", ["const:b93:8"]]
+ 00534344 ["COPY", "register:4040:8", ["const:2a6000:8"]]
+ 00534348 ["COPY", "tmp:0:8", ["const:6c8:8"]]
~~~


### [`00511554`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511554.md) → [`005343ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005343ec.md) FUN_005343ec

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005343fc",
      "incomplete_value": false,
      "site": "005343fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511564",
      "incomplete_value": false,
      "site": "00511564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      16,
      "DATA",
      [
        "storage",
        "00be9f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      16,
      "DATA",
      [
        "storage",
        "00c66b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0051155c ["COPY", "register:4048:8", ["const:be9000:8"]]
- 00511560 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 005343f4 ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 005343f8 ["COPY", "tmp:0:8", ["const:b18:8"]]
~~~


### [`00511580`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511580.md) → [`00534418`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534418.md) FUN_00534418

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00534428",
      "incomplete_value": false,
      "site": "00534428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511590",
      "incomplete_value": false,
      "site": "00511590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      16,
      "DATA",
      [
        "storage",
        "00be9f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      16,
      "DATA",
      [
        "storage",
        "00c66b48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00511588 ["COPY", "register:4048:8", ["const:be9000:8"]]
- 0051158c ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00534420 ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 00534424 ["COPY", "tmp:0:8", ["const:b48:8"]]
~~~


### [`005115ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005115ac.md) → [`00534444`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534444.md) FUN_00534444

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534468",
      "incomplete_value": true,
      "site": "00534474",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005115d0",
      "incomplete_value": true,
      "site": "005115dc",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534494",
      "incomplete_value": true,
      "site": "00534494",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005115fc",
      "incomplete_value": true,
      "site": "005115fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "005344c0",
      "incomplete_value": true,
      "site": "005344c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511628",
      "incomplete_value": true,
      "site": "00511628",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      24,
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      24,
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 005115bc ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 005115c0 ["COPY", "register:40a8:8", ["const:bea000:8"]]
- 005115c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 00534454 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00534458 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 0053445c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
- 005115ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00534484 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 005115fc ["INT_ADD", "register:40f0:8", ["const:5115fc:8", "const:4:8"]]
+ 00534494 ["INT_ADD", "register:40f0:8", ["const:534494:8", "const:4:8"]]
~~~


### [`00511658`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511658.md) → [`005344f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005344f0.md) FUN_005344f0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534514",
      "incomplete_value": true,
      "site": "00534520",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051167c",
      "incomplete_value": true,
      "site": "00511688",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534540",
      "incomplete_value": true,
      "site": "00534540",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005116a8",
      "incomplete_value": true,
      "site": "005116a8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0053456c",
      "incomplete_value": true,
      "site": "0053456c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005116d4",
      "incomplete_value": true,
      "site": "005116d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      24,
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      24,
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00511668 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0051166c ["COPY", "register:40a8:8", ["const:bea000:8"]]
- 00511670 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 00534500 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00534504 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00534508 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
- 00511698 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00534530 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 005116a8 ["INT_ADD", "register:40f0:8", ["const:5116a8:8", "const:4:8"]]
+ 00534540 ["INT_ADD", "register:40f0:8", ["const:534540:8", "const:4:8"]]
~~~


### [`00511720`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511720.md) → [`005345b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345b8.md) FUN_005345b8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d1fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d1fc.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00540094`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540094.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005345cc",
      "incomplete_value": true,
      "site": "005345d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511734",
      "incomplete_value": true,
      "site": "00511738",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f8:8"
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
        "00c1b1f8",
        null,
        "pointer"
      ]
    ],
    [
      20,
      "PARAM",
      [
        "storage",
        "00bea368",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9abe8",
        null,
        "pointer"
      ]
    ],
    [
      20,
      "PARAM",
      [
        "storage",
        "00c66f28",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 0051172c ["COPY", "register:4008:8", ["const:c1b000:8"]]
+ 005345c4 ["COPY", "register:4008:8", ["const:c9a000:8"]]
- 00511734 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1f8:8"]]
+ 005345cc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:be8:8"]]
- 00511738 ["INT_ADD", "register:40f0:8", ["const:511738:8", "const:4:8"]]
+ 005345d0 ["INT_ADD", "register:40f0:8", ["const:5345d0:8", "const:4:8"]]
~~~


### [`0051175c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051175c.md) → [`005345f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345f4.md) FUN_005345f4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d1fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d1fc.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00540094`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540094.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00534608",
      "incomplete_value": true,
      "site": "00534610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511770",
      "incomplete_value": true,
      "site": "00511778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f8:8"
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
        "00c1b1f8",
        null,
        "pointer"
      ]
    ],
    [
      20,
      "PARAM",
      [
        "storage",
        "00bea368",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9abe8",
        null,
        "pointer"
      ]
    ],
    [
      20,
      "PARAM",
      [
        "storage",
        "00c66f28",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00511768 ["COPY", "register:4008:8", ["const:c1b000:8"]]
+ 00534600 ["COPY", "register:4008:8", ["const:c9a000:8"]]
- 00511770 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1f8:8"]]
+ 00534608 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:be8:8"]]
- 00511778 ["INT_ADD", "register:40f0:8", ["const:511778:8", "const:4:8"]]
+ 00534610 ["INT_ADD", "register:40f0:8", ["const:534610:8", "const:4:8"]]
~~~


### [`00511934`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511934.md) → [`005347cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005347cc.md) FUN_005347cc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005347e8",
      "incomplete_value": true,
      "site": "005347ec",
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
      "definition_site": "00511950",
      "incomplete_value": true,
      "site": "00511954",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534828",
      "incomplete_value": true,
      "site": "0053482c",
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
      "definition_site": "00511990",
      "incomplete_value": true,
      "site": "00511994",
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
      20,
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00beaac8",
        null,
        "undefined1[72]"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67688",
        null,
        "undefined1[72]"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00511940 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005347d8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00511948 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 005347e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce0:8"]]
- 00511964 ["INT_ADD", "register:40f0:8", ["const:511964:8", "const:4:8"]]
+ 005347fc ["INT_ADD", "register:40f0:8", ["const:5347fc:8", "const:4:8"]]
~~~


### [`005119e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005119e4.md) → [`0053487c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053487c.md) FUN_0053487c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534898",
      "incomplete_value": true,
      "site": "0053489c",
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
      "definition_site": "00511a00",
      "incomplete_value": true,
      "site": "00511a04",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005119f0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00534888 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005119f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 00534890 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 00511a10 ["INT_ADD", "register:40f0:8", ["const:511a10:8", "const:4:8"]]
+ 005348a8 ["INT_ADD", "register:40f0:8", ["const:5348a8:8", "const:4:8"]]
~~~


### [`00511eb0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511eb0.md) → [`00534d48`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534d48.md) FUN_00534d48

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534d64",
      "incomplete_value": true,
      "site": "00534d68",
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
      "definition_site": "00511ecc",
      "incomplete_value": true,
      "site": "00511ed0",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00511ebc ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00534d54 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00511ec4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00534d5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00511edc ["INT_ADD", "register:40f0:8", ["const:511edc:8", "const:4:8"]]
+ 00534d74 ["INT_ADD", "register:40f0:8", ["const:534d74:8", "const:4:8"]]
~~~


### [`00511f10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511f10.md) → [`00534da8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534da8.md) FUN_00534da8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534dc4",
      "incomplete_value": true,
      "site": "00534dc8",
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
      "definition_site": "00511f2c",
      "incomplete_value": true,
      "site": "00511f30",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00511f1c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00534db4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00511f24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00534dbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00511f3c ["INT_ADD", "register:40f0:8", ["const:511f3c:8", "const:4:8"]]
+ 00534dd4 ["INT_ADD", "register:40f0:8", ["const:534dd4:8", "const:4:8"]]
~~~


### [`00511fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511fe0.md) → [`00534e78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534e78.md) FUN_00534e78

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534e94",
      "incomplete_value": true,
      "site": "00534e98",
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
      "definition_site": "00511ffc",
      "incomplete_value": true,
      "site": "00512000",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534ecc",
      "incomplete_value": true,
      "site": "00534ecc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00512034",
      "incomplete_value": true,
      "site": "00512034",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      20,
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00511fec ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00534e84 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00511ff4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 00534e8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 0051200c ["INT_ADD", "register:40f0:8", ["const:51200c:8", "const:4:8"]]
+ 00534ea4 ["INT_ADD", "register:40f0:8", ["const:534ea4:8", "const:4:8"]]
~~~


### [`00512058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512058.md) → [`00534ef0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ef0.md) FUN_00534ef0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534f0c",
      "incomplete_value": true,
      "site": "00534f10",
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
      "definition_site": "00512074",
      "incomplete_value": true,
      "site": "00512078",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534f44",
      "incomplete_value": true,
      "site": "00534f44",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005120ac",
      "incomplete_value": true,
      "site": "005120ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      20,
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512064 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00534efc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051206c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 00534f04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 00512084 ["INT_ADD", "register:40f0:8", ["const:512084:8", "const:4:8"]]
+ 00534f1c ["INT_ADD", "register:40f0:8", ["const:534f1c:8", "const:4:8"]]
~~~


### [`0051215c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/0051215c.md) → [`00534ff4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ff4.md) FUN_00534ff4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535008",
      "incomplete_value": true,
      "site": "00535008",
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
      "definition_site": "00512170",
      "incomplete_value": true,
      "site": "00512170",
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
      8,
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      20,
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      8,
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      20,
      "DATA",
      [
        "storage",
        "00c66958",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0051215c ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00534ff4 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00512164 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1c0:8"]]
+ 00534ffc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bb0:8"]]
~~~


### [`00512480`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512480.md) → [`00535318`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535318.md) FUN_00535318

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535334",
      "incomplete_value": true,
      "site": "00535338",
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
      "definition_site": "0051249c",
      "incomplete_value": true,
      "site": "005124a0",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0051248c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535324 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0053532c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005124ac ["INT_ADD", "register:40f0:8", ["const:5124ac:8", "const:4:8"]]
+ 00535344 ["INT_ADD", "register:40f0:8", ["const:535344:8", "const:4:8"]]
~~~


### [`005124c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005124c8.md) → [`00535360`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535360.md) FUN_00535360

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053537c",
      "incomplete_value": true,
      "site": "00535380",
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
      "definition_site": "005124e4",
      "incomplete_value": true,
      "site": "005124e8",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005124d4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0053536c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005124dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00535374 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005124f4 ["INT_ADD", "register:40f0:8", ["const:5124f4:8", "const:4:8"]]
+ 0053538c ["INT_ADD", "register:40f0:8", ["const:53538c:8", "const:4:8"]]
~~~


### [`00512510`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512510.md) → [`005353a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353a8.md) FUN_005353a8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005353c4",
      "incomplete_value": true,
      "site": "005353c8",
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
      "definition_site": "0051252c",
      "incomplete_value": true,
      "site": "00512530",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0051251c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005353b4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512524 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005353bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0051253c ["INT_ADD", "register:40f0:8", ["const:51253c:8", "const:4:8"]]
+ 005353d4 ["INT_ADD", "register:40f0:8", ["const:5353d4:8", "const:4:8"]]
~~~


### [`00512558`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512558.md) → [`005353f0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353f0.md) FUN_005353f0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053540c",
      "incomplete_value": true,
      "site": "00535410",
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
      "definition_site": "00512574",
      "incomplete_value": true,
      "site": "00512578",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512564 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005353fc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051256c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00535404 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00512584 ["INT_ADD", "register:40f0:8", ["const:512584:8", "const:4:8"]]
+ 0053541c ["INT_ADD", "register:40f0:8", ["const:53541c:8", "const:4:8"]]
~~~


### [`005125a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125a0.md) → [`00535438`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535438.md) FUN_00535438

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535454",
      "incomplete_value": true,
      "site": "00535458",
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
      "definition_site": "005125bc",
      "incomplete_value": true,
      "site": "005125c0",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005125ac ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535444 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005125b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0053544c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005125cc ["INT_ADD", "register:40f0:8", ["const:5125cc:8", "const:4:8"]]
+ 00535464 ["INT_ADD", "register:40f0:8", ["const:535464:8", "const:4:8"]]
~~~


### [`005125e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125e8.md) → [`00535480`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535480.md) FUN_00535480

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053549c",
      "incomplete_value": true,
      "site": "005354a0",
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
      "definition_site": "00512604",
      "incomplete_value": true,
      "site": "00512608",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005125f4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0053548c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005125fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00535494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00512614 ["INT_ADD", "register:40f0:8", ["const:512614:8", "const:4:8"]]
+ 005354ac ["INT_ADD", "register:40f0:8", ["const:5354ac:8", "const:4:8"]]
~~~


### [`00512630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512630.md) → [`005354c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005354c8.md) FUN_005354c8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005354e4",
      "incomplete_value": true,
      "site": "005354e8",
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
      "definition_site": "0051264c",
      "incomplete_value": true,
      "site": "00512650",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0051263c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005354d4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512644 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005354dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0051265c ["INT_ADD", "register:40f0:8", ["const:51265c:8", "const:4:8"]]
+ 005354f4 ["INT_ADD", "register:40f0:8", ["const:5354f4:8", "const:4:8"]]
~~~


### [`00512678`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512678.md) → [`00535510`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535510.md) FUN_00535510

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053552c",
      "incomplete_value": true,
      "site": "00535530",
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
      "definition_site": "00512694",
      "incomplete_value": true,
      "site": "00512698",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512684 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0053551c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051268c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00535524 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005126a4 ["INT_ADD", "register:40f0:8", ["const:5126a4:8", "const:4:8"]]
+ 0053553c ["INT_ADD", "register:40f0:8", ["const:53553c:8", "const:4:8"]]
~~~


### [`005126c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005126c0.md) → [`00535558`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535558.md) FUN_00535558

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535574",
      "incomplete_value": true,
      "site": "00535578",
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
      "definition_site": "005126dc",
      "incomplete_value": true,
      "site": "005126e0",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005126cc ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535564 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005126d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0053556c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005126ec ["INT_ADD", "register:40f0:8", ["const:5126ec:8", "const:4:8"]]
+ 00535584 ["INT_ADD", "register:40f0:8", ["const:535584:8", "const:4:8"]]
~~~


### [`00512708`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512708.md) → [`005355a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355a0.md) FUN_005355a0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005355bc",
      "incomplete_value": true,
      "site": "005355c0",
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
      "definition_site": "00512724",
      "incomplete_value": true,
      "site": "00512728",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512714 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005355ac ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051271c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005355b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00512734 ["INT_ADD", "register:40f0:8", ["const:512734:8", "const:4:8"]]
+ 005355cc ["INT_ADD", "register:40f0:8", ["const:5355cc:8", "const:4:8"]]
~~~


### [`00512750`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512750.md) → [`005355e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355e8.md) FUN_005355e8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535604",
      "incomplete_value": true,
      "site": "00535608",
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
      "definition_site": "0051276c",
      "incomplete_value": true,
      "site": "00512770",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0051275c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005355f4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005355fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0051277c ["INT_ADD", "register:40f0:8", ["const:51277c:8", "const:4:8"]]
+ 00535614 ["INT_ADD", "register:40f0:8", ["const:535614:8", "const:4:8"]]
~~~


### [`00512798`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512798.md) → [`00535630`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535630.md) FUN_00535630

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053564c",
      "incomplete_value": true,
      "site": "00535650",
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
      "definition_site": "005127b4",
      "incomplete_value": true,
      "site": "005127b8",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005127a4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0053563c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005127ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00535644 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005127c4 ["INT_ADD", "register:40f0:8", ["const:5127c4:8", "const:4:8"]]
+ 0053565c ["INT_ADD", "register:40f0:8", ["const:53565c:8", "const:4:8"]]
~~~


### [`005127e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005127e0.md) → [`00535678`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535678.md) FUN_00535678

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535694",
      "incomplete_value": true,
      "site": "00535698",
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
      "definition_site": "005127fc",
      "incomplete_value": true,
      "site": "00512800",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005127ec ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535684 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005127f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0053568c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0051280c ["INT_ADD", "register:40f0:8", ["const:51280c:8", "const:4:8"]]
+ 005356a4 ["INT_ADD", "register:40f0:8", ["const:5356a4:8", "const:4:8"]]
~~~


### [`00512828`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512828.md) → [`005356c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005356c0.md) FUN_005356c0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005356dc",
      "incomplete_value": true,
      "site": "005356e0",
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
      "definition_site": "00512844",
      "incomplete_value": true,
      "site": "00512848",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512834 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005356cc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051283c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005356d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00512854 ["INT_ADD", "register:40f0:8", ["const:512854:8", "const:4:8"]]
+ 005356ec ["INT_ADD", "register:40f0:8", ["const:5356ec:8", "const:4:8"]]
~~~


### [`00512870`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512870.md) → [`00535708`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535708.md) FUN_00535708

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535724",
      "incomplete_value": true,
      "site": "00535728",
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
      "definition_site": "0051288c",
      "incomplete_value": true,
      "site": "00512890",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0051287c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535714 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0053571c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0051289c ["INT_ADD", "register:40f0:8", ["const:51289c:8", "const:4:8"]]
+ 00535734 ["INT_ADD", "register:40f0:8", ["const:535734:8", "const:4:8"]]
~~~


### [`005128b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005128b8.md) → [`00535750`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535750.md) FUN_00535750

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053576c",
      "incomplete_value": true,
      "site": "00535770",
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
      "definition_site": "005128d4",
      "incomplete_value": true,
      "site": "005128d8",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005128c4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0053575c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005128cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00535764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005128e4 ["INT_ADD", "register:40f0:8", ["const:5128e4:8", "const:4:8"]]
+ 0053577c ["INT_ADD", "register:40f0:8", ["const:53577c:8", "const:4:8"]]
~~~


### [`00512900`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512900.md) → [`00535798`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535798.md) FUN_00535798

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005357b4",
      "incomplete_value": true,
      "site": "005357b8",
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
      "definition_site": "0051291c",
      "incomplete_value": true,
      "site": "00512920",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 0051290c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005357a4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512914 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005357ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0051292c ["INT_ADD", "register:40f0:8", ["const:51292c:8", "const:4:8"]]
+ 005357c4 ["INT_ADD", "register:40f0:8", ["const:5357c4:8", "const:4:8"]]
~~~


### [`00512948`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512948.md) → [`005357e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005357e0.md) FUN_005357e0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005357fc",
      "incomplete_value": true,
      "site": "00535800",
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
      "definition_site": "00512964",
      "incomplete_value": true,
      "site": "00512968",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512954 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005357ec ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051295c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005357f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00512974 ["INT_ADD", "register:40f0:8", ["const:512974:8", "const:4:8"]]
+ 0053580c ["INT_ADD", "register:40f0:8", ["const:53580c:8", "const:4:8"]]
~~~


### [`005129d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005129d4.md) → [`0053586c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/0053586c.md) FUN_0053586c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535888",
      "incomplete_value": true,
      "site": "0053588c",
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
      "definition_site": "005129f0",
      "incomplete_value": true,
      "site": "005129f4",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 005129e0 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535878 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005129e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00535880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00512a00 ["INT_ADD", "register:40f0:8", ["const:512a00:8", "const:4:8"]]
+ 00535898 ["INT_ADD", "register:40f0:8", ["const:535898:8", "const:4:8"]]
~~~


### [`00512a1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512a1c.md) → [`005358b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358b4.md) FUN_005358b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005358d0",
      "incomplete_value": true,
      "site": "005358d4",
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
      "definition_site": "00512a38",
      "incomplete_value": true,
      "site": "00512a3c",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512a28 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005358c0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512a30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005358c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00512a48 ["INT_ADD", "register:40f0:8", ["const:512a48:8", "const:4:8"]]
+ 005358e0 ["INT_ADD", "register:40f0:8", ["const:5358e0:8", "const:4:8"]]
~~~


### [`00512c94`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) → [`00535b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) FUN_00535b2c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 35件 [`0047f2d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f2d0.md) [`00482154`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482154.md) [`00482df4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482df4.md) [`00484754`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484754.md) [`00484d30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484d30.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 35件 [`004a2168`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md) [`004a4fec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md) [`004a5c8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md) [`004a75ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md) [`004a7bc8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00535b3c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00512ca4",
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
      "definition_site": "00535b38",
      "incomplete_value": false,
      "site": "00535b3c",
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
      "definition_site": "00512ca0",
      "incomplete_value": false,
      "site": "00512ca4",
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
- 00512c9c ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00512ca0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00535b34 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00535b38 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00512ca4 ["INT_ADD", "register:40f0:8", ["const:512ca4:8", "const:4:8"]]
- 00512ca4 ["CALL", null, ["ram:418c38:8"]]
+ 00535b3c ["INT_ADD", "register:40f0:8", ["const:535b3c:8", "const:4:8"]]
+ 00535b3c ["CALL", null, ["ram:43b738:8"]]
~~~


### [`00512ca8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) → [`00535b40`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) FUN_00535b40

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 32件 [`004826c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004826c4.md) [`00483d44`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483d44.md) [`00484024`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484024.md) [`00485f54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485f54.md) [`0049f624`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md) · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 32件 [`004a555c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md) [`004a6bdc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6bdc.md) [`004a6ebc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6ebc.md) [`004a8dec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md) [`004c24bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c24bc.md) · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00535ba8",
      "incomplete_value": true,
      "site": "00535ba8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00512d10",
      "incomplete_value": true,
      "site": "00512d10",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00535be4",
      "incomplete_value": true,
      "site": "00535be4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00512d4c",
      "incomplete_value": true,
      "site": "00512d4c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      88,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      88,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512cc4 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00535b5c ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00512d00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00535b98 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00512d10 ["INT_ADD", "register:40f0:8", ["const:512d10:8", "const:4:8"]]
+ 00535ba8 ["INT_ADD", "register:40f0:8", ["const:535ba8:8", "const:4:8"]]
~~~


### [`00512d84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512d84.md) → [`00535c1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c1c.md) FUN_00535c1c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535c38",
      "incomplete_value": true,
      "site": "00535c3c",
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
      "definition_site": "00512da0",
      "incomplete_value": true,
      "site": "00512da4",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512d90 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535c28 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00535c30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00512db0 ["INT_ADD", "register:40f0:8", ["const:512db0:8", "const:4:8"]]
+ 00535c48 ["INT_ADD", "register:40f0:8", ["const:535c48:8", "const:4:8"]]
~~~


### [`00512dcc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512dcc.md) → [`00535c64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c64.md) FUN_00535c64

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0048cd38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) · 呼出先 7件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb100`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb100.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`004afbd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) · 呼出先 7件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535d24",
      "incomplete_value": true,
      "site": "00535d24",
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
      "definition_site": "00512e8c",
      "incomplete_value": true,
      "site": "00512e8c",
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00535d70",
      "incomplete_value": false,
      "site": "00535d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00512ed8",
      "incomplete_value": false,
      "site": "00512edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00535c84",
      "incomplete_value": false,
      "site": "00535c98",
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
            "const:20c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00512dec",
      "incomplete_value": false,
      "site": "00512e00",
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
            "const:be8:8"
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
      32,
      "PARAM",
      [
        "storage",
        "002afbe8",
        null,
        "string"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002a03cd",
        null,
        null
      ]
    ],
    [
      172,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      32,
      "PARAM",
      [
        "storage",
        "002c120c",
        null,
        "string"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002b0987",
        null,
        null
      ]
    ],
    [
      172,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512de8 ["COPY", "register:4000:8", ["const:2af000:8"]]
- 00512dec ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00535c80 ["COPY", "register:4000:8", ["const:2c1000:8"]]
+ 00535c84 ["COPY", "tmp:0:8", ["const:20c:8"]]
- 00512e00 ["INT_ADD", "register:40f0:8", ["const:512e00:8", "const:4:8"]]
+ 00535c98 ["INT_ADD", "register:40f0:8", ["const:535c98:8", "const:4:8"]]
- 00512e04 ["COPY", "register:4008:8", ["const:2a0000:8"]]
- 00512e08 ["COPY", "tmp:0:8", ["const:3cd:8"]]
+ 00535c9c ["COPY", "register:4008:8", ["const:2b0000:8"]]
+ 00535ca0 ["COPY", "tmp:0:8", ["const:987:8"]]
~~~


### [`00512fd4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512fd4.md) → [`00535e6c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535e6c.md) FUN_00535e6c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535e88",
      "incomplete_value": true,
      "site": "00535e8c",
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
      "definition_site": "00512ff0",
      "incomplete_value": true,
      "site": "00512ff4",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00512fe0 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535e78 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512fe8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00535e80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00513000 ["INT_ADD", "register:40f0:8", ["const:513000:8", "const:4:8"]]
+ 00535e98 ["INT_ADD", "register:40f0:8", ["const:535e98:8", "const:4:8"]]
~~~


### [`0051301c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051301c.md) → [`00535eb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535eb4.md) FUN_00535eb4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535ed0",
      "incomplete_value": true,
      "site": "00535ed4",
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
      "definition_site": "00513038",
      "incomplete_value": true,
      "site": "0051303c",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00513028 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535ec0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00513030 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00535ec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00513048 ["INT_ADD", "register:40f0:8", ["const:513048:8", "const:4:8"]]
+ 00535ee0 ["INT_ADD", "register:40f0:8", ["const:535ee0:8", "const:4:8"]]
~~~


### [`0051308c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051308c.md) → [`00535f24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md) FUN_00535f24

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004d5f58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5f58.md) [`004d6094`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6094.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004f8df0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md) [`004f8f2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f2c.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00535f4c",
      "incomplete_value": false,
      "site": "00535f5c",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005130b4",
      "incomplete_value": false,
      "site": "005130c4",
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
            "const:3c0:8"
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
      "definition_site": "00535f74",
      "incomplete_value": false,
      "site": "00535f78",
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
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005130dc",
      "incomplete_value": false,
      "site": "005130e0",
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
            "const:3d0:8"
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
      "definition_site": "00535f88",
      "incomplete_value": false,
      "site": "00535f9c",
      "value": [
        "leaf",
        "const:4f8f2c:8"
      ]
    },
    "old": {
      "definition_site": "005130f0",
      "incomplete_value": false,
      "site": "00513104",
      "value": [
        "leaf",
        "const:4d6094:8"
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
      24,
      "READ",
      [
        "storage",
        "00c253d0",
        null,
        "undefined1"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "00c253c0",
        null,
        "undefined8"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "00c253d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      24,
      "READ",
      [
        "storage",
        "00ca4e90",
        null,
        "undefined1"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "00ca4e80",
        null,
        "undefined8"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "00ca4e90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00513098 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0051309c ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 00535f30 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 00535f34 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 005130b0 ["COPY", "register:4008:8", ["const:c25000:8"]]
- 005130b4 ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 00535f48 ["COPY", "register:4008:8", ["const:ca4000:8"]]
+ 00535f4c ["COPY", "tmp:0:8", ["const:e80:8"]]
- 005130c4 ["INT_ADD", "register:40f0:8", ["const:5130c4:8", "const:4:8"]]
+ 00535f5c ["INT_ADD", "register:40f0:8", ["const:535f5c:8", "const:4:8"]]
~~~


### [`00513138`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513138.md) → [`00535fd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md) FUN_00535fd0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004a2edc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2edc.md) [`004bf57c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`004c05ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) · 呼出先 5件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf30.md)
- 新版 呼出元 3件 [`004c5d74`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5d74.md) [`004e2414`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`004e3484`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) · 呼出先 5件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58980`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58980.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005360c8",
      "incomplete_value": true,
      "site": "005360d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513230",
      "incomplete_value": true,
      "site": "0051323c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:48:8"
              ]
            ]
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
      "definition_site": "005360c4",
      "incomplete_value": false,
      "site": "005360d4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0051322c",
      "incomplete_value": false,
      "site": "0051323c",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      244,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      248,
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      248,
      "PARAM",
      [
        "storage",
        "00be9e68",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      244,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      248,
      "READ",
      [
        "storage",
        "00c9aa38",
        null,
        "pointer"
      ]
    ],
    [
      248,
      "PARAM",
      [
        "storage",
        "00c66a28",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00513170 ["INT_ADD", "register:40f0:8", ["const:513170:8", "const:4:8"]]
+ 00536008 ["INT_ADD", "register:40f0:8", ["const:536008:8", "const:4:8"]]
- 005131b0 ["INT_ADD", "register:40f0:8", ["const:5131b0:8", "const:4:8"]]
+ 00536048 ["INT_ADD", "register:40f0:8", ["const:536048:8", "const:4:8"]]
- 005131e0 ["INT_ADD", "register:40f0:8", ["const:5131e0:8", "const:4:8"]]
+ 00536078 ["INT_ADD", "register:40f0:8", ["const:536078:8", "const:4:8"]]
~~~


### [`0051328c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051328c.md) → [`00536124`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536124.md) FUN_00536124

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536140",
      "incomplete_value": true,
      "site": "00536144",
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
      "definition_site": "005132a8",
      "incomplete_value": true,
      "site": "005132ac",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00513298 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00536130 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005132a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00536138 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005132b8 ["INT_ADD", "register:40f0:8", ["const:5132b8:8", "const:4:8"]]
+ 00536150 ["INT_ADD", "register:40f0:8", ["const:536150:8", "const:4:8"]]
~~~


### [`005132d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) → [`0053616c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) FUN_0053616c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`004ababc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ababc.md) [`004d2b8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2b8c.md) [`004d3aec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3aec.md) [`004d3ba0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3ba0.md) · 呼出先 8件 [`0051345c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051345c.md) [`00bbad34`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 4件 [`004ce954`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md) [`004f5a24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5a24.md) [`004f6984`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6984.md) [`004f6a38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6a38.md) · 呼出先 8件 [`005362f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md) [`00c3777c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00536250",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005133b8",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536260",
      "incomplete_value": true,
      "site": "00536268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005133c8",
      "incomplete_value": true,
      "site": "005133d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
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
      "definition_site": "00536264",
      "incomplete_value": true,
      "site": "00536268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005133cc",
      "incomplete_value": true,
      "site": "005133d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:c1b000:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      228,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      244,
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      244,
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      228,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      244,
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      244,
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00513324 ["INT_ADD", "register:40f0:8", ["const:513324:8", "const:4:8"]]
+ 005361bc ["INT_ADD", "register:40f0:8", ["const:5361bc:8", "const:4:8"]]
- 00513350 ["INT_ADD", "register:40f0:8", ["const:513350:8", "const:4:8"]]
+ 005361e8 ["INT_ADD", "register:40f0:8", ["const:5361e8:8", "const:4:8"]]
- 00513398 ["INT_ADD", "register:40f0:8", ["const:513398:8", "const:4:8"]]
+ 00536230 ["INT_ADD", "register:40f0:8", ["const:536230:8", "const:4:8"]]
~~~


