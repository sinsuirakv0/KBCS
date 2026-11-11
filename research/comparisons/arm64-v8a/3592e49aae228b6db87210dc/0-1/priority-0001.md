# v15.7.4 → v16.0.0 · 最優先の変更候補 (1)

[一覧の目次](README.md)

### [`00418338`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418338.md) → [`0043ae38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae38.md) _INIT_3

根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b7d2a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2a0.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bf9ce8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ce8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043ae54",
      "incomplete_value": false,
      "site": "0043ae58",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418354",
      "incomplete_value": false,
      "site": "00418358",
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
            "const:a40:8"
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
      "definition_site": "0043ae6c",
      "incomplete_value": true,
      "site": "0043ae78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:760:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041836c",
      "incomplete_value": true,
      "site": "00418378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
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
      "definition_site": "0043ae68",
      "incomplete_value": false,
      "site": "0043ae78",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418368",
      "incomplete_value": false,
      "site": "00418378",
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
            "const:a18:8"
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
      16,
      "READ",
      [
        "storage",
        "00c24a40",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00c24a40",
        null,
        "undefined1"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00c24a18",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "00ca4500",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00ca4500",
        null,
        "undefined1"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00418340 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00418344 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0043ae40 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043ae44 ["COPY", "tmp:0:8", ["const:500:8"]]
- 00418350 ["COPY", "register:4000:8", ["const:c24000:8"]]
- 00418354 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0043ae50 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 0043ae54 ["COPY", "tmp:0:8", ["const:500:8"]]
- 00418358 ["INT_ADD", "register:40f0:8", ["const:418358:8", "const:4:8"]]
+ 0043ae58 ["INT_ADD", "register:40f0:8", ["const:43ae58:8", "const:4:8"]]
~~~


### [`004183ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md) → [`0043aeec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043aeec.md) Java_jp_co_ponos_battlecats_MyActivity_appInit

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0053c5e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5e8.md) [`00547c90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md) [`00acba34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba34.md) [`00acc348`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc348.md) [`00accf90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0055f480`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f480.md) [`0056ab28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) [`00b2b4c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4c4.md) [`00b2bdd8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md) [`00b2ca20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043af30",
      "incomplete_value": false,
      "site": "0043af3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418430",
      "incomplete_value": false,
      "site": "0041843c",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043af54",
      "incomplete_value": false,
      "site": "0043af54",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418454",
      "incomplete_value": false,
      "site": "00418454",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043af54",
      "incomplete_value": false,
      "site": "0043af54",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:510:8"
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
      "definition_site": "00418454",
      "incomplete_value": false,
      "site": "00418454",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:a50:8"
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
      20,
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "00be5fe8",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00c24a58",
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
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "00c62ba8",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00ca4518",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 004183fc ["COPY", "register:40b0:8", ["const:c24000:8"]]
- 00418400 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a50:8"]]
+ 0043aefc ["COPY", "register:40b0:8", ["const:ca4000:8"]]
+ 0043af00 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:510:8"]]
- 00418418 ["INT_ADD", "register:40f0:8", ["const:418418:8", "const:4:8"]]
+ 0043af18 ["INT_ADD", "register:40f0:8", ["const:43af18:8", "const:4:8"]]
- 0041841c ["INT_ADD", "register:40f0:8", ["const:41841c:8", "const:4:8"]]
+ 0043af1c ["INT_ADD", "register:40f0:8", ["const:43af1c:8", "const:4:8"]]
~~~


### [`004184bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004184bc.md) → [`0043afbc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043afbc.md) Java_jp_co_ponos_battlecats_MyActivity_appUpdateDraw

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0053257c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053257c.md) [`0056cb70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md) [`00acba3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba3c.md) [`00acd468`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd468.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00555414`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555414.md) [`0058fa08`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md) [`00b2b4cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md) [`00b2cf0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cf0c.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b028",
      "incomplete_value": true,
      "site": "0043b028",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418528",
      "incomplete_value": true,
      "site": "00418528",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b088",
      "incomplete_value": true,
      "site": "0043b088",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418588",
      "incomplete_value": true,
      "site": "00418588",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0043b01c",
      "value": [
        "leaf",
        "ram:b2cf0c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0041851c",
      "value": [
        "leaf",
        "ram:acd468:8"
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
      44,
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined1"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00c24a60",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      44,
      "READ",
      [
        "storage",
        "00ca4528",
        null,
        "undefined1"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00ca4520",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 004184d4 ["COPY", "register:40a8:8", ["const:c24000:8"]]
+ 0043afd4 ["COPY", "register:40a8:8", ["const:ca4000:8"]]
- 004184e0 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 004184e4 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 0043afe0 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043afe4 ["COPY", "tmp:0:8", ["const:528:8"]]
- 004184f0 ["INT_ADD", "register:40f0:8", ["const:4184f0:8", "const:4:8"]]
+ 0043aff0 ["INT_ADD", "register:40f0:8", ["const:43aff0:8", "const:4:8"]]
~~~


### [`004185a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004185a8.md) → [`0043b0a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b0a8.md) Java_jp_co_ponos_battlecats_MyActivity_gfxInit

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`004186bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004186bc.md) [`0056c8a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c8a4.md) [`0056f4d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f4d8.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043b1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b1bc.md) [`0058f73c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f73c.md) [`00592370`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592370.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b0f0",
      "incomplete_value": false,
      "site": "0043b0f0",
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
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004185f0",
      "incomplete_value": false,
      "site": "004185f0",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0043b0f4",
      "incomplete_value": true,
      "site": "0043b0f4",
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
      "definition_site": "004185f4",
      "incomplete_value": true,
      "site": "004185f4",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043b154",
      "incomplete_value": true,
      "site": "0043b158",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418654",
      "incomplete_value": true,
      "site": "00418658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a70:8"
              ]
            ]
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
      36,
      "READ",
      [
        "storage",
        "00c24a80",
        null,
        "undefined1"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "WRITE",
      [
        "storage",
        "00c24a70",
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
        "00ca4540",
        null,
        "undefined1"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00ca4538",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "WRITE",
      [
        "storage",
        "00ca4530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 004185c4 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 004185c8 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 0043b0c4 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b0c8 ["COPY", "tmp:0:8", ["const:540:8"]]
- 004185d8 ["INT_ADD", "register:40f0:8", ["const:4185d8:8", "const:4:8"]]
+ 0043b0d8 ["INT_ADD", "register:40f0:8", ["const:43b0d8:8", "const:4:8"]]
- 004185dc ["COPY", "register:4040:8", ["const:c24000:8"]]
- 004185e0 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 0043b0dc ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b0e0 ["COPY", "tmp:0:8", ["const:530:8"]]
~~~


### [`0041870c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041870c.md) → [`0043b20c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b20c.md) Java_jp_co_ponos_battlecats_MyActivity_getDrawableWidth

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b214",
      "incomplete_value": true,
      "site": "0043b218",
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
      "definition_site": "00418714",
      "incomplete_value": true,
      "site": "00418718",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "READ",
      [
        "storage",
        "00c24dc8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      8,
      "READ",
      [
        "storage",
        "00ca4888",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041870c ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00418710 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0043b20c ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b210 ["COPY", "tmp:0:8", ["const:870:8"]]
~~~


### [`0041871c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041871c.md) → [`0043b21c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b21c.md) Java_jp_co_ponos_battlecats_MyActivity_getDrawableHeight

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b224",
      "incomplete_value": true,
      "site": "0043b228",
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
      "definition_site": "00418724",
      "incomplete_value": true,
      "site": "00418728",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "READ",
      [
        "storage",
        "00c24dcc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      8,
      "READ",
      [
        "storage",
        "00ca488c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041871c ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00418720 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0043b21c ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b220 ["COPY", "tmp:0:8", ["const:870:8"]]
~~~


### [`0041872c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041872c.md) → [`0043b22c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b22c.md) Java_jp_co_ponos_battlecats_MyActivity_getWindowWidth

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b234",
      "incomplete_value": true,
      "site": "0043b238",
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
      "definition_site": "00418734",
      "incomplete_value": true,
      "site": "00418738",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "READ",
      [
        "storage",
        "00c24db8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      8,
      "READ",
      [
        "storage",
        "00ca4878",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041872c ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00418730 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0043b22c ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b230 ["COPY", "tmp:0:8", ["const:870:8"]]
~~~


### [`0041873c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041873c.md) → [`0043b23c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b23c.md) Java_jp_co_ponos_battlecats_MyActivity_getWindowHeight

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b244",
      "incomplete_value": true,
      "site": "0043b248",
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
      "definition_site": "00418744",
      "incomplete_value": true,
      "site": "00418748",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "READ",
      [
        "storage",
        "00c24dbc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      8,
      "READ",
      [
        "storage",
        "00ca487c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041873c ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00418740 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0043b23c ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b240 ["COPY", "tmp:0:8", ["const:870:8"]]
~~~


### [`0041874c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041874c.md) → [`0043b24c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b24c.md) Java_jp_co_ponos_battlecats_MyActivity_getSizeWidth

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b254",
      "incomplete_value": true,
      "site": "0043b258",
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
      "definition_site": "00418754",
      "incomplete_value": true,
      "site": "00418758",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "READ",
      [
        "storage",
        "00c24dc0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      8,
      "READ",
      [
        "storage",
        "00ca4880",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041874c ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00418750 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0043b24c ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b250 ["COPY", "tmp:0:8", ["const:870:8"]]
~~~


### [`0041875c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041875c.md) → [`0043b25c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b25c.md) Java_jp_co_ponos_battlecats_MyActivity_getSizeHeight

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b264",
      "incomplete_value": true,
      "site": "0043b268",
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
      "definition_site": "00418764",
      "incomplete_value": true,
      "site": "00418768",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "READ",
      [
        "storage",
        "00c24dc4",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      8,
      "READ",
      [
        "storage",
        "00ca4884",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041875c ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00418760 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0043b25c ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b260 ["COPY", "tmp:0:8", ["const:870:8"]]
~~~


### [`0041876c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041876c.md) → [`0043b26c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b26c.md) Java_jp_co_ponos_battlecats_MyActivity_gfxResize

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056cb70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md) [`00accf90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058fa08`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md) [`00b2ca20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md)

