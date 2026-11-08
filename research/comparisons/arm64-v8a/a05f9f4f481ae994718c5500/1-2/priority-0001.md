# v15.7.3 → v15.7.4 · 最優先の変更候補 (1)

[一覧の目次](README.md)

### [`00418338`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418338.md) → [`00418338`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418338.md) _INIT_3

根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b7d25c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d25c.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b7d2a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2a0.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:a00:8"
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
                "const:d20:8"
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
            "const:9d8:8"
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
        "00c24a00",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00c24a00",
        null,
        "undefined1"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00c249d8",
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
  ]
}
~~~


~~~diff
- 00418344 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00418344 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 00418354 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00418354 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 00418368 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 00418368 ["COPY", "tmp:0:8", ["const:a18:8"]]
~~~


### [`004183ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md) → [`004183ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md) Java_jp_co_ponos_battlecats_MyActivity_appInit

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0053c5e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5e8.md) [`00547c90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00547/00547c90.md) [`00acb9f0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb9f0.md) [`00acc304`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc304.md) [`00accf4c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0053c5e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5e8.md) [`00547c90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md) [`00acba34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba34.md) [`00acc348`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc348.md) [`00accf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:f98:8"
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
            "const:a10:8"
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
                "const:a10:8"
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
        "00c24a10",
        null,
        "undefined8"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "00be5f98",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00c24a18",
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
  ]
}
~~~


~~~diff
- 00418400 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a10:8"]]
+ 00418400 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a50:8"]]
- 00418430 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00418430 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0041844c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0041844c ["COPY", "tmp:0:8", ["const:a50:8"]]
~~~


### [`004184bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004184bc.md) → [`004184bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004184bc.md) Java_jp_co_ponos_battlecats_MyActivity_appUpdateDraw

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0053257c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053257c.md) [`0056cb70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cb70.md) [`00acb9f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb9f8.md) [`00acd424`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd424.md) [`00bdafb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0053257c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053257c.md) [`0056cb70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md) [`00acba3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba3c.md) [`00acd468`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd468.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:a20:8"
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00418504",
      "incomplete_value": true,
      "site": "0041851c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00418504",
      "incomplete_value": true,
      "site": "0041851c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a10:8"
              ]
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
      44,
      "READ",
      [
        "storage",
        "00c24a28",
        null,
        "undefined1"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00c24a20",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c24a10",
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
  ]
}
~~~


~~~diff
- 004184e4 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 004184e4 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 004184f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a20:8"]]
+ 004184f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a60:8"]]
- 00418504 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a10:8"]]
+ 00418504 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a50:8"]]
~~~


### [`004185a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004185a8.md) → [`004185a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004185a8.md) Java_jp_co_ponos_battlecats_MyActivity_gfxInit

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`004186bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004186bc.md) [`0056c8a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c8a4.md) [`0056f4d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f4d8.md) [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004186bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004186bc.md) [`0056c8a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c8a4.md) [`0056f4d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f4d8.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
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
            "const:a30:8"
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
                "const:a30:8"
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
        "00c24a40",
        null,
        "undefined1"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00c24a38",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "WRITE",
      [
        "storage",
        "00c24a30",
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
  ]
}
~~~


~~~diff
- 004185c8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 004185c8 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 004185e0 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 004185e0 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 00418654 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a30:8"]]
+ 00418654 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
~~~


### [`0041870c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041870c.md) → [`0041870c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041870c.md) Java_jp_co_ponos_battlecats_MyActivity_getDrawableWidth

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
        "00c24d88",
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
        "00c24dc8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418710 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418710 ["COPY", "tmp:0:8", ["const:db0:8"]]
~~~


### [`0041871c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041871c.md) → [`0041871c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041871c.md) Java_jp_co_ponos_battlecats_MyActivity_getDrawableHeight

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
        "00c24d8c",
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
        "00c24dcc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418720 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418720 ["COPY", "tmp:0:8", ["const:db0:8"]]
~~~


### [`0041872c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041872c.md) → [`0041872c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041872c.md) Java_jp_co_ponos_battlecats_MyActivity_getWindowWidth

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
        "00c24d78",
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
        "00c24db8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418730 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418730 ["COPY", "tmp:0:8", ["const:db0:8"]]
~~~


### [`0041873c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041873c.md) → [`0041873c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041873c.md) Java_jp_co_ponos_battlecats_MyActivity_getWindowHeight

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
        "00c24d7c",
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
        "00c24dbc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418740 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418740 ["COPY", "tmp:0:8", ["const:db0:8"]]
~~~


### [`0041874c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041874c.md) → [`0041874c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041874c.md) Java_jp_co_ponos_battlecats_MyActivity_getSizeWidth

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
        "00c24d80",
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
        "00c24dc0",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418750 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418750 ["COPY", "tmp:0:8", ["const:db0:8"]]
~~~


### [`0041875c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041875c.md) → [`0041875c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041875c.md) Java_jp_co_ponos_battlecats_MyActivity_getSizeHeight

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
        "00c24d84",
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
        "00c24dc4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418760 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418760 ["COPY", "tmp:0:8", ["const:db0:8"]]
~~~


### [`0041876c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041876c.md) → [`0041876c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041876c.md) Java_jp_co_ponos_battlecats_MyActivity_gfxResize

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056cb70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cb70.md) [`00accf4c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056cb70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md) [`00accf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "READ",
      [
        "storage",
        "00c1ad38",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00c2655c",
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
  ]
}
~~~


~~~diff
- 00418784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d30:8"]]
+ 00418784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 00418788 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d38:8"]]
+ 00418788 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d88:8"]]
- 00418798 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d40:8"]]
+ 00418798 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d90:8"]]
~~~


### [`00418828`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md) → [`00418828`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md) Java_jp_co_ponos_battlecats_MyActivity_appTouch

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00acd34c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd34c.md) [`00acd394`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd394.md) [`00acd3dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd3dc.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00acd390`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd390.md) [`00acd3d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd3d8.md) [`00acd420`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:a48:8"
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
            "const:a4c:8"
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
                "const:a10:8"
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
        "00c24a10",
        null,
        "undefined8"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00c24a10",
        null,
        "undefined8"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "00c24a48",
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
  ]
}
~~~


~~~diff
- 00418874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a10:8"]]
+ 00418874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
- 00418898 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a10:8"]]
+ 00418898 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
- 004188a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 004188a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
~~~


### [`00418b18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b18.md) → [`00418b18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md) Java_jp_co_ponos_battlecats_MyActivity_kill

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00acbcd0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbcd0.md) [`00acc528`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md) [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00acbd14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd14.md) [`00acc56c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc56c.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
                "const:a10:8"
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
        "00c24a10",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c24a10",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00c24a18",
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
  ]
}
~~~


~~~diff
- 00418b28 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 00418b28 ["COPY", "tmp:0:8", ["const:a50:8"]]
~~~


### [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) → [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) FUN_00418c24

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 272件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e10c.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 272件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:1b2:8"
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
        "002a91b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      12,
      "PARAM",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418c30 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 00418c30 ["COPY", "tmp:0:8", ["const:24c:8"]]
~~~


### [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md) → [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md) FUN_00418c38

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 223件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00420bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bd8.md) [`00426e78`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e78.md) [`00439eb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439eb4.md) · 呼出先 4件 [`00418c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c88.md) [`00bbae18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae18.md) [`00bdb050`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 223件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00420bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bd8.md) [`00426e78`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) [`00439eb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439eb4.md) · 呼出先 4件 [`00418c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c88.md) [`00bbae5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae5c.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00418c68",
      "incomplete_value": true,
      "site": "00418c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418c68",
      "incomplete_value": true,
      "site": "00418c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
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
      "definition_site": "00418c6c",
      "incomplete_value": true,
      "site": "00418c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418c6c",
      "incomplete_value": true,
      "site": "00418c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
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
      48,
      "READ",
      [
        "storage",
        "00c1ad50",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00c169e0",
        "_ZTISt12length_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00c1ad58",
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
        "00c1ada0",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00c16a30",
        "_ZTISt12length_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00c1ada8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00418c68 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d50:8"]]
+ 00418c68 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:da0:8"]]
- 00418c6c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:d58:8"]]
+ 00418c6c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:da8:8"]]
~~~


### [`00419248`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419248.md) → [`00419248`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419248.md) FUN_00419248

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0041924c",
      "incomplete_value": false,
      "site": "00419250",
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
    "old": {
      "definition_site": "0041924c",
      "incomplete_value": false,
      "site": "00419250",
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
            "const:f98:8"
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
        "00be5f98",
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
        "00be5fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041924c ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0041924c ["COPY", "tmp:0:8", ["const:fe8:8"]]
~~~


### [`00419258`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419258.md) → [`00419258`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419258.md) FUN_00419258

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00419268",
      "incomplete_value": false,
      "site": "00419270",
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
    "old": {
      "definition_site": "00419268",
      "incomplete_value": false,
      "site": "00419270",
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
            "const:f98:8"
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
        "00be5f98",
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
        "00be5fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00419268 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00419268 ["COPY", "tmp:0:8", ["const:fe8:8"]]
~~~


### [`00419294`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419294.md) → [`00419294`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419294.md) _INIT_4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418394`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418394.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418394`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418394.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      128,
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
  ]
}
~~~


~~~diff
- 004192c0 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 004192c0 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 004192cc ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 004192cc ["COPY", "tmp:0:8", ["const:377:8"]]
- 004192e8 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 004192e8 ["COPY", "tmp:0:8", ["const:38a:8"]]
~~~


### [`00419640`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419640.md) → [`00419640`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419640.md) _INIT_5

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041969c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/0041969c.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041969c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/0041969c.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:a70:8"
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
            "const:a68:8"
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
      "definition_site": "0041967c",
      "incomplete_value": false,
      "site": "00419680",
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
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041967c",
      "incomplete_value": false,
      "site": "00419680",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
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
        "00c24a70",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00c24a70",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "PARAM",
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
      52,
      "PARAM",
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


~~~diff
- 0041964c ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 0041964c ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 0041965c ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 0041965c ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00419674 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 00419674 ["COPY", "tmp:0:8", ["const:aa8:8"]]
~~~


### [`004196bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/004196bc.md) → [`004196bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/004196bc.md) _INIT_6

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041969c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/0041969c.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041969c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/0041969c.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:a80:8"
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
            "const:a78:8"
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
      "definition_site": "004196f8",
      "incomplete_value": false,
      "site": "004196fc",
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
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004196f8",
      "incomplete_value": false,
      "site": "004196fc",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
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
        "00c24a80",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00c24a80",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "00c24a78",
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
      52,
      "PARAM",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 004196c8 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 004196c8 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 004196d8 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 004196d8 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 004196f0 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 004196f0 ["COPY", "tmp:0:8", ["const:ab8:8"]]
~~~


### [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) → [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) FUN_00419718

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00420580`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420580.md) [`00420858`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420858.md) · 呼出先 49件 [`0041aa74`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041aa74.md) [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`0041ba38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041ba38.md)
- 新版 呼出元 2件 [`00420580`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420580.md) [`00420858`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420858.md) · 呼出先 49件 [`0041aa74`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041aa74.md) [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`0041ba38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 11件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
                "const:952:8"
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
                "const:520:8"
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
      "definition_site": "00419ca0",
      "incomplete_value": true,
      "site": "00419ca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00419ca0",
      "incomplete_value": true,
      "site": "00419ca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:952:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      148,
      "PARAM",
      [
        "storage",
        "002af912",
        null,
        "string"
      ]
    ],
    [
      204,
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      376,
      "READ",
      [
        "storage",
        "00297952",
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
  ]
}
~~~


~~~diff
- 004197ac ["COPY", "tmp:0:8", ["const:912:8"]]
+ 004197ac ["COPY", "tmp:0:8", ["const:87e:8"]]
- 004197e4 ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 004197e4 ["COPY", "tmp:0:8", ["const:259:8"]]
- 00419888 ["COPY", "tmp:0:8", ["const:952:8"]]
+ 00419888 ["COPY", "tmp:0:8", ["const:8c5:8"]]
~~~


### [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md) → [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) FUN_0041ac3c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) · 呼出先 13件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e10c.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`0046517c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/0046517c.md) [`004652a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/004652a0.md)
- 新版 呼出元 2件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) · 呼出先 13件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`0046517c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046517c.md) [`004652a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004652a0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      656,
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      664,
      "READ",
      [
        "storage",
        "00c13408",
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
  ]
}
~~~


~~~diff
- 0041aec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 0041aec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 0041aecc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d78:8"]]
+ 0041aecc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:dc8:8"]]
- 0041aef4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 0041aef4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
~~~


### [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) → [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) FUN_0041b064

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 39件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md) [`00421b40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b40.md) · 呼出先 6件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 39件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`00421b40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) · 呼出先 6件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:8ca:8"
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
        "002958ca",
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
        "0029583d",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0041b214 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 0041b214 ["COPY", "tmp:0:8", ["const:83d:8"]]
~~~


### [`0041b338`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b338.md) → [`0041b338`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b338.md) FUN_0041b338

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045fc34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045fc34.md) · 呼出先 3件 [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`0045fc34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045fc34.md) · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
        "00c1ad68",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00be8530",
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
  ]
}
~~~


~~~diff
- 0041b34c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d68:8"]]
+ 0041b34c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
~~~