変更の種類 branch_value, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b2c8",
      "incomplete_value": true,
      "site": "0043b2c8",
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
            "const:2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004187c8",
      "incomplete_value": true,
      "site": "004187c8",
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
            "const:2c:8"
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
      "definition_site": "0043b2c8",
      "incomplete_value": true,
      "site": "0043b2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:2c:8"
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
      "definition_site": "004187c8",
      "incomplete_value": true,
      "site": "004187c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:2c:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b2f4",
      "incomplete_value": true,
      "site": "0043b2f4",
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
            "const:2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004187f4",
      "incomplete_value": true,
      "site": "004187f4",
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
            "const:2c:8"
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
      24,
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00c2659c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      24,
      "READ",
      [
        "storage",
        "00c9a770",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "READ",
      [
        "storage",
        "00c9a778",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00ca605c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418778 ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 0041877c ["COPY", "register:4048:8", ["const:c1a000:8"]]
- 00418780 ["COPY", "register:4050:8", ["const:c1a000:8"]]
- 00418784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 0043b278 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0043b27c ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 0043b280 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 0043b284 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:770:8"]]
- 00418788 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d88:8"]]
+ 0043b288 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
- 00418798 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d90:8"]]
+ 0043b298 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:780:8"]]
~~~


### [`00418828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md) → [`0043b328`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b328.md) Java_jp_co_ponos_battlecats_MyActivity_appTouch

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00acd390`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd390.md) [`00acd3d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd3d8.md) [`00acd420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd420.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b2ce34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce34.md) [`00b2ce7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce7c.md) [`00b2cec4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cec4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b3d0",
      "incomplete_value": true,
      "site": "0043b3d0",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004188d0",
      "incomplete_value": true,
      "site": "004188d0",
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
            "const:a88:8"
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
      "definition_site": "0043b3d4",
      "incomplete_value": true,
      "site": "0043b3d4",
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
            "const:54c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004188d4",
      "incomplete_value": true,
      "site": "004188d4",
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
            "const:a8c:8"
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
      "definition_site": "0043b374",
      "incomplete_value": true,
      "site": "0043b37c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
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
    "old": {
      "definition_site": "00418874",
      "incomplete_value": true,
      "site": "0041887c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a50:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      76,
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      76,
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "00ca4548",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418848 ["COPY", "register:4098:8", ["const:c24000:8"]]
- 0041884c ["COPY", "register:40a0:8", ["const:c24000:8"]]
+ 0043b348 ["COPY", "register:4098:8", ["const:ca4000:8"]]
+ 0043b34c ["COPY", "register:40a0:8", ["const:ca4000:8"]]
- 00418868 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043b368 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00418874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
+ 0043b374 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:510:8"]]
~~~


### [`004188e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004188e8.md) → [`0043b3e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b3e8.md) Java_jp_co_ponos_battlecats_MyActivity_appKey

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00566a7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00acbd78`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd78.md) [`00acbd7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd7c.md) [`00acd38c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd38c.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00589914`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00b2b808`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b808.md) [`00b2b80c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b80c.md) [`00b2ce30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "site": "0043b4c4",
      "value": [
        "leaf",
        "ram:b2b80c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004189c4",
      "value": [
        "leaf",
        "ram:acbd7c:8"
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
      "site": "0043b4ec",
      "value": [
        "leaf",
        "ram:b2ce30:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004189ec",
      "value": [
        "leaf",
        "ram:acd38c:8"
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
      60,
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      140,
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      60,
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      140,
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418920 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00418924 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
+ 0043b420 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b424 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:510:8"]]
- 00418954 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043b454 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00418960 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
+ 0043b460 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:510:8"]]
~~~


### [`00418b18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md) → [`0043b618`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b618.md) Java_jp_co_ponos_battlecats_MyActivity_kill

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00acbd14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd14.md) [`00acc56c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc56c.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b2b7a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md) [`00b2bffc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bffc.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043b630",
      "incomplete_value": true,
      "site": "0043b634",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
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
    "old": {
      "definition_site": "00418b30",
      "incomplete_value": true,
      "site": "00418b34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a50:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00c24a58",
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
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00ca4518",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418b24 ["COPY", "register:40a0:8", ["const:c24000:8"]]
- 00418b28 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0043b624 ["COPY", "register:40a0:8", ["const:ca4000:8"]]
+ 0043b628 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00418b34 ["INT_ADD", "register:40f0:8", ["const:418b34:8", "const:4:8"]]
+ 0043b634 ["INT_ADD", "register:40f0:8", ["const:43b634:8", "const:4:8"]]
- 00418b3c ["INT_ADD", "register:40f0:8", ["const:418b3c:8", "const:4:8"]]
+ 0043b63c ["INT_ADD", "register:40f0:8", ["const:43b63c:8", "const:4:8"]]
~~~


### [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) → [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) FUN_0043b724

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 272件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 272件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043d73c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440c0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440c0c.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0043b734",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00418c34",
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
      "definition_site": "0043b730",
      "incomplete_value": false,
      "site": "0043b734",
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
            "const:ee3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418c30",
      "incomplete_value": false,
      "site": "00418c34",
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
            "const:24c:8"
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
        "002a924c",
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
        "002b9ee3",
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
- 00418c2c ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00418c30 ["COPY", "tmp:0:8", ["const:24c:8"]]
+ 0043b72c ["COPY", "register:4000:8", ["const:2b9000:8"]]
+ 0043b730 ["COPY", "tmp:0:8", ["const:ee3:8"]]
- 00418c34 ["INT_ADD", "register:40f0:8", ["const:418c34:8", "const:4:8"]]
- 00418c34 ["CALL", null, ["ram:418c38:8"]]
+ 0043b734 ["INT_ADD", "register:40f0:8", ["const:43b734:8", "const:4:8"]]
+ 0043b734 ["CALL", null, ["ram:43b738:8"]]
~~~


### [`00419294`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419294.md) → [`0043bd94`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd94.md) _INIT_4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418394`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418394.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043ae94`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae94.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043bdd0",
      "incomplete_value": true,
      "site": "0043bdec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004192d0",
      "incomplete_value": true,
      "site": "004192ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "0043bdf4",
      "incomplete_value": true,
      "site": "0043be10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004192f4",
      "incomplete_value": true,
      "site": "00419310",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043be14",
      "incomplete_value": true,
      "site": "0043be30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00419314",
      "incomplete_value": true,
      "site": "00419330",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 15,
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
- 004192bc ["COPY", "register:4098:8", ["const:c24000:8"]]
- 004192c0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0043bdbc ["COPY", "register:4098:8", ["const:ca4000:8"]]
+ 0043bdc0 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 004192c8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 004192cc ["COPY", "tmp:0:8", ["const:377:8"]]
+ 0043bdc8 ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 0043bdcc ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 004192e4 ["COPY", "register:4050:8", ["const:2a7000:8"]]
- 004192e8 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 0043bde4 ["COPY", "register:4050:8", ["const:2b7000:8"]]
+ 0043bde8 ["COPY", "tmp:0:8", ["const:ef9:8"]]
~~~


### [`00419640`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419640.md) → [`0043c140`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c140.md) _INIT_5

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041969c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/0041969c.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043c19c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c19c.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043c15c",
      "incomplete_value": false,
      "site": "0043c160",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041965c",
      "incomplete_value": false,
      "site": "00419660",
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
            "const:ab0:8"
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
      "definition_site": "0043c16c",
      "incomplete_value": false,
      "site": "0043c180",
      "value": [
        "leaf",
        "const:43c19c:8"
      ]
    },
    "old": {
      "definition_site": "0041966c",
      "incomplete_value": false,
      "site": "00419680",
      "value": [
        "leaf",
        "const:41969c:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043c174",
      "incomplete_value": false,
      "site": "0043c180",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00419674",
      "incomplete_value": false,
      "site": "00419680",
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
      16,
      "READ",
      [
        "storage",
        "00c24ab0",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00c24ab0",
        null,
        "undefined1"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "0041969c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "00ca4570",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00ca4570",
        null,
        "undefined1"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "0043c19c",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00419648 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 0041964c ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 0043c148 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043c14c ["COPY", "tmp:0:8", ["const:570:8"]]
- 00419658 ["COPY", "register:4000:8", ["const:c24000:8"]]
- 0041965c ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 0043c158 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 0043c15c ["COPY", "tmp:0:8", ["const:570:8"]]
- 00419660 ["INT_ADD", "register:40f0:8", ["const:419660:8", "const:4:8"]]
+ 0043c160 ["INT_ADD", "register:40f0:8", ["const:43c160:8", "const:4:8"]]
~~~


### [`004196bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/004196bc.md) → [`0043c1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c1bc.md) _INIT_6

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041969c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/0041969c.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043c19c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c19c.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043c1d8",
      "incomplete_value": false,
      "site": "0043c1dc",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004196d8",
      "incomplete_value": false,
      "site": "004196dc",
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
            "const:ac0:8"
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
      "definition_site": "0043c1e8",
      "incomplete_value": false,
      "site": "0043c1fc",
      "value": [
        "leaf",
        "const:43c19c:8"
      ]
    },
    "old": {
      "definition_site": "004196e8",
      "incomplete_value": false,
      "site": "004196fc",
      "value": [
        "leaf",
        "const:41969c:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043c1f0",
      "incomplete_value": false,
      "site": "0043c1fc",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004196f0",
      "incomplete_value": false,
      "site": "004196fc",
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
      16,
      "READ",
      [
        "storage",
        "00c24ac0",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00c24ac0",
        null,
        "undefined1"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "0041969c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "00ca4580",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00ca4580",
        null,
        "undefined1"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "0043c19c",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 004196c4 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 004196c8 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0043c1c4 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043c1c8 ["COPY", "tmp:0:8", ["const:580:8"]]
- 004196d4 ["COPY", "register:4000:8", ["const:c24000:8"]]
- 004196d8 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0043c1d4 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 0043c1d8 ["COPY", "tmp:0:8", ["const:580:8"]]
- 004196dc ["INT_ADD", "register:40f0:8", ["const:4196dc:8", "const:4:8"]]
+ 0043c1dc ["INT_ADD", "register:40f0:8", ["const:43c1dc:8", "const:4:8"]]
~~~


### [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) → [`0043c218`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) FUN_0043c218

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00420580`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420580.md) [`00420858`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420858.md) · 呼出先 49件 [`0041aa74`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041aa74.md) [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`0041ba38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md)
- 新版 呼出元 2件 [`00443080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443080.md) [`00443358`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443358.md) · 呼出先 49件 [`0043d574`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d574.md) [`0043d73c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`0043db64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0043df70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`0043e538`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e538.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 22件, `call_target` 6件, `store_condition` 1件, `store_destination` 7件, `store_value` 10件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c3a0",
      "incomplete_value": true,
      "site": "0043c3a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004198a0",
      "incomplete_value": true,
      "site": "004198a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c484",
      "incomplete_value": false,
      "site": "0043c484",
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
                "const:c65000:8"
              ],
              [
                "leaf",
                "const:130:8"
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
      "definition_site": "00419984",
      "incomplete_value": false,
      "site": "00419984",
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
                "const:be8000:8"
              ],
              [
                "leaf",
                "const:570:8"
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c5c0",
      "incomplete_value": true,
      "site": "0043c5c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:6e3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00419ac0",
      "incomplete_value": true,
      "site": "00419ac0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:66b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      148,
      "PARAM",
      [
        "storage",
        "002af87e",
        null,
        "string"
      ]
    ],
    [
      204,
      "PARAM",
      [
        "storage",
        "002a9259",
        null,
        null
      ]
    ],
    [
      376,
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      148,
      "PARAM",
      [
        "storage",
        "002c0ea2",
        null,
        "string"
      ]
    ],
    [
      204,
      "PARAM",
      [
        "storage",
        "002b9ef0",
        null,
        null
      ]
    ],
    [
      376,
      "READ",
      [
        "storage",
        "002a7500",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00419768 ["INT_ADD", "register:40f0:8", ["const:419768:8", "const:4:8"]]
+ 0043c268 ["INT_ADD", "register:40f0:8", ["const:43c268:8", "const:4:8"]]
- 00419770 ["INT_ADD", "register:40f0:8", ["const:419770:8", "const:4:8"]]
+ 0043c270 ["INT_ADD", "register:40f0:8", ["const:43c270:8", "const:4:8"]]
- 00419788 ["INT_ADD", "register:40f0:8", ["const:419788:8", "const:4:8"]]
+ 0043c288 ["INT_ADD", "register:40f0:8", ["const:43c288:8", "const:4:8"]]
~~~


### [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) → [`0043d73c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) FUN_0043d73c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) · 呼出先 13件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`0046517c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046517c.md) [`004652a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004652a0.md)
- 新版 呼出元 2件 [`0043c218`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043ec20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) · 呼出先 13件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440c0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440c0c.md) [`00487de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488014`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488014.md) [`00488138`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043d9d8",
      "incomplete_value": true,
      "site": "0043d9dc",
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
      "definition_site": "0041aed8",
      "incomplete_value": true,
      "site": "0041aedc",
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
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043d9d4",
      "incomplete_value": true,
      "site": "0043d9e0",
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
      "definition_site": "0041aed4",
      "incomplete_value": true,
      "site": "0041aee0",
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043d9ec",
      "incomplete_value": true,
      "site": "0043d9ec",
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
                "const:48:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "0041aeec",
      "incomplete_value": true,
      "site": "0041aeec",
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
                "const:48:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      652,
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      656,
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      664,
      "READ",
      [
        "storage",
        "00c13458",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      652,
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      656,
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      664,
      "READ",
      [
        "storage",
        "00c92e00",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041ac6c ["INT_ADD", "register:40f0:8", ["const:41ac6c:8", "const:4:8"]]
+ 0043d76c ["INT_ADD", "register:40f0:8", ["const:43d76c:8", "const:4:8"]]
- 0041ac78 ["INT_ADD", "register:40f0:8", ["const:41ac78:8", "const:4:8"]]
+ 0043d778 ["INT_ADD", "register:40f0:8", ["const:43d778:8", "const:4:8"]]
- 0041aca4 ["INT_ADD", "register:40f0:8", ["const:41aca4:8", "const:4:8"]]
+ 0043d7a4 ["INT_ADD", "register:40f0:8", ["const:43d7a4:8", "const:4:8"]]
~~~


### [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) → [`0043db64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) FUN_0043db64

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 39件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`00421b40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) · 呼出先 6件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 39件 [`0043c218`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043df70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`0043ec20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f8dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00444640`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444640.md) · 呼出先 6件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043dd14",
      "incomplete_value": false,
      "site": "0043dd1c",
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
            "const:276:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b214",
      "incomplete_value": false,
      "site": "0041b21c",
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
            "const:83d:8"
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
      432,
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      432,
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0041b0fc ["INT_ADD", "register:40f0:8", ["const:41b0fc:8", "const:4:8"]]
+ 0043dbfc ["INT_ADD", "register:40f0:8", ["const:43dbfc:8", "const:4:8"]]
- 0041b14c ["INT_ADD", "register:40f0:8", ["const:41b14c:8", "const:4:8"]]
+ 0043dc4c ["INT_ADD", "register:40f0:8", ["const:43dc4c:8", "const:4:8"]]
- 0041b1d8 ["INT_ADD", "register:40f0:8", ["const:41b1d8:8", "const:4:8"]]
+ 0043dcd8 ["INT_ADD", "register:40f0:8", ["const:43dcd8:8", "const:4:8"]]
~~~


### [`0041b338`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b338.md) → [`0043de38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043de38.md) FUN_0043de38

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045fc34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045fc34.md) · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00482acc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) · 呼出先 3件 [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043de54",
      "incomplete_value": true,
      "site": "0043de58",
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
      "definition_site": "0041b354",
      "incomplete_value": true,
      "site": "0041b358",
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
      20,
      "READ",
      [
        "storage",
        "00c1adb8",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00be8580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9a7a8",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c65140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041b344 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0043de44 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0041b34c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
+ 0043de4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7a8:8"]]
- 0041b368 ["INT_ADD", "register:40f0:8", ["const:41b368:8", "const:4:8"]]
+ 0043de68 ["INT_ADD", "register:40f0:8", ["const:43de68:8", "const:4:8"]]
~~~


### [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) → [`0043df70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) FUN_0043df70

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) · 呼出先 20件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00420674`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420674.md) [`00420678`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420678.md) [`00420704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420704.md) [`00420708`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420708.md)
- 新版 呼出元 2件 [`0043c218`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043ec20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) · 呼出先 20件 [`0043db64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00443174`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443174.md) [`00443178`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443178.md) [`00443204`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443204.md) [`00443208`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443208.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043e164",
      "incomplete_value": false,
      "site": "0043e164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b664",
      "incomplete_value": false,
      "site": "0041b664",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043e188",
      "incomplete_value": false,
      "site": "0043e188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b688",
      "incomplete_value": false,
      "site": "0041b688",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043e19c",
      "incomplete_value": false,
      "site": "0043e19c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b69c",
      "incomplete_value": false,
      "site": "0041b69c",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00428cb4"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "0029583f",
        null,
        "undefined4"
      ]
    ],
    [
      128,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073ab94"
      ]
    ]
  ],
  "added": [
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b804"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "002a5278",
        null,
        "undefined4"
      ]
    ],
    [
      128,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041b49c ["INT_ADD", "register:40f0:8", ["const:41b49c:8", "const:4:8"]]
- 0041b49c ["CALL", null, ["ram:428cb4:8"]]
+ 0043df9c ["INT_ADD", "register:40f0:8", ["const:43df9c:8", "const:4:8"]]
+ 0043df9c ["CALL", null, ["ram:44b804:8"]]
- 0041b4a4 ["INT_ADD", "register:40f0:8", ["const:41b4a4:8", "const:4:8"]]
+ 0043dfa4 ["INT_ADD", "register:40f0:8", ["const:43dfa4:8", "const:4:8"]]
- 0041b4b8 ["INT_ADD", "register:40f0:8", ["const:41b4b8:8", "const:4:8"]]
+ 0043dfb8 ["INT_ADD", "register:40f0:8", ["const:43dfb8:8", "const:4:8"]]
~~~


### [`0041ba38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md) → [`0043e538`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e538.md) FUN_0043e538

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) · 呼出先 11件 [`004203a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203a4.md) [`004203a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203a8.md) [`00420430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420430.md) [`00420434`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420434.md) [`00420578`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420578.md)
- 新版 呼出元 1件 [`0043c218`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) · 呼出先 11件 [`00442ea4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442ea4.md) [`00442ea8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442ea8.md) [`00442f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442f30.md) [`00442f34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442f34.md) [`00443078`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443078.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043e5f0",
      "incomplete_value": false,
      "site": "0043e5f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041baf0",
      "incomplete_value": false,
      "site": "0041baf0",
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
            "const:c8:8"
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
      "definition_site": "0043e614",
      "incomplete_value": false,
      "site": "0043e614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bb14",
      "incomplete_value": false,
      "site": "0041bb14",
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
            "const:158:8"
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
      "definition_site": "0043e628",
      "incomplete_value": false,
      "site": "0043e628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bb28",
      "incomplete_value": false,
      "site": "0041bb28",
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
            "const:1e8:8"
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
      48,
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00c25e10",
        null,
        "undefined1"
      ]
    ],
    [
      184,
      "DATA",
      [
        "storage",
        "00be60c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00c9a7c8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00ca58d0",
        null,
        "undefined1"
      ]
    ],
    [
      184,
      "DATA",
      [
        "storage",
        "00c62c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041ba54 ["COPY", "register:4000:8", ["const:c1a000:8"]]
+ 0043e554 ["COPY", "register:4000:8", ["const:c9a000:8"]]
- 0041ba68 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:dd8:8"]]
+ 0043e568 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7c8:8"]]
- 0041ba6c ["INT_ADD", "register:40f0:8", ["const:41ba6c:8", "const:4:8"]]
+ 0043e56c ["INT_ADD", "register:40f0:8", ["const:43e56c:8", "const:4:8"]]
~~~


### [`0041be0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) → [`0043e90c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) FUN_0043e90c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 38件 [`0060468c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/0060468c.md) [`00651720`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651720.md) [`006584d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) [`0068d484`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) [`00695904`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 5件 [`0041be9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be9c.md) [`0041bf20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 38件 [`0062a184`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a184.md) [`00677a00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) [`0067e7b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006b37cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b37cc.md) [`006bbc58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 5件 [`0043e99c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e99c.md) [`0043ea20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ea20.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043e940",
      "incomplete_value": false,
      "site": "0043e944",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041be40",
      "incomplete_value": false,
      "site": "0041be44",
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
            "const:b20:8"
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
      "definition_site": "0043e950",
      "incomplete_value": false,
      "site": "0043e954",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041be50",
      "incomplete_value": false,
      "site": "0041be54",
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
            "const:ac8:8"
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
      "definition_site": "0043e95c",
      "incomplete_value": false,
      "site": "0043e970",
      "value": [
        "leaf",
        "const:43e99c:8"
      ]
    },
    "old": {
      "definition_site": "0041be5c",
      "incomplete_value": false,
      "site": "0041be70",
      "value": [
        "leaf",
        "const:41be9c:8"
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
      20,
      "READ",
      [
        "storage",
        "00c24b20",
        null,
        "undefined1"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c24ac8",
        null,
        null
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "00c24b20",
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
        "00ca45e0",
        null,
        "undefined1"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00ca4588",
        null,
        null
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "00ca45e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041be18 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 0041be1c ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 0043e918 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043e91c ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 0041be28 ["COPY", "register:4000:8", ["const:c24000:8"]]
- 0041be2c ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 0043e928 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 0043e92c ["COPY", "tmp:0:8", ["const:588:8"]]
- 0041be3c ["COPY", "register:4000:8", ["const:c24000:8"]]
- 0041be40 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 0043e93c ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 0043e940 ["COPY", "tmp:0:8", ["const:5e0:8"]]
~~~


### [`0041bf20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md) → [`0043ea20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ea20.md) FUN_0043ea20

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041be0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`00420940`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420940.md) · 呼出先 4件 [`00ad3bf8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3bf8.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`0043c218`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043e90c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`00443440`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443440.md) · 呼出先 4件 [`00b336b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b336b0.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043ea8c",
      "incomplete_value": true,
      "site": "0043ea98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bf8c",
      "incomplete_value": true,
      "site": "0041bf98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:300:8"
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
      "definition_site": "0043ea88",
      "incomplete_value": true,
      "site": "0043ea9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:62c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bf88",
      "incomplete_value": true,
      "site": "0041bf9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a7:8"
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
      "definition_site": "0043ea88",
      "incomplete_value": true,
      "site": "0043ea9c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0041bf88",
      "incomplete_value": true,
      "site": "0041bf9c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      104,
      "READ",
      [
        "storage",
        "0029e2a7",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "0029e2b7",
        null,
        "string"
      ]
    ],
    [
      108,
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
      104,
      "READ",
      [
        "storage",
        "002ae62c",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "002ae63c",
        null,
        "string"
      ]
    ],
    [
      108,
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


~~~diff
- 0041bf78 ["INT_ADD", "register:40f0:8", ["const:41bf78:8", "const:4:8"]]
+ 0043ea78 ["INT_ADD", "register:40f0:8", ["const:43ea78:8", "const:4:8"]]
- 0041bf7c ["COPY", "register:4040:8", ["const:29e000:8"]]
- 0041bf80 ["COPY", "tmp:0:8", ["const:2a7:8"]]
+ 0043ea7c ["COPY", "register:4040:8", ["const:2ae000:8"]]
+ 0043ea80 ["COPY", "tmp:0:8", ["const:62c:8"]]
- 0041bf84 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0043ea84 ["COPY", "register:4048:8", ["const:2c2000:8"]]
~~~


### [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) → [`0043ec20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) FUN_0043ec20

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0073496c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`0081fa64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00821350`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) [`0084c390`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) [`0084f35c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f35c.md) · 呼出先 24件 [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`00428d08`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428d08.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md)
- 新版 呼出元 9件 [`0075eb40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`008519cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`008532c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/008532c8.md) [`0087f328`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`008822f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008822f4.md) · 呼出先 24件 [`0043d73c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`0043db64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0043df70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`0044b858`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b858.md) [`004813f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043eecc",
      "incomplete_value": true,
      "site": "0043eed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041c3cc",
      "incomplete_value": true,
      "site": "0041c3d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0043efa8",
      "value": [
        "leaf",
        "ram:482acc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0041c4a8",
      "value": [
        "leaf",
        "ram:45fc34:8"
      ]
    },
    "ordinal": 35,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043f134",
      "incomplete_value": false,
      "site": "0043f13c",
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
            "const:5a5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041c634",
      "incomplete_value": false,
      "site": "0041c63c",
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
            "const:37f:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      328,
      "READ",
      [
        "storage",
        "00c1adb8",
        null,
        "pointer"
      ]
    ],
    [
      388,
      "PARAM",
      [
        "storage",
        "002af87e",
        null,
        "string"
      ]
    ],
    [
      436,
      "PARAM",
      [
        "storage",
        "002a9259",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      328,
      "READ",
      [
        "storage",
        "00c9a7a8",
        null,
        "pointer"
      ]
    ],
    [
      388,
      "PARAM",
      [
        "storage",
        "002c0ea2",
        null,
        "string"
      ]
    ],
    [
      436,
      "PARAM",
      [
        "storage",
        "002b9ef0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0041c15c ["INT_ADD", "register:40f0:8", ["const:41c15c:8", "const:4:8"]]
+ 0043ec5c ["INT_ADD", "register:40f0:8", ["const:43ec5c:8", "const:4:8"]]
- 0041c170 ["INT_ADD", "register:40f0:8", ["const:41c170:8", "const:4:8"]]
+ 0043ec70 ["INT_ADD", "register:40f0:8", ["const:43ec70:8", "const:4:8"]]
- 0041c180 ["INT_ADD", "register:40f0:8", ["const:41c180:8", "const:4:8"]]
+ 0043ec80 ["INT_ADD", "register:40f0:8", ["const:43ec80:8", "const:4:8"]]
~~~


### [`0041c8f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) → [`0043f3f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) FUN_0043f3f8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 25件 [`0060468c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/0060468c.md) [`00651720`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651720.md) [`006584d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) [`0068d484`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) [`00695904`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 4件 [`00420b98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b98.md) [`00420b9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b9c.md) [`00ad3e98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3e98.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 25件 [`0062a184`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a184.md) [`00677a00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) [`0067e7b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006b37cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b37cc.md) [`006bbc58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 4件 [`00443698`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443698.md) [`0044369c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044369c.md) [`00b33950`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33950.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043f424",
      "incomplete_value": false,
      "site": "0043f42c",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041c924",
      "incomplete_value": false,
      "site": "0041c92c",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
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
        "00be6518",
        null,
        "undefined *"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00be6538",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00be6540",
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
        "00c630d8",
        null,
        "undefined *"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c630f8",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c63100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041c920 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 0041c924 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0043f420 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0043f424 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0041c938 ["INT_ADD", "register:40f0:8", ["const:41c938:8", "const:4:8"]]
+ 0043f438 ["INT_ADD", "register:40f0:8", ["const:43f438:8", "const:4:8"]]
- 0041c964 ["INT_ADD", "register:40f0:8", ["const:41c964:8", "const:4:8"]]
+ 0043f464 ["INT_ADD", "register:40f0:8", ["const:43f464:8", "const:4:8"]]
~~~


### [`0041c9f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c9f4.md) → [`0043f4f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f4f4.md) FUN_0043f4f4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00acc56c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc56c.md) · 呼出先 4件 [`00420b98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b98.md) [`00420b9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b9c.md) [`00ad3e98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3e98.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00b2bffc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bffc.md) · 呼出先 4件 [`00443698`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443698.md) [`0044369c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044369c.md) [`00b33950`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33950.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043f514",
      "incomplete_value": false,
      "site": "0043f524",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041ca14",
      "incomplete_value": false,
      "site": "0041ca24",
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
            "const:518:8"
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
      48,
      "DATA",
      [
        "storage",
        "00be6518",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00be6538",
        null,
        "pointer"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00be6540",
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
        "00c630d8",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00c630f8",
        null,
        "pointer"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00c63100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041ca10 ["COPY", "register:4048:8", ["const:be6000:8"]]
- 0041ca14 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0043f510 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0043f514 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0041ca30 ["INT_ADD", "register:40f0:8", ["const:41ca30:8", "const:4:8"]]
+ 0043f530 ["INT_ADD", "register:40f0:8", ["const:43f530:8", "const:4:8"]]
- 0041ca5c ["INT_ADD", "register:40f0:8", ["const:41ca5c:8", "const:4:8"]]
+ 0043f55c ["INT_ADD", "register:40f0:8", ["const:43f55c:8", "const:4:8"]]
~~~


### [`0041cad8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cad8.md) → [`0043f5d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f5d8.md) FUN_0043f5d8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0041c8ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8ec.md) · 呼出先 6件 [`00420938`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420938.md) [`0042093c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042093c.md) [`00420b18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b18.md) [`00420b1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b1c.md) [`00ad3bfc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3bfc.md)
- 新版 呼出元 1件 [`0043f3ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3ec.md) · 呼出先 6件 [`00443438`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443438.md) [`0044343c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044343c.md) [`00443618`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443618.md) [`0044361c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044361c.md) [`00b336b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b336b4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043f5f8",
      "incomplete_value": false,
      "site": "0043f61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041caf8",
      "incomplete_value": false,
      "site": "0041cb1c",
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
            "const:3f8:8"
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
      "definition_site": "0043f614",
      "incomplete_value": false,
      "site": "0043f620",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041cb14",
      "incomplete_value": false,
      "site": "0041cb20",
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
            "const:488:8"
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
      "definition_site": "0043f62c",
      "incomplete_value": false,
      "site": "0043f640",
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
            "const:62c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041cb2c",
      "incomplete_value": false,
      "site": "0041cb40",
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
            "const:2a7:8"
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
      68,
      "DATA",
      [
        "storage",
        "00be63f8",
        null,
        "undefined *"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00be6488",
        null,
        "undefined *"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "0029e2a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      68,
      "DATA",
      [
        "storage",
        "00c62fb8",
        null,
        "undefined *"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00c63048",
        null,
        "undefined *"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "002ae62c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041caf4 ["COPY", "register:4048:8", ["const:be6000:8"]]
- 0041caf8 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 0043f5f4 ["COPY", "register:4048:8", ["const:c62000:8"]]
+ 0043f5f8 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0041cb10 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 0041cb14 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 0043f610 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0043f614 ["COPY", "tmp:0:8", ["const:48:8"]]
- 0041cb28 ["COPY", "register:4018:8", ["const:29e000:8"]]
- 0041cb2c ["COPY", "tmp:0:8", ["const:2a7:8"]]
+ 0043f628 ["COPY", "register:4018:8", ["const:2ae000:8"]]
+ 0043f62c ["COPY", "tmp:0:8", ["const:62c:8"]]
~~~


### [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) → [`0043f8dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) FUN_0043f8dc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a2ba68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2ba68.md) [`00ab1dc8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1dc8.md) · 呼出先 23件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00420bd8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bd8.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md)
- 新版 呼出元 2件 [`00a898d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a89/00a898d8.md) [`00b11858`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11858.md) · 呼出先 23件 [`0043db64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`004436d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004436d8.md) [`004813f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043fa60",
      "incomplete_value": true,
      "site": "0043fa60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041cf60",
      "incomplete_value": true,
      "site": "0041cf60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043fdb4",
      "incomplete_value": true,
      "site": "0043fdc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041d2b4",
      "incomplete_value": true,
      "site": "0041d2c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:900:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043fec8",
      "incomplete_value": true,
      "site": "0043fed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041d3c8",
      "incomplete_value": true,
      "site": "0041d3d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 84,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      108,
      "PARAM",
      [
        "storage",
        "002a9259",
        null,
        null
      ]
    ],
    [
      372,
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ],
    [
      696,
      "READ",
      [
        "storage",
        "00294539",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      108,
      "PARAM",
      [
        "storage",
        "002b9ef0",
        null,
        null
      ]
    ],
    [
      372,
      "READ",
      [
        "storage",
        "002a7500",
        null,
        "string"
      ]
    ],
    [
      696,
      "READ",
      [
        "storage",
        "002a3e4f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041ce14 ["INT_ADD", "register:40f0:8", ["const:41ce14:8", "const:4:8"]]
+ 0043f914 ["INT_ADD", "register:40f0:8", ["const:43f914:8", "const:4:8"]]
- 0041ce1c ["INT_ADD", "register:40f0:8", ["const:41ce1c:8", "const:4:8"]]
+ 0043f91c ["INT_ADD", "register:40f0:8", ["const:43f91c:8", "const:4:8"]]
- 0041ce40 ["INT_ADD", "register:40f0:8", ["const:41ce40:8", "const:4:8"]]
+ 0043f940 ["INT_ADD", "register:40f0:8", ["const:43f940:8", "const:4:8"]]
~~~


### [`0041e03c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e03c.md) → [`00440b3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440b3c.md) FUN_00440b3c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00692224`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/00692224.md) [`007da86c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da86c.md) [`007e5fa4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 4件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)
- 新版 呼出元 4件 [`006b8578`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8578.md) [`0080f0e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080f0e8.md) [`0081a7d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00440b6c",
      "incomplete_value": true,
      "site": "00440b74",
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
      "definition_site": "0041e06c",
      "incomplete_value": true,
      "site": "0041e074",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00440b78",
      "incomplete_value": true,
      "site": "00440b78",
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
      "definition_site": "0041e078",
      "incomplete_value": true,
      "site": "0041e078",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00440b88",
      "incomplete_value": true,
      "site": "00440b88",
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
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "0041e088",
      "incomplete_value": true,
      "site": "0041e088",
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
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
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
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c13458",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c92e00",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041e04c ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 0041e050 ["COPY", "register:40b0:8", ["const:c1a000:8"]]
+ 00440b4c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00440b50 ["COPY", "register:40b0:8", ["const:c9a000:8"]]
- 0041e058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00440b58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7b0:8"]]
- 0041e05c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:dc8:8"]]
+ 00440b5c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:7b8:8"]]
~~~


### [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) → [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) FUN_00440e80

根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 535件 [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`00439bc0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439bc0.md) [`0043aca0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aca0.md) [`0043ec60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043ec60.md) · 呼出先 4件 [`00bbad34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb1e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1e0.md)
- 新版 呼出元 573件 [`0043f8dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00440c0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440c0c.md) [`0045ca58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ca58.md) [`0045db38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045db38.md) [`00461af8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461af8.md) · 呼出先 4件 [`00c3777c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57c30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00440ea8",
      "incomplete_value": true,
      "site": "00440eb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041e3a8",
      "incomplete_value": true,
      "site": "0041e3b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
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
      "definition_site": "00440eac",
      "incomplete_value": true,
      "site": "00440eb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041e3ac",
      "incomplete_value": true,
      "site": "0041e3b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "00c16908",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c1ade8",
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
        "00c9a7d0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "00c962b0",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c9a7d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041e390 ["INT_ADD", "register:40f0:8", ["const:41e390:8", "const:4:8"]]
+ 00440e90 ["INT_ADD", "register:40f0:8", ["const:440e90:8", "const:4:8"]]
- 0041e398 ["INT_ADD", "register:40f0:8", ["const:41e398:8", "const:4:8"]]
+ 00440e98 ["INT_ADD", "register:40f0:8", ["const:440e98:8", "const:4:8"]]
- 0041e39c ["COPY", "register:4008:8", ["const:c1a000:8"]]
- 0041e3a0 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 00440e9c ["COPY", "register:4008:8", ["const:c9a000:8"]]
+ 00440ea0 ["COPY", "register:4010:8", ["const:c9a000:8"]]
~~~


### [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) → [`00440f1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) FUN_00440f1c

根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 43件 [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004629d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/004629d4.md) [`0049100c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/0049100c.md) [`0049b54c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049b54c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 42件 [`00440c0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440c0c.md) [`00473500`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`0048586c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048586c.md) [`004b3ea4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md) [`004be3e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004be3e4.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00440f2c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0041e42c",
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
      "definition_site": "00440f28",
      "incomplete_value": false,
      "site": "00440f2c",
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
      "definition_site": "0041e428",
      "incomplete_value": false,
      "site": "0041e42c",
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
- 0041e424 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 0041e428 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00440f24 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00440f28 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0041e42c ["INT_ADD", "register:40f0:8", ["const:41e42c:8", "const:4:8"]]
- 0041e42c ["CALL", null, ["ram:418c38:8"]]
+ 00440f2c ["INT_ADD", "register:40f0:8", ["const:440f2c:8", "const:4:8"]]
+ 00440f2c ["CALL", null, ["ram:43b738:8"]]
~~~


### [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) → [`00441278`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md) FUN_00441278

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0041e650`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e650.md) [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) [`005f1af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1af0.md) [`005f5668`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f5/005f5668.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md)
- 新版 呼出元 4件 [`00441150`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441150.md) [`00441278`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md) [`00617330`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617330.md) [`0061aeb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061aeb8.md) · 呼出先 21件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441278`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004413e8",
      "incomplete_value": false,
      "site": "004413f0",
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
            "const:f13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041e8e8",
      "incomplete_value": false,
      "site": "0041e8f0",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004414a0",
      "incomplete_value": false,
      "site": "004414a8",
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
            "const:da7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041e9a0",
      "incomplete_value": false,
      "site": "0041e9a8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004414bc",
      "incomplete_value": false,
      "site": "004414c8",
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
            "const:ea9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041e9bc",
      "incomplete_value": false,
      "site": "0041e9c8",
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
      368,
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      552,
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      580,
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      368,
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      552,
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      580,
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041e7f4 ["INT_ADD", "register:40f0:8", ["const:41e7f4:8", "const:4:8"]]
+ 004412f4 ["INT_ADD", "register:40f0:8", ["const:4412f4:8", "const:4:8"]]
- 0041e878 ["INT_ADD", "register:40f0:8", ["const:41e878:8", "const:4:8"]]
+ 00441378 ["INT_ADD", "register:40f0:8", ["const:441378:8", "const:4:8"]]
- 0041e8e4 ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 0041e8e8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 004413e4 ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 004413e8 ["COPY", "tmp:0:8", ["const:f13:8"]]
~~~


### [`0041f3d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md) → [`00441ed4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441ed4.md) FUN_00441ed4

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) [`0041f3d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md) [`0045a988`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a988.md) [`0046ff30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`00710214`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710214.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 7件 [`00441278`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md) [`00441ed4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441ed4.md) [`0047d820`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md) [`00492dc8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`0073a314`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a314.md) · 呼出先 21件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044203c",
      "incomplete_value": false,
      "site": "00442044",
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
            "const:f13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041f53c",
      "incomplete_value": false,
      "site": "0041f544",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004420f4",
      "incomplete_value": false,
      "site": "004420fc",
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
            "const:da7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041f5f4",
      "incomplete_value": false,
      "site": "0041f5fc",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00442110",
      "incomplete_value": false,
      "site": "0044211c",
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
            "const:ea9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041f610",
      "incomplete_value": false,
      "site": "0041f61c",
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
      360,
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      544,
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      572,
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      360,
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      544,
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      572,
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041f44c ["INT_ADD", "register:40f0:8", ["const:41f44c:8", "const:4:8"]]
+ 00441f4c ["INT_ADD", "register:40f0:8", ["const:441f4c:8", "const:4:8"]]
- 0041f4d0 ["INT_ADD", "register:40f0:8", ["const:41f4d0:8", "const:4:8"]]
+ 00441fd0 ["INT_ADD", "register:40f0:8", ["const:441fd0:8", "const:4:8"]]
- 0041f538 ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 0041f53c ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00442038 ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 0044203c ["COPY", "tmp:0:8", ["const:f13:8"]]
~~~


### [`0041fddc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) → [`004428dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) FUN_004428dc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 130件 [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) [`0041f280`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f280.md) [`0041f354`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`0041f3d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md) [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) · 呼出先 1件 [`0041fdf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 129件 [`00441278`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md) [`00441d80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441d80.md) [`00441e54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`00441ed4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441ed4.md) [`00446d80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d80.md) · 呼出先 1件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "004428ec",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0041fdec",
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
      "definition_site": "004428e8",
      "incomplete_value": false,
      "site": "004428ec",
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
            "const:ee3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041fde8",
      "incomplete_value": false,
      "site": "0041fdec",
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
            "const:24c:8"
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
        "002a924c",
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
        "002b9ee3",
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
- 0041fde4 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 0041fde8 ["COPY", "tmp:0:8", ["const:24c:8"]]
+ 004428e4 ["COPY", "register:4000:8", ["const:2b9000:8"]]
+ 004428e8 ["COPY", "tmp:0:8", ["const:ee3:8"]]
- 0041fdec ["INT_ADD", "register:40f0:8", ["const:41fdec:8", "const:4:8"]]
- 0041fdec ["CALL", null, ["ram:41fdf0:8"]]
+ 004428ec ["INT_ADD", "register:40f0:8", ["const:4428ec:8", "const:4:8"]]
+ 004428ec ["CALL", null, ["ram:4428f0:8"]]
~~~


### [`00420234`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420234.md) → [`00442d34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442d34.md) FUN_00442d34

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
      "definition_site": "00442d48",
      "incomplete_value": false,
      "site": "00442d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420248",
      "incomplete_value": false,
      "site": "0042024c",
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
            "const:38:8"
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
        "00be6038",
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
        "00c62bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420240 ["INT_ADD", "register:40f0:8", ["const:420240:8", "const:4:8"]]
+ 00442d40 ["INT_ADD", "register:40f0:8", ["const:442d40:8", "const:4:8"]]
- 00420244 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00420248 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00442d44 ["COPY", "register:4040:8", ["const:c62000:8"]]
+ 00442d48 ["COPY", "tmp:0:8", ["const:bf8:8"]]
~~~


### [`00420258`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420258.md) → [`00442d58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442d58.md) FUN_00442d58

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
      "definition_site": "00442d5c",
      "incomplete_value": false,
      "site": "00442d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042025c",
      "incomplete_value": false,
      "site": "00420260",
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
            "const:38:8"
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
        "00be6038",
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
        "00c62bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420258 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 0042025c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00442d58 ["COPY", "register:4040:8", ["const:c62000:8"]]
+ 00442d5c ["COPY", "tmp:0:8", ["const:bf8:8"]]
~~~


### [`0042035c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042035c.md) → [`00442e5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442e5c.md) FUN_00442e5c

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
      "definition_site": "00442e80",
      "incomplete_value": false,
      "site": "00442e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420380",
      "incomplete_value": false,
      "site": "00420380",
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
            "const:c8:8"
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
        "00be60c8",
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
        "00c62c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420370 ["INT_ADD", "register:40f0:8", ["const:420370:8", "const:4:8"]]
+ 00442e70 ["INT_ADD", "register:40f0:8", ["const:442e70:8", "const:4:8"]]
- 00420378 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 0042037c ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00442e78 ["COPY", "register:4040:8", ["const:c62000:8"]]
+ 00442e7c ["COPY", "tmp:0:8", ["const:c88:8"]]
~~~


### [`00420390`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420390.md) → [`00442e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442e90.md) FUN_00442e90

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
      "definition_site": "00442e9c",
      "incomplete_value": false,
      "site": "00442e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042039c",
      "incomplete_value": false,
      "site": "0042039c",
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
            "const:c8:8"
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
        "00be60c8",
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
        "00c62c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420394 ["COPY", "register:4048:8", ["const:be6000:8"]]
- 00420398 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00442e94 ["COPY", "register:4048:8", ["const:c62000:8"]]
+ 00442e98 ["COPY", "tmp:0:8", ["const:c88:8"]]
~~~


### [`004203e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203e8.md) → [`00442ee8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442ee8.md) FUN_00442ee8

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
      "definition_site": "00442f0c",
      "incomplete_value": false,
      "site": "00442f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042040c",
      "incomplete_value": false,
      "site": "0042040c",
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
            "const:158:8"
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
        "00be6158",
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
        "00c62d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 004203fc ["INT_ADD", "register:40f0:8", ["const:4203fc:8", "const:4:8"]]
+ 00442efc ["INT_ADD", "register:40f0:8", ["const:442efc:8", "const:4:8"]]
- 00420404 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00420408 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00442f04 ["COPY", "register:4040:8", ["const:c62000:8"]]
+ 00442f08 ["COPY", "tmp:0:8", ["const:d18:8"]]
~~~


### [`0042041c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042041c.md) → [`00442f1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442f1c.md) FUN_00442f1c

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
      "definition_site": "00442f28",
      "incomplete_value": false,
      "site": "00442f28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420428",
      "incomplete_value": false,
      "site": "00420428",
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
            "const:158:8"
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
        "00be6158",
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
        "00c62d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420420 ["COPY", "register:4048:8", ["const:be6000:8"]]
- 00420424 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00442f20 ["COPY", "register:4048:8", ["const:c62000:8"]]
+ 00442f24 ["COPY", "tmp:0:8", ["const:d18:8"]]
~~~


### [`00420530`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420530.md) → [`00443030`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443030.md) FUN_00443030

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
      "definition_site": "00443054",
      "incomplete_value": false,
      "site": "00443054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420554",
      "incomplete_value": false,
      "site": "00420554",
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
            "const:1e8:8"
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
        "00be61e8",
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
        "00c62da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420544 ["INT_ADD", "register:40f0:8", ["const:420544:8", "const:4:8"]]
+ 00443044 ["INT_ADD", "register:40f0:8", ["const:443044:8", "const:4:8"]]
- 0042054c ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00420550 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 0044304c ["COPY", "register:4040:8", ["const:c62000:8"]]
+ 00443050 ["COPY", "tmp:0:8", ["const:da8:8"]]
~~~


### [`00420564`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420564.md) → [`00443064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443064.md) FUN_00443064

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
      "definition_site": "00443070",
      "incomplete_value": false,
      "site": "00443070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420570",
      "incomplete_value": false,
      "site": "00420570",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00be61e8",
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
        "00c62da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420568 ["COPY", "register:4048:8", ["const:be6000:8"]]
- 0042056c ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 00443068 ["COPY", "register:4048:8", ["const:c62000:8"]]
+ 0044306c ["COPY", "tmp:0:8", ["const:da8:8"]]
~~~


### [`0042062c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042062c.md) → [`0044312c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044312c.md) FUN_0044312c

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
      "definition_site": "00443150",
      "incomplete_value": false,
      "site": "00443150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420650",
      "incomplete_value": false,
      "site": "00420650",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "DATA",
      [
        "storage",
        "00be6278",
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
        "00c62e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420640 ["INT_ADD", "register:40f0:8", ["const:420640:8", "const:4:8"]]
+ 00443140 ["INT_ADD", "register:40f0:8", ["const:443140:8", "const:4:8"]]
- 00420648 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 0042064c ["COPY", "tmp:0:8", ["const:278:8"]]
+ 00443148 ["COPY", "register:4040:8", ["const:c62000:8"]]
+ 0044314c ["COPY", "tmp:0:8", ["const:e38:8"]]
~~~


### [`00420660`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420660.md) → [`00443160`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443160.md) FUN_00443160

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
      "definition_site": "0044316c",
      "incomplete_value": false,
      "site": "0044316c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042066c",
      "incomplete_value": false,
      "site": "0042066c",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00be6278",
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
        "00c62e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420664 ["COPY", "register:4048:8", ["const:be6000:8"]]
- 00420668 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 00443164 ["COPY", "register:4048:8", ["const:c62000:8"]]
+ 00443168 ["COPY", "tmp:0:8", ["const:e38:8"]]
~~~


### [`004206bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206bc.md) → [`004431bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004431bc.md) FUN_004431bc

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
      "definition_site": "004431e0",
      "incomplete_value": false,
      "site": "004431e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004206e0",
      "incomplete_value": false,
      "site": "004206e0",
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
            "const:2f8:8"
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
        "00be62f8",
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
        "00c62eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 004206d0 ["INT_ADD", "register:40f0:8", ["const:4206d0:8", "const:4:8"]]
+ 004431d0 ["INT_ADD", "register:40f0:8", ["const:4431d0:8", "const:4:8"]]
- 004206d8 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 004206dc ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 004431d8 ["COPY", "register:4040:8", ["const:c62000:8"]]
+ 004431dc ["COPY", "tmp:0:8", ["const:eb8:8"]]
~~~


### [`004206f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206f0.md) → [`004431f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004431f0.md) FUN_004431f0

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
      "definition_site": "004431fc",
      "incomplete_value": false,
      "site": "004431fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004206fc",
      "incomplete_value": false,
      "site": "004206fc",
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
            "const:2f8:8"
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
        "00be62f8",
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
        "00c62eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 004206f4 ["COPY", "register:4048:8", ["const:be6000:8"]]
- 004206f8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 004431f4 ["COPY", "register:4048:8", ["const:c62000:8"]]
+ 004431f8 ["COPY", "tmp:0:8", ["const:eb8:8"]]
~~~


### [`00420808`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420808.md) → [`00443308`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443308.md) FUN_00443308

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
      "definition_site": "0044332c",
      "incomplete_value": false,
      "site": "0044332c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042082c",
      "incomplete_value": false,
      "site": "0042082c",
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
            "const:378:8"
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
        "00be6378",
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
        "00c62f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0042081c ["INT_ADD", "register:40f0:8", ["const:42081c:8", "const:4:8"]]
+ 0044331c ["INT_ADD", "register:40f0:8", ["const:44331c:8", "const:4:8"]]
- 00420824 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00420828 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00443324 ["COPY", "register:4040:8", ["const:c62000:8"]]
+ 00443328 ["COPY", "tmp:0:8", ["const:f38:8"]]
~~~


### [`0042083c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042083c.md) → [`0044333c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044333c.md) FUN_0044333c

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
      "definition_site": "00443348",
      "incomplete_value": false,
      "site": "00443348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420848",
      "incomplete_value": false,
      "site": "00420848",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00be6378",
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
        "00c62f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420840 ["COPY", "register:4048:8", ["const:be6000:8"]]
- 00420844 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00443340 ["COPY", "register:4048:8", ["const:c62000:8"]]
+ 00443344 ["COPY", "tmp:0:8", ["const:f38:8"]]
~~~


### [`00420904`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420904.md) → [`00443404`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443404.md) FUN_00443404

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
      "definition_site": "00443418",
      "incomplete_value": false,
      "site": "0044341c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420918",
      "incomplete_value": false,
      "site": "0042091c",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00be63f8",
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
        "00c62fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420910 ["INT_ADD", "register:40f0:8", ["const:420910:8", "const:4:8"]]
+ 00443410 ["INT_ADD", "register:40f0:8", ["const:443410:8", "const:4:8"]]
- 00420914 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00420918 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00443414 ["COPY", "register:4040:8", ["const:c62000:8"]]
+ 00443418 ["COPY", "tmp:0:8", ["const:fb8:8"]]
~~~


### [`00420928`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420928.md) → [`00443428`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443428.md) FUN_00443428

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
      "definition_site": "0044342c",
      "incomplete_value": false,
      "site": "00443430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042092c",
      "incomplete_value": false,
      "site": "00420930",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00be63f8",
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
        "00c62fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420928 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 0042092c ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00443428 ["COPY", "register:4040:8", ["const:c62000:8"]]
+ 0044342c ["COPY", "tmp:0:8", ["const:fb8:8"]]
~~~


### [`00420940`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420940.md) → [`00443440`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443440.md) FUN_00443440

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041be9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be9c.md) [`0041bf20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043e99c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e99c.md) [`0043ea20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ea20.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004434d4",
      "incomplete_value": false,
      "site": "004434d4",
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
            "const:5bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004209d4",
      "incomplete_value": false,
      "site": "004209d4",
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
            "const:afc:8"
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
      "definition_site": "004434fc",
      "incomplete_value": false,
      "site": "00443500",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004209fc",
      "incomplete_value": false,
      "site": "00420a00",
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
            "const:b20:8"
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
      "definition_site": "0044350c",
      "incomplete_value": false,
      "site": "00443510",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420a0c",
      "incomplete_value": false,
      "site": "00420a10",
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
            "const:ac8:8"
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
      80,
      "READ",
      [
        "storage",
        "00c24b20",
        null,
        "undefined1"
      ]
    ],
    [
      132,
      "READ",
      [
        "storage",
        "00c24b20",
        null,
        "undefined1"
      ]
    ],
    [
      148,
      "WRITE",
      [
        "storage",
        "00c24afc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      80,
      "READ",
      [
        "storage",
        "00ca45e0",
        null,
        "undefined1"
      ]
    ],
    [
      132,
      "READ",
      [
        "storage",
        "00ca45e0",
        null,
        "undefined1"
      ]
    ],
    [
      148,
      "WRITE",
      [
        "storage",
        "00ca45bc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420988 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 0042098c ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 00443488 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0044348c ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 004209a8 ["INT_ADD", "register:40f0:8", ["const:4209a8:8", "const:4:8"]]
+ 004434a8 ["INT_ADD", "register:40f0:8", ["const:4434a8:8", "const:4:8"]]
- 004209b8 ["INT_ADD", "register:40f0:8", ["const:4209b8:8", "const:4:8"]]
+ 004434b8 ["INT_ADD", "register:40f0:8", ["const:4434b8:8", "const:4:8"]]
~~~


### [`00420ae4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ae4.md) → [`004435e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004435e4.md) FUN_004435e4

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
      "definition_site": "004435f8",
      "incomplete_value": false,
      "site": "004435fc",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420af8",
      "incomplete_value": false,
      "site": "00420afc",
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
            "const:488:8"
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
        "00be6488",
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
        "00c63048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420af0 ["INT_ADD", "register:40f0:8", ["const:420af0:8", "const:4:8"]]
+ 004435f0 ["INT_ADD", "register:40f0:8", ["const:4435f0:8", "const:4:8"]]
- 00420af4 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00420af8 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 004435f4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004435f8 ["COPY", "tmp:0:8", ["const:48:8"]]
~~~


### [`00420b08`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b08.md) → [`00443608`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443608.md) FUN_00443608

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
      "definition_site": "0044360c",
      "incomplete_value": false,
      "site": "00443610",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b0c",
      "incomplete_value": false,
      "site": "00420b10",
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00be6488",
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
        "00c63048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420b08 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00420b0c ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00443608 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044360c ["COPY", "tmp:0:8", ["const:48:8"]]
~~~


### [`00420b20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b20.md) → [`00443620`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443620.md) FUN_00443620

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044362c",
      "incomplete_value": true,
      "site": "0044362c",
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
            "const:44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b2c",
      "incomplete_value": true,
      "site": "00420b2c",
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
            "const:44:8"
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
      8,
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      12,
      "WRITE",
      [
        "storage",
        "00c24df4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      8,
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      12,
      "WRITE",
      [
        "storage",
        "00ca48b4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420b20 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00443620 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00420b28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d78:8"]]
+ 00443628 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:768:8"]]
~~~


### [`00420b64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b64.md) → [`00443664`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443664.md) FUN_00443664

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
      "definition_site": "00443678",
      "incomplete_value": false,
      "site": "0044367c",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b78",
      "incomplete_value": false,
      "site": "00420b7c",
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
            "const:518:8"
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
        "00be6518",
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
        "00c630d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420b70 ["INT_ADD", "register:40f0:8", ["const:420b70:8", "const:4:8"]]
+ 00443670 ["INT_ADD", "register:40f0:8", ["const:443670:8", "const:4:8"]]
- 00420b74 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00420b78 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00443674 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00443678 ["COPY", "tmp:0:8", ["const:d8:8"]]
~~~


### [`00420b88`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b88.md) → [`00443688`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443688.md) FUN_00443688

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
      "definition_site": "0044368c",
      "incomplete_value": false,
      "site": "00443690",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b8c",
      "incomplete_value": false,
      "site": "00420b90",
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
            "const:518:8"
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
        "00be6518",
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
        "00c630d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420b88 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00420b8c ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00443688 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044368c ["COPY", "tmp:0:8", ["const:d8:8"]]
~~~


### [`00420ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ba0.md) → [`004436a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004436a0.md) FUN_004436a0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004436a8",
      "incomplete_value": false,
      "site": "004436a8",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:870:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420ba8",
      "incomplete_value": false,
      "site": "00420ba8",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:db0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:44:8"
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
      8,
      "WRITE",
      [
        "storage",
        "00c24df4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      8,
      "WRITE",
      [
        "storage",
        "00ca48b4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420ba0 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00420ba4 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 004436a0 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 004436a4 ["COPY", "tmp:0:8", ["const:870:8"]]
~~~


### [`00420bd8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bd8.md) → [`004436d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004436d8.md) FUN_004436d8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0043f8dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "004436e8",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00420be8",
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
      "definition_site": "004436e4",
      "incomplete_value": false,
      "site": "004436e8",
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
      "definition_site": "00420be4",
      "incomplete_value": false,
      "site": "00420be8",
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
- 00420be0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00420be4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 004436e0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 004436e4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00420be8 ["INT_ADD", "register:40f0:8", ["const:420be8:8", "const:4:8"]]
- 00420be8 ["CALL", null, ["ram:418c38:8"]]
+ 004436e8 ["INT_ADD", "register:40f0:8", ["const:4436e8:8", "const:4:8"]]
+ 004436e8 ["CALL", null, ["ram:43b738:8"]]
~~~


### [`00420bec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bec.md) → [`004436ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004436ec.md) _INIT_7

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00443728",
      "incomplete_value": true,
      "site": "00443744",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00420c28",
      "incomplete_value": true,
      "site": "00420c44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044374c",
      "incomplete_value": true,
      "site": "00443768",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00420c4c",
      "incomplete_value": true,
      "site": "00420c68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044376c",
      "incomplete_value": true,
      "site": "00443788",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420c6c",
      "incomplete_value": true,
      "site": "00420c88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 15,
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
- 00420c14 ["COPY", "register:4098:8", ["const:c24000:8"]]
- 00420c18 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 00443714 ["COPY", "register:4098:8", ["const:ca4000:8"]]
+ 00443718 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00420c20 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00420c24 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00443720 ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 00443724 ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 00420c3c ["COPY", "register:4050:8", ["const:2a7000:8"]]
- 00420c40 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 0044373c ["COPY", "register:4050:8", ["const:2b7000:8"]]
+ 00443740 ["COPY", "tmp:0:8", ["const:ef9:8"]]
~~~


### [`00420f7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420f7c.md) → [`00443a7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443a7c.md) _INIT_8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00443ab8",
      "incomplete_value": true,
      "site": "00443ad4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00420fb8",
      "incomplete_value": true,
      "site": "00420fd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "00443adc",
      "incomplete_value": true,
      "site": "00443af8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00420fdc",
      "incomplete_value": true,
      "site": "00420ff8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00443afc",
      "incomplete_value": true,
      "site": "00443b18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420ffc",
      "incomplete_value": true,
      "site": "00421018",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 15,
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
- 00420fa4 ["COPY", "register:4098:8", ["const:c24000:8"]]
- 00420fa8 ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 00443aa4 ["COPY", "register:4098:8", ["const:ca4000:8"]]
+ 00443aa8 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 00420fb0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00420fb4 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00443ab0 ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 00443ab4 ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 00420fcc ["COPY", "register:4050:8", ["const:2a7000:8"]]
- 00420fd0 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 00443acc ["COPY", "register:4050:8", ["const:2b7000:8"]]
+ 00443ad0 ["COPY", "tmp:0:8", ["const:ef9:8"]]
~~~


### [`0042130c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/0042130c.md) → [`00443e0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443e0c.md) FUN_00443e0c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00428010`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428010.md) · 呼出先 8件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 1件 [`0044ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab10.md) · 呼出先 8件 [`004445d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 22件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00443ed0",
      "incomplete_value": false,
      "site": "00443ed0",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004213d0",
      "incomplete_value": false,
      "site": "004213d0",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00443f08",
      "incomplete_value": false,
      "site": "00443f08",
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
            "const:634:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421408",
      "incomplete_value": false,
      "site": "00421408",
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
            "const:b74:8"
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
      "definition_site": "00443f5c",
      "incomplete_value": false,
      "site": "00443f5c",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
    "old": {
      "definition_site": "0042145c",
      "incomplete_value": false,
      "site": "0042145c",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 12,
    "slot": 1
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
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c24b60",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00ca4620",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00421328 ["COPY", "register:40b8:8", ["const:c24000:8"]]
- 0042132c ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 00443e28 ["COPY", "register:40b8:8", ["const:ca4000:8"]]
+ 00443e2c ["COPY", "tmp:0:8", ["const:648:8"]]
- 00421344 ["COPY", "register:40a0:8", ["const:c24000:8"]]
- 00421348 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b60:8"]]
+ 00443e44 ["COPY", "register:40a0:8", ["const:ca4000:8"]]
+ 00443e48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
- 0042135c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b60:8"]]
+ 00443e5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
~~~


### [`004215a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md) → [`004440a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004440a0.md) FUN_004440a0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0081f58c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) [`0084004c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/0084004c.md) [`008406e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md) [`00840b80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840b80.md) [`00844bd8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) · 呼出先 4件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 6件 [`008514c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`00872338`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872338.md) [`008729d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md) [`00872e6c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872e6c.md) [`00876ec4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 4件 [`004445d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004440f0",
      "incomplete_value": false,
      "site": "004440f0",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
    "old": {
      "definition_site": "004215f0",
      "incomplete_value": false,
      "site": "004215f0",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004440f4",
      "incomplete_value": false,
      "site": "004440f4",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "004215f4",
      "incomplete_value": false,
      "site": "004215f4",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004440f4",
      "incomplete_value": false,
      "site": "004440f4",
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
                "const:8:8"
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
      "definition_site": "004215f4",
      "incomplete_value": false,
      "site": "004215f4",
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
                "const:8:8"
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
      16,
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00c24b58",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00ca4618",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 004215a8 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 004215ac ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 004440a8 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 004440ac ["COPY", "tmp:0:8", ["const:648:8"]]
- 004215b8 ["COPY", "register:4000:8", ["const:c24000:8"]]
- 004215bc ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 004440b8 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 004440bc ["COPY", "tmp:0:8", ["const:618:8"]]
- 004215c8 ["COPY", "register:4000:8", ["const:c24000:8"]]
- 004215cc ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 004440c8 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 004440cc ["COPY", "tmp:0:8", ["const:648:8"]]
~~~


### [`00421614`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421614.md) → [`00444114`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444114.md) FUN_00444114

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00428080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md) · 呼出先 6件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0044ab80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab80.md) · 呼出先 6件 [`004445d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 29件, `call_target` 1件, `store_destination` 38件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444168",
      "incomplete_value": false,
      "site": "00444168",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421668",
      "incomplete_value": false,
      "site": "00421668",
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
            "const:b60:8"
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
      "definition_site": "00444168",
      "incomplete_value": false,
      "site": "00444168",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:620:8"
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
      "definition_site": "00421668",
      "incomplete_value": false,
      "site": "00421668",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b60:8"
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
      "definition_site": "004441ec",
      "incomplete_value": true,
      "site": "004441ec",
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
            "const:634:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004216ec",
      "incomplete_value": true,
      "site": "004216ec",
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
            "const:b74:8"
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
      20,
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c24b60",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00c24b88",
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
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00ca4620",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00421620 ["COPY", "register:40a0:8", ["const:c24000:8"]]
- 00421624 ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 00444120 ["COPY", "register:40a0:8", ["const:ca4000:8"]]
+ 00444124 ["COPY", "tmp:0:8", ["const:648:8"]]
- 00421630 ["COPY", "register:4098:8", ["const:c24000:8"]]
- 00421634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b60:8"]]
+ 00444130 ["COPY", "register:4098:8", ["const:ca4000:8"]]
+ 00444134 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00421644 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b60:8"]]
+ 00444144 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
~~~


### [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) → [`00444424`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444424.md) FUN_00444424

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) [`00428080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md) · 呼出先 10件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`00423ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423ad4.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 2件 [`004460ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004460ac.md) [`0044ab80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab80.md) · 呼出先 10件 [`004445d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00446298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446298.md) [`004465d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004465d4.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444580",
      "incomplete_value": false,
      "site": "00444580",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
    "old": {
      "definition_site": "00421a80",
      "incomplete_value": false,
      "site": "00421a80",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444584",
      "incomplete_value": false,
      "site": "00444584",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "00421a84",
      "incomplete_value": false,
      "site": "00421a84",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444584",
      "incomplete_value": false,
      "site": "00444584",
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
                "const:8:8"
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
      "definition_site": "00421a84",
      "incomplete_value": false,
      "site": "00421a84",
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
                "const:8:8"
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
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      208,
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      312,
      "PARAM",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      328,
      "PARAM",
      [
        "storage",
        "00c24b58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      208,
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      312,
      "PARAM",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      328,
      "PARAM",
      [
        "storage",
        "00ca4618",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00421954 ["INT_ADD", "register:40f0:8", ["const:421954:8", "const:4:8"]]
+ 00444454 ["INT_ADD", "register:40f0:8", ["const:444454:8", "const:4:8"]]
- 0042196c ["INT_ADD", "register:40f0:8", ["const:42196c:8", "const:4:8"]]
+ 0044446c ["INT_ADD", "register:40f0:8", ["const:44446c:8", "const:4:8"]]
- 00421984 ["INT_ADD", "register:40f0:8", ["const:421984:8", "const:4:8"]]
+ 00444484 ["INT_ADD", "register:40f0:8", ["const:444484:8", "const:4:8"]]
~~~


### [`00421b40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) → [`00444640`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444640.md) FUN_00444640

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084004c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/0084004c.md) · 呼出先 13件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00422098`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md) [`00424230`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424230.md) [`0052dd44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd44.md)
- 新版 呼出元 1件 [`00872338`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872338.md) · 呼出先 13件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00444b98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) [`00446d30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d30.md) [`00550bdc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bdc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004448cc",
      "incomplete_value": false,
      "site": "004448d0",
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
            "const:ef5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421dcc",
      "incomplete_value": false,
      "site": "00421dd0",
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
            "const:25e:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      652,
      "PARAM",
      [
        "storage",
        "002a925e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      652,
      "PARAM",
      [
        "storage",
        "002b9ef5",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00421b94 ["INT_ADD", "register:40f0:8", ["const:421b94:8", "const:4:8"]]
+ 00444694 ["INT_ADD", "register:40f0:8", ["const:444694:8", "const:4:8"]]
- 00421ba0 ["INT_ADD", "register:40f0:8", ["const:421ba0:8", "const:4:8"]]
+ 004446a0 ["INT_ADD", "register:40f0:8", ["const:4446a0:8", "const:4:8"]]
- 00421ba8 ["INT_ADD", "register:40f0:8", ["const:421ba8:8", "const:4:8"]]
+ 004446a8 ["INT_ADD", "register:40f0:8", ["const:4446a8:8", "const:4:8"]]
~~~


### [`00422098`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md) → [`00444b98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) FUN_00444b98

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00421b40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) · 呼出先 14件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0042818c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/0042818c.md) [`00464a54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)
- 新版 呼出元 4件 [`00444640`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444640.md) [`006e42d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e42d4.md) [`006ef704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ef/006ef704.md) [`006f2494`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 14件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0044ac8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ac8c.md) [`004878ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00444bd8",
      "incomplete_value": false,
      "site": "00444bdc",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004220d8",
      "incomplete_value": false,
      "site": "004220dc",
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
      "definition_site": "00444cf4",
      "incomplete_value": true,
      "site": "00444cf8",
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
      "definition_site": "004221f4",
      "incomplete_value": true,
      "site": "004221f8",
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00444cf0",
      "incomplete_value": true,
      "site": "00444cfc",
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
      "definition_site": "004221f0",
      "incomplete_value": true,
      "site": "004221fc",
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
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      68,
      "DATA",
      [
        "storage",
        "00be6598",
        null,
        "undefined *"
      ]
    ],
    [
      332,
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      336,
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      68,
      "DATA",
      [
        "storage",
        "00c63158",
        null,
        "undefined *"
      ]
    ],
    [
      332,
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      336,
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 004220d0 ["INT_ADD", "register:40f0:8", ["const:4220d0:8", "const:4:8"]]
+ 00444bd0 ["INT_ADD", "register:40f0:8", ["const:444bd0:8", "const:4:8"]]
- 004220d4 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 004220d8 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00444bd4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00444bd8 ["COPY", "tmp:0:8", ["const:158:8"]]
- 004220e8 ["INT_ADD", "register:40f0:8", ["const:4220e8:8", "const:4:8"]]
+ 00444be8 ["INT_ADD", "register:40f0:8", ["const:444be8:8", "const:4:8"]]
~~~


### [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) → [`00444de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) FUN_00444de0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008406e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md) [`00844bd8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) · 呼出先 42件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`00423878`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423878.md) [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md)
- 新版 呼出元 2件 [`008729d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md) [`00876ec4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 42件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004460ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004460ac.md) [`00446298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446298.md) [`00446378`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446378.md) [`00446d80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d80.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_destination` 1件, `store_value` 26件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00444e2c",
      "incomplete_value": false,
      "site": "00444e30",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042232c",
      "incomplete_value": false,
      "site": "00422330",
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
            "const:598:8"
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
      "definition_site": "00444e84",
      "incomplete_value": true,
      "site": "00444e88",
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
      "definition_site": "00422384",
      "incomplete_value": true,
      "site": "00422388",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00444e80",
      "incomplete_value": true,
      "site": "00444e8c",
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
      "definition_site": "00422380",
      "incomplete_value": true,
      "site": "0042238c",
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
    "ordinal": 17,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      80,
      "DATA",
      [
        "storage",
        "00be6598",
        null,
        "undefined *"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      152,
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      80,
      "DATA",
      [
        "storage",
        "00c63158",
        null,
        "undefined *"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      152,
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00422324 ["INT_ADD", "register:40f0:8", ["const:422324:8", "const:4:8"]]
+ 00444e24 ["INT_ADD", "register:40f0:8", ["const:444e24:8", "const:4:8"]]
- 00422328 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 0042232c ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00444e28 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00444e2c ["COPY", "tmp:0:8", ["const:158:8"]]
- 0042233c ["INT_ADD", "register:40f0:8", ["const:42233c:8", "const:4:8"]]
+ 00444e3c ["INT_ADD", "register:40f0:8", ["const:444e3c:8", "const:4:8"]]
~~~


### [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) → [`004460ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004460ac.md) FUN_004460ac

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) · 呼出先 11件 [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`0052dccc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00444de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) · 呼出先 11件 [`00444424`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444424.md) [`004445d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00446298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446298.md) [`00550b64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446168",
      "incomplete_value": false,
      "site": "00446168",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00423668",
      "incomplete_value": false,
      "site": "00423668",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044623c",
      "incomplete_value": false,
      "site": "0044623c",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
    "old": {
      "definition_site": "0042373c",
      "incomplete_value": false,
      "site": "0042373c",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446240",
      "incomplete_value": false,
      "site": "00446240",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "00423740",
      "incomplete_value": false,
      "site": "00423740",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      172,
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      188,
      "WRITE",
      [
        "storage",
        "00c24b70",
        null,
        "undefined4"
      ]
    ],
    [
      356,
      "PARAM",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      172,
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      188,
      "WRITE",
      [
        "storage",
        "00ca4630",
        null,
        "undefined4"
      ]
    ],
    [
      356,
      "PARAM",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 004235d4 ["INT_ADD", "register:40f0:8", ["const:4235d4:8", "const:4:8"]]
+ 004460d4 ["INT_ADD", "register:40f0:8", ["const:4460d4:8", "const:4:8"]]
- 004235e4 ["INT_ADD", "register:40f0:8", ["const:4235e4:8", "const:4:8"]]
+ 004460e4 ["INT_ADD", "register:40f0:8", ["const:4460e4:8", "const:4:8"]]
- 00423604 ["INT_ADD", "register:40f0:8", ["const:423604:8", "const:4:8"]]
+ 00446104 ["INT_ADD", "register:40f0:8", ["const:446104:8", "const:4:8"]]
~~~


### [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) → [`00446298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446298.md) FUN_00446298

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) [`00423bbc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md) · 呼出先 4件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0052dd5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd5c.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`00444424`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444424.md) [`00444de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`004460ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004460ac.md) [`004466bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004466bc.md) · 呼出先 4件 [`0043db64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00550bf4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf4.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004462e0",
      "incomplete_value": true,
      "site": "004462e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:991:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004237e0",
      "incomplete_value": true,
      "site": "004237e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd3:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "READ",
      [
        "storage",
        "00298bd3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      52,
      "READ",
      [
        "storage",
        "002a8991",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 004237bc ["INT_ADD", "register:40f0:8", ["const:4237bc:8", "const:4:8"]]
+ 004462bc ["INT_ADD", "register:40f0:8", ["const:4462bc:8", "const:4:8"]]
- 004237c0 ["COPY", "register:4048:8", ["const:298000:8"]]
- 004237c4 ["COPY", "tmp:0:8", ["const:bd3:8"]]
+ 004462c0 ["COPY", "register:4048:8", ["const:2a8000:8"]]
+ 004462c4 ["COPY", "tmp:0:8", ["const:991:8"]]
- 004237f4 ["INT_ADD", "register:40f0:8", ["const:4237f4:8", "const:4:8"]]
+ 004462f4 ["INT_ADD", "register:40f0:8", ["const:4462f4:8", "const:4:8"]]
~~~


### [`00423bbc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md) → [`004466bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004466bc.md) FUN_004466bc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00423fe4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe4.md) · 呼出先 16件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`004782e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md) [`0052dd44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd44.md) [`0052dd48`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd48.md)
- 新版 呼出元 1件 [`00446ae4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446ae4.md) · 呼出先 16件 [`004445d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00446298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446298.md) [`0049b17c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`00550bdc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bdc.md) [`00550be0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 20件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446880",
      "incomplete_value": false,
      "site": "00446880",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
    "old": {
      "definition_site": "00423d80",
      "incomplete_value": false,
      "site": "00423d80",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446884",
      "incomplete_value": false,
      "site": "00446884",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "00423d84",
      "incomplete_value": false,
      "site": "00423d84",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446884",
      "incomplete_value": false,
      "site": "00446884",
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
                "const:8:8"
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
      "definition_site": "00423d84",
      "incomplete_value": false,
      "site": "00423d84",
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
                "const:8:8"
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
      52,
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      124,
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      52,
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      124,
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00423be4 ["INT_ADD", "register:40f0:8", ["const:423be4:8", "const:4:8"]]
+ 004466e4 ["INT_ADD", "register:40f0:8", ["const:4466e4:8", "const:4:8"]]
- 00423be8 ["COPY", "register:40b8:8", ["const:c24000:8"]]
- 00423bec ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 004466e8 ["COPY", "register:40b8:8", ["const:ca4000:8"]]
+ 004466ec ["COPY", "tmp:0:8", ["const:648:8"]]
- 00423bfc ["INT_ADD", "register:40f0:8", ["const:423bfc:8", "const:4:8"]]
+ 004466fc ["INT_ADD", "register:40f0:8", ["const:4466fc:8", "const:4:8"]]
~~~


### [`00423f2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423f2c.md) → [`00446a2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446a2c.md) FUN_00446a2c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00446a5c",
      "incomplete_value": true,
      "site": "00446a64",
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
      "definition_site": "00423f5c",
      "incomplete_value": true,
      "site": "00423f64",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00446a68",
      "incomplete_value": true,
      "site": "00446a68",
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
      "definition_site": "00423f68",
      "incomplete_value": true,
      "site": "00423f68",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446a78",
      "incomplete_value": true,
      "site": "00446a78",
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
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "00423f78",
      "incomplete_value": true,
      "site": "00423f78",
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
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
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
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c13458",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c92e00",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00423f3c ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 00423f40 ["COPY", "register:40b0:8", ["const:c1a000:8"]]
+ 00446a3c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00446a40 ["COPY", "register:40b0:8", ["const:c9a000:8"]]
- 00423f48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00446a48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7b0:8"]]
- 00423f4c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:dc8:8"]]
+ 00446a4c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:7b8:8"]]
~~~


### [`00423fe8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe8.md) → [`00446ae8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446ae8.md) FUN_00446ae8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00423ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423ad4.md) · 呼出先 6件 [`004240ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/004240ec.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) [`00bdb2c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2c0.md)
- 新版 呼出元 1件 [`004465d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004465d4.md) · 呼出先 6件 [`00446bec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446bec.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d00.md) [`00c57d10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00446b4c",
      "incomplete_value": false,
      "site": "00446b58",
      "value": [
        "leaf",
        "const:446bec:8"
      ]
    },
    "old": {
      "definition_site": "0042404c",
      "incomplete_value": false,
      "site": "00424058",
      "value": [
        "leaf",
        "const:4240ec:8"
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00446b9c",
      "incomplete_value": false,
      "site": "00446ba0",
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
            "const:e5a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042409c",
      "incomplete_value": false,
      "site": "004240a0",
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
      100,
      "PARAM",
      [
        "storage",
        "004240ec",
        null,
        null
      ]
    ],
    [
      180,
      "PARAM",
      [
        "storage",
        "00294544",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "PARAM",
      [
        "storage",
        "00446bec",
        null,
        null
      ]
    ],
    [
      180,
      "PARAM",
      [
        "storage",
        "002a3e5a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0042401c ["INT_ADD", "register:40f0:8", ["const:42401c:8", "const:4:8"]]
+ 00446b1c ["INT_ADD", "register:40f0:8", ["const:446b1c:8", "const:4:8"]]
- 00424024 ["INT_ADD", "register:40f0:8", ["const:424024:8", "const:4:8"]]
+ 00446b24 ["INT_ADD", "register:40f0:8", ["const:446b24:8", "const:4:8"]]
- 00424030 ["INT_ADD", "register:40f0:8", ["const:424030:8", "const:4:8"]]
+ 00446b30 ["INT_ADD", "register:40f0:8", ["const:446b30:8", "const:4:8"]]
~~~


### [`004240ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/004240ec.md) → [`00446bec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446bec.md) FUN_00446bec

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00423fe8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe8.md) · 呼出先 5件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) [`00bdb2f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdb300`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb300.md)
- 新版 呼出元 1件 [`00446ae8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446ae8.md) · 呼出先 5件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57d40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c57d50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)

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
      "site": "00446c40",
      "value": [
        "leaf",
        "ram:c57d50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00424140",
      "value": [
        "leaf",
        "ram:bdb300:8"
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
      84,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb300"
      ]
    ]
  ],
  "added": [
    [
      84,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57d50"
      ]
    ]
  ]
}
~~~


~~~diff
- 00424114 ["INT_ADD", "register:40f0:8", ["const:424114:8", "const:4:8"]]
+ 00446c14 ["INT_ADD", "register:40f0:8", ["const:446c14:8", "const:4:8"]]
- 00424124 ["INT_ADD", "register:40f0:8", ["const:424124:8", "const:4:8"]]
+ 00446c24 ["INT_ADD", "register:40f0:8", ["const:446c24:8", "const:4:8"]]
- 0042412c ["INT_ADD", "register:40f0:8", ["const:42412c:8", "const:4:8"]]
+ 00446c2c ["INT_ADD", "register:40f0:8", ["const:446c2c:8", "const:4:8"]]
~~~


### [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) → [`00446d80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d80.md) FUN_00446d80

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) · 呼出先 23件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00444de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`00446d80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d80.md) · 呼出先 23件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00446ed4",
      "incomplete_value": false,
      "site": "00446edc",
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
            "const:f13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004243d4",
      "incomplete_value": false,
      "site": "004243dc",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00446f90",
      "incomplete_value": false,
      "site": "00446f98",
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
            "const:da7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00424490",
      "incomplete_value": false,
      "site": "00424498",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00446fa8",
      "incomplete_value": false,
      "site": "00446fb4",
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
            "const:ea9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004244a8",
      "incomplete_value": false,
      "site": "004244b4",
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
      340,
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      528,
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      552,
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      340,
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      528,
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      552,
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 004242fc ["INT_ADD", "register:40f0:8", ["const:4242fc:8", "const:4:8"]]
+ 00446dfc ["INT_ADD", "register:40f0:8", ["const:446dfc:8", "const:4:8"]]
- 00424370 ["INT_ADD", "register:40f0:8", ["const:424370:8", "const:4:8"]]
+ 00446e70 ["INT_ADD", "register:40f0:8", ["const:446e70:8", "const:4:8"]]
- 004243d0 ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 004243d4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00446ed0 ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 00446ed4 ["COPY", "tmp:0:8", ["const:f13:8"]]
~~~


### [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) → [`004476b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) FUN_004476b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 27件 [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004264e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) [`00426e8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) [`005be404`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 27件 [`00446d80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d80.md) [`004476b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00448fe8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/00448fe8.md) [`0044998c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/0044998c.md) [`005e30d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) · 呼出先 22件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00447808",
      "incomplete_value": false,
      "site": "00447810",
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
            "const:f13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00424d08",
      "incomplete_value": false,
      "site": "00424d10",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044782c",
      "incomplete_value": false,
      "site": "00447838",
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
            "const:ea9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00424d2c",
      "incomplete_value": false,
      "site": "00424d38",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00447960",
      "incomplete_value": false,
      "site": "00447968",
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
            "const:da7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00424e60",
      "incomplete_value": false,
      "site": "00424e68",
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
      340,
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      376,
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      684,
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      340,
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      376,
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      684,
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00424c30 ["INT_ADD", "register:40f0:8", ["const:424c30:8", "const:4:8"]]
+ 00447730 ["INT_ADD", "register:40f0:8", ["const:447730:8", "const:4:8"]]
- 00424ca4 ["INT_ADD", "register:40f0:8", ["const:424ca4:8", "const:4:8"]]
+ 004477a4 ["INT_ADD", "register:40f0:8", ["const:4477a4:8", "const:4:8"]]
- 00424d04 ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 00424d08 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00447804 ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 00447808 ["COPY", "tmp:0:8", ["const:f13:8"]]
~~~


### [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) → [`00447eb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) FUN_00447eb4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 170件 [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00458974`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458974.md) [`0059fbec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059fbec.md) [`005a45f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 177件 [`004476b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00447eb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047b80c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md) [`005c421c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md) [`005c8ebc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) · 呼出先 22件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00448004",
      "incomplete_value": false,
      "site": "0044800c",
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
            "const:f13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00425504",
      "incomplete_value": false,
      "site": "0042550c",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00448028",
      "incomplete_value": false,
      "site": "00448034",
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
            "const:ea9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00425528",
      "incomplete_value": false,
      "site": "00425534",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044815c",
      "incomplete_value": false,
      "site": "00448164",
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
            "const:da7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042565c",
      "incomplete_value": false,
      "site": "00425664",
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
      336,
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      372,
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      680,
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      336,
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      372,
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      680,
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0042542c ["INT_ADD", "register:40f0:8", ["const:42542c:8", "const:4:8"]]
+ 00447f2c ["INT_ADD", "register:40f0:8", ["const:447f2c:8", "const:4:8"]]
- 004254a0 ["INT_ADD", "register:40f0:8", ["const:4254a0:8", "const:4:8"]]
+ 00447fa0 ["INT_ADD", "register:40f0:8", ["const:447fa0:8", "const:4:8"]]
- 00425500 ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 00425504 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00448000 ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 00448004 ["COPY", "tmp:0:8", ["const:f13:8"]]
~~~


### [`00425ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md) → [`004486a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/004486a0.md) FUN_004486a0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00425ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md) · 呼出先 23件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00444de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`004486a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/004486a0.md) · 呼出先 23件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004487f8",
      "incomplete_value": false,
      "site": "00448800",
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
            "const:f13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00425cf8",
      "incomplete_value": false,
      "site": "00425d00",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004488b4",
      "incomplete_value": false,
      "site": "004488bc",
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
            "const:da7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00425db4",
      "incomplete_value": false,
      "site": "00425dbc",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004488cc",
      "incomplete_value": false,
      "site": "004488d8",
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
            "const:ea9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00425dcc",
      "incomplete_value": false,
      "site": "00425dd8",
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
      344,
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      532,
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      556,
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      344,
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      532,
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      556,
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00425c20 ["INT_ADD", "register:40f0:8", ["const:425c20:8", "const:4:8"]]
+ 00448720 ["INT_ADD", "register:40f0:8", ["const:448720:8", "const:4:8"]]
- 00425c94 ["INT_ADD", "register:40f0:8", ["const:425c94:8", "const:4:8"]]
+ 00448794 ["INT_ADD", "register:40f0:8", ["const:448794:8", "const:4:8"]]
- 00425cf4 ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 00425cf8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 004487f4 ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 004487f8 ["COPY", "tmp:0:8", ["const:f13:8"]]
~~~


### [`004264e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) → [`00448fe8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/00448fe8.md) FUN_00448fe8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00425ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md) [`004264e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) [`005be404`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) [`005fa9ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fa/005fa9ec.md) [`005fd41c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fd41c.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 10件 [`004486a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/004486a0.md) [`00448fe8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/00448fe8.md) [`005e30d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`006203f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/006203f0.md) [`00622e20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622e20.md) · 呼出先 22件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449140",
      "incomplete_value": false,
      "site": "00449148",
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
            "const:f13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00426640",
      "incomplete_value": false,
      "site": "00426648",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449164",
      "incomplete_value": false,
      "site": "00449170",
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
            "const:ea9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00426664",
      "incomplete_value": false,
      "site": "00426670",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449298",
      "incomplete_value": false,
      "site": "004492a0",
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
            "const:da7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00426798",
      "incomplete_value": false,
      "site": "004267a0",
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
      344,
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      380,
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      688,
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      344,
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      380,
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      688,
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00426564 ["INT_ADD", "register:40f0:8", ["const:426564:8", "const:4:8"]]
+ 00449064 ["INT_ADD", "register:40f0:8", ["const:449064:8", "const:4:8"]]
- 004265dc ["INT_ADD", "register:40f0:8", ["const:4265dc:8", "const:4:8"]]
+ 004490dc ["INT_ADD", "register:40f0:8", ["const:4490dc:8", "const:4:8"]]
- 0042663c ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 00426640 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0044913c ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 00449140 ["COPY", "tmp:0:8", ["const:f13:8"]]
~~~


### [`00426e78`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) → [`00449978`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) FUN_00449978

根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00426cec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426cec.md) [`004c2f88`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2f88.md) [`005aca98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md) [`005af810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af810.md) [`0073ea18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ea18.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`004497ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/004497ec.md) [`004e5e20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md) [`005d1764`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d44dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md) [`00768d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768d24.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00449988",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00426e88",
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
      "definition_site": "00449984",
      "incomplete_value": false,
      "site": "00449988",
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
      "definition_site": "00426e84",
      "incomplete_value": false,
      "site": "00426e88",
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
- 00426e80 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00426e84 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00449980 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00449984 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00426e88 ["INT_ADD", "register:40f0:8", ["const:426e88:8", "const:4:8"]]
- 00426e88 ["CALL", null, ["ram:418c38:8"]]
+ 00449988 ["INT_ADD", "register:40f0:8", ["const:449988:8", "const:4:8"]]
+ 00449988 ["CALL", null, ["ram:43b738:8"]]
~~~


### [`00426e8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) → [`0044998c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/0044998c.md) FUN_0044998c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00426e8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) [`0046c588`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md) [`005b7004`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7004.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`00444de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`0044998c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/0044998c.md) [`0048f420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md) [`005dbcd4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md) · 呼出先 21件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449af8",
      "incomplete_value": false,
      "site": "00449b00",
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
            "const:f13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00426ff8",
      "incomplete_value": false,
      "site": "00427000",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449bb8",
      "incomplete_value": false,
      "site": "00449bc0",
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
            "const:da7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004270b8",
      "incomplete_value": false,
      "site": "004270c0",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449bd4",
      "incomplete_value": false,
      "site": "00449be0",
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
            "const:ea9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004270d4",
      "incomplete_value": false,
      "site": "004270e0",
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
      364,
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      556,
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      584,
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      364,
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      556,
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      584,
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00426f08 ["INT_ADD", "register:40f0:8", ["const:426f08:8", "const:4:8"]]
+ 00449a08 ["INT_ADD", "register:40f0:8", ["const:449a08:8", "const:4:8"]]
- 00426f8c ["INT_ADD", "register:40f0:8", ["const:426f8c:8", "const:4:8"]]
+ 00449a8c ["INT_ADD", "register:40f0:8", ["const:449a8c:8", "const:4:8"]]
- 00426ff4 ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 00426ff8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00449af4 ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 00449af8 ["COPY", "tmp:0:8", ["const:f13:8"]]
~~~


### [`00427778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427778.md) → [`0044a278`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044a278.md) FUN_0044a278

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00427778`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427778.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00444de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`0044a278`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044a278.md) · 呼出先 22件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044a3c8",
      "incomplete_value": false,
      "site": "0044a3d0",
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
            "const:f13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004278c8",
      "incomplete_value": false,
      "site": "004278d0",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044a3ec",
      "incomplete_value": false,
      "site": "0044a3f8",
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
            "const:ea9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004278ec",
      "incomplete_value": false,
      "site": "004278f8",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044a520",
      "incomplete_value": false,
      "site": "0044a528",
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
            "const:da7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427a20",
      "incomplete_value": false,
      "site": "00427a28",
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
      336,
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      372,
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      680,
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      336,
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      372,
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      680,
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 004277f0 ["INT_ADD", "register:40f0:8", ["const:4277f0:8", "const:4:8"]]
+ 0044a2f0 ["INT_ADD", "register:40f0:8", ["const:44a2f0:8", "const:4:8"]]
- 00427864 ["INT_ADD", "register:40f0:8", ["const:427864:8", "const:4:8"]]
+ 0044a364 ["INT_ADD", "register:40f0:8", ["const:44a364:8", "const:4:8"]]
- 004278c4 ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 004278c8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0044a3c4 ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 0044a3c8 ["COPY", "tmp:0:8", ["const:f13:8"]]
~~~


### [`00427f68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f68.md) → [`0044aa68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044aa68.md) FUN_0044aa68

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
      "definition_site": "0044aa7c",
      "incomplete_value": false,
      "site": "0044aa80",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427f7c",
      "incomplete_value": false,
      "site": "00427f80",
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
            "const:610:8"
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
        "00be6610",
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
        "00c631d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00427f74 ["INT_ADD", "register:40f0:8", ["const:427f74:8", "const:4:8"]]
+ 0044aa74 ["INT_ADD", "register:40f0:8", ["const:44aa74:8", "const:4:8"]]
- 00427f78 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00427f7c ["COPY", "tmp:0:8", ["const:610:8"]]
+ 0044aa78 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044aa7c ["COPY", "tmp:0:8", ["const:1d0:8"]]
~~~


### [`00427f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f8c.md) → [`0044aa8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044aa8c.md) FUN_0044aa8c

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
      "definition_site": "0044aa90",
      "incomplete_value": false,
      "site": "0044aa94",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427f90",
      "incomplete_value": false,
      "site": "00427f94",
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
            "const:610:8"
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
        "00be6610",
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
        "00c631d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00427f8c ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00427f90 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 0044aa8c ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044aa90 ["COPY", "tmp:0:8", ["const:1d0:8"]]
~~~


### [`00427fd4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427fd4.md) → [`0044aad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044aad4.md) FUN_0044aad4

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
      "definition_site": "0044aae8",
      "incomplete_value": false,
      "site": "0044aaec",
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
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427fe8",
      "incomplete_value": false,
      "site": "00427fec",
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
            "const:690:8"
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
        "00be6690",
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
        "00c63250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00427fe0 ["INT_ADD", "register:40f0:8", ["const:427fe0:8", "const:4:8"]]
+ 0044aae0 ["INT_ADD", "register:40f0:8", ["const:44aae0:8", "const:4:8"]]
- 00427fe4 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00427fe8 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 0044aae4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044aae8 ["COPY", "tmp:0:8", ["const:250:8"]]
~~~


### [`00427ff8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427ff8.md) → [`0044aaf8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044aaf8.md) FUN_0044aaf8

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
      "definition_site": "0044aafc",
      "incomplete_value": false,
      "site": "0044ab00",
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
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427ffc",
      "incomplete_value": false,
      "site": "00428000",
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
            "const:690:8"
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
        "00be6690",
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
        "00c63250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00427ff8 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00427ffc ["COPY", "tmp:0:8", ["const:690:8"]]
+ 0044aaf8 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044aafc ["COPY", "tmp:0:8", ["const:250:8"]]
~~~


### [`00428044`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428044.md) → [`0044ab44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab44.md) FUN_0044ab44

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
      "definition_site": "0044ab58",
      "incomplete_value": false,
      "site": "0044ab5c",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428058",
      "incomplete_value": false,
      "site": "0042805c",
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
            "const:710:8"
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
        "00be6710",
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
        "00c632d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00428050 ["INT_ADD", "register:40f0:8", ["const:428050:8", "const:4:8"]]
+ 0044ab50 ["INT_ADD", "register:40f0:8", ["const:44ab50:8", "const:4:8"]]
- 00428054 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00428058 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 0044ab54 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044ab58 ["COPY", "tmp:0:8", ["const:2d0:8"]]
~~~


### [`00428068`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428068.md) → [`0044ab68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab68.md) FUN_0044ab68

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 1件 [`0083a0e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ab6c",
      "incomplete_value": false,
      "site": "0044ab70",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042806c",
      "incomplete_value": false,
      "site": "00428070",
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
            "const:710:8"
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
        "00be6710",
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
        "00c632d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00428068 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 0042806c ["COPY", "tmp:0:8", ["const:710:8"]]
+ 0044ab68 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044ab6c ["COPY", "tmp:0:8", ["const:2d0:8"]]
~~~


### [`00428080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md) → [`0044ab80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab80.md) FUN_0044ab80

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00421614`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421614.md) [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 1件 [`00b1195c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 6件 [`00444114`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444114.md) [`00444424`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444424.md) [`004445d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044abdc",
      "incomplete_value": false,
      "site": "0044abdc",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
    "old": {
      "definition_site": "004280dc",
      "incomplete_value": false,
      "site": "004280dc",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044abe0",
      "incomplete_value": false,
      "site": "0044abe0",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "004280e0",
      "incomplete_value": false,
      "site": "004280e0",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044abe0",
      "incomplete_value": false,
      "site": "0044abe0",
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
                "const:8:8"
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
      "definition_site": "004280e0",
      "incomplete_value": false,
      "site": "004280e0",
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
                "const:8:8"
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
      28,
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "00c24b58",
        null,
        "undefined8"
      ]
    ],
    [
      56,
      "PARAM",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "00ca4618",
        null,
        "undefined8"
      ]
    ],
    [
      56,
      "PARAM",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00428094 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00428098 ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 0044ab94 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0044ab98 ["COPY", "tmp:0:8", ["const:648:8"]]
- 004280a4 ["COPY", "register:4000:8", ["const:c24000:8"]]
- 004280a8 ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 0044aba4 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 0044aba8 ["COPY", "tmp:0:8", ["const:618:8"]]
- 004280b4 ["COPY", "register:4000:8", ["const:c24000:8"]]
- 004280b8 ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 0044abb4 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 0044abb8 ["COPY", "tmp:0:8", ["const:648:8"]]
~~~


### [`00428128`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428128.md) → [`0044ac28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ac28.md) FUN_0044ac28

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423ad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423ad4.md) · 呼出先 7件 [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb280`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb290`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 2件 [`004445d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`004465d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004465d4.md) · 呼出先 7件 [`00c57a60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57ce0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

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
      "site": "0044ac60",
      "value": [
        "leaf",
        "ram:c57cd0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00428160",
      "value": [
        "leaf",
        "ram:bdb280:8"
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
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb280"
      ]
    ]
  ],
  "added": [
    [
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57cd0"
      ]
    ]
  ]
}
~~~


~~~diff
- 00428140 ["INT_ADD", "register:40f0:8", ["const:428140:8", "const:4:8"]]
+ 0044ac40 ["INT_ADD", "register:40f0:8", ["const:44ac40:8", "const:4:8"]]
- 00428148 ["INT_ADD", "register:40f0:8", ["const:428148:8", "const:4:8"]]
+ 0044ac48 ["INT_ADD", "register:40f0:8", ["const:44ac48:8", "const:4:8"]]
- 00428150 ["INT_ADD", "register:40f0:8", ["const:428150:8", "const:4:8"]]
+ 0044ac50 ["INT_ADD", "register:40f0:8", ["const:44ac50:8", "const:4:8"]]
~~~


### [`00428290`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428290.md) → [`0044ad90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ad90.md) _INIT_9

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044adcc",
      "incomplete_value": true,
      "site": "0044ade8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004282cc",
      "incomplete_value": true,
      "site": "004282e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044adf0",
      "incomplete_value": true,
      "site": "0044ae0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004282f0",
      "incomplete_value": true,
      "site": "0042830c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ae10",
      "incomplete_value": true,
      "site": "0044ae2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428310",
      "incomplete_value": true,
      "site": "0042832c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 15,
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
- 004282b8 ["COPY", "register:4098:8", ["const:c24000:8"]]
- 004282bc ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 0044adb8 ["COPY", "register:4098:8", ["const:ca4000:8"]]
+ 0044adbc ["COPY", "tmp:0:8", ["const:600:8"]]
- 004282c4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 004282c8 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 0044adc4 ["COPY", "register:4048:8", ["const:2b7000:8"]]
+ 0044adc8 ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 004282e0 ["COPY", "register:4050:8", ["const:2a7000:8"]]
- 004282e4 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 0044ade0 ["COPY", "register:4050:8", ["const:2b7000:8"]]
+ 0044ade4 ["COPY", "tmp:0:8", ["const:ef9:8"]]
~~~


### [`00428620`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428620.md) → [`0044b120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b120.md) FUN_0044b120

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0042d2a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d2a8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00450140`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b12c",
      "incomplete_value": true,
      "site": "0044b13c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:6ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042862c",
      "incomplete_value": true,
      "site": "0042863c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:675:8"
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
      "definition_site": "0044b140",
      "incomplete_value": true,
      "site": "0044b140",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428640",
      "incomplete_value": true,
      "site": "00428640",
      "value": [
        "LOAD",
        "8",
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
        "002ac675",
        null,
        "string"
      ]
    ],
    [
      20,
      "READ",
      [
        "storage",
        "002ac683",
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
        "002bd6ed",
        null,
        "string"
      ]
    ],
    [
      20,
      "READ",
      [
        "storage",
        "002bd6fb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00428624 ["COPY", "register:4050:8", ["const:2ac000:8"]]
- 00428628 ["COPY", "tmp:0:8", ["const:675:8"]]
+ 0044b124 ["COPY", "register:4050:8", ["const:2bd000:8"]]
+ 0044b128 ["COPY", "tmp:0:8", ["const:6ed:8"]]
~~~


### [`00428648`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428648.md) → [`0044b148`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b148.md) FUN_0044b148

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00605bdc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/00605bdc.md) [`006091c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/006091c4.md) [`00824eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 3件 [`0062b6d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b6d4.md) [`0062ecbc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md) [`00856dec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b170",
      "incomplete_value": true,
      "site": "0044b180",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428670",
      "incomplete_value": true,
      "site": "00428680",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044b184",
      "incomplete_value": true,
      "site": "0044b184",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428684",
      "incomplete_value": true,
      "site": "00428684",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b190",
      "incomplete_value": false,
      "site": "0044b198",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428690",
      "incomplete_value": false,
      "site": "00428698",
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
            "const:5f9:8"
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
      40,
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "002925f9",
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
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00428660 ["COPY", "register:4048:8", ["const:2ae000:8"]]
- 00428664 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0044b160 ["COPY", "register:4048:8", ["const:2bf000:8"]]
+ 0044b164 ["COPY", "tmp:0:8", ["const:b5a:8"]]
- 0042868c ["COPY", "register:4008:8", ["const:292000:8"]]
- 00428690 ["COPY", "tmp:0:8", ["const:5f9:8"]]
+ 0044b18c ["COPY", "register:4008:8", ["const:2a1000:8"]]
+ 0044b190 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 00428698 ["INT_ADD", "register:40f0:8", ["const:428698:8", "const:4:8"]]
+ 0044b198 ["INT_ADD", "register:40f0:8", ["const:44b198:8", "const:4:8"]]
~~~


### [`00428714`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428714.md) → [`0044b214`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b214.md) FUN_0044b214

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00429a14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429a14.md) [`0079bdf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`00824eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00868124`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) · 呼出先 5件 [`00574744`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574744.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 4件 [`0044c794`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md) [`007cceac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00856dec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0089b248`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) · 呼出先 5件 [`005975dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975dc.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b240",
      "incomplete_value": true,
      "site": "0044b250",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428740",
      "incomplete_value": true,
      "site": "00428750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044b254",
      "incomplete_value": true,
      "site": "0044b254",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428754",
      "incomplete_value": true,
      "site": "00428754",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b260",
      "incomplete_value": false,
      "site": "0044b268",
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
            "const:f16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428760",
      "incomplete_value": false,
      "site": "00428768",
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
            "const:3a7:8"
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
      44,
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      76,
      "PARAM",
      [
        "storage",
        "002a73a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      44,
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      76,
      "PARAM",
      [
        "storage",
        "002b7f16",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00428730 ["COPY", "register:4048:8", ["const:2ae000:8"]]
- 00428734 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0044b230 ["COPY", "register:4048:8", ["const:2bf000:8"]]
+ 0044b234 ["COPY", "tmp:0:8", ["const:b5a:8"]]
- 0042875c ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 00428760 ["COPY", "tmp:0:8", ["const:3a7:8"]]
+ 0044b25c ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 0044b260 ["COPY", "tmp:0:8", ["const:f16:8"]]
- 00428768 ["INT_ADD", "register:40f0:8", ["const:428768:8", "const:4:8"]]
+ 0044b268 ["INT_ADD", "register:40f0:8", ["const:44b268:8", "const:4:8"]]
~~~


### [`004288b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md) → [`0044b3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) FUN_0044b3b4

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`0042f000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md) [`0042f610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) [`0042fd7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00432904`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432904.md) [`00432e80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432e80.md) · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 10件 [`00451e98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) [`004524a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`00452c14`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`0045579c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md) [`00455d18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md) · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b3d8",
      "incomplete_value": true,
      "site": "0044b3ec",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:260:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004288d8",
      "incomplete_value": true,
      "site": "004288ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b80:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b3e4",
      "incomplete_value": true,
      "site": "0044b3f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:918:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004288e4",
      "incomplete_value": true,
      "site": "004288f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2cc:8"
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
      "definition_site": "0044b3e4",
      "incomplete_value": true,
      "site": "0044b3f0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004288e4",
      "incomplete_value": true,
      "site": "004288f0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 7,
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
        "002b1b80",
        null,
        null
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002a12cc",
        null,
        "string"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002a12dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "002c3260",
        null,
        null
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002b1918",
        null,
        "string"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002b1928",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 004288c8 ["INT_ADD", "register:40f0:8", ["const:4288c8:8", "const:4:8"]]
+ 0044b3c8 ["INT_ADD", "register:40f0:8", ["const:44b3c8:8", "const:4:8"]]
- 004288cc ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 0044b3cc ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 004288d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b80:8"]]
+ 0044b3d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
~~~


### [`004289a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md) → [`0044b4a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) FUN_0044b4a4

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0043344c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/0043344c.md) [`00434024`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434024.md) [`00434528`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434528.md) [`004349a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/004349a0.md) [`00435358`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435358.md) · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 7件 [`004562e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md) [`00456ebc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md) [`004573c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md) [`00457838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md) [`004581f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md) · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b4c8",
      "incomplete_value": true,
      "site": "0044b4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:260:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004289c8",
      "incomplete_value": true,
      "site": "004289dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b80:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b4d4",
      "incomplete_value": true,
      "site": "0044b4e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:131:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004289d4",
      "incomplete_value": true,
      "site": "004289e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:640:8"
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
      "definition_site": "0044b4d4",
      "incomplete_value": true,
      "site": "0044b4e0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004289d4",
      "incomplete_value": true,
      "site": "004289e0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 7,
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
        "002b1b80",
        null,
        null
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002a6640",
        null,
        "string"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002a6650",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "002c3260",
        null,
        null
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002b7131",
        null,
        "string"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002b7141",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 004289b8 ["INT_ADD", "register:40f0:8", ["const:4289b8:8", "const:4:8"]]
+ 0044b4b8 ["INT_ADD", "register:40f0:8", ["const:44b4b8:8", "const:4:8"]]
- 004289bc ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 0044b4bc ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 004289c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b80:8"]]
+ 0044b4c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
~~~


### [`004289f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289f4.md) → [`0044b4f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4f4.md) FUN_0044b4f4

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0042ca70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca70.md) [`0042ce34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ce34.md) [`00431534`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) [`00a26e20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26e20.md) · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 5件 [`0043c218`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0044f908`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md) [`0044fccc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md) [`004543cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`00a84cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84cb0.md) · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b51c",
      "incomplete_value": true,
      "site": "0044b528",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428a1c",
      "incomplete_value": true,
      "site": "00428a28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:300:8"
              ]
            ]
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
      "definition_site": "0044b518",
      "incomplete_value": true,
      "site": "0044b52c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:99e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428a18",
      "incomplete_value": true,
      "site": "00428a2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:be0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b518",
      "incomplete_value": true,
      "site": "0044b52c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00428a18",
      "incomplete_value": true,
      "site": "00428a2c",
      "value": [
        "LOAD",
        "16",
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
      36,
      "READ",
      [
        "storage",
        "00298be0",
        null,
        "string"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "00298bf0",
        null,
        "string"
      ]
    ],
    [
      40,
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
      36,
      "READ",
      [
        "storage",
        "002a899e",
        null,
        "string"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "002a89ae",
        null,
        "string"
      ]
    ],
    [
      40,
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


~~~diff
- 00428a08 ["INT_ADD", "register:40f0:8", ["const:428a08:8", "const:4:8"]]
+ 0044b508 ["INT_ADD", "register:40f0:8", ["const:44b508:8", "const:4:8"]]
- 00428a0c ["COPY", "register:4040:8", ["const:298000:8"]]
- 00428a10 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 0044b50c ["COPY", "register:4040:8", ["const:2a8000:8"]]
+ 0044b510 ["COPY", "tmp:0:8", ["const:99e:8"]]
- 00428a14 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0044b514 ["COPY", "register:4048:8", ["const:2c2000:8"]]
~~~


### [`00428a44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428a44.md) → [`0044b544`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b544.md) FUN_0044b544

根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004508a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) [`00454f34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454f34.md) · 呼出先 6件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb100`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb100.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 2件 [`0047373c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) [`00477dcc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md) · 呼出先 6件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b584",
      "incomplete_value": true,
      "site": "0044b590",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:510:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428a84",
      "incomplete_value": true,
      "site": "00428a90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "0044b580",
      "incomplete_value": true,
      "site": "0044b594",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:eb4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428a80",
      "incomplete_value": true,
      "site": "00428a94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:890:8"
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
      "definition_site": "0044b580",
      "incomplete_value": true,
      "site": "0044b594",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00428a80",
      "incomplete_value": true,
      "site": "00428a94",
      "value": [
        "LOAD",
        "16",
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
      60,
      "READ",
      [
        "storage",
        "002af890",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "002af8a0",
        null,
        "string"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "002b0f20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      60,
      "READ",
      [
        "storage",
        "002c0eb4",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "002c0ec4",
        null,
        "string"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "002c2510",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00428a70 ["INT_ADD", "register:40f0:8", ["const:428a70:8", "const:4:8"]]
+ 0044b570 ["INT_ADD", "register:40f0:8", ["const:44b570:8", "const:4:8"]]
- 00428a74 ["COPY", "register:4040:8", ["const:2af000:8"]]
- 00428a78 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 0044b574 ["COPY", "register:4040:8", ["const:2c0000:8"]]
+ 0044b578 ["COPY", "tmp:0:8", ["const:eb4:8"]]
- 00428a7c ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0044b57c ["COPY", "register:4048:8", ["const:2c2000:8"]]
~~~