### [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) → [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) FUN_0041b470

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) · 呼出先 20件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`00420674`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420674.md) [`00420678`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420678.md) [`00420704`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420704.md) [`00420708`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420708.md)
- 新版 呼出元 2件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) · 呼出先 20件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00420674`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420674.md) [`00420678`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420678.md) [`00420704`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420704.md) [`00420708`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420708.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:228:8"
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
            "const:2a8:8"
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
            "const:328:8"
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
      80,
      "PARAM",
      [
        "storage",
        "002958cc",
        null,
        "undefined4"
      ]
    ],
    [
      344,
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      344,
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
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
      344,
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      344,
      "PARAM",
      [
        "storage",
        "00c25e10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041b4c0 ["COPY", "tmp:0:8", ["const:8cc:8"]]
+ 0041b4c0 ["COPY", "tmp:0:8", ["const:83f:8"]]
- 0041b5c8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
+ 0041b5c8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:dd8:8"]]
- 0041b660 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 0041b660 ["COPY", "tmp:0:8", ["const:278:8"]]
~~~


### [`0041ba38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041ba38.md) → [`0041ba38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md) FUN_0041ba38

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) · 呼出先 11件 [`004203a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004203a4.md) [`004203a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004203a8.md) [`00420430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420430.md) [`00420434`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420434.md) [`00420578`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420578.md)
- 新版 呼出元 1件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) · 呼出先 11件 [`004203a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203a4.md) [`004203a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203a8.md) [`00420430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420430.md) [`00420434`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420434.md) [`00420578`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420578.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:78:8"
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
            "const:108:8"
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
            "const:198:8"
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
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      184,
      "DATA",
      [
        "storage",
        "00be6078",
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
  ]
}
~~~


~~~diff
- 0041ba68 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
+ 0041ba68 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:dd8:8"]]
- 0041baec ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0041baec ["COPY", "tmp:0:8", ["const:c8:8"]]
- 0041bb10 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 0041bb10 ["COPY", "tmp:0:8", ["const:158:8"]]
~~~


### [`0041be0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) → [`0041be0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) FUN_0041be0c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 38件 [`0060468c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/0060468c.md) [`00651720`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651720.md) [`006584d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md) [`0068d484`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) [`00695904`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) · 呼出先 5件 [`0041be9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be9c.md) [`0041bf20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bf20.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 38件 [`0060468c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/0060468c.md) [`00651720`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651720.md) [`006584d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) [`0068d484`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) [`00695904`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 5件 [`0041be9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be9c.md) [`0041bf20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:ae0:8"
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
            "const:a88:8"
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
      "definition_site": "0041be64",
      "incomplete_value": false,
      "site": "0041be70",
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
    "old": {
      "definition_site": "0041be64",
      "incomplete_value": false,
      "site": "0041be70",
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
            "const:a88:8"
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
      20,
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c24a88",
        null,
        null
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "00c24ae0",
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
  ]
}
~~~


~~~diff
- 0041be1c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0041be1c ["COPY", "tmp:0:8", ["const:b20:8"]]
- 0041be2c ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 0041be2c ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 0041be40 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0041be40 ["COPY", "tmp:0:8", ["const:b20:8"]]
~~~


### [`0041bf20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bf20.md) → [`0041bf20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md) FUN_0041bf20

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041be0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`00420940`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420940.md) · 呼出先 4件 [`00ad3bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3bb4.md) [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041be0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`00420940`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420940.md) · 呼出先 4件 [`00ad3bf8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3bf8.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
                "const:21c:8"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0041bfa0",
      "incomplete_value": true,
      "site": "0041bfa0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0041bfa0",
      "incomplete_value": true,
      "site": "0041bfa0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 23,
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
        "0029e21c",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "0029e22c",
        null,
        "string"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "0029e23a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
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
      112,
      "READ",
      [
        "storage",
        "0029e2c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041bf80 ["COPY", "tmp:0:8", ["const:21c:8"]]
+ 0041bf80 ["COPY", "tmp:0:8", ["const:2a7:8"]]
~~~


### [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) → [`0041c120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) FUN_0041c120

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0073496c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`0081fa64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00821350`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821350.md) [`0084c390`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md) [`0084f35c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f35c.md) · 呼出先 24件 [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`00428d08`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428d08.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md)
- 新版 呼出元 9件 [`0073496c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`0081fa64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00821350`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) [`0084c390`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) [`0084f35c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f35c.md) · 呼出先 24件 [`0041ac3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041b470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`00428d08`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428d08.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
                "const:952:8"
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
    "kind": "call_argument_candidate",
    "new": {
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
            "const:381:8"
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
        "00c1ad68",
        null,
        "pointer"
      ]
    ],
    [
      388,
      "PARAM",
      [
        "storage",
        "002af912",
        null,
        "string"
      ]
    ],
    [
      436,
      "PARAM",
      [
        "storage",
        "002a91bf",
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
  ]
}
~~~


~~~diff
- 0041c268 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d68:8"]]
+ 0041c268 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:db8:8"]]
- 0041c274 ["COPY", "tmp:0:8", ["const:912:8"]]
+ 0041c274 ["COPY", "tmp:0:8", ["const:87e:8"]]
- 0041c27c ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 0041c27c ["COPY", "tmp:0:8", ["const:259:8"]]
~~~


### [`0041c8f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) → [`0041c8f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) FUN_0041c8f8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 25件 [`0060468c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/0060468c.md) [`00651720`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651720.md) [`006584d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md) [`0068d484`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) [`00695904`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) · 呼出先 4件 [`00420b98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b98.md) [`00420b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b9c.md) [`00ad3e54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3e54.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 25件 [`0060468c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/0060468c.md) [`00651720`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651720.md) [`006584d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) [`0068d484`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) [`00695904`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 4件 [`00420b98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b98.md) [`00420b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b9c.md) [`00ad3e98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3e98.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:4c8:8"
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
        "00be64c8",
        null,
        "undefined *"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00be64e8",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00be64f0",
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
  ]
}
~~~


~~~diff
- 0041c924 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0041c924 ["COPY", "tmp:0:8", ["const:518:8"]]
~~~


### [`0041c9f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c9f4.md) → [`0041c9f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c9f4.md) FUN_0041c9f4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00acc528`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md) · 呼出先 4件 [`00420b98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b98.md) [`00420b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b9c.md) [`00ad3e54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3e54.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00acc56c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc56c.md) · 呼出先 4件 [`00420b98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b98.md) [`00420b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b9c.md) [`00ad3e98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3e98.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:4c8:8"
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
        "00be64c8",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00be64e8",
        null,
        "pointer"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00be64f0",
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
  ]
}
~~~


~~~diff
- 0041ca14 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0041ca14 ["COPY", "tmp:0:8", ["const:518:8"]]
~~~


### [`0041cad8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cad8.md) → [`0041cad8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cad8.md) FUN_0041cad8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0041c8ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8ec.md) · 呼出先 6件 [`00420938`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420938.md) [`0042093c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042093c.md) [`00420b18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b18.md) [`00420b1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b1c.md) [`00ad3bb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3bb8.md)
- 新版 呼出元 1件 [`0041c8ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8ec.md) · 呼出先 6件 [`00420938`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420938.md) [`0042093c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042093c.md) [`00420b18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b18.md) [`00420b1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b1c.md) [`00ad3bfc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3bfc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:3a8:8"
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
            "const:438:8"
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
            "const:21c:8"
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
        "00be63a8",
        null,
        "undefined *"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00be6438",
        null,
        "undefined *"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "0029e21c",
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
  ]
}
~~~


~~~diff
- 0041caf8 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0041caf8 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 0041cb14 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 0041cb14 ["COPY", "tmp:0:8", ["const:488:8"]]
- 0041cb2c ["COPY", "tmp:0:8", ["const:21c:8"]]
+ 0041cb2c ["COPY", "tmp:0:8", ["const:2a7:8"]]
~~~


### [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md) → [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) FUN_0041cddc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a2ba24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2ba24.md) [`00ab1d84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1d84.md) · 呼出先 23件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00420bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bd8.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md)
- 新版 呼出元 2件 [`00a2ba68`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2ba68.md) [`00ab1dc8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1dc8.md) · 呼出先 23件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00420bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bd8.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
                "const:952:8"
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
                "const:74e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 84,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0041d530",
      "incomplete_value": true,
      "site": "0041d548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:389:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041d530",
      "incomplete_value": true,
      "site": "0041d548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 93,
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
        "002a91bf",
        null,
        null
      ]
    ],
    [
      372,
      "READ",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ],
    [
      696,
      "READ",
      [
        "storage",
        "002945c6",
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
  ]
}
~~~


~~~diff
- 0041ce48 ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 0041ce48 ["COPY", "tmp:0:8", ["const:259:8"]]
- 0041cf48 ["COPY", "tmp:0:8", ["const:952:8"]]
+ 0041cf48 ["COPY", "tmp:0:8", ["const:8c5:8"]]
- 0041d088 ["COPY", "tmp:0:8", ["const:5c6:8"]]
+ 0041d088 ["COPY", "tmp:0:8", ["const:539:8"]]
~~~


### [`0041e03c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e03c.md) → [`0041e03c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e03c.md) FUN_0041e03c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00692224`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/00692224.md) [`007da86c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da86c.md) [`007e5fa4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 4件 [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb120.md)
- 新版 呼出元 4件 [`00692224`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/00692224.md) [`007da86c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da86c.md) [`007e5fa4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 4件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c13408",
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
  ]
}
~~~


~~~diff
- 0041e058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 0041e058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 0041e05c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 0041e05c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:dc8:8"]]
- 0041e084 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
+ 0041e084 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
~~~


### [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) → [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) FUN_0041e380

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 535件 [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md) [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e10c.md) [`00439bc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439bc0.md) [`0043aca0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043aca0.md) [`0043ec60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043ec60.md) · 呼出先 4件 [`00bbacf0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb190`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb190.md)
- 新版 呼出元 535件 [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`00439bc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439bc0.md) [`0043aca0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aca0.md) [`0043ec60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043ec60.md) · 呼出先 4件 [`00bbad34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb1e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
                "const:d90:8"
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
                "const:d98:8"
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
        "00c1ad90",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "00c168b8",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c1ad98",
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
  ]
}
~~~


~~~diff
- 0041e3a8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d90:8"]]
+ 0041e3a8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:de0:8"]]
- 0041e3ac ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:d98:8"]]
+ 0041e3ac ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:de8:8"]]
~~~


### [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) → [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) FUN_0041e41c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 43件 [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e10c.md) [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`004629d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00462/004629d4.md) [`0049100c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/0049100c.md) [`0049b54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049b/0049b54c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 43件 [`0041e10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004629d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/004629d4.md) [`0049100c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/0049100c.md) [`0049b54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049b54c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
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
      12,
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


~~~diff
- 0041e428 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0041e428 ["COPY", "tmp:0:8", ["const:39d:8"]]
~~~


### [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md) → [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) FUN_0041e778

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0041e650`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e650.md) [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md) [`005f1af0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1af0.md) [`005f5668`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f5/005f5668.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md)
- 新版 呼出元 4件 [`0041e650`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e650.md) [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) [`005f1af0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1af0.md) [`005f5668`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f5/005f5668.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      368,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      552,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      580,
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
  ]
}
~~~


~~~diff
- 0041e8e8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0041e8e8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
- 0041e9a0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0041e9a0 ["COPY", "tmp:0:8", ["const:379:8"]]
- 0041e9bc ["COPY", "tmp:0:8", ["const:919:8"]]
+ 0041e9bc ["COPY", "tmp:0:8", ["const:885:8"]]
~~~


### [`0041f3d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f3d4.md) → [`0041f3d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md) FUN_0041f3d4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md) [`0041f3d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f3d4.md) [`0045a988`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a988.md) [`0046ff30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`00710214`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710214.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 7件 [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) [`0041f3d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md) [`0045a988`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a988.md) [`0046ff30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`00710214`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710214.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      360,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      544,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      572,
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
  ]
}
~~~


~~~diff
- 0041f53c ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0041f53c ["COPY", "tmp:0:8", ["const:3a4:8"]]
- 0041f5f4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0041f5f4 ["COPY", "tmp:0:8", ["const:379:8"]]
- 0041f610 ["COPY", "tmp:0:8", ["const:919:8"]]
+ 0041f610 ["COPY", "tmp:0:8", ["const:885:8"]]
~~~


### [`0041fddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) → [`0041fddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) FUN_0041fddc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 130件 [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md) [`0041f280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f280.md) [`0041f354`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md) [`0041f3d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f3d4.md) [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md) · 呼出先 1件 [`0041fdf0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 130件 [`0041e778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) [`0041f280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f280.md) [`0041f354`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`0041f3d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md) [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) · 呼出先 1件 [`0041fdf0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:1b2:8"
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
        "002a91b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      12,
      "PARAM",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041fde8 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 0041fde8 ["COPY", "tmp:0:8", ["const:24c:8"]]
~~~


### [`0041fdf0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) → [`0041fdf0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) FUN_0041fdf0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 222件 [`0041fddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00463ea0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00463/00463ea0.md) [`0047c518`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`0047c52c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c52c.md) [`0047c540`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c540.md) · 呼出先 4件 [`0041fe40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fe40.md) [`00bbae18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae18.md) [`00bdb050`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 222件 [`0041fddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00463ea0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ea0.md) [`0047c518`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`0047c52c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c52c.md) [`0047c540`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c540.md) · 呼出先 4件 [`0041fe40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fe40.md) [`00bbae5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae5c.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041fe20",
      "incomplete_value": true,
      "site": "0041fe28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041fe20",
      "incomplete_value": true,
      "site": "0041fe28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
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
      "definition_site": "0041fe24",
      "incomplete_value": true,
      "site": "0041fe28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041fe24",
      "incomplete_value": true,
      "site": "0041fe28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
      48,
      "READ",
      [
        "storage",
        "00c1ada0",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00c16a20",
        "_ZTISt12out_of_range",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00c1ada8",
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
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00c16a70",
        "_ZTISt12out_of_range",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00c1adf8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0041fe20 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:da0:8"]]
+ 0041fe20 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 0041fe24 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:da8:8"]]
+ 0041fe24 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:df8:8"]]
~~~


### [`00420234`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420234.md) → [`00420234`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420234.md) FUN_00420234

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
        "00be5fe8",
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
        "00be6038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420244 ["COPY", "register:4040:8", ["const:be5000:8"]]
- 00420248 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 00420244 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00420248 ["COPY", "tmp:0:8", ["const:38:8"]]
~~~


### [`00420258`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420258.md) → [`00420258`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420258.md) FUN_00420258

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
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
        "00be5fe8",
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
        "00be6038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420258 ["COPY", "register:4040:8", ["const:be5000:8"]]
- 0042025c ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 00420258 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0042025c ["COPY", "tmp:0:8", ["const:38:8"]]
~~~


### [`0042035c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042035c.md) → [`0042035c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042035c.md) FUN_0042035c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:78:8"
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
        "00be6078",
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
        "00be60c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0042037c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0042037c ["COPY", "tmp:0:8", ["const:c8:8"]]
~~~


### [`00420390`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420390.md) → [`00420390`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420390.md) FUN_00420390

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
            "const:78:8"
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
        "00be6078",
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
        "00be60c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420398 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00420398 ["COPY", "tmp:0:8", ["const:c8:8"]]
~~~


### [`004203e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004203e8.md) → [`004203e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203e8.md) FUN_004203e8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:108:8"
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
        "00be6108",
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
        "00be6158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420408 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00420408 ["COPY", "tmp:0:8", ["const:158:8"]]
~~~


### [`0042041c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042041c.md) → [`0042041c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042041c.md) FUN_0042041c

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00be6108",
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
        "00be6158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420424 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00420424 ["COPY", "tmp:0:8", ["const:158:8"]]
~~~


### [`00420530`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420530.md) → [`00420530`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420530.md) FUN_00420530

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:198:8"
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
        "00be6198",
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
        "00be61e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420550 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00420550 ["COPY", "tmp:0:8", ["const:1e8:8"]]
~~~


### [`00420564`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420564.md) → [`00420564`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420564.md) FUN_00420564

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
            "const:198:8"
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
        "00be6198",
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
        "00be61e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0042056c ["COPY", "tmp:0:8", ["const:198:8"]]
+ 0042056c ["COPY", "tmp:0:8", ["const:1e8:8"]]
~~~


### [`0042062c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042062c.md) → [`0042062c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042062c.md) FUN_0042062c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:228:8"
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
        "00be6228",
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
        "00be6278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0042064c ["COPY", "tmp:0:8", ["const:228:8"]]
+ 0042064c ["COPY", "tmp:0:8", ["const:278:8"]]
~~~


### [`00420660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420660.md) → [`00420660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420660.md) FUN_00420660

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00be6228",
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
        "00be6278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420668 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00420668 ["COPY", "tmp:0:8", ["const:278:8"]]
~~~


### [`004206bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004206bc.md) → [`004206bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206bc.md) FUN_004206bc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:2a8:8"
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
        "00be62a8",
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
        "00be62f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 004206dc ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 004206dc ["COPY", "tmp:0:8", ["const:2f8:8"]]
~~~


### [`004206f0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004206f0.md) → [`004206f0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206f0.md) FUN_004206f0

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
      12,
      "DATA",
      [
        "storage",
        "00be62a8",
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
        "00be62f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 004206f8 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 004206f8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
~~~


### [`00420808`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420808.md) → [`00420808`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420808.md) FUN_00420808

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:328:8"
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
        "00be6328",
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
        "00be6378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420828 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00420828 ["COPY", "tmp:0:8", ["const:378:8"]]
~~~


### [`0042083c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042083c.md) → [`0042083c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042083c.md) FUN_0042083c

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00be6328",
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
        "00be6378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420844 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00420844 ["COPY", "tmp:0:8", ["const:378:8"]]
~~~


### [`00420904`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420904.md) → [`00420904`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420904.md) FUN_00420904

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "DATA",
      [
        "storage",
        "00be63a8",
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
        "00be63f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420918 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00420918 ["COPY", "tmp:0:8", ["const:3f8:8"]]
~~~


### [`00420928`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420928.md) → [`00420928`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420928.md) FUN_00420928

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      8,
      "DATA",
      [
        "storage",
        "00be63a8",
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
        "00be63f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0042092c ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0042092c ["COPY", "tmp:0:8", ["const:3f8:8"]]
~~~


### [`00420940`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420940.md) → [`00420940`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420940.md) FUN_00420940

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041be9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be9c.md) [`0041bf20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bf20.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041be9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be9c.md) [`0041bf20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
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
            "const:abc:8"
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
            "const:ae0:8"
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
            "const:a88:8"
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
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      132,
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      148,
      "WRITE",
      [
        "storage",
        "00c24abc",
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
  ]
}
~~~


~~~diff
- 0042098c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0042098c ["COPY", "tmp:0:8", ["const:b20:8"]]
- 004209c0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 004209c0 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 004209d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:abc:8"]]
+ 004209d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:afc:8"]]
~~~


### [`00420ae4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420ae4.md) → [`00420ae4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ae4.md) FUN_00420ae4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:438:8"
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
        "00be6438",
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
        "00be6488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420af8 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00420af8 ["COPY", "tmp:0:8", ["const:488:8"]]
~~~


### [`00420b08`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b08.md) → [`00420b08`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b08.md) FUN_00420b08

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
            "const:438:8"
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
        "00be6438",
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
        "00be6488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420b0c ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00420b0c ["COPY", "tmp:0:8", ["const:488:8"]]
~~~


### [`00420b20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b20.md) → [`00420b20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b20.md) FUN_00420b20

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
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      12,
      "WRITE",
      [
        "storage",
        "00c24db4",
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
  ]
}
~~~


~~~diff
- 00420b28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d28:8"]]
+ 00420b28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d78:8"]]
~~~


### [`00420b64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b64.md) → [`00420b64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b64.md) FUN_00420b64

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
        "00be64c8",
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
        "00be6518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420b78 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 00420b78 ["COPY", "tmp:0:8", ["const:518:8"]]
~~~


### [`00420b88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b88.md) → [`00420b88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b88.md) FUN_00420b88

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
            "const:4c8:8"
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
        "00be64c8",
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
        "00be6518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420b8c ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 00420b8c ["COPY", "tmp:0:8", ["const:518:8"]]
~~~


### [`00420ba0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420ba0.md) → [`00420ba0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ba0.md) FUN_00420ba0

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
                "const:d70:8"
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
        "00c24db4",
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
        "00c24df4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00420ba4 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00420ba4 ["COPY", "tmp:0:8", ["const:db0:8"]]
~~~


### [`00420bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bd8.md) → [`00420bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bd8.md) FUN_00420bd8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0041cddc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
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
      12,
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


~~~diff
- 00420be4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00420be4 ["COPY", "tmp:0:8", ["const:39d:8"]]
~~~


### [`00420bec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bec.md) → [`00420bec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bec.md) _INIT_7

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      128,
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
  ]
}
~~~


~~~diff
- 00420c18 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00420c18 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00420c24 ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 00420c24 ["COPY", "tmp:0:8", ["const:377:8"]]
- 00420c40 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 00420c40 ["COPY", "tmp:0:8", ["const:38a:8"]]
~~~


### [`00420f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420f7c.md) → [`00420f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420f7c.md) _INIT_8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      128,
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
  ]
}
~~~


~~~diff
- 00420fa8 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 00420fa8 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00420fb4 ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 00420fb4 ["COPY", "tmp:0:8", ["const:377:8"]]
- 00420fd0 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 00420fd0 ["COPY", "tmp:0:8", ["const:38a:8"]]
~~~


### [`0042130c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/0042130c.md) → [`0042130c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/0042130c.md) FUN_0042130c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00428010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428010.md) · 呼出先 8件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00bd6e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)
- 新版 呼出元 1件 [`00428010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428010.md) · 呼出先 8件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 22件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
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
            "const:b30:8"
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
            "const:b34:8"
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
                "const:b18:8"
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
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c24b20",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c24b48",
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
  ]
}
~~~


~~~diff
- 0042132c ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 0042132c ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00421348 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b20:8"]]
+ 00421348 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b60:8"]]
- 0042135c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b20:8"]]
+ 0042135c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b60:8"]]
~~~


### [`004215a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md) → [`004215a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md) FUN_004215a0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0081f58c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f58c.md) [`0084004c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084004c.md) [`008406e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406e4.md) [`00840b80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840b80.md) [`00844bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844bd8.md) · 呼出先 4件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 6件 [`0081f58c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) [`0084004c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/0084004c.md) [`008406e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md) [`00840b80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840b80.md) [`00844bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) · 呼出先 4件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
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
                "const:b18:8"
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
                "const:b18:8"
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
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00c24b18",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "00c24b48",
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
  ]
}
~~~


~~~diff
- 004215ac ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 004215ac ["COPY", "tmp:0:8", ["const:b88:8"]]
- 004215bc ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 004215bc ["COPY", "tmp:0:8", ["const:b58:8"]]
- 004215cc ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 004215cc ["COPY", "tmp:0:8", ["const:b88:8"]]
~~~


### [`00421614`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421614.md) → [`00421614`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421614.md) FUN_00421614

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00428080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428080.md) · 呼出先 6件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00428080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md) · 呼出先 6件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 29件, `call_target` 1件, `store_destination` 38件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
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
            "const:b20:8"
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
                "const:b20:8"
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
            "const:b34:8"
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
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c24b20",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00c24b48",
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
  ]
}
~~~


~~~diff
- 00421624 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00421624 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00421634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00421634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b60:8"]]
- 00421644 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00421644 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b60:8"]]
~~~


### [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md) → [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) FUN_00421924

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md) [`00428080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428080.md) · 呼出先 10件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md) [`00423ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423ad4.md) [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) [`00428080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md) · 呼出先 10件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`00423ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423ad4.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
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
                "const:b18:8"
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
                "const:b18:8"
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
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      312,
      "PARAM",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      328,
      "PARAM",
      [
        "storage",
        "00c24b18",
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
  ]
}
~~~


~~~diff
- 004219f0 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 004219f0 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00421a5c ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00421a5c ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00421a6c ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 00421a6c ["COPY", "tmp:0:8", ["const:b58:8"]]
~~~


### [`00421b40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b40.md) → [`00421b40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) FUN_00421b40

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084004c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084004c.md) · 呼出先 13件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`00422098`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/00422098.md) [`00424230`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424230.md) [`0052dd44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd44.md)
- 新版 呼出元 1件 [`0084004c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/0084004c.md) · 呼出先 13件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00422098`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md) [`00424230`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424230.md) [`0052dd44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd44.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:1c4:8"
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
        "002a91c4",
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
        "002a925e",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00421dcc ["COPY", "tmp:0:8", ["const:1c4:8"]]
+ 00421dcc ["COPY", "tmp:0:8", ["const:25e:8"]]
~~~


### [`00422098`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/00422098.md) → [`00422098`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md) FUN_00422098

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00421b40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b40.md) · 呼出先 14件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0042818c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/0042818c.md) [`00464a54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`00421b40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) · 呼出先 14件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0042818c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/0042818c.md) [`00464a54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:548:8"
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
        "00be6548",
        null,
        "undefined *"
      ]
    ],
    [
      332,
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      336,
      "READ",
      [
        "storage",
        "00c1ad78",
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
  ]
}
~~~


~~~diff
- 004220d8 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 004220d8 ["COPY", "tmp:0:8", ["const:598:8"]]
- 004221e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 004221e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 004221e8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 004221e8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:dc8:8"]]
~~~


### [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) → [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) FUN_004222e0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008406e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406e4.md) [`00844bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844bd8.md) · 呼出先 42件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md) [`00423878`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423878.md) [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md)
- 新版 呼出元 2件 [`008406e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md) [`00844bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) · 呼出先 42件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`00423878`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423878.md) [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 1件, `store_value` 21件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:548:8"
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
        "00be6548",
        null,
        "undefined *"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      152,
      "READ",
      [
        "storage",
        "00c1ad78",
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
  ]
}
~~~


~~~diff
- 0042232c ["COPY", "tmp:0:8", ["const:548:8"]]
+ 0042232c ["COPY", "tmp:0:8", ["const:598:8"]]
- 00422374 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 00422374 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 00422378 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d78:8"]]
+ 00422378 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:dc8:8"]]
~~~


### [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md) → [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) FUN_004235ac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) · 呼出先 11件 [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md) [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md) [`0052dccc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dccc.md) [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) · 呼出先 11件 [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`0052dccc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
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
            "const:b30:8"
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
                "const:b18:8"
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
                "const:b18:8"
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
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      188,
      "WRITE",
      [
        "storage",
        "00c24b30",
        null,
        "undefined4"
      ]
    ],
    [
      356,
      "PARAM",
      [
        "storage",
        "00c24b48",
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
  ]
}
~~~


~~~diff
- 00423654 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00423654 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00423668 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b30:8"]]
+ 00423668 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b70:8"]]
- 00423708 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00423708 ["COPY", "tmp:0:8", ["const:b88:8"]]
~~~


### [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md) → [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) FUN_00423798

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md) [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md) [`00423bbc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423bbc.md) · 呼出先 4件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0052dd5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd5c.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 4件 [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`004235ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) [`00423bbc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md) · 呼出先 4件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0052dd5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd5c.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
                "const:c60:8"
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
        "00298c60",
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
        "00298bd3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 004237c4 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 004237c4 ["COPY", "tmp:0:8", ["const:bd3:8"]]
~~~


### [`00423bbc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423bbc.md) → [`00423bbc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md) FUN_00423bbc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00423fe4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423fe4.md) · 呼出先 16件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md) [`004782e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004782e4.md) [`0052dd44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd44.md) [`0052dd48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd48.md)
- 新版 呼出元 1件 [`00423fe4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe4.md) · 呼出先 16件 [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`004782e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md) [`0052dd44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd44.md) [`0052dd48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd48.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 20件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
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
                "const:b18:8"
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
                "const:b18:8"
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
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      124,
      "READ",
      [
        "storage",
        "00c24b48",
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
  ]
}
~~~


~~~diff
- 00423bec ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00423bec ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00423c44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b18:8"]]
+ 00423c44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b58:8"]]
- 00423c68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 00423c68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b78:8"]]
~~~


### [`00423f2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423f2c.md) → [`00423f2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423f2c.md) FUN_00423f2c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb120.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c13408",
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
  ]
}
~~~


~~~diff
- 00423f48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 00423f48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 00423f4c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 00423f4c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:dc8:8"]]
- 00423f74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
+ 00423f74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
~~~


### [`00423fe8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423fe8.md) → [`00423fe8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe8.md) FUN_00423fe8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00423ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423ad4.md) · 呼出先 6件 [`004240ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/004240ec.md) [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb260.md) [`00bdb270`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb270.md)
- 新版 呼出元 1件 [`00423ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423ad4.md) · 呼出先 6件 [`004240ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/004240ec.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) [`00bdb2c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:5d1:8"
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
      180,
      "PARAM",
      [
        "storage",
        "002945d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
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
  ]
}
~~~


~~~diff
- 0042409c ["COPY", "tmp:0:8", ["const:5d1:8"]]
+ 0042409c ["COPY", "tmp:0:8", ["const:544:8"]]
~~~


### [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md) → [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) FUN_00424280

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md) · 呼出先 23件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) · 呼出先 23件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:2ee:8"
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
            "const:919:8"
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
        "002a730a",
        null,
        null
      ]
    ],
    [
      528,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      552,
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
  ]
}
~~~


~~~diff
- 004243d4 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 004243d4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
- 00424490 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00424490 ["COPY", "tmp:0:8", ["const:379:8"]]
- 004244a8 ["COPY", "tmp:0:8", ["const:919:8"]]
+ 004244a8 ["COPY", "tmp:0:8", ["const:885:8"]]
~~~


### [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) → [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) FUN_00424bb4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 27件 [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md) [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004264e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md) [`00426e8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e8c.md) [`005be404`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be404.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 27件 [`00424280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004264e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) [`00426e8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) [`005be404`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      340,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      376,
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      684,
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
  ]
}
~~~


~~~diff
- 00424d08 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00424d08 ["COPY", "tmp:0:8", ["const:3a4:8"]]
- 00424d2c ["COPY", "tmp:0:8", ["const:919:8"]]
+ 00424d2c ["COPY", "tmp:0:8", ["const:885:8"]]
- 00424e60 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00424e60 ["COPY", "tmp:0:8", ["const:379:8"]]
~~~


### [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) → [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) FUN_004253b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 170件 [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00458974`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00458/00458974.md) [`0059fbec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059fbec.md) [`005a45f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 170件 [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00458974`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458974.md) [`0059fbec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059fbec.md) [`005a45f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      336,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      372,
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      680,
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
  ]
}
~~~


~~~diff
- 00425504 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00425504 ["COPY", "tmp:0:8", ["const:3a4:8"]]
- 00425528 ["COPY", "tmp:0:8", ["const:919:8"]]
+ 00425528 ["COPY", "tmp:0:8", ["const:885:8"]]
- 0042565c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0042565c ["COPY", "tmp:0:8", ["const:379:8"]]
~~~


### [`00425ba0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/00425ba0.md) → [`00425ba0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md) FUN_00425ba0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`00425ba0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/00425ba0.md) · 呼出先 23件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00425ba0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md) · 呼出先 23件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:2ee:8"
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
            "const:919:8"
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
        "002a730a",
        null,
        null
      ]
    ],
    [
      532,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      556,
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
  ]
}
~~~


~~~diff
- 00425cf8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00425cf8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
- 00425db4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00425db4 ["COPY", "tmp:0:8", ["const:379:8"]]
- 00425dcc ["COPY", "tmp:0:8", ["const:919:8"]]
+ 00425dcc ["COPY", "tmp:0:8", ["const:885:8"]]
~~~


### [`004264e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md) → [`004264e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) FUN_004264e8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00425ba0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/00425ba0.md) [`004264e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md) [`005be404`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be404.md) [`005fa9ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fa/005fa9ec.md) [`005fd41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fd41c.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 10件 [`00425ba0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md) [`004264e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) [`005be404`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) [`005fa9ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fa/005fa9ec.md) [`005fd41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fd41c.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      344,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      380,
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      688,
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
  ]
}
~~~


~~~diff
- 00426640 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00426640 ["COPY", "tmp:0:8", ["const:3a4:8"]]
- 00426664 ["COPY", "tmp:0:8", ["const:919:8"]]
+ 00426664 ["COPY", "tmp:0:8", ["const:885:8"]]
- 00426798 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00426798 ["COPY", "tmp:0:8", ["const:379:8"]]
~~~


### [`00426e78`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e78.md) → [`00426e78`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) FUN_00426e78

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`00426cec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426cec.md) [`004c2f88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2f88.md) [`005aca98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005aca98.md) [`005af810`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005af810.md) [`0073ea18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ea18.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`00426cec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426cec.md) [`004c2f88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2f88.md) [`005aca98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md) [`005af810`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af810.md) [`0073ea18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ea18.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
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
      12,
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


~~~diff
- 00426e84 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00426e84 ["COPY", "tmp:0:8", ["const:39d:8"]]
~~~


### [`00426e8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e8c.md) → [`00426e8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) FUN_00426e8c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`00426e8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e8c.md) [`0046c588`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c588.md) [`005b7004`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7004.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00426e8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) [`0046c588`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md) [`005b7004`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7004.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      364,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      556,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      584,
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
  ]
}
~~~


~~~diff
- 00426ff8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00426ff8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
- 004270b8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 004270b8 ["COPY", "tmp:0:8", ["const:379:8"]]
- 004270d4 ["COPY", "tmp:0:8", ["const:919:8"]]
+ 004270d4 ["COPY", "tmp:0:8", ["const:885:8"]]
~~~


### [`00427778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427778.md) → [`00427778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427778.md) FUN_00427778

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`00427778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427778.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`004222e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00427778`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427778.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      336,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      372,
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      680,
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
  ]
}
~~~


~~~diff
- 004278c8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 004278c8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
- 004278ec ["COPY", "tmp:0:8", ["const:919:8"]]
+ 004278ec ["COPY", "tmp:0:8", ["const:885:8"]]
- 00427a20 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00427a20 ["COPY", "tmp:0:8", ["const:379:8"]]
~~~


### [`00427f68`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427f68.md) → [`00427f68`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f68.md) FUN_00427f68

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:5c0:8"
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
        "00be65c0",
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
        "00be6610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00427f7c ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00427f7c ["COPY", "tmp:0:8", ["const:610:8"]]
~~~


### [`00427f8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427f8c.md) → [`00427f8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f8c.md) FUN_00427f8c

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
            "const:5c0:8"
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
        "00be65c0",
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
        "00be6610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00427f90 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00427f90 ["COPY", "tmp:0:8", ["const:610:8"]]
~~~


### [`00427fd4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427fd4.md) → [`00427fd4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427fd4.md) FUN_00427fd4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:640:8"
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
        "00be6640",
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
        "00be6690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00427fe8 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00427fe8 ["COPY", "tmp:0:8", ["const:690:8"]]
~~~


### [`00427ff8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427ff8.md) → [`00427ff8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427ff8.md) FUN_00427ff8

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
            "const:640:8"
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
        "00be6640",
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
        "00be6690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00427ffc ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00427ffc ["COPY", "tmp:0:8", ["const:690:8"]]
~~~


### [`00428044`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428044.md) → [`00428044`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428044.md) FUN_00428044

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
            "const:6c0:8"
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
        "00be66c0",
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
        "00be6710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00428058 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00428058 ["COPY", "tmp:0:8", ["const:710:8"]]
~~~


### [`00428068`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428068.md) → [`00428068`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428068.md) FUN_00428068

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
            "const:6c0:8"
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
        "00be66c0",
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
        "00be6710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0042806c ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 0042806c ["COPY", "tmp:0:8", ["const:710:8"]]
~~~


### [`00428080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428080.md) → [`00428080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md) FUN_00428080

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00421614`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421614.md) [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md) [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00421614`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421614.md) [`00421924`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) [`00421ad4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
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
                "const:b18:8"
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
                "const:b18:8"
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
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "00c24b18",
        null,
        "undefined8"
      ]
    ],
    [
      56,
      "PARAM",
      [
        "storage",
        "00c24b48",
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
  ]
}
~~~


~~~diff
- 00428098 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00428098 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 004280a8 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 004280a8 ["COPY", "tmp:0:8", ["const:b58:8"]]
- 004280b8 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 004280b8 ["COPY", "tmp:0:8", ["const:b88:8"]]
~~~


### [`00428290`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428290.md) → [`00428290`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428290.md) _INIT_9

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      128,
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
  ]
}
~~~


~~~diff
- 004282bc ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 004282bc ["COPY", "tmp:0:8", ["const:b40:8"]]
- 004282c8 ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 004282c8 ["COPY", "tmp:0:8", ["const:377:8"]]
- 004282e4 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 004282e4 ["COPY", "tmp:0:8", ["const:38a:8"]]
~~~


### [`00428648`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428648.md) → [`00428648`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428648.md) FUN_00428648

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00605bdc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/00605bdc.md) [`006091c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/006091c4.md) [`00824eb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 3件 [`00605bdc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/00605bdc.md) [`006091c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/006091c4.md) [`00824eb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:686:8"
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
      72,
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ],
  "added": [
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
  ]
}
~~~


~~~diff
- 00428690 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 00428690 ["COPY", "tmp:0:8", ["const:5f9:8"]]
~~~


### [`00428714`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428714.md) → [`00428714`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428714.md) FUN_00428714

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00429a14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429a14.md) [`0079bdf0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`00824eb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`00868124`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) · 呼出先 5件 [`00574744`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574744.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 4件 [`00429a14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429a14.md) [`0079bdf0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`00824eb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00868124`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) · 呼出先 5件 [`00574744`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574744.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
            "const:30d:8"
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
      76,
      "PARAM",
      [
        "storage",
        "002a730d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
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
  ]
}
~~~


~~~diff
- 00428760 ["COPY", "tmp:0:8", ["const:30d:8"]]
+ 00428760 ["COPY", "tmp:0:8", ["const:3a7:8"]]
~~~


### [`004288b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004288b4.md) → [`004288b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md) FUN_004288b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`0042f000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f000.md) [`0042f610`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md) [`0042fd7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`00432904`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432904.md) [`00432e80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432e80.md) · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 10件 [`0042f000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md) [`0042f610`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) [`0042fd7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00432904`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432904.md) [`00432e80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432e80.md) · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
                "const:241:8"
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
      48,
      "READ",
      [
        "storage",
        "002a1241",
        null,
        "string"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002a1251",
        null,
        "string"
      ]
    ]
  ],
  "added": [
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
  ]
}
~~~


~~~diff
- 004288e0 ["COPY", "tmp:0:8", ["const:241:8"]]
+ 004288e0 ["COPY", "tmp:0:8", ["const:2cc:8"]]
~~~


### [`00428904`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428904.md) → [`00428904`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428904.md) FUN_00428904

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004303e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/004303e0.md) [`0057ecc8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ecc8.md) [`0057fee8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057fee8.md) [`00581790`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581790.md) · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 4件 [`004303e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/004303e0.md) [`0057ecc8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ecc8.md) [`0057fee8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057fee8.md) [`00581790`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581790.md) · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428928",
      "incomplete_value": true,
      "site": "0042893c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428928",
      "incomplete_value": true,
      "site": "0042893c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:869:8"
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
      "definition_site": "00428928",
      "incomplete_value": true,
      "site": "0042893c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00428928",
      "incomplete_value": true,
      "site": "0042893c",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428940",
      "incomplete_value": true,
      "site": "00428940",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428940",
      "incomplete_value": true,
      "site": "00428940",
      "value": [
        "LOAD",
        "8",
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
        "00296869",
        null,
        "string"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "00296879",
        null,
        "string"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00296887",
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
        "002967dc",
        null,
        "string"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "002967ec",
        null,
        "string"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "002967fa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00428920 ["COPY", "tmp:0:8", ["const:869:8"]]
+ 00428920 ["COPY", "tmp:0:8", ["const:7dc:8"]]
~~~


### [`00428954`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428954.md) → [`00428954`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428954.md) FUN_00428954

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00430dd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430dd8.md) · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00430dd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430dd8.md) · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428978",
      "incomplete_value": true,
      "site": "00428988",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:262:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428978",
      "incomplete_value": true,
      "site": "00428988",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1c8:8"
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
      "definition_site": "00428978",
      "incomplete_value": true,
      "site": "00428988",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00428978",
      "incomplete_value": true,
      "site": "00428988",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042898c",
      "incomplete_value": true,
      "site": "00428990",
      "value": [
        "LOAD",
        "16",
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
                "const:1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042898c",
      "incomplete_value": true,
      "site": "00428990",
      "value": [
        "LOAD",
        "16",
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
                "const:1a:8"
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
        "002a91c8",
        null,
        "string"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "002a91d8",
        null,
        "string"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "002a91e2",
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
        "002a9262",
        null,
        "string"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "002a9272",
        null,
        "string"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "002a927c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00428970 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00428970 ["COPY", "tmp:0:8", ["const:262:8"]]
~~~


### [`004289a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289a4.md) → [`004289a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md) FUN_004289a4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0043344c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/0043344c.md) [`00434024`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434024.md) [`00434528`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434528.md) [`004349a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/004349a0.md) [`00435358`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435358.md) · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 7件 [`0043344c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/0043344c.md) [`00434024`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434024.md) [`00434528`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434528.md) [`004349a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/004349a0.md) [`00435358`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435358.md) · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
                "const:5a6:8"
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
      48,
      "READ",
      [
        "storage",
        "002a65a6",
        null,
        "string"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "002a65b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
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
  ]
}
~~~


~~~diff
- 004289d0 ["COPY", "tmp:0:8", ["const:5a6:8"]]
+ 004289d0 ["COPY", "tmp:0:8", ["const:640:8"]]
~~~


